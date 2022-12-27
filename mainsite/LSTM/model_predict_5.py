# -*- coding: utf-8 -*-

# Import the necessary modules
import pickle
import numpy as np
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from django.conf import settings
import os


# 導入字典
with open(os.path.join(settings.PROJECT_FILE, "word_dict_5.txt"), 'rb') as f:
    word_dictionary = pickle.load(f)
with open(os.path.join(settings.PROJECT_FILE, "label_dict.txt"), 'rb') as f:
    output_dictionary = pickle.load(f)

def predict(review):
    try:
        # 數據預處理
        input_shape = 100
        sent = review
        x = [[word_dictionary[word] for word in sent]]
        x = pad_sequences(maxlen=input_shape, sequences=x, padding='post', value=0)

        # 載入模型
        model_save_path = os.path.join(settings.PROJECT_FILE, "corpus_model_5.h5")
        lstm_model = load_model(model_save_path)

        # 模型預測
        y_predict = lstm_model.predict(x)
        label_dict = {v:k for k,v in output_dictionary.items()}

        # 得到正、負、中立等字串，label_dict[np.argmax(y_predict) 
        print("\n流程體驗")
        ans = -100
        if label_dict[np.argmax(y_predict)] == '正':
            print("預測分數為", 1)
            ans = 1
        elif label_dict[np.argmax(y_predict)] == '負':
            print("預測分數為", -1)
            ans = -1
        else:
            print("預測分數為", 0)
            ans = 0

    except KeyError as err:
        print("您輸入的句子有不在詞彙表中，請重新輸入！")
        print("不在詞彙表中的單詞為：%s." % err)
        ans = -2

    return ans