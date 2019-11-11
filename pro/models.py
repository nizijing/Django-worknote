from django.db import models

# Create your models here.
class EventInfo(models.Model):
	event_status_choices = (
			(0, '未处理完'),
			(1, '已处理完'),
			)
	event_name	= models.CharField(verbose_name = '事件名称', max_length=24)
	event_status= models.PositiveSmallIntegerField(verbose_name = '事件状态', choices = event_status_choices, default = 0)

	def __str__(self):
		return self.event_name

	class Meta:
		verbose_name = '1-事件信息'
		verbose_name_plural = '1-事件信息'


class TaskInfo(models.Model):
	task_status_choices = (
			(0, '未处理完'),
			(1, '低优先级'),
			(2, '放弃处理'),
			(3, '已处理完'),
			)
	task_id		= models.ForeignKey(
			EventInfo,
			verbose_name = '所属事件',
			on_delete = models.CASCADE
			)
	task_name	= models.CharField(verbose_name = '任务名称', max_length=24)
	task_status = models.PositiveSmallIntegerField(verbose_name = '任务状态', choices = task_status_choices, default = 0)
	task_mtime	= models.DateField(verbose_name = '修改时间', null=True)
	task_note	= models.CharField('备注', max_length = 100, default='', blank=True)

	def __str__(self):
		return self.task_name

	class Meta:
		verbose_name = '2-任务信息'
		verbose_name_plural = '2-任务信息'

