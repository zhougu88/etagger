- summary
  - https://docs.google.com/spreadsheets/d/1Zj9MF0LK2IE4XHiKTRkRpd8EajEnfqLGvI-IqUMC7A0/edit?usp=sharing

- experiments 14
```
* test 11
word embedding size : 100(glove6b)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : 150 -> 200, project input to 2*qrnn_size, no dropout in qrnn, dropout only in residual
qrnn_filter_size : 3
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

# trial 1
token : 0.8877875673029858
chunk : 0.8809187279151944
conlleval : 88.10
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.01200345084152056 sec

# trial 2
token : 0.8837638376383764
chunk : 0.8761163674949155
conlleval : 87.60
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.011934106823675796 sec

# modified trial 1 (rnn_num_layers : 3, applied projection to first layer only)
token : 0.8759533833668923
chunk : 0.8673442333186036
conlleval : 86.73
average processing time per bucket(sentence)
  - 1 GPU(TITAN X PASCAL) : 0.01733937467995477

* test 10
word embedding size : 100(glove6b)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : 150 -> 250, project input to 2*qrnn_size, no dropout in qrnn, dropout only in residual
qrnn_filter_size : 3
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.8769974897446886
chunk : 0.8702669149596524
conlleval : 87.03
average processing time per bucket(sentence)
  - 1 GPU(TITAN X PASCAL) : 0.01541237780636219 sec

* test 9
word embedding size : 100(glove6b)
keep_prob : 0.7 -> 0.9
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : 150 -> 200, project input to 2*qrnn_size, no dropout in qrnn, dropout only in residual
qrnn_filter_size : 3
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70 -> 140
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.8875768458214134
chunk : 0.8807323299005368
conlleval : 88.07
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.010713322025427472

* test 8
word embedding size : 100(glove6b)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : 150 -> 200, project input to 2*qrnn_size, no dropout in qrnn, dropout only in residual
qrnn_filter_size : 3
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70 -> 140
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.8892680845877263
chunk : 0.8809544851966417
conlleval : 88.10          -> Glove(6B) + CNN + QRNN + CRF best
average processing time per bucket(sentence)
  - 1 GPU(TITAN X PASCAL) : 0.013028464151645457 sec
  - 32 CPU : 0.004297458387741437 sec
  - 1 CPU : 0.004832443533451109 sec
  - 1 CPU(freezed) : 0.0056305657768870795 sec
  - C++
    - 32 CPU : 0.004124 sec
    - 1 CPU : 0.004734 sec

* test 7
word embedding size : 100(glove6b)
keep_prob : 0.7 -> 0.9
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : 150, project input to 2*qrnn_size, no dropout in qrnn, dropout only in residual
qrnn_filter_size : 3
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70 -> 140
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.8797020029311187
chunk : 0.8713414094968608
conlleval : 87.13
average processing time per bucket(sentence)
  - 1 GPU(TITAN X PASCAL) : 0.012709235847319894 sec
  - 32 CPU : 0.003801368411537361 sec
  - 1 CPU : 0.0040382987513216 sec
  - 1 CPU(freezed) : 0.004771721414841477 sec
  - C++
    - 32 CPU : 0.003750 sec
    - 1 CPU : 0.004354 sec

* test 6
word embedding size : 100(glove6b)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : 150, project input to 2*qrnn_size, no dropout in qrnn, dropout only in residual
qrnn_filter_size : 3
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70 -> 140
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.878465605213008
chunk : 0.8706007820831853
conlleval : 87.06
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.011456906924936333

* test 5
word embedding size : 100(glove6b)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : half of input dimension, add residual connection
qrnn_filter_size : 3
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.8446446199407699
chunk : 0.8288918797667114
conlleval : 82.89
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.011665834989661632

* test 4
word embedding size : 100(glove6b)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : 50 -> 150
qrnn_filter_size : 3
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.8595364764874946
chunk : 0.8505259436047026
conlleval : 85.05
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.011682364309002342

* test 3
word embedding size : 100(glove6b)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : 50 -> 100
qrnn_filter_size : 3
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.8543594739405748
chunk : 0.841045566937478
conlleval : 84.10
average processing time per bucket(sentence)
  - 1 GPU(TITAN X PASCAL) : 0.015160589471831513 sec
  - 32 CPU : 0.003978579556903156 sec 
  - 1 CPU : 0.00444540009307033 sec, 0.003874917436759195 sec, 0.00438998971259814 sec
  - 1 CPU(freezed) : 0.003884217897015467 sec
  - C++
    - 32 CPU : 0.003198 sec
    - 1 CPU : 0.003701 sec

* test 2
word embedding size : 100(glove6b)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : 50
qrnn_filter_size : 3
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.7630551942018212
chunk : 0.6628828828828829
conlleval : 66.29
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.012013942035608778 sec

* test 1
word embedding size : 100(glove6b)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused -> qrnn
rnn_size : 200
qrnn_size : 50
qrnn_filter_size : 3
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.8263637498439645
chunk : 0.8129554655870445
conlleval : 81.30
average processing time per bucket(sentence)
  - 1 GPU(TITAN X PASCAL) : 0.015130160556424584 sec
  - 32 CPU : 0.003301392354872017 sec
```

