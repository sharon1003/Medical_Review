import pandas as pd
import numpy as np
import time
from datetime import timedelta

#切句模組
import jieba
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import os
from django.conf import settings
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0' # 所有訊息 
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' # 警告(WARNING)、錯誤(ERROR)
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # 錯誤(ERROR)
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # 致命錯誤(FATAL)

os.environ["CUDA_VISIBLE_DEVICES"] = ""

#CNN
from tensorflow import keras 
from tensorflow.keras.models import Sequential  #用來啟動 NN
from tensorflow.keras.layers import Conv2D  # Convolution Operation
from tensorflow.keras.layers import MaxPooling2D # Pooling
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense # Fully Connected Networks
from tensorflow.keras.layers import Dropout

from sklearn.pipeline import Pipeline
import pickle

stopword = open(os.path.join(settings.MODULE_FILE, "Jieba_File/stopword.txt"), 'r', encoding='utf-8')

def input_cut(word):
    vocabulary = []
    rule = re.compile(r"[^\u4E00-\u9FA5]")
    for s in word:
        text = rule.sub('', str(s))
        vocabulary.append(list(jieba.cut(text)))
    #去掉stopword，並整理資料型態
    for index, w in enumerate(vocabulary):
        tmp = []
        for voc in w:
            if voc not in stopword:
                tmp.append(voc.strip())
    return tmp


# 載入模型
model_save_path = os.path.join(settings.PROJECT_FILE, "CNN.h5")
train_model = keras.models.load_model(model_save_path)

def CNN(review):
    print("\nPlease enter your sentence:")
    Sen = review

    A = [Sen]

    dict = pickle.load(open(os.path.join(settings.PROJECT_FILE, "bag_of_word.pickle"), 'rb'))
    input_array = [0] * 18254
    A = input_cut(A)
    for i in range(18254):
        while dict[i] in A:
            A.remove(dict[i])
            input_array[i] += 1

    A = np.reshape(input_array, (-1, 18254, 1, 1))
    result = train_model.predict(A)
    # print(result)
    rate = [0.32, 0.035, 0.1, 0.05, 0.1, 0.15, 0.03]
    aspect = []
    for i in range(7):
        if result[0][i] >= rate[i]:
            print("1", end='\t')
            aspect.append(i+1)
        else:
            print("0", end='\t')

    print('面向', aspect)
    print()

    return aspect # 回傳的是list型態
