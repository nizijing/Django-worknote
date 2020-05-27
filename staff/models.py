from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.models import Permission, GroupManager


# Create your models here.
class MyUser(AbstractUser):
	num = models.SmallIntegerField(verbose_name = '工号', default = -1, db_index=True, unique=True)
	position = models.CharField(verbose_name = '职位', blank = True, max_length=24)


	def get_full_name(self):
		return self.first_name

	def get_short_name(self):
		return self.first_name

	def __str__(self):
		return self.first_name

	class Meta:
		verbose_name = '员工信息'
		verbose_name_plural = '员工信息'
