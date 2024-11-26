from django.shortcuts import render, get_object_or_404, redirect
from .models import Coupon,UserCoupon

def questnowformworldfunction(request):
          return render(request, 'questnow.html')

def questnotformworldfunction(request):
          return render(request, 'questnot.html')

def questdoformworldfunction(request):
          return render(request, 'questdo.html')

def questgoformworldfunction(request):
          return render(request, 'questgo.html')

def questyesformworldfunction(request):
          return render(request, 'questyes.html')

def questoutformworldfunction(request):
          return render(request, 'questout.html')


def questfinformworldfunction(request):
          return render(request, 'questfin.html')

def coupon_list(request):
    coupons = Coupon.objects.filter(status=False)  # 未使用クーポン
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


# Create your views here.
