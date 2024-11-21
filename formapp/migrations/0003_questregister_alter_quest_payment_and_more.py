# Generated by Django 4.0 on 2024-11-19 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_quest_delete_questrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('answer_photo', models.ImageField(upload_to='quest_photos/')),
                ('hours', models.CharField(max_length=100)),
                ('reward', models.PositiveIntegerField()),
                ('additional_notes', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='quest',
            name='payment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quest',
            name='prefecture',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quest',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
