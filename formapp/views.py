from django.shortcuts import render, redirect
from .forms import QuestModelForm, QuestRegisterForm
import logging

logger = logging.getLogger(__name__)

# クエスト依頼フォームの表示と保存
def quest_form_view(request):
    print("遷移_1:",request.method)
    if request.method == 'POST':
        form = QuestModelForm(request.POST)
        if form.is_valid():
            print("is_valid1:",request.method)
            instance = form.save()
            logger.info(f"Saved Quest: {instance}")  # ログに出力
            return redirect('formapp:quest_register')  # 次のフォームにリダイレクト
        else:
            logger.info(f"Form Errors: {form.errors}")  # エラー内容をログに出力
    else:
        form = QuestModelForm()

    return render(request, 'formapp/quest_form.html', {'form': form})

# お題登録フォームの表示と保存
def quest_register_view(request):
    print("遷移_2:",request.method)
    if request.method == 'POST':
        form = QuestRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            print("is_valid2:",request.method)
            form.save()
            print(form.cleaned_data)
            return redirect('formapp:quest_success')  # 完了ページにリダイレクト
    else:
        form = QuestRegisterForm()

    return render(request, 'formapp/quest_register.html', {'form': form})

# クエスト発注完了ページ
def quest_success_view(request):
    return render(request, 'formapp/quest_success.html')