- experiments 13
```
* test 2
word embedding size : 100(glove6b)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
highway_used : False
rnn_used : True
rnn_type : fused
rnn_size : 256 -> 512
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
#learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9245039621598378
chunk : 0.9160021265284423
conlleval : 91.50
average processing time per bucket(sentence)
 - 1 GPU(V100 TESLA) : 0.0772566176651614 sec

* test 1
word embedding size : 100(glove6b)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
highway_used : False
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
#learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9288173100565528
chunk : 0.9214399716261749
conlleval : 91.94          -> Glove(6B) + BERT(large) + ELMo + CNN + LSTM + CRF best
average processing time per bucket(sentence)
 - 1 GPU(V100 TESLA) : 0.07457650762686382 sec

```

- experiments 12
```
* test 6
word embedding size : 300(glove6B) -> 100(glove6B)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9142962011
chunk : 0.9085608269  -> Glove(6B) + CNN + LSTM + CRF best

* test 5
word embedding size : 300(glove6B) -> 100(glove6B)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9116655428186109
chunk : 0.9047450424929179
# python, 32 processor CPU : 0.003053264560968687
# python, frozen, 1 processor CPU : 0.0042755354628630235
# c++, frozen, 32 processor CPU : 0.002789
# c++, frozen, 1 processor CPU : 0.003340
# memory RES : 450M
# c++, frozen -> transformed, 32 processor CPU : 0.002561
# :: token : 0.9116763714373276
# c++, frozen -> transformed, 1 processor CPU : 0.003224
# c++, frozen -> memmapped, 32 processor CPU : 0.002040
# c++, frozen -> memmapped, 1 processor CPU : 0.002683
# memory RES : ~ 160M
# c++, frozen -> transformed -> memmapped, 32 processor CPU : 0.002189
# c++, frozen -> transformed -> memmapped, 1 processor CPU : 0.002709

* test 4
word embedding size : 300(glove6B)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True -> False
rnn_type : fused
rnn_size : 200 -> 276
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9 -> 0.0003
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False -> True
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.8935103064407609
chunk : 0.8876146788990825

* test 3
word embedding size : 300(glove6B)
keep_prob : 0.7 -> 0.32
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200 -> 276
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9004202448382971
chunk : 0.8977252689120084

* test 2
word embedding size : 300(glove6B) -> 200(glove840B)
keep_prob : 0.7 -> 0.32
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200 -> 276
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20 -> 10
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9069880691502313
chunk : 0.9019642385272615

* test 1
word embedding size : 300(glove6B)
keep_prob : 0.7 -> 0.32
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200 -> 275
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 20 -> 10
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9059735188236012
chunk : 0.9027189265536724

```

