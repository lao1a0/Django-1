import random
from django.db import models

# Create your models here.
class CreateStu(models.Model):

    name = models.CharField(max_length=10,db_column='name')
    # classroom = models.CharField(max_length=20, db_column='classroom')
    classroom = models.CharField(max_length=20,db_column='classroom')
    # 默认为女生
    sex = models.IntegerField(db_column='sex')
    class Meta:
        db_table = 'laolao'