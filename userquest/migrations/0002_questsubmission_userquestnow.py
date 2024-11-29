# Generated by Django 5.1.3 on 2024-11-29 03:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0008_merge_20241126_1233'),
        ('userquest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestSubMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False, verbose_name='完了判定')),
                ('quest_register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formapp.questregister', verbose_name='クエスト詳細')),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False, verbose_name='クエスト完了判定')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='formapp.quest', verbose_name='クエスト')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]