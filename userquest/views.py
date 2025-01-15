from django.shortcuts import render, get_object_or_404, redirect
from .models import Coupon,UserCoupon
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import PhotoSubmission
from formapp.models import QuestRegister
from .utils import get_exif_data, get_geotagging, get_coordinates
from django.core.files.storage import default_storage
from PIL import Image
from django.db.models import Q  # 複数条件を扱うために必要
from django.contrib.auth.decorators import login_required
from django.views import View 
from formapp.models import Quest  # Questモデルをインポート
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



def questnowformworldfunction(request):
          return render(request, 'questnow.html')

def questnotformworldfunction(request):
          return render(request, 'questnot.html')

# def questdoformworldfunction(request):
#           return render(request, 'questdo.html')

# お題写真アップロード画面
# def questgoformworldfunction(request):
#           return render(request, 'questgo.html')

@method_decorator(login_required, name='dispatch')
class QuestGoView(View):
    template_names_yes = "questyes.html"
    template_names_out = "questout.html"
    
    def get_context_data(self, **kwargs):
       # クエストの主キーを取得
        quest = Quest.objects.get(pk=kwargs['pk'])
        # 現在のクエストに紐づくお題を取得
        quest_registers = quest.quest_registers.all()
        print(quest_registers)
        # 共通のコンテキストを返す
        return {
            'quest': quest,  # クエスト情報
            'quest_registers': quest_registers,  # お題情報
        }
        
    # getメソッド
    def get(self, request, *args, **kwargs):
        # contextデータを取得
        context = self.get_context_data(**kwargs)
        return render(request, "questgo.html", context)
    
    # postメソッド
    def post(self, request, *args, **kwargs):
          # contextデータを取得
          context = self.get_context_data(**kwargs)
          photo = request.FILES['photo']
          if not photo:
            return render(request, self.template_names_out, {'result': '写真がアップロードされていません。'})
          
          temp_path = default_storage.save(photo.name, photo)
          print('if文クリア')
          try:
              print('try内部侵入')
              # EXIF情報から緯度・経度を取得
              image = Image.open("media\\"+temp_path)
              exif_data = get_exif_data(image)
              geotags = get_geotagging(exif_data)
              coordinates = get_coordinates(geotags)

              print('iamge:',image,',exif_data:',exif_data,',geotags:',geotags,',coordinates:',coordinates)
              if coordinates and len(coordinates) == 2:  # 緯度と経度の両方が存在する場合のみ
                latitude, longitude = coordinates
                PhotoSubmission.objects.create(
                    photo=photo,
                    latitude=latitude,
                    longitude=longitude,
                )

                # 緯度・経度の範囲を計算
                latitude_min = latitude - 1/70
                latitude_max = latitude + 1/70
                longitude_min = longitude - 1/70
                longitude_max = longitude + 1/70

                # 位置情報管理アプリのデータと照合（範囲内で検索）
                if QuestRegister.objects.filter(
                    Q(latitude__gte=latitude_min, latitude__lte=latitude_max) &
                    Q(longitude__gte=longitude_min, longitude__lte=longitude_max)
                    ).exists():
                    # 成功した場合
                    print('判定：成功')
                    print(request, latitude, longitude, context)
                    return render(request, self.template_names_yes,context)
                else:
                    # 照合失敗
                    print('判定：失敗')
                    return render(request, self.template_names_out, {'latitude': latitude, 'longitude': longitude, 'context': context})
              else:
                # 位置情報が存在しない場合
                print('判定：位置情報なし')
                return render(request, self.template_names_out, {'result': '位置情報が含まれていません。', 'context':context})
          except Exception as e:
            # 例外発生時も失敗判定
            print('判定：例外発生')
            return render(request,self.template_names_out, {'result': f'エラーが発生しました: {e}', 'context':context})


class QuestYesView(View):
    """クエスト挑戦ページのビュー"""
    template_name = "questyes.html"
    def get(self, request, *args, **kwargs):
        # クエストの主キーを取得
        quest = Quest.objects.get(pk=kwargs['pk'])
        # 現在のクエストに紐づくお題を取得
        quest_registers = quest.quest_registers.all()
        print(quest)

        # クエスト詳細ページを表示
        context = {
            'quest': quest, #クエスト情報
            'quest_registers': quest_registers,  # お題情報
        }
        return render(request, self.template_name, context) 
   
   
class QuestOutView(View):
  template_name = "questout.html"
  def get(self, request, *args, **kwargs):
    quest = Quest.objects.get(pk=kwargs['pk'])
    quest_registers = quest.quest_resigters.all()
    print(quest)
    context = {
        'quest': quest, #クエスト情報
        'quest_registers': quest_registers,  # お題情報
        }
    return render(request, self.template_name, context) 

class QuestFinView(View):
  template_name = "questfin.html"
  def get(self, request, *args, **kwargs):
    quest = Quest.objects.get(pk=kwargs['pk'])
    quest_registers = quest.quest_resigters.all()
    print(quest)
    context = {
        'quest': quest, #クエスト情報
        'quest_registers': quest_registers,  # お題情報
        }
    return render(request, self.template_name, context) 



@login_required
def coupon_list(request):
    user_coupons = UserCoupon.objects.filter(user_account_id=request.user,
                                             coupon_status=0)  # 未使用クーポン
    
    coupons = [
        {
            'id': user_coupon.coupon_id.coupon_id,
            'name':user_coupon.coupon_id.coupon_description,
        }
        for user_coupon in user_coupons
    ]
    print(coupons)
    return render(request, 'coupon.html', {'coupons': coupons})

def coupon_detail(request, coupon_id):
    user_coupon = get_object_or_404(UserCoupon, coupon__id=coupon_id)
    coupon = user_coupon.coupon
    return render(request, 'coupon_detail.html', {'coupon': coupon, 'user_coupon': user_coupon})

def used_coupons(request):
    coupons = Coupon.objects.filter(status=True)  # 使用済みクーポン
    return render(request, 'couponnot.html', {'coupons': coupons})

def coupon_complete(request):
    # 完了メッセージの表示だけの場合
    return render(request, 'couponend.html')

# クエスト挑戦画面
def quest_challenge_view(request):
  return render(request, 'quest_challenge.html')




# Create your views here.
