from django import forms
from .models import Quest, QuestRegister
from django.core.exceptions import ValidationError

# クエスト依頼
class QuestModelForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['title', 'description', 'deadline', 'requester', 'prefecture', 'reward', 'payment']
        
    # 都道府県フィールド
    PREFECTURE_CHOICES = [
      # ('key', 'name')
        (0, '北海道'),
        (1, '青森県'),
        (2, '岩手県'),
        (3, '宮城県'),
        (4, '秋田県'),
        (5, '山形県'),
        (6, '福島県'),
        (7, '茨城県'),
        (8, '栃木県'),
        (9, '群馬県'),
        (10, '埼玉県'),
        (11, '千葉県'),
        (12, '東京都'),
        (13, '神奈川県'),
        (14, '新潟県'),
        (15, '富山県'),
        (16, '石川県'),
        (17, '福井県'),
        (18, '山梨県'),
        (19, '長野県'),
        (20, '岐阜県'),
        (21, '静岡県'),
        (22, '愛知県'),
        (23, '三重県'),
        (24, '滋賀県'),
        (25, '京都府'),
        (26, '大阪府'),
        (27, '兵庫県'),
        (28, '奈良県'),
        (29, '和歌山県'),
        (30, '鳥取県'),
        (31, '島根県'),
        (32, '岡山県'),
        (33, '広島県'),
        (34, '山口県'),
        (35, '徳島県'),
        (36, '香川県'),
        (37, '愛媛県'),
        (38, '高知県'),
        (39, '福岡県'),
        (40, '佐賀県'),
        (41, '長崎県'),
        (42, '熊本県'),
        (43, '大分県'),
        (44, '宮崎県'),
        (45, '鹿児島県'),
        (46, '沖縄県'),
    ]

    # 報酬（クーポン）フィールド
    REWARD_CHOICES = [
        (1, '3%off'),
        (2, '5%off'),
        (3, '10%off'),
    ]
    
    # タイトル
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # クエスト内容
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    # 期限
    deadline = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    # 依頼者
    requester = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # 都道府県
    prefecture = forms.ChoiceField(
        choices=PREFECTURE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'prefecture'})
    )
    # 報酬
    reward = forms.ChoiceField(
        choices=REWARD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'reward'})
    ) 
    # 支払方法
    payment = forms.ChoiceField(
        choices=[
            ('銀行振込', '銀行振込'),
            ('クレジットカード', 'クレジットカード'),
            ('コンビニ支払い', 'コンビニ支払い'),
        ],
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'payment'})
    )
    
    
    

# お題登録フォーム
class QuestRegisterForm(forms.ModelForm):
    class Meta:
        model = QuestRegister
<<<<<<< HEAD
        fields = ['name', 'address', 'answer_photo', 'additional_notes']
        widgets = {   
            # 住所
=======
        fields = ['quest_id', 'name', 'address', 'answer_photo', 'additional_notes']
        
        widgets = {  
                   
            # クエストIDを非表示
            'quest_id': forms.HiddenInput(),       
                    
            # 名前
>>>>>>> 5d29d4c148ee754ff4bbdca8e8a867129026f260
            'name': forms.TextInput(attrs={
                'placeholder': '名前を入力',
                'class': 'form-control',
            }),
            # 場所
            'address': forms.TextInput(attrs={
                'placeholder': '住所を入力',
                'class': 'form-control',
            }),
            # 解答写真
            'answer_photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            # お題内容
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

