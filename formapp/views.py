from django.shortcuts import render, redirect
from .forms import QuestModelForm, QuestRegisterForm
import logging

from django.urls import reverse
from .models import Quest

logger = logging.getLogger(__name__)

# クエスト依頼フォームの表示と保存
def quest_form_view(request):
    print("クエスト依頼フォーム",request.method)
    if request.method == 'POST':
        form = QuestModelForm(request.POST)
        if form.is_valid():
            print("フォームバリデーション",request.method)
            instance = form.save()
            return redirect('formapp:quest_register', quest_id=instance.id)  # 引数を渡す  
        else:
            print("フォームエラー", form.errors)
    else:
        form = QuestModelForm()

    return render(request, 'formapp/quest_form.html', {'form': form})



# お題登録フォームの表示と保存
def quest_register_view(request, quest_id):
    try:
        # クエスト ID を取得
        quest = Quest.objects.get(id=quest_id)
    except Quest.DoesNotExist:
        return redirect('formapp:quest_form')  # クエストが存在しない場合、再度登録画面に戻る
    
    if request.method == 'POST':
        print("お題登録フォーム", request.method)
        form = QuestRegisterForm(request.POST, request.FILES)
        
        form.instance.quest = quest #ここでquest_idを関連付ける
        print(quest)
 
        if form.is_valid():
            # フォームを保存する際に、quest_idが保存される
            form.save()
            print("登録成功：", form.cleaned_data )
            return redirect('formapp:quest_success')  # 完了ページにリダイレクト
        else:
            print("フォームエラー", form.errors)     
    else:
        # ページ遷移
        form = QuestRegisterForm(initial={'quest_id': quest})
        print("お題登録フォーム遷移:",request.method)

    return render(request, 'formapp/quest_register.html', {'form': form, 'quest_id':quest_id,})

# クエスト発注完了ページ
def quest_success_view(request):
    print("クエスト発注完了ページ")
    return render(request, 'formapp/quest_success.html')
