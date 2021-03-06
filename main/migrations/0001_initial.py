# Generated by Django 4.0.4 on 2022-04-29 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=128, unique=True, verbose_name='유저 이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('nickname', models.CharField(max_length=10, null=True, verbose_name='유저 닉네임')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')),
            ],
            options={
                'db_table': 'test_user',
            },
        ),
    ]
