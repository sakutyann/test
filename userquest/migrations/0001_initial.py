# Generated by Django 4.0 on 2024-11-25 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_customuser_groups_and_more'),
        ('formapp', '0004_remove_questregister_hours_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_id', models.AutoField(primary_key=True, serialize=False, verbose_name='クーポンID')),
                ('coupon_description', models.TextField(null=True, verbose_name='クーポン詳細')),
                ('used_at', models.DateTimeField(verbose_name='使用期限')),
                ('quest_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='formapp.quest', verbose_name='クエストID')),
            ],
        ),
        migrations.CreateModel(
            name='UserCoupon',
            fields=[
                ('user_coupon_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ユーザークーポンID')),
                ('issued_at', models.DateTimeField(auto_now_add=True, verbose_name='発行日時')),
                ('coupon_status', models.BooleanField(default=False, verbose_name='ステータス')),
                ('coupon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userquest.coupon', verbose_name='クーポンID')),
                ('user_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser', verbose_name='ユーザーID')),
            ],
        ),
    ]
