from django.db import models
from django.utils import timezone
import random


# Create your models here.
class UserData(models.Model):
    # 필요한 데이터 정의
    user_name = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    user_pwd = models.CharField(max_length=10)
    published_date = models.DateTimeField(blank=True, null=True)

    # 메소드 정의
    def generate(self):
        self.published_date = timezone.now()
        self.save()  # 오브젝트를 db에 저장

    def __str__(self):
        return '%s - %s' % (self.user_id, self.user_name)
