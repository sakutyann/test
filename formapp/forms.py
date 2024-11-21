from django import forms
from .models import Quest, QuestRegister
from django.core.exceptions import ValidationError


# クエスト登録フォーム
class QuestRegisterForm(forms.ModelForm):
    class Meta:
        model = QuestRegister
        fields = ['name', 'address', 'answer_photo', 'hours', 'reward', 'additional_notes']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': '名前を入力',
                'class': 'form-control',
            }),
            'address': forms.TextInput(attrs={
                'placeholder': '住所を入力',
                'class': 'form-control',
            }),
            'answer_photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'hours': forms.TextInput(attrs={
                'placeholder': '例: 9:00 - 17:00',
                'class': 'form-control',
            }),
            'reward': forms.NumberInput(attrs={
                'placeholder': '報酬額を入力',
                'class': 'form-control',
            }),
            'additional_notes': forms.Textarea(attrs={
                'placeholder': '特記事項など',
                'class': 'form-control',
                'rows': 3,
            }),
        }

    # 画像サイズ制限のバリデーション
    def clean_answer_photo(self):
        photo = self.cleaned_data.get('answer_photo')
        if photo:
            max_size = 5 * 1024 * 1024  # 5MB
            if photo.size > max_size:
                raise ValidationError("画像サイズは5MB以内にしてください。")
        return photo


class QuestModelForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['title', 'description', 'deadline', 'requester', 'prefecture', 'payment']
    
    PREFECTURE_CHOICES = [
        ('北海道', '北海道'),
        ('青森県', '青森県'),
        ('岩手県', '岩手県'),
        ('宮城県', '宮城県'),
        ('秋田県', '秋田県'),
        ('山形県', '山形県'),
        ('福島県', '福島県'),
        ('茨城県', '茨城県'),
        ('栃木県', '栃木県'),
        ('群馬県', '群馬県'),
        ('埼玉県', '埼玉県'),
        ('千葉県', '千葉県'),
        ('東京都', '東京都'),
        ('神奈川県', '神奈川県'),
        ('新潟県', '新潟県'),
        ('富山県', '富山県'),
        ('石川県', '石川県'),
        ('福井県', '福井県'),
        ('山梨県', '山梨県'),
        ('長野県', '長野県'),
        ('岐阜県', '岐阜県'),
        ('静岡県', '静岡県'),
        ('愛知県', '愛知県'),
        ('三重県', '三重県'),
        ('滋賀県', '滋賀県'),
        ('京都府', '京都府'),
        ('大阪府', '大阪府'),
        ('兵庫県', '兵庫県'),
        ('奈良県', '奈良県'),
        ('和歌山県', '和歌山県'),
        ('鳥取県', '鳥取県'),
        ('島根県', '島根県'),
        ('岡山県', '岡山県'),
        ('広島県', '広島県'),
        ('山口県', '山口県'),
        ('徳島県', '徳島県'),
        ('香川県', '香川県'),
        ('愛媛県', '愛媛県'),
        ('高知県', '高知県'),
        ('福岡県', '福岡県'),
        ('佐賀県', '佐賀県'),
        ('長崎県', '長崎県'),
        ('熊本県', '熊本県'),
        ('大分県', '大分県'),
        ('宮崎県', '宮崎県'),
        ('鹿児島県', '鹿児島県'),
        ('沖縄県', '沖縄県'),
    ]
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    deadline = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    requester = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prefecture = forms.ChoiceField(
        choices=PREFECTURE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'prefecture'})
    )
    payment = forms.ChoiceField(
        choices=[
            ('銀行振込', '銀行振込'),
            ('クレジットカード', 'クレジットカード'),
            ('コンビニ支払い', 'コンビニ支払い'),
        ],
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'payment'})
    )