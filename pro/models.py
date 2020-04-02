from django.db import models
from django.utils import timezone
from datetime import datetime

FINISHJOB=3

# Create your models here.
class ProInfo(models.Model):
	province_choice = (
			(11, '北京'),
			(12, '天津'),
			(13, '河北'),
			(14, '山西'),
			(15, '内蒙'),
			(21, '辽宁'),
			(22, '吉林'),
			(23, '黑龙江'),
			(31, '上海'),
			(32, '江苏'),
			(33, '浙江'),
			(34, '安徽'),
			(35, '福建'),
			(36, '江西'),
			(37, '山东'),
			(41, '河南'),
			(42, '湖北'),
			(43, '湖南'),
			(44, '广东'),
			(45, '广西'),
			(46, '海南'),
			(50, '重庆'),
			(51, '四川'),
			(52, '贵州'),
			(53, '云南'),
			(54, '西藏'),
			(61, '陕西'),
			(62, '甘肃'),
			(63, '青海'),
			(64, '宁夏'),
			(65, '新疆'),
			(71, '台湾'),
			(81, '香港'),
			(82, '澳门'),
			(91, '国外'),
			)
	province	 = models.PositiveSmallIntegerField('省市', choices = province_choice, default = 33)
	pro_name	 = models.CharField('项目名称', max_length = 24, unique = True)
	pro_ctime	 = models.DateField('创建时间', default = timezone.now)
	pro_status   = models.BooleanField('任务状态', default = False) 
	pro_link	 = models.URLField('link')

	def get_event_status(self):
		for item in EventInfo.objects.filter(pro_id=self.id):
			if not item.event_priority == FINISHJOB:
				return False
		return True
	get_event_status.boolean = True
	get_event_status.short_description = '事件状态'

	def __str__(self):
		return self.pro_name

	class Meta:
		verbose_name = '1-项目信息'
		verbose_name_plural = '1-项目信息'


class EventInfo(models.Model):
	event_priority_choices = (
				(0, '高'),
				(1, '中'),
				(2, '低'),
				(FINISHJOB, '已完成'),
				(4, '不处理'),
				)
	pro			= models.ForeignKey(ProInfo, verbose_name = '所属项目', on_delete = models.PROTECT)
	event_name		= models.CharField(verbose_name = '事件名称', max_length=24)
	event_ctime	= models.DateField('创建时间', auto_now_add = True)
	event_priority	= models.PositiveSmallIntegerField('优先级', choices = event_priority_choices, default = 1)
	event_note		= models.CharField('备注', max_length = 100, blank = True, default = '')

	def __str__(self):
		return self.event_name

	class Meta:
		verbose_name = '2-事件信息'
		verbose_name_plural = '2-事件信息'


class TaskInfo(models.Model):
	task_id		  = models.ForeignKey(
				EventInfo,
				verbose_name = '所属事件',
				on_delete = models.CASCADE
				)
	task_name	 = models.CharField(verbose_name = '任务名称', max_length=24)
	task_status = models.BooleanField(verbose_name = '任务状态', default = False)
	task_mtime	 = models.DateField(verbose_name = '修改时间',  auto_now=True)
	task_note	 = models.CharField('备注', max_length = 100, default='', blank=True)

	def __str__(self):
		return self.task_name

	class Meta:
		verbose_name = '3-任务信息'
		verbose_name_plural = '3-任务信息'

	def get_pro_name(self):
		return self.task_id.pro
	get_pro_name.short_description = '所属项目'

