# UserCreateionFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """UsercreationFormのサブクラス
    クラス
    """
    class Meta:
        """UserCreationFormのインナークラス
        Attributes:
            model:連携するUserモデル
            fields:フォームで使用するフィールド
        """
        # 連携するUSerモデルを設定
        model = CustomUser
        # フォームで使用するフィールドを設定
        # ユーザー名、メールアドレス、パスワード
        fields = ('username', 'email', 'password1', 'password2')
        
