import jieba
import pandas as pd
import numpy as np
import re
import csv
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB 
from sklearn.metrics import classification_report, confusion_matrix
import os
from django.conf import settings

# 取得檔案資料
def get_data(sentence, stopword):

	# 刪除「非中文字」的char並搭配使用jieba分詞
	word = []
	rule = re.compile(r"[^\u4e00-\u9fa5]")
	s = rule.sub('', sentence) # 將「非中文字母」去掉並替換成'' 
	word = list(jieba.cut(s))
	# print(word)

	# 刪除stopword
	tmp = []
	for voc in word:
		if voc not in stopword:
			tmp.append(voc.strip())
	w = ' '.join(tmp)
	words = []
	words.append(w)
	# print(words)

	return words


def predict_model_1(review):
	# jieba.load_userdict(os.path.join(settings.PROJECT_FILE, "dict.txt.big")) #使用user自訂的字典，需要在setting定義路徑，這樣manage.py才看得懂
	with open(os.path.join(settings.MODULE_FILE, "Jieba_File/stopword.txt"), 'r', encoding='utf-8') as fin:
		with open(os.path.join(settings.MODULE_FILE, "bayes_model_1.pickle"), 'rb') as bayes_model:

			stopword = fin.read().split('\n')

			review = get_data(str(review), stopword)
			mult_bayse_model = pickle.load(bayes_model)

			# 因為model也同時包含countvec所以不用做多餘的轉換
			print('\n醫療評價 predicted: ', mult_bayse_model.predict(review)) 
			predict_ans = mult_bayse_model.predict(review)
			return predict_ans


def predict_model_2(review):
	# jieba.load_userdict(os.path.join(settings.PROJECT_FILE, "dict.txt.big")) #使用user自訂的字典，需要在setting定義路徑，這樣manage.py才看得懂
	with open(os.path.join(settings.MODULE_FILE, "Jieba_File/stopword.txt"), 'r', encoding='utf-8') as fin:
		with open(os.path.join(settings.MODULE_FILE, "bayes_model_2.pickle"), 'rb') as bayes_model:

			stopword = fin.read().split('\n')

			review = get_data(str(review), stopword)
			mult_bayse_model = pickle.load(bayes_model)
			
			# 因為model也同時包含countvec所以不用做多餘的轉換
			print('\n交通方便 predicted: ', mult_bayse_model.predict(review)) 
			predict_ans = mult_bayse_model.predict(review)
			return predict_ans

def predict_model_3(review):
	# jieba.load_userdict(os.path.join(settings.PROJECT_FILE, "dict.txt.big")) #使用user自訂的字典，需要在setting定義路徑，這樣manage.py才看得懂
	with open(os.path.join(settings.MODULE_FILE, "Jieba_File/stopword.txt"), 'r', encoding='utf-8') as fin:
		with open(os.path.join(settings.MODULE_FILE, "bayes_model_3.pickle"), 'rb') as bayes_model:

			stopword = fin.read().split('\n')

			review = get_data(str(review), stopword)
			mult_bayse_model = pickle.load(bayes_model)
			
			# 因為model也同時包含countvec所以不用做多餘的轉換
			print('\n醫療環境 predicted: ', mult_bayse_model.predict(review)) 
			predict_ans = mult_bayse_model.predict(review)
			return predict_ans


def predict_model_4(review):
	# jieba.load_userdict(os.path.join(settings.PROJECT_FILE, "dict.txt.big")) #使用user自訂的字典，需要在setting定義路徑，這樣manage.py才看得懂
	with open(os.path.join(settings.MODULE_FILE, "Jieba_File/stopword.txt"), 'r', encoding='utf-8') as fin:
		with open(os.path.join(settings.MODULE_FILE, "bayes_model_4.pickle"), 'rb') as bayes_model:

			stopword = fin.read().split('\n')

			review = get_data(str(review), stopword)
			mult_bayse_model = pickle.load(bayes_model)


			# 因為model也同時包含countvec所以不用做多餘的轉換
			print('\n專業程度 predicted: ', mult_bayse_model.predict(review)) 
			predict_ans = mult_bayse_model.predict(review)
			return predict_ans


def predict_model_5(review):
	# jieba.load_userdict(os.path.join(settings.PROJECT_FILE, "dict.txt.big")) #使用user自訂的字典，需要在setting定義路徑，這樣manage.py才看得懂
	with open(os.path.join(settings.MODULE_FILE, "Jieba_File/stopword.txt"), 'r', encoding='utf-8') as fin:
		with open(os.path.join(settings.MODULE_FILE, "bayes_model_5.pickle"), 'rb') as bayes_model:

			stopword = fin.read().split('\n')

			review = get_data(str(review), stopword)
			mult_bayse_model = pickle.load(bayes_model)


			# 因為model也同時包含countvec所以不用做多餘的轉換
			print('\n流程體驗 predicted: ', mult_bayse_model.predict(review)) 
			predict_ans = mult_bayse_model.predict(review)
			return predict_ans

def predict_model_6(review):
	# jieba.load_userdict(os.path.join(settings.PROJECT_FILE, "dict.txt.big")) #使用user自訂的字典，需要在setting定義路徑，這樣manage.py才看得懂
	with open(os.path.join(settings.MODULE_FILE, "Jieba_File/stopword.txt"), 'r', encoding='utf-8') as fin:
		with open(os.path.join(settings.MODULE_FILE, "bayes_model_6.pickle"), 'rb') as bayes_model:

			stopword = fin.read().split('\n')

			review = get_data(str(review), stopword)
			mult_bayse_model = pickle.load(bayes_model)
			
			# 因為model也同時包含countvec所以不用做多餘的轉換
			print('\n服務態度 predicted: ', mult_bayse_model.predict(review)) 
			predict_ans = mult_bayse_model.predict(review)
			return predict_ans


def predict_model_7(review):
	# jieba.load_userdict(os.path.join(settings.PROJECT_FILE, "dict.txt.big")) #使用user自訂的字典，需要在setting定義路徑，這樣manage.py才看得懂
	with open(os.path.join(settings.MODULE_FILE, "Jieba_File/stopword.txt"), 'r', encoding='utf-8') as fin:
		with open(os.path.join(settings.MODULE_FILE, "bayes_model_7.pickle"), 'rb') as bayes_model:

			stopword = fin.read().split('\n')

			review = get_data(str(review), stopword)
			mult_bayse_model = pickle.load(bayes_model)
			
			# 因為model也同時包含countvec所以不用做多餘的轉換
			print('\n溝通能力 predicted: ', mult_bayse_model.predict(review)) 
			predict_ans = mult_bayse_model.predict(review)
			return predict_ans