from django.db import models
from django.utils import timezone

# Create your models here.
class ProInfo(models.Model):
    pro_name    = models.CharField('项目名称', max_length = 24, unique = True)
    pro_ctime   = models.DateField('创建时间', default = timezone.now)
    pro_type    = models.CharField('项目类型', max_length = 16)
    pro_link    = models.URLField('link', blank = True)

    note    = models.CharField('备注', max_length = 100, blank = True)

    def __str__(self):
        return self.pro_name

    class Meta:
        verbose_name = '1-项目信息'
        verbose_name_plural = '1-项目信息'


class DeviceInfo(models.Model):
    pro = models.ForeignKey(ProInfo, verbose_name = '所属项目', on_delete = models.DO_NOTHING)
    hostname    = models.CharField('主机名', max_length = 24)
    ip          = models.GenericIPAddressField('ip')
    os_name     = models.CharField('OS', max_length = 16)
    unit_name   = models.CharField('组件名', max_length = 16)
    nature      = models.CharField('配置', max_length = 16, help_text = 'such as 2C4G200G')
    isvhost     = models.BooleanField('是否虚拟机')
    hostDevice  = models.GenericIPAddressField('宿主机')
    note        = models.CharField('备注', max_length = 100, blank = True)
    
    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = '2-设备信息'
        verbose_name_plural = '2-设备信息'


class UnitInfo(models.Model):
    pro         = models.ForeignKey(ProInfo, verbose_name = '所属项目', on_delete = models.DO_NOTHING)
    unit_name   = models.CharField('关系名', max_length = 16)
    src_unit    = models.CharField('源组件', max_length = 16)
    src_app     = models.CharField('源应用', max_length = 16)
    src_port    = models.CharField('源端口', max_length = 16)

    dest_unit   = models.CharField('目的组件', max_length = 16)
    dest_vip    = models.CharField('组件vip', max_length = 48)
    dest_app    = models.CharField('目的应用', max_length = 16)
    dest_port   = models.CharField('目的端口', max_length = 16)

    test_way    = models.CharField('测试方法', max_length = 200, default = '')
    note        = models.CharField('备注', max_length = 48, blank = True)

    def __str__(self):
        return self.unit_name

    class Meta:
        verbose_name = '3-组件关系'
        verbose_name_plural = '3-组件关系'


class AppInfo(models.Model):
    pro         = models.ForeignKey(ProInfo, verbose_name = '所属项目', on_delete = models.DO_NOTHING)
    unit_name   = models.CharField('组件', max_length = 16)
    app_name    = models.CharField('应用', max_length = 24)
    app_user    = models.CharField('用户', max_length = 24)
    app_passwd  = models.CharField('密码', max_length = 24)
    start_way   = models.CharField('启动方式', max_length = 100, default = '')
    note        = models.CharField('备注', max_length = 100, blank = True)
    
    def __str__(self):
        return self.app_name

    class Meta:
        verbose_name = '4-应用信息'
        verbose_name_plural = '4-应用信息'


