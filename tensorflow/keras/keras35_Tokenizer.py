from tensorflow.keras.preprocessing.text import Tokenizer

text = "나는 진짜 진짜 맛있는 밥을 마구 마구 먹었다."

token = Tokenizer()
token.fit_on_texts([text]) #어절 순으로 토큰화해서 잘라내고 숫자매김.

print(token.word_index)
# {'진짜': 1, '마구': 2, '나는': 3, '맛있는': 4, '밥을': 5, '먹었다': 6}

x = token.texts_to_sequences([text]) #입력된 문장의 단어 순서를 숫자로 나타내줌.
print(x)
# [[3, 1, 1, 4, 5, 2, 2, 6]] 
#어떤 분석을 하든 모든걸 숫자로 바꾸는 것(수치화)

from tensorflow.keras.utils import to_categorical
word_size = len(token.word_index) #6
x = to_categorical(x)
print(x)
print(x.shape)# (1, 8, 7)
# 원래 (1, 8, 6) 이어야 하지만 시작이 0부터 시작해서 8, 7이 된 것...
# 한 문장이 3차원 데이터셋이 됨. 
# 문장이 10개라면, (10, 1, 8, 7) 이 되었을것

'''
[[[0. 0. 0. 1. 0. 0. 0.]
  [0. 1. 0. 0. 0. 0. 0.]
  [0. 1. 0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 1. 0. 0.]
  [0. 0. 0. 0. 0. 1. 0.]
  [0. 0. 1. 0. 0. 0. 0.]
  [0. 0. 1. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0. 0. 1.]]]

가로 길이 : 들어있는 총 단어 갯수 길이 (+1) / 많이 들어있는 순서, 중복 제외
세로 길이 : 문장에 들어있는 단어 갯수만큼 / 나열 순서대로, 중복 포함

단어가 100만 종류 있다면 쓸데없는 0이 너무 많음 ( 데이터 너무 많아짐)
평면에 좌표로 나타내서 줄일 수 있다면(벡터화) 100만, 100만을 100만, 2 로까지 바꿔줄 수 있음!
즉, 우리가 전처리를 통해 데이터를 늘리거나 줄일 수 있다. : Embedding 
'''
 