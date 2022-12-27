from django.contrib import admin
from .models import Review # 引入Post類別

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
	list_display = ('title', 'review', 'pub_date')


# admin.site.register(Message, MessageAdmin) # 然後透過admin.site.register註冊
# admin.site.register(Review, ReviewAdmin) # 然後透過admin.site.register註冊
admin.site.register(Review) # 然後透過admin.site.register註冊


