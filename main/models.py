
from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=128,unique=True,null =True,verbose_name='이메일')
    nickname = models.CharField(max_length=16,unique=True, null =True,verbose_name='닉네임')
    password = models.CharField(max_length=16,null =True, verbose_name='비밀번호')
    register_dttm = models.DateTimeField(auto_now_add=True, null =True,verbose_name='계정 생성시간')

    def __str__(self):
        return self.email
    class Meta:
        db_table ='user'
        verbose_name = '유저'
        verbose_name_plural = '유저'
    REQUIRED_FIELDS = ['email', 'password']
    email.db_index = True
    EMAIL_FIELD = 'email'