- experiments 11
```
* test 22
word embedding size : 100(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.9
keep_prob : 0.9
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
highway : True
highway dropout : keep_prob
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 1
learning_rate : exponential_decay(), 2e-5 / 2000 / 0.9 + Warmup 2epoch + AdamWeightDecayOptimizer
gradient clipping : 1.0
#learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token :
chunk :
conlleval :

* test 21
word embedding size : 100(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.9
keep_prob : 0.9
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
highway : True
highway dropout : keep_prob
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 1
learning_rate : exponential_decay(), 2e-5 / 2000 / 0.9 + Warmup 2epoch + AdamWeightDecayOptimizer
gradient clipping : 1.0
#learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.9277306824419101
chunk : 0.920271341732006
conlleval : 91.83

* test 20
word embedding size : 100(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.9
keep_prob : 0.9
#chr_conv_type : conv1d
#chracter embedding size : 25
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 53
#pos embedding size : 7
#pos embedding random init : -0.5 ~ 0.5
#chk embedding size : 10
#chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 1
learning_rate : exponential_decay(), 2e-5 / 2000 / 0.9 + Warmup 2epoch + AdamWeightDecayOptimizer
gradient clipping : 1.0
#learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.9249954153676875
chunk : 0.9174911660777386
conlleval : 91.58

* test 19
#word embedding size : 100(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.9
keep_prob : 0.9
#chr_conv_type : conv1d
#chracter embedding size : 25
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 53
#pos embedding size : 7
#pos embedding random init : -0.5 ~ 0.5
#chk embedding size : 10
#chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 1
learning_rate : exponential_decay(), 2e-5 / 2000 / 0.9 + Warmup 2epoch + AdamWeightDecayOptimizer
gradient clipping : 1.0
#learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

# warmup : 2epoch, decay step : 2000
token : 0.9308840695459852
chunk : 0.9227087395851798
conlleval : 92.06

# warmup : 1epoch, decay step : 1000
token : 0.930369281646151
chunk : 0.9202085358310506
conlleval : 91.87

# warmup : 2epoch, decay step : 2000, correct is_training(use tf.bool is_train)
token : 0.9310957309977338
chunk : 0.9240976645435245
conlleval : 92.23          -> BERT large + LSTM + CRF best

* test 18
#word embedding size : 100(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.9
keep_prob : 0.9
#chr_conv_type : conv1d
#chracter embedding size : 25
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 53
#pos embedding size : 7
#pos embedding random init : -0.5 ~ 0.5
#chk embedding size : 10
#chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 1
learning_rate : exponential_decay(), 2e-5 / 1000 / 0.9
gradient clipping : 1.0
#learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.9286369473491102
chunk : 0.9227642276422764
conlleval : 92.08

* test 17
#word embedding size : 100(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.9
keep_prob : 0.9
#chr_conv_type : conv1d
#chracter embedding size : 25
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 53
#pos embedding size : 7
#pos embedding random init : -0.5 ~ 0.5
#chk embedding size : 10
#chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256 -> 200
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9 + AdamWeightDecayOptimizer
gradient clipping : 1.5 -> 1.0
#learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

token : 0.9255195243057684
chunk : 0.9179514442672337
conlleval : 91.65

* test 16
#word embedding size : 100(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.9
keep_prob : 0.7 -> 0.9
#chr_conv_type : conv1d
#chracter embedding size : 25
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 53
#pos embedding size : 7
#pos embedding random init : -0.5 ~ 0.5
#chk embedding size : 10
#chk embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256 -> 200
rnn_num_layers : 2 -> 1
#learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
#gradient clipping : 1.5 -> 10
learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 10
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

# epoch 10
token : 0.9307875894988067
chunk : 0.9220033565939405
conlleval : 91.97

# epoch 4
token : 0.9273462386669934
chunk : 0.9191677733510403
conlleval : 91.67

# epoch 10
token : 0.9275397796817625
chunk : 0.9186036235086168
conlleval : 91.78

* test 15
#word embedding size : 100(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.9
#keep_prob : 0.7
#chr_conv_type : conv1d
#chracter embedding size : 25
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 53
#pos embedding size : 7
#pos embedding random init : -0.5 ~ 0.5
#chk embedding size : 10
#chk embedding random init : -0.5 ~ 0.5
rnn_used : True -> False
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
#learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
#gradient clipping : 1.5 -> 10
learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 4 -> 10
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : True

# lr 2e-5, bs 16
token : 0.929012534393152
chunk : 0.9215426705498191
conlleval : 92.00          -> BERT large + CRF best

# same setting + epoch 70
token : 0.9241430060710124
chunk : 0.9144678590401983
conlleval : 91.36

* test 14
#word embedding size : 100(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.9
#keep_prob : 0.7
#chr_conv_type : conv1d
#chracter embedding size : 25
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 53
#pos embedding size : 7
#pos embedding random init : -0.5 ~ 0.5
#chk embedding size : 10
#chk embedding random init : -0.5 ~ 0.5
rnn_used : True -> False
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
#learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
#gradient clipping : 1.5 -> 10
learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1 -> 2e-5, 3e-5, 5e-5
epoch : 4
batch_size : 16 -> 16, 32
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
#CRF
+
do_shuffle : True

# lr 2e-5, bs 16
token : 0.9291608092414889
chunk : 0.9220033565939405
conlleval : 91.82          -> BERT large + Softmax best
-> repair (begining 'I-' and 'X')
token : 0.9298879431755558
chunk : 0.9220033565939405
conlleval : 91.82

# lr 2e-5, bs 32
token : 0.925267338832875
chunk : 0.9168650268888302
conlleval : 91.29

# lr 3e-5, bs 16
token : 0.9251850492445096
chunk : 0.9159092914497485
conlleval : 91.26

# lr 3e-5, bs 32
token : pass
chunk : pass
conlleval : pass

# lr 5e-5, bs 16
token : 0.9269876270978806
chunk : 0.9181456953642385
conlleval : 91.52

# lr 5e-5, bs 32
token : 0.9251025782350419
chunk : 0.9154518950437317
conlleval : 91.24

* test 13
word embedding size : 100(glove6b)
bert embedding : cased_L-12_H-768_A-12
bert_keep_prob : 0.8
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5 -> 10
#learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : False -> True

token : 0.917588123892724
chunk : 0.9089466725429706
conlleval : 90.75
average processing time per bucket(sentence)
  - 1 GPU(TITAN X PASCAL) : 0.03662970762428839


* test 12
word embedding size : 300(glove6B) -> 100(glove6b)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5 -> 10
#learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9243863327988158
chunk : 0.9169861792242533
conlleval : 91.44
average processing time per bucket(sentence)
  - 1 GPU(V100) :  0.040497000132010894 sec

* test 11
word embedding size : 300(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
#learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
#gradient clipping : 1.5
learning_rate : use optimization.py from bert, 2e-5 / warmup proportion 0.1
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9240039350713232
chunk : 0.9142300194931774


* test 10
word embedding size : 300(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8 -> 0.9
keep_prob : 0.7 -> 0.8
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9 -> 1e-4
gradient clipping : 1.5
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9242442785460777
chunk : 0.9142150366640163

* test 9
word embedding size : 300(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
keep_prob : 0.7 -> 0.32
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 16 -> 10
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9198576337751595
chunk : 0.9114214992927864

* test 8
word embedding size : 300(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256 -> 512
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9237002025658338
chunk : 0.91440205364256

* test 7
word embedding size : 300(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True -> False
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 16
+
tf_used : False -> True
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9244949032533724
chunk : 0.9170714474962465 -> Glove(6B) + BERT large + CNN + Transformer + CRF best

* test 6
word embedding size : 300(glove6B) -> 300(glove840B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9187365838699787
chunk : 0.9078341013824885

* test 5
#word embedding size : 300(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
keep_prob : 0.7
#chr_conv_type : conv1d
#chracter embedding size : 50
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 25
#pos embedding size : 7
#pos embedding random init : -0.5 ~ 0.5
rnn_used : True -> False
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
#CRF

# BERT only(no glove, no cnn, no lstm, no crf)
token : 0.9275558564658091
chunk : 0.9169470515317868

* test 4
#word embedding size : 300(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
keep_prob : 0.7
#chr_conv_type : conv1d
#chracter embedding size : 50
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 25
#pos embedding size : 7
#pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9270596895895958
chunk : 0.9180153886972672

* test 3
word embedding size : 300(glove6B)
bert embedding : cased_L-24_H-1024_A-16
bert_keep_prob : 0.8
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9278869778869779
chunk : 0.918813634351483 -> Glove(6B) + BERT large + CNN + LSTM + CRF best

* test 2
word embedding size : 300(glove6B)
bert embedding : cased_L-12_H-768_A-12
bert_keep_prob : 0.8
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.921535076998289
chunk : 0.9123210182075304 -> Glove(6B) + BERT base + CNN + LSTM + CRF best

* test 1
#word embedding size : 300(glove6B)
bert embedding : cased_L-12_H-768_A-12
bert_keep_prob : 0.8
keep_prob : 0.7
#chr_conv_type : conv1d
#chracter embedding size : 50
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 25
#pos embedding size : 7
#pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 2e-5 / 5000 / 0.9
gradient clipping : 1.5
epoch : 70
batch_size : 16
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9234725113260683
chunk : 0.9131509267431598 -> BERT base + LSTM + CRF best

```

