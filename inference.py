from __future__ import print_function
import sys
import time
import argparse
import tensorflow as tf
import numpy as np
from embvec import EmbVec
from config import Config
from model import Model
from input import Input

def build_input_feed_dict(model, bucket):
    """Build input and feed_dict for bucket(inference only)
    """
    config = model.config
    inp = Input(bucket, config, build_output=False)
    feed_dict = {model.input_data_pos_ids: inp.example['pos_ids'],
                 model.input_data_chk_ids: inp.example['chk_ids'],
                 model.is_train: False,
                 model.sentence_length: inp.max_sentence_length}
    feed_dict[model.input_data_word_ids] = inp.example['word_ids']
    feed_dict[model.input_data_wordchr_ids] = inp.example['wordchr_ids']
    if 'elmo' in config.emb_class:
        feed_dict[model.elmo_input_data_wordchr_ids] = inp.example['elmo_wordchr_ids']
    if 'bert' in config.emb_class:
        feed_dict[model.bert_input_data_token_ids] = inp.example['bert_token_ids']
        feed_dict[model.bert_input_data_token_masks] = inp.example['bert_token_masks']
        feed_dict[model.bert_input_data_segment_ids] = inp.example['bert_segment_ids']
        if 'elmo' in config.emb_class:
            feed_dict[model.bert_input_data_elmo_indices] = inp.example['bert_elmo_indices']
    return inp, feed_dict

def inference_bucket(config):
    """Inference for bucket.
    """

    # create model and compile
    model = Model(config)
    model.compile()
    sess = model.sess

    # restore model
    saver = tf.train.Saver()
    saver.restore(sess, config.restore)
    sys.stderr.write('model restored' +'\n')
    '''
    print(tf.global_variables())
    print(tf.trainable_variables())
    '''
    num_buckets = 0
    total_duration_time = 0.0
    bucket = []
    while 1:
        try: line = sys.stdin.readline()
        except KeyboardInterrupt: break
        if not line: break
        line = line.strip()
        if not line and len(bucket) >= 1:
            start_time = time.time()
            inp, feed_dict = build_input_feed_dict(model, bucket)
            logits_indices, sentence_lengths = sess.run([model.logits_indices, model.sentence_lengths], feed_dict=feed_dict)
            tags = config.logit_indices_to_tags(logits_indices[0], sentence_lengths[0])
            for i in range(len(bucket)):
                if 'bert' in config.emb_class:
                    j = inp.example['bert_wordidx2tokenidx'][0][i]
                    out = bucket[i] + ' ' + tags[j]
                else:
                    out = bucket[i] + ' ' + tags[i]
                sys.stdout.write(out + '\n')
            sys.stdout.write('\n')
            bucket = []
            duration_time = time.time() - start_time
            out = 'duration_time : ' + str(duration_time) + ' sec'
            tf.logging.info(out)
            num_buckets += 1
            total_duration_time += duration_time
        if line : bucket.append(line)
    if len(bucket) != 0:
        start_time = time.time()
        inp, feed_dict = build_input_feed_dict(model, bucket)
        logits_indices, sentence_lengths = sess.run([model.logits_indices, model.sentence_lengths], feed_dict=feed_dict)
        tags = config.logit_indices_to_tags(logits_indices[0], sentence_lengths[0])
        for i in range(len(bucket)):
            if 'bert' in config.emb_class:
                j = inp.example['bert_wordidx2tokenidx'][0][i]
                out = bucket[i] + ' ' + tags[j]
            else:
                out = bucket[i] + ' ' + tags[i]
            sys.stdout.write(out + '\n')
        sys.stdout.write('\n')
        duration_time = time.time() - start_time
        out = 'duration_time : ' + str(duration_time) + ' sec'
        tf.logging.info(out)
        num_buckets += 1
        total_duration_time += duration_time

    out = 'total_duration_time : ' + str(total_duration_time) + ' sec' + '\n'
    out += 'average processing time / bucket : ' + str(total_duration_time / num_buckets) + ' sec'
    tf.logging.info(out)

    sess.close()

def inference_line(config):
    """Inference for raw string.
    """
    def get_entity(doc, begin, end):
        for ent in doc.ents:
            # check included
            if ent.start_char <= begin and end <= ent.end_char:
                if ent.start_char == begin: return 'B-' + ent.label_
                else: return 'I-' + ent.label_
        return 'O'
     
    def build_bucket(nlp, line):
        bucket = []
        doc = nlp(line)
        for token in doc:
            begin = token.idx
            end   = begin + len(token.text) - 1
            temp = []
            '''
            print(token.i, token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                  token.shape_, token.is_alpha, token.is_stop, begin, end)
            '''
            temp.append(token.text)
            temp.append(token.tag_)
            temp.append('O')     # no chunking info
            entity = get_entity(doc, begin, end)
            temp.append(entity)  # entity by spacy
            temp = ' '.join(temp)
            bucket.append(temp)
        return bucket

    import spacy
    nlp = spacy.load('en')

    # create model and compile
    model = Model(config)
    model.compile()
    sess = model.sess

    # restore model
    saver = tf.train.Saver()
    saver.restore(sess, config.restore)
    tf.logging.info('model restored' +'\n')

    while 1:
        try: line = sys.stdin.readline()
        except KeyboardInterrupt: break
        if not line: break
        line = line.strip()
        if not line: continue
        # create bucket
        try: bucket = build_bucket(nlp, line)
        except Exception as e:
            sys.stderr.write(str(e) +'\n')
            continue
        inp, feed_dict = build_input_feed_dict(model, bucket)
        logits_indices, sentence_lengths = sess.run([model.logits_indices, model.sentence_lengths], feed_dict=feed_dict)
        tags = config.logit_indices_to_tags(logits_indices[0], sentence_lengths[0])
        for i in range(len(bucket)):
            if 'bert' in config.emb_class:
                j = inp.example['bert_wordidx2tokenidx'][0][i]
                out = bucket[i] + ' ' + tags[j]
            else:
                out = bucket[i] + ' ' + tags[i]
            sys.stdout.write(out + '\n')
        sys.stdout.write('\n')

    sess.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--emb_path', type=str, help='path to word embedding vector + vocab(.pkl)', required=True)
    parser.add_argument('--wrd_dim', type=int, help='dimension of word embedding vector', required=True)
    parser.add_argument('--word_length', type=int, default=15, help='max word length')
    parser.add_argument('--restore', type=str, help='path to saved model(ex, ./checkpoint/ner_model)', required=True)
    parser.add_argument('--mode', type=str, default='bulk', help='bulk, bucket, line')

    args = parser.parse_args()
    tf.logging.set_verbosity(tf.logging.INFO)

    config = Config(args, is_training=False, emb_class='glove', use_crf=True)
    if args.mode == 'bucket': inference_bucket(config)
    if args.mode == 'line':   inference_line(config)
