from django.db import models

# Create your models here.


#クエスト依頼フォーム
class QuestRequest(models.Model):
    #クエストタイトル
    title = models.CharField(max_length=100) 
    #内容
    description = models.TextField()
    #期限
    deadline = models.DateField()
    #依頼者名
    requester = models.CharField(max_length=100)
    #都道府県
    prefecture = models.CharField(max_length=50)
    #支払い方法
    payment = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

