from django.db import models

# Create your models here.

# myapp/models.py

# modelsモジュールをインポートします
from django.db import models

# QuestRequestモデルを定義します。クエスト依頼情報を管理するテーブルを作成します
class QuestRequest(models.Model):
    # タイトルフィールドを定義、100文字まで保存できる題名
    title = models.CharField(max_length=100, verbose_name="題名")

    # 内容フィールドを定義、テキストを複数行保存できる内容
    description = models.TextField(verbose_name="内容")

    # 期限フィールドを定義、日付形式で保存する期限
    deadline = models.DateField(verbose_name="期限")
    
    #クーポン
    coupon = models.CharField(max_length=50 , verbose_name="クーポン")


    # 依頼者名フィールドを定義、100文字まで保存できる依頼者の名前
    requester = models.CharField(max_length=100, verbose_name="依頼者名")

    # 都道府県フィールドを定義、都道府県名を保存
    prefecture = models.CharField(max_length=50, verbose_name="都道府県")

    # 支払い方法フィールドを定義、支払い方法を保存
    payment = models.CharField(max_length=50, verbose_name="支払い方法")

    # 管理画面などで表示するオブジェクト名をタイトルに設定
    def __str__(self):
        return self.title

