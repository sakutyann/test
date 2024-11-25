from django.db import models

# クエスト依頼フォームのモデル
class Quest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    requester = models.CharField(max_length=100)
    prefecture = models.CharField(max_length=100)
    reward = models.CharField(max_length=3)
    payment = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title} (ID: {self.id})"

# お題登録フォームのモデル
class QuestRegister(models.Model):
    name = models.CharField(max_length=100)
    quest_id = models.ForeignKey(Quest, on_delete=models.PROTECT, verbose_name="クエストID",related_name="quest_registers")
    address = models.CharField(max_length=200)
    answer_photo = models.ImageField(upload_to='quest_photos/')
    additional_notes = models.TextField()

    def __str__(self):
        return self.name