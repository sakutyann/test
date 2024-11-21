from django.shortcuts import render
from django.views import View

            
            
class MainView(View):
    """クエスト一覧ページのビュー"""
    template_name = "main.html"

    def get(self, request, *args, **kwargs):
        # ユーザーがログインしているかを確認し、必要な情報を提供
        context = {
            'is_authenticated': request.user.is_authenticated,
            'username': request.user.username if request.user.is_authenticated else None,
        }
        return render(request, self.template_name, context)

def loginworldfunction(request):
          return render(request, 'login.html')

def accountworldfunction(request):
          return render(request, 'account.html')

def logoutworldfunction(request):
          return render(request, 'logout.html')

def logoutokworldfunction(request):
          return render(request, 'logoutok.html')

def formworldfunction(request):
          return render(request, 'form.html')

def questformworldfunction(request):
          return render(request, 'questform.html')

def couponformworldfunction(request):
          return render(request, 'coupon.html')

def couponuseformworldfunction(request):
          return render(request, 'couponuse.html')

def couponendformworldfunction(request):
          return render(request, 'couponend.html')

def couponpastformworldfunction(request):
          return render(request, 'couponpast.html')

# 初期画面
def title_view(request):
    return render(request, 'title.html')

def questlookformworldfunction(request):
          return render(request, 'questlook.html')

def couponnotformworldfunction(request):
          return render(request, 'couponnot.html')

def questokformworldfunction(request):
          return render(request, 'questok.html')

def questerformworldfunction(request):
          return render(request, 'quester.html')

def newaccountformworldfunction(request):
          return render(request, 'newaccount.html')

# 進行中クエスト
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


