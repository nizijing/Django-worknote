from django.db import models


# Create your models here.
class ProInfo(models.Model):
    pro_name    = models.CharField('项目名称', max_length = 24, unique = True)
    pro_link    = models.URLField('link')

    def __str__(self):
        return self.pro_name

    class Meta:
        verbose_name = '1-项目信息'
        verbose_name_plural = '1-项目信息'


class EventInfo(models.Model):
    event_status_choices = (
		(0, '未处理完'),
		(1, '已处理完'),
	        )
    pro             = models.ForeignKey(ProInfo, verbose_name = '所属项目', on_delete = models.PROTECT)
    event_name	    = models.CharField(verbose_name = '事件名称', max_length=24)
    event_ctime     = models.DateField('创建时间', auto_now_add = True)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = '2-事件信息'
        verbose_name_plural = '2-事件信息'

    def get_event_status(self):
        return True
        #return all(id.task_status)
    get_event_status.boolean = True
    get_event_status.short_description = '已完成?'


class TaskInfo(models.Model):
    task_priority_choices = (
			(0, '高'),
			(1, '中'),
			(2, '低'),
			(3, '不处理'),
			)
    task_id		= models.ForeignKey(
			EventInfo,
			verbose_name = '所属事件',
			on_delete = models.CASCADE
			)
    task_name	= models.CharField(verbose_name = '任务名称', max_length=24)
    task_status = models.BooleanField(verbose_name = '任务状态', default = False)
    task_mtime	= models.DateField(verbose_name = '修改时间', null=True, auto_now=True)
    task_note	= models.CharField('备注', max_length = 100, default='', blank=True)

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = '3-任务信息'
        verbose_name_plural = '3-任务信息'


