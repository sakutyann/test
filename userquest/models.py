from django.db import models
from django.contrib.auth.models import User  # ユーザー情報をリンクする場合に使用
from formapp.models import Quest
from django.conf import settings


class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True, verbose_name="クーポンID")
    quest_id = models.ForeignKey(Quest,on_delete=models.PROTECT, verbose_name="クエストID")
    coupon_description = models.TextField(null=True, verbose_name="クーポン詳細")
    used_at = models.DateTimeField(verbose_name="使用期限")
    
    def __str__(self):
        return f"Coupon {self.coupon_id}"

class UserCoupon(models.Model):
    user_coupon_id = models.AutoField(primary_key=True, verbose_name="ユーザークーポンID")
    user_account_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name="ユーザーID")
    coupon_id = models.ForeignKey(Coupon, on_delete=models.CASCADE, verbose_name="クーポンID"
    ) 
    issued_at = models.DateTimeField(auto_now_add=True, verbose_name="発行日時")
    coupon_status = models.BooleanField(default=False, verbose_name="ステータス")  # False: 未使用, True: 使用済み

    def __str__(self):
        return f"Coupon {self.coupon_id} for User {self.user_account_id}"




from django.db import models
class PhotoSubmission(models.Model):
    photo = models.ImageField(upload_to='photos/')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
