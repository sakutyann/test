from django.shortcuts import render
from .models import PhotoSubmission
from formapp.models import QuestRegister
from .utils import get_exif_data, get_geotagging, get_coordinates
from django.core.files.storage import default_storage
from PIL import Image
from django.db.models import Q  # 複数条件を扱うために必要

def questnowformworldfunction(request):
          return render(request, 'questnow.html')

def questnotformworldfunction(request):
          return render(request, 'questnot.html')

def questdoformworldfunction(request):
          return render(request, 'questdo.html')

def questgoformworldfunction(request):
          return render(request, 'questgo.html')


def questgoformworldfunction(request):
    if request.method == 'POST':
        photo = request.FILES['photo']
        temp_path = default_storage.save(photo.name, photo)

        try:
            # EXIF情報から緯度・経度を取得
            image = Image.open(temp_path)
            exif_data = get_exif_data(image)
            geotags = get_geotagging(exif_data)
            coordinates = get_coordinates(geotags)

            if coordinates and len(coordinates) == 2:  # 緯度と経度の両方が存在する場合のみ
                latitude, longitude = coordinates
                PhotoSubmission.objects.create(
                    photo=photo,
                    latitude=latitude,
                    longitude=longitude,
                )

                # 緯度・経度の範囲を計算
                latitude_min = latitude - 1/10
                latitude_max = latitude + 1/10
                longitude_min = longitude - 1/10
                longitude_max = longitude + 1/10

                # 位置情報管理アプリのデータと照合（範囲内で検索）
                if QuestRegister.objects.filter(
                    Q(latitude__gte=latitude_min, latitude__lte=latitude_max) &
                    Q(longitude__gte=longitude_min, longitude__lte=longitude_max)
                ).exists():
                    # 成功した場合
                    return render(request, 'questyes.html', {'latitude': latitude, 'longitude': longitude})
                else:
                    # 照合失敗
                    return render(request, 'questout.html', {'latitude': latitude, 'longitude': longitude})
            else:
                # 位置情報が存在しない場合
                return render(request, 'questout.html', {'result': '位置情報が含まれていません。'})
        except Exception as e:
            # 例外発生時も失敗判定
            return render(request, 'questout.html', {'result': f'エラーが発生しました: {e}'})

    return render(request, 'questgo.html')


def questyesformworldfunction(request):
          return render(request, 'questyes.html')

def questoutformworldfunction(request):
          return render(request, 'questout.html')


def questfinformworldfunction(request):
          return render(request, 'questfin.html')

# Create your views here.
