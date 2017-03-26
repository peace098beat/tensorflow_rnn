# tensorflow_rnn
Tensorflow r1.0で動作するRNN解析環境

## ロードマップ

* sin波の予測
* ローレンツ方程式の予測
* Bitcoinの予測


## 基本機能
# 乱数シード
seed: 0
# 学習データのパス
train_data_path: "../train_data/normal.npy"
# 入力層のノード数
num_of_input_nodes: 1
# 隠れ層のノード数
num_of_hidden_nodes: 2
# 出力層のノード数
num_of_output_nodes: 1
# RNNのシーケンス長
length_of_sequences: 50
# 学習の繰り返し回数
num_of_training_epochs: 2000
# 予測の繰り返し回数
num_of_prediction_epochs: 100
# ミニバッチあたりのサンプル数
size_of_mini_batch: 100
# 学習率
learning_rate: 0.1
# （よく分かっていません）
forget_bias: 1.0
# オプティマイザ
optimizer: "AdamOptimizer"