from django.db import models

# クエスト依頼フォームのモデル
class Quest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    requester = models.CharField(max_length=100)
    prefecture = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

# クエスト登録フォームのモデル
class QuestRegister(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    answer_photo = models.ImageField(upload_to='quest_photos/')
    hours = models.CharField(max_length=100)
    reward = models.PositiveIntegerField()
    additional_notes = models.TextField()

    def __str__(self):
        return self.name

    