- experiments 10
```
* test 17
word embedding size : 100(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
highway : False
highway dropout : keep_prob
rnn_used : True
rnn_type : fused
rnn_size : 200 -> 250
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : False -> True

token : 0.9260371346283474
chunk : 0.9202475685234306
conlleval : 92.02
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.04172190127491822 sec

* test 16
word embedding size : 100(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
chk embedding size : 10
chk embedding random init : -0.5 ~ 0.5
highway : False
highway dropout : keep_prob
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF
+
do_shuffle : False -> True

# trial 1
token : 0.9297237839159129
chunk : 0.924091828656874
conlleval : 92.40
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.036901780694367184 sec

# trial 2
token : 0.927712322042219
chunk : 0.9243876464323749
conlleval : 92.46
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.038546528412387114 sec

# trial 3
token : 0.9302496328928046
chunk : 0.9256344504377046
conlleval : 92.56
average processing time per bucket(sentence)
  - 1 GPU(V100 TESLA) : 0.03891986110181943 sec


* test 15
word embedding size : 300(glove6B) -> 100(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
highway : False
highway dropout : keep_prob
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

# trial 1
token : 0.9289991445680068
chunk : 0.924080768891632

# trial 2
token : 0.9319326698611623
chunk : 0.9258044499601098

# trial 3
token : 0.9295585177938118
chunk : 0.9231721333215455

# trial 4
token : 0.931816792025928
chunk : 0.9268680445151033 -> Glove(6B) + ELMo + CNN + LSTM + CRF best

# trial 5
token : 0.9280303030303031
chunk : 0.9223438051535474

# average 1,..,5
token : 0.930067485455842
chunk : 0.924453840368388 

# trial 6
token : 0.9298031062736946
chunk : 0.9242330474759083

# trial 7
token : 0.9288692666176109
chunk : 0.9229543039319873

# trial 8
token : 0.9310681984844782
chunk : 0.9245416078984485

# trial 9
token : 0.9304884758818854
chunk : 0.92371534522338

# trial 10
token : 0.9318654434250764
chunk : 0.9253942938153464

# averge 1,...,10
token : 0.93044691
chunk : 0.9245217835

# extra trial 1
token : 0.930668791761172
chunk : 0.9239341942331505
conlleval : 92.34
average processing time per bucket(sentence)
  - 1 GPU(V100 TELSA) :0.0385546259719567 sec

# extra trial 2
token : 0.9321836971809455
chunk : 0.9266184512259658
conlleval : 92.64

* test 14
word embedding size : 300(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7 -> 0.32
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
highway : False
highway dropout : keep_prob
rnn_used : True
rnn_type : fused
rnn_size : 256 -> 276
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20 -> 10
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9285190615835778
chunk : 0.9224922669023421

* test 13
word embedding size : 300(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
highway : False
highway dropout : keep_prob
rnn_used : True
rnn_type : fused
rnn_size : 200 -> 256
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9285013490311503
chunk : 0.9224482544194723

* test 12
word embedding size : 300(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
highway : False -> True
highway dropout : keep_prob
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9254662182818709
chunk : 0.9184397163120568

* test 11
word embedding size : 300(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
highway : False
highway dropout : keep_prob
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9277366456586918
chunk : 0.9221376747478321

* test 10
word embedding size : 300(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50 -> 25
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25 -> 53
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
highway : False -> True
rnn_used : True
rnn_type : fused
rnn_size : 200 -> 400
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9247654669201054
chunk : 0.9190915542938254

* test 9
word embedding size : 300(glove6B) -> 300(glove840B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
#chr_conv_type : conv1d
#chracter embedding size : 50
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.923434726727462
chunk : 0.9179051663128095

* test 8
word embedding size : 300(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True -> False
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9 -> 0.0003
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False -> True
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9272257111193203
chunk : 0.9184724689165186 -> Glove(6B) + ELMo + CNN + Transformer + CRF best

* test 7
word embedding size : 300(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9 -> 0.0003
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False -> True
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9226059270144501
chunk : 0.9152152771638229

* test 6
word embedding size : 300(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200 -> 300
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9241421196477377
chunk : 0.9194512838550827

* test 5
word embedding size : 300(glove6B)
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

# trial 1
token : 0.9280469897209985
chunk : 0.9212688875143589

# trial 2
token : 0.9270737820160156
chunk : 0.9221662691050446

# trial 3
token : 0.92896509491733
chunk : 0.9235392910810573

# trial 4
token : 0.9258261933904528
chunk : 0.9212528755972395

# trial 5
token : 0.9266772577294391
chunk : 0.9211896566940252


* test 4
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
#chr_conv_type : conv1d
#chracter embedding size : 50
#chracter embedding random init : -1.0 ~ 1.0
#filter_sizes : [3]
#num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9262964099416999
chunk : 0.9179978700745474

* test 3
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7 -> 0.5
keep_prob : 0.7 -> 0.5
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.924035934730795
chunk : 0.9174620007069636

* test 2
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
elmo_keep_prob : 0.7
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.924101686629186
chunk : 0.9174117022218288

* test 1
word embedding size : 300(glove6B)
keep_prob : 0.7
chr_conv_type : conv1d
chracter embedding size : 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 25
pos embedding size : 7
pos embedding random init : -0.5 ~ 0.5
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9129239230064161
chunk : 0.9063326865408361

```


- experiments 9
```
* test 7
word embedding size : 300(glove840B) -> 100(glove6B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100 -> 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50 -> 25
pos embedding size : 6 -> 7
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.8986217457886677
chunk : 0.8906723738184412

* test 6
word embedding size : 300(glove840B) -> 100(glove6B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.8900472189857117
chunk : 0.8782570031124943

* test 5
word embedding size : 300(glove840B) -> 300(glove6B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100 -> 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50 -> 25
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5 -> not used
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200 -> 100
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.8973603437691837
chunk : 0.8835348506401138

* test 4
word embedding size : 300(glove840B) -> 300(glove6B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100 -> 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50 -> 25
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5 -> not used
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9001650669438162
chunk : 0.8887512169218514

* test 3
word embedding size : 300(glove840B) -> 100(glove6B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100 -> 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50 -> 25
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5 -> not used
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.8949877750611247
chunk : 0.8858156028368794

* test 2
word embedding size : 300(glove840B) -> 100(glove6B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100 -> 50
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50 -> 25
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5 -> not used
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200 -> 100
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.8915692307692308
chunk : 0.8800214247455811

* test 1
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9152852267186738
chunk : 0.9094911075893644 -> Glove(840B) + CNN + LSTM + CRF best

```

- experiments 8
```
* test 4
keep_prob : 0.5
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
using elmo dropout : keep_prob
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2 -> 1
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9283657086831301
chunk : 0.9224785644833378

* test 3
keep_prob : 0.5
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
using elmo dropout : keep_prob
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200 -> 100
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9300104096503582
chunk : 0.9225059644782186

* test 2
keep_prob : 0.5
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
using elmo dropout : keep_prob
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

# train 1
token : 0.9322728663199756
chunk : 0.9253625751680227 -> ELMo + CNN + etc feature + LSTM + CRF best

# trial 2
token : 0.9282793139229689
chunk : 0.922873045322025

# trial 3
token : 0.9265253771453001
chunk : 0.9207247017233762

# trial 4
token : 0.9265571358509073
chunk : 0.9206939281288724

* test 1
keep_prob : 0.5
elmo embedding params : elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
elmo embedding size : 1024
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.923971596474045
chunk : 0.9175303392683143

```

- experiments 7
```

* test 11
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : False
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.0003 / 12000 / 0.7 -> 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : True
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64 -> 128
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9016393442622951
chunk : 0.8987274655355251

* test 10
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : False -> True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.0003 / 12000 / 0.7 -> 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : True
tf_keep_prob : 0.8
tf_mh_num_layers : 4 -> 1
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.910979409787988
chunk : 0.9047451049567825 -> Glove(840B) + CNN + etc feature + LSTM + Transformer + CRF best

* test 9
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : False
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.0003 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : True
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 3
+
save model by f1(token)
+
CRF

token : 0.9083215796897038
chunk : 0.904078014184397  -> Glove(840B) + CNN + etc feature + Transformer + CRF best

* test 8
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : False
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.0003 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : True
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
tf_ffn_kernel_size : 1 -> 3
=> change num_units in '__feedforward()' to '[4*model_dim, model_dim]'
=> add masking operation to 'before multihead_attention()', 'inside feedforward()'
+
save model by f1(token) -> f1(chunk)
+
CRF

token : 0.9002635934530743
chunk : 0.8959943156585842

* test 7
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : False
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.0003 / 12000 / 0.9 -> 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : True
tf_keep_prob : 0.8
tf_mh_num_layers : 4 -> 5
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
+
save model by f1(token) -> f1(chunk)
+
CRF
+
bug fix for masking

token : 0.8919512195121951
chunk : 0.8836309262028323

* test 6
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : False
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7 -> 0.0003 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : True
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
+
positional encoding at the begining of every blocks
+
save model by f1(token) -> f1(chunk)
+
CRF

token : 0.8925447984832733
chunk : 0.8813469675599436

* test 5
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : False
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7 -> 0.0003 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : True
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
+
save model by f1(token) -> f1(chunk)
+
CRF

token : 0.8964842555793334
chunk : 0.886369628262589


* test 4
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : False
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7 -> 0.0003 / 12000 / 0.9
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : True
tf_keep_prob : 0.8
tf_mh_num_layers : 4
tf_mh_num_heads : 4
tf_mh_num_units : 64 -> 128
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
+
save model by f1(token)
+
CRF

token : 0.8663967611336032
chunk : 0.8577638671535385

* test 3
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : False
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : True
tf_keep_prob : 0.5 -> 0.8
tf_mh_num_layers : 1 -> 3
tf_mh_num_heads : 4
tf_mh_num_units : 64
tf_mh_keep_prob : 0.8
tf_ffn_keep_prob : 0.8
+
save model by f1(token)
+
CRF

token : 0.8836723406870276
chunk : 0.8729698885084716

* test 2
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : False
tf_mh_num_layers : 1
tf_mh_num_heads : 4
tf_mh_num_units : 32
tf_keep_prob : 0.5
+
save model by f1(token)
+
CRF

token : 0.9132052455016773
chunk : 0.9064951088393407

* test 1
word embedding size : 300(glove840B)
keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos one-hot : 5
shape vec : 9
rnn_used : True
rnn_type : fused
rnn_size : 200
rnn_num_layers : 2
learning_rate : exponential_decay(), 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
tf_used : True
tf_mh_num_layers : 1
tf_mh_num_heads : 4
tf_mh_num_units : 32
tf_keep_prob : 0.5
+
save model by f1(token)
+
CRF

token : 0.9109902865171972
chunk : 0.905463853826463

```

- experiments 6
```
* test 13 ( == same setting with test 7)
word embedding size : 300(glove840B)
wrd_keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : fused
rnn_size : 200
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.913468589586898
chunk : 0.9075200564224631

* test 12
word embedding size : 300(glove840B)
wrd_keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : fused
rnn_size : 200
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001 -> 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9155697055041939
chunk : 0.9095246509984096

* test 11
word embedding size : 300(glove840B)
wrd_keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 30 -> 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 50
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : fused
rnn_size : 200
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001 -> 0.001 / 12000 / 0.7
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9136721371484351
chunk : 0.9099091149739699

* test 10
word embedding size : 300(glove840B)
wrd_keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 30 -> 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30 -> 50
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : fused
rnn_size : 200 -> 100
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9117467302285784
chunk : 0.9078377661924539

* test 9
word embedding size : 300(glove840B)
wrd_keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 30 -> 100
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30 -> 50
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : fused
rnn_size : 200 -> 100
num_layers : 2 -> 1
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9119120342089188
chunk : 0.9059798906332687

* test 8
word embedding size : 300(glove840B)
wrd_keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : fused
rnn_size : 200
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by : f1(token) -> f1(chunk)
+
CRF

token : 0.9131098491787263
chunk : 0.9068618804021874

* test 7
word embedding size : 300(glove840B)
wrd_keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : fused
rnn_size : 200
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9157317073170732
chunk : 0.9102156238953694 -> Glove(840B) + CNN + etc feature + LSTM + multi-head attention + CRF best

# re-run #
token : 0.9121906507791018
chunk : 0.9068618804021874

* test 6
word embedding size : 100
wrd_keep_prob : 0.5
chr_conv_type : conv1d
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : fused
rnn_size : 200
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9128493670111919
chunk : 0.9066360748323333

* test 5
word embedding size : 100
wrd_keep_prob : 0.5
chr_conv_type : conv2d
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : fused
rnn_size : 200
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9087149546919662
chunk : 0.9053483462350458

* test 4
word embedding size : 100
wrd_keep_prob : 0.5
chr_conv_type : conv2d -> conv1d
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : normal
rnn_size : 200
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9075067024128687
chunk : 0.9050426823902139

* test 3
word embedding size : 100
wrd_keep_prob : 0.5
chr_conv_type : conv2d with __conv2d masking__
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : normal
rnn_size : 200
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9098120576031243
chunk : 0.905320744727786

* test 2
word embedding size : 100
wrd_keep_prob : 0.5
chr_conv_type : conv2d
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 6
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_type : normal
rnn_size : 200
num_layers : 2
rnn_keep_prob : 0.5
learning_rate : 0.001 / 15000 / 1.0, exponential_decay() => fixed 0.001
gradient clipping : 10
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9138489758483644
chunk : 0.9082082965578112

* test 1
word embedding size : 100 -> 300 (Glove840B)
wrd_keep_prob : 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
rnn_keep_prob : 0.5
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9063109161793372
chunk : 0.900184680327148

```

- experiments 5
```
* test 8
word embedding size : 100
wrd_keep_prob : 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_size : 200
num_layers : 2 -> 1
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
rnn_keep_prob : 0.5
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.9107797604497677
chunk : 0.9061231692253398

* test 7
word embedding size : 100
wrd_keep_prob : 0.5 -> new (loss decreases more smoothly)
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
filter_sizes : [3]
num_filters : 30
chr_keep_prob : 0.5
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
pos_keep_prob : 0.5
pos one-hot : 5
shape vec : 9
rnn_size : 200
num_layers : 2 -> use multiple bidirectional_dynamic_rnn() -> 2 times slower than tf.contrib.rnn.MultiRNNCell() with tf.contrib.rnn.static_bidirectional_rnn()
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
rnn_keep_prob : 0.5
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.91112196313
chunk : 0.90743845407


* test 6
word embedding size : 100 -> 200
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 (fixed)
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token)
+
CRF

token : 0.900907530047
chunk : 0.891468060600

* test 5
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 20
+
save model by f1(token)
+
CRF

token : 0.905106800884
chunk : 0.898973814578

* test 4
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(chunk)
+
CRF

token : 0.908800785565
chunk : 0.900097164561

* test 3
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token), bug fix for token_eval.compute_f1()
+
CRF

token : 0.909514467876
chunk : 0.901569941788

* test 2
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token), bug fix for token_eval.compute_f1()
+
CRF(loss only)

token : 0.904864135435
chunk : 0.889849955869

* test 1
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(chunk)

token : 0.906159975483
chunk : 0.890888242039

```

- experiments 4
```
* test 10
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 128 -> 20
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()
+
save model by f1(token), mis-setting for out of class id in token_eval.compute_f1()

token : 0.906612635845
chunk : 0.895862800565 -> this is a coincidence by the mis-setting

* test 9
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9  -> 9 (disjoint upperInitial and mixedCaps), fixed after this setting
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 128 -> 64
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.901891180611
chunk : 0.886795774647

* test 8
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.903553921569
chunk : 0.886343612334

* test 7
word embedding size : 100
#pos embedding
#pos embedding size : 5
#pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
#pos_keep_prob : 0.5
epoch : 70
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.900515210991
chunk : 0.884615384615

* test 6
word embedding size : 100
#pos embedding
#pos embedding size : 5
#pos embedding random init : -0.5 ~ 0.5
#chracter embedding size : 30
#chracter embedding random init : -1.0 ~ 1.0
pos one-hot : 5
shape vec : 9
#filter_size : 3
#num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
#cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
#pos_keep_prob : 0.5
epoch : 70
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.895365211535
chunk : 0.8775977456851004

* test 5
word embedding size : 100
#pos embedding
#pos embedding size : 5
#pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
#pos one-hot : 5
shape vec : 5 -> 9
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
#pos_keep_prob : 0.5
epoch : 70 -> 80
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.901030169242
chunk : 0.8844185636139051

* test 4
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 8
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.902409196527
chunk : 0.885191054763

* test 3
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 8
mh_num_units : 64
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.899779735683
chunk : 0.884354938000

* test 2
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 30
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3
num_filters : 30
rnn_size : 200
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 70
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.901651376147
chunk : 0.886935115174

* test 1
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96 -> 30
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3
num_filters : 32 -> 30
rnn_size : 256 -> 200
num_layers : 2 -> 1
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.7 -> 0.5
rnn_keep_prob : 0.32 -> 0.5
pos_keep_prob : 0.5
epoch : 50 -> 70
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.901541674344
chunk : 0.884938533651

```

- experiments 3
```
* test 13
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.7
rnn_keep_prob : 0.32
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.900360878341
chunk : 0.886441723196

* test 12
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.7
rnn_keep_prob : 0.32
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 2
mh_num_units : 32
mh_dropout : 0.5
normalize() instead of layer_norm()

token : 0.898353833915
chunk : 0.8851071334097523

* test 11
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3
num_filters : 32
rnn_size : 500
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.7
rnn_keep_prob : 0.32
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 2
mh_num_units : 32
mh_dropout : 0.5
without layer norm

token : 0.889773423148
chunk : 0.877369302653619

* test 10
word embedding size : 100
pos embedding
shape vec
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 2
mh_num_units : 32
mh_dropout : 0.5

token : 0.895744811873
chunk : 0.8798867857774633

* test 9
word embedding size : 100
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3
num_filters : 32
rnn_size : 500
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.7
rnn_keep_prob : 0.32
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 2
mh_num_units : 32
mh_dropout : 0.5

token : 0.897407543924
chunk : 0.8832155477031802

* test 8
word embedding size : 300
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3
num_filters : 32
rnn_size : 500
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.7
rnn_keep_prob : 0.32
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 2
mh_num_units : 32
mh_dropout : 0.5

token : 0.896001962227
chunk : 0.8801692972401023

* test 7
word embedding size : 300
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 4
mh_num_units : 32
mh_dropout : 0.5

0.895288278904

* test 6
word embedding size : 300
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 2
mh_num_units : 32
mh_dropout : 0.5

0.896419516418

* test 5
word embedding size : 300
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 20
cnn_keep_prob : 0.5
rnn_keep_prob : 0.8
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 2
mh_num_units : 32
mh_dropout : 0.5

0.897379106681

* test 4
word embedding size : 300
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.0001, intermid_epoch = 10
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 1
mh_num_units : 32
mh_dropout : 0.5

0.893447642376

* test 3
word embedding size : 300
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.0001 -> 0.0002 (change), intermid_epoch = 15
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention(softmax with masking)
mh_num_heads : 2
mh_num_units : 32
mh_dropout : 0.2

0.881420496436

* test 2
word embedding size : 300
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention
mh_num_heads : 2
mh_linear_key_dim : 32
mh_linear_val_dim : 32
mh_dropout : 0.5

0.896346749226

* test 1
word embedding size : 300
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
pos_keep_prob : 0.5
epoch : 50
batch_size : 128
+
multi head attention
mh_num_heads : 1
mh_linear_key_dim : 32
mh_linear_val_dim : 32
mh_dropout : 0.5

0.894368789106

```

