from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from mainsite import models, LSTM, Aspect
import mainsite.Aspect.bayse
import mainsite.LSTM.model_predict_1
import mainsite.LSTM.model_predict_2
import mainsite.LSTM.model_predict_3
import mainsite.LSTM.model_predict_4
import mainsite.LSTM.model_predict_5
import mainsite.LSTM.model_predict_6
import mainsite.LSTM.model_predict_7
import mainsite.LSTM.cnn_model




# view.py的功用 --> 如何存取在資料庫的資料
# Create your views here.
def homepage(request):  # 建立homepage用來取得所有文章
	posts = models.Message.objects.all()
	post_lists = list()

	return render(request, 'index.html', locals())

def posting(request):

	if request.method == 'POST':
		all_review = request.POST['message']
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']

		if all_review != None:

			# Step1 進入CNN module進行分類
			aspect = LSTM.cnn_model.CNN(all_review) # 回傳為list
			# 一開始都是無關
			review1 = -10
			review2 = -10
			review3 = -10
			review4 = -10
			review5 = -10
			review6 = -10
			review7 = -10

			# Step2 進入LSTM
			for i in aspect:
				if i == 1:
					review1 = LSTM.model_predict_1.predict(all_review)
					if review1 == -2:
						review1 = Aspect.bayse.predict_model_1(str(all_review))[0]

				if i == 2:
					review2 = LSTM.model_predict_2.predict(all_review)
					if review2 == -2:
						review2 = Aspect.bayse.predict_model_2(str(all_review))[0]

				if i == 3:
					review3 = LSTM.model_predict_3.predict(all_review)
					if review3 == -2:
						review3 = Aspect.bayse.predict_model_3(str(all_review))[0]

				if i == 4:
					review4 = LSTM.model_predict_4.predict(all_review)
					if review4 == -2:
						review4 = Aspect.bayse.predict_model_4(str(all_review))[0]

				if i == 5:
					review5 = LSTM.model_predict_5.predict(all_review)
					if review5 == -2:
						review5 = Aspect.bayse.predict_model_5(str(all_review))[0]

				if i == 6:
					review6 = LSTM.model_predict_6.predict(all_review)
					if review6 == -2:
						review6 = Aspect.bayse.predict_model_6(str(all_review))[0]

				if i == 7:
					review7 = LSTM.model_predict_7.predict(all_review)
					if review7 == -2:
						review7 = Aspect.bayse.predict_model_7(str(all_review))[0]


			# review1 = LSTM.model_predict_1.predict(all_review)
			# review2 = LSTM.model_predict_2.predict(all_review)
			# review3 = LSTM.model_predict_3.predict(all_review)
			# review4 = LSTM.model_predict_4.predict(all_review)
			# review5 = LSTM.model_predict_5.predict(all_review)
			# review6 = LSTM.model_predict_6.predict(all_review)
			# review7 = LSTM.model_predict_7.predict(all_review)

			# if review1 == -2:
			# 	review1 = Aspect.bayse.predict_model_1(str(all_review))[0]
			# if review2 == -2:
			# 	review2 = Aspect.bayse.predict_model_2(str(all_review))[0]
			# if review3 == -2:
			# 	review3 = Aspect.bayse.predict_model_3(str(all_review))[0]
			# if review4 == -2:
			# 	review4 = Aspect.bayse.predict_model_4(str(all_review))[0]
			# if review5 == -2:
			# 	review5 = Aspect.bayse.predict_model_5(str(all_review))[0]
			# if review6 == -2:
			# 	review6 = Aspect.bayse.predict_model_6(str(all_review))[0]
			# if review7 == -2:
			# 	review7 = Aspect.bayse.predict_model_7(str(all_review))[0]

			# 把資料存入資料庫
			# hos_review = models.Review.objects.create(name=name, email=email, subject=subject, review=all_review)
			# hos_review.save()
			return render(request, 'contact.html', locals())
		else:
			review = '請再輸入一次'
	else:
		review = -2 # 因為一開始沒有資料，所以先給它空字串
		
	return render(request, 'contact.html', locals())

