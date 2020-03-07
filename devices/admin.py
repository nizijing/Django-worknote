from django.contrib import admin
from .models import ProInfo, DeviceInfo, UnitInfo, AppInfo
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class DeviceInfoResource(resources.ModelResource):
    class Meta:
        model = DeviceInfo

class UnitInfoResource(resources.ModelResource):
    class Meta:
        model = UnitInfo

class AppInfoInline(admin.TabularInline):
    model = AppInfo
    extra = 0


class UnitInfoInline(admin.TabularInline):
    model = UnitInfo
    extra = 0


class DeviceInfoInline(admin.TabularInline):
     model = DeviceInfo
     extra = 0


@admin.register(ProInfo)
class ProInfoAdmin(admin.ModelAdmin):
    inlines     = (UnitInfoInline, AppInfoInline)
    list_filter = ('pro_type', )
    list_display    = ('id','pro_name', 'pro_type', 'pro_ctime', 'pro_link', 'note')
    search_fields   = ('pro_name', )
    list_display_links  = ('pro_name',)


@admin.register(DeviceInfo)
class DevicesAdmin(ImportExportModelAdmin):
    list_filter     = ('pro', )
    list_display    = ('pro', 'hostname', 'ip', 'unit_name', 'isvhost', 'hostDevice', 'os_name', 'nature', 'note')
    search_fields   = ('pro__pro_name', )
    resource_class  = DeviceInfoResource


@admin.register(UnitInfo)
class UnitAdmin(ImportExportModelAdmin):
    list_filter     = ('pro', )
    list_display    = ('pro', 'unit_name', 'src_unit', 'src_app', 'dest_unit', 'dest_vip', 'dest_app', 'dest_port', 'test_way', 'note')
    search_fields   = ('pro__pro_name', )
    resource_class  = UnitInfoResource