- experiments 2
```
* test 17
word embedding size : 300
pos embedding
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.002 (change), intermid_epoch = 15
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128

0.890206249228

* test 17
word embedding size : 300
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
shape vec
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.002 (change), intermid_epoch = 15
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128

0.893637926799

* test 16
word embedding size : 300
pos embedding
pos embedding size : 5
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.002 (change), intermid_epoch = 15
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128

0.891214677092

* test 15
word embedding size : 300
remove pos embedding
pos embedding size : 10
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.002 (change), intermid_epoch = 15
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128

0.887810272794

* test 14
word embedding size : 300
remove pos embedding
pos embedding size : 50
pos embedding random init : -0.5 ~ 0.5
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.002 (change), intermid_epoch = 15
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128

0.886979997546

* test 13
word embedding size : 300
word embedding trainable : True
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.002 (change), intermid_epoch = 15
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128

0.859092036715


* test 12
word embedding size : 300
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.002 (change), intermid_epoch = 15
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128

0.895851286471

* test 11
word embedding size : 300
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128
+
longest matching gazetteer feature(ignore length less than 10)

0.876311566473

* test 10
word embedding size : 300
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001 -> 0.002 (change), intermid_step = 1000
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128
+
longest matching gazetteer feature(ignore length less than 10)

0.888393410133

* test 9
word embedding size : 300
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.0001 -> 0.001 (change), intermid_step = 1000
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128

0.886325787948

* test 8
word embedding size : 300
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128
+
longest matching gazetteer feature(without MISC)

0.866472158421

* test 7
word embedding size : 300
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128

0.892918613228

* test 6
replace all digit to '0'
word embedding size : 300
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128
+
longest matching gazetteer feature(from test data)

0.913716137712

=> ok. this result supports that gazetteer features are very helpful. but, 
if we construct gazetteer vocab from the training data, the f-score decreases.

* test 5
replace all digit to '0'
word embedding size : 300
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128
+
longest matching gazetteer feature

0.870375031462

* test 4
replace all digit to '0'
word embedding size : 300
chracter embedding size : 96
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 128

0.890053001356

* test 3
replace all digit to '0'
random shuffling
word embedding size : 300
chracter embedding size : 53
chracter embedding random init : -1.0 ~ 1.0
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.5
rnn_keep_prob : 0.5
epoch : 50
batch_size : 64
+
longest matching gazetteer feature

0.87932312253

* test 2
replace all digit to '0'
random shuffling
word embedding size : 50
chracter embedding size : 64
chracter embedding random init : -0.5 ~ 0.5
filter_size : 3,4,5
num_filters : 32
rnn_size : 256
num_layers : 2
learning_rate : 0.001
cnn_keep_prob : 0.32
rnn_keep_prob : 0.32
epoch : 50
batch_size : 64

0.881000551775

* test 1
replace all digit to '0'
random shuffling
word embedding size : 50
chracter embedding size : 64
chracter embedding random init : -0.5 ~ 0.5
filter_size : 3
num_filters : 48
rnn_size : 256
num_layers : 1
learning_rate : 0.001
cnn_keep_prob : 0.32
rnn_keep_prob : 0.32
epoch : 64
batch_size : 64

0.884797152151

```

- experiments 1
```
* weak entity types : B-ORG, I-ORG, B-MISC, I-MISC

* chr_embedding : max

rnn_size : 256, keep_prob : 0.5, chr_embedding : max
0.892409321671

* chr embedding : conv

rnn_size : 256, keep_prob : 0.5, chr_embedding : conv
0.895172667607
0.893800406329
0.892967114177
0.893781430148

rnn_size : 256, cnn_keep_prob : 0.7, rnn_keep_prob : 0.8, chr_embedding : conv
0.892371739929

rnn_size : 256, cnn_keep_prob : 0.6, rnn_keep_prob : 0.6, chr_embedding : conv
0.893224198412

* gazetteer feature

rnn_size : 256, keep_prob : 0.5, chr_embedding : conv, gazetteer : token-based m-hot vector
0.855807086614

rnn_size : 512, keep_prob : 0.5, chr_embedding : conv, gazetteer : token-based m-hot vector
0.873537604457

rnn_size : 256, keep_prob : 0.5, chr_embedding : conv, gazetteer : token-based 0|1
0.877048661647

even though we use '0|1' indicating gazetteer, it is worse than basic models.
the loss is even increasing along steps. why?

try to adjust keep_probs.
rnn_size : 256, cnn_keep_prob : 0.8, rnn_keep_prob : 0.8, chr_embedding : conv, gazetteer : token-based 0|1
0.879918632001

try to filter digit/ascii symbol/short word from gazetteer vocab.
rnn_size : 256, cnn_keep_prob : 0.8, rnn_keep_prob : 0.8, chr_embedding : conv, gazetteer : token-based 0|1
0.877144298688

use m-hot vector and apply unambiguous gazetteer only
rnn_size : 256, cnn_keep_prob : 0.8, rnn_keep_prob : 0.8, chr_embedding : conv, gazetteer : token-based m-hot vector
0.883349826818

including unambiguous 'O' gazetteer
rnn_size : 256, cnn_keep_prob : 0.8, rnn_keep_prob : 0.8, chr_embedding : conv, gazetteer : token-based m-hot vector
0.878849345381
```
