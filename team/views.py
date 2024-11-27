# from django.shortcuts import render
# from django.views import View

            
# #クエスト一覧  
# class MainView(View):
#     """クエスト一覧ページのビュー"""
#     template_name = "main.html"

#     def get(self, request, *args, **kwargs):
#         # ユーザーがログインしているかを確認し、必要な情報を提供
#         context = {
#             'is_authenticated': request.user.is_authenticated,
#             'username': request.user.username if request.user.is_authenticated else None,
#         }
#         return render(request, self.template_name, context)    
    
    
from django.shortcuts import render
from django.views import View 
from formapp.models import Quest  # Questモデルをインポート
from formapp.forms import QuestModelForm  # QuestModelFormをインポート

class MainView(View):
    """クエスト一覧ページのビュー"""
    template_name = "main.html"

    def get(self, request, *args, **kwargs):
        # クエストデータを取得
        quests = Quest.objects.all()

        # 0～46のキーに基づいて都道府県別にクエストを分ける
        prefectures = {}
        for quest in quests:
            # 都道府県のキーを取得
            prefecture_key = quest.prefecture

            # まだその都道府県のキーが辞書に無ければ、リストを初期化
            if prefecture_key not in prefectures:
                prefectures[prefecture_key] = []

            # 都道府県キーに対応するリストにクエストを追加
            prefectures[prefecture_key].append(quest)

        # ユーザーがログインしているかを確認
        context = {
            'is_authenticated': request.user.is_authenticated,
            'username': request.user.username if request.user.is_authenticated else None,
            'prefectures': prefectures,  # 都道府県別に分けたクエストデータ
        }

        return render(request, self.template_name, context)
    
    



class QuestDetailView(View):
    """クエスト詳細ページのビュー"""
    template_name = "questdo.html"

    def get(self, request, *args, **kwargs):
        # クエストの主キーを取得
        quest = Quest.objects.get(pk=kwargs['pk'])
        # 現在のクエストに紐づくお題を取得
        quest_registers = quest.quest_registers.all()
        print(quest)
        
        # デバッグ用: データ確認
        print(f"Quest ID: {quest.id}")
        print(f"Quest Registers: {quest_registers}")
        
        # クエスト詳細ページを表示
        context = {
            'quest': quest, #クエスト情報
            'quest_registers': quest_registers,  # お題情報
        }
        
        return render(request, self.template_name, context) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
# def questnowformworldfunction(request):
#           return render(request, 'questnow.html')

# def questnotformworldfunction(request):
#           return render(request, 'questnot.html')

# def questdoformworldfunction(request):
#           return render(request, 'questdo.html')

# def questgoformworldfunction(request):
#           return render(request, 'questgo.html')

# def questyesformworldfunction(request):
#           return render(request, 'questyes.html')

# def questoutformworldfunction(request):
#           return render(request, 'questout.html')


# def questfinformworldfunction(request):
#           return render(request, 'questfin.html')


