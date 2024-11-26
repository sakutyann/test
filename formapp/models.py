from django.db import models
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


# クエスト依頼フォームのモデル
class Quest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    requester = models.CharField(max_length=100)
    prefecture = models.CharField(max_length=100)
    reward = models.CharField(max_length=3, default="1")
    payment = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title} (ID: {self.id})"

# お題登録フォームのモデル
class QuestRegister(models.Model):
    name = models.CharField(max_length=100)
    quest_id = models.ForeignKey(Quest, on_delete=models.PROTECT, verbose_name="クエストID",related_name="quest_registers", null=True)
    address = models.CharField(max_length=200)
    answer_photo = models.ImageField(upload_to='quest_photos/')
    additional_notes = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
 
    def save(self, *args, **kwargs):
        # 保存処理
        super().save(*args, **kwargs)
        if self.answer_photo and not self.latitude and not self.longitude:
            self.extract_gps_data()
 
    def extract_gps_data(self):
        """画像からGPSデータを抽出"""
        try:
            img = Image.open(self.answer_photo)
            exif_data = img._getexif()
            if not exif_data:
                raise ValueError("EXIFデータが見つかりません。")
 
            gps_info = {}
            for tag, value in exif_data.items():
                decoded = TAGS.get(tag)
                if decoded == "GPSInfo":
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        gps_info[sub_decoded] = value[t]
 
            if gps_info:
 
                self.latitude = self._get_decimal_from_dms(
                    gps_info.get("GPSLatitude"),
                   
                    gps_info.get("GPSLatitudeRef"),
                )
                self.longitude = self._get_decimal_from_dms(
                    gps_info.get("GPSLongitude"),
 
                    gps_info.get("GPSLongitudeRef"),
                )
                print(f"Latitude: {self.latitude}, Longitude: {self.longitude}")
                self.save(update_fields=['latitude', 'longitude'])
            else:
                raise ValueError("GPS情報が存在しません。")
 
        except Exception as e:
            print(f"GPSデータ抽出中のエラー: {e}")
 
    def _get_decimal_from_dms(self, dms, ref):
        """度分秒から10進数に変換"""
        if dms:
            # dmsが各要素がIFDRational型のリストまたはタプルの場合
            degrees = float(dms[0].numerator) / float(dms[0].denominator)  # degrees
            minutes = float(dms[1].numerator) / float(dms[1].denominator)  # minutes
            seconds = float(dms[2].numerator) / float(dms[2].denominator)  # seconds
 
            # 10進数に変換
            decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
 
            # 南緯、または西経の場合、符号を反転
            if ref in ['S', 'W']:
                decimal = -decimal
 
            return decimal
        return None




    def __str__(self):
        return self.name