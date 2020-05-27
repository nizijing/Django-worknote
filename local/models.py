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
    hostname    = models.CharField('主机简称', max_length = 24)
    ip          = models.GenericIPAddressField('ip')
    os_name     = models.CharField('OS', max_length = 16)
    director	= models.CharField('负责人', max_length = 16)
    nature      = models.CharField('配置', max_length = 16, help_text = 'such as 2C4G200G')
    isvhost     = models.BooleanField('虚机')
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


class OhostInfo(models.Model):
    area        = models.CharField(verbose_name = '所在地', max_length = 24)
    hostname    = models.CharField('主机简称', max_length = 24)
    root        = models.CharField('root账号', max_length = 16, default = '')
    rootpasswd  = models.CharField('root密码', max_length = 24, default = '')
    ip          = models.GenericIPAddressField('ip')
    ohost       = models.GenericIPAddressField('宿主机', default = '0.0.0.0', help_text = '没有就写0.0.0.0')
    os_name     = models.CharField('OS', max_length = 16)
    director	= models.CharField('运维负责人', max_length = 16, default = '')
    user        = models.CharField('使用人', max_length = 16, default = '')
    cpus        = models.SmallIntegerField('cpu核数')
    mems        = models.SmallIntegerField('内存/G')
    disk        = models.SmallIntegerField('磁盘/G')
    isvhost     = models.BooleanField('虚机', default = True)
    status      = models.BooleanField('已分配', default = 'False')
    note        = models.CharField('用处/备注', max_length = 50, blank = True)
    needs       = models.CharField('其他要求', max_length = 50, blank = True)
    
    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = 'x-测试环境'
        verbose_name_plural = 'x-测试环境'
        permissions = (
                    ('report_virtualinfo', '导出表格'),
                    ('import_virtualinfo', '导入表格'),
                )
