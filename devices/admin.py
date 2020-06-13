from django.contrib import admin
from .models import ProInfo, DeviceInfo, UnitInfo, AppInfo, VirtualInfo, vhostInfo
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


class VirtualInline(admin.TabularInline):
    model = VirtualInfo
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
    list_filter     = ('pro', 'director', 'director')
    list_display    = ('pro', 'hostname', 'ip', 'isvhost', 'os_name', 'nature', 'director', 'note')
    search_fields   = ('pro__pro_name', )
    resource_class  = DeviceInfoResource


@admin.register(UnitInfo)
class UnitAdmin(ImportExportModelAdmin):
    list_filter     = ('pro', )
    list_display    = ('pro', 'unit_name', 'src_unit', 'src_app', 'dest_unit', 'dest_vip', 'dest_app', 'dest_port', 'test_way', 'note')
    search_fields   = ('pro__pro_name', )
    resource_class  = UnitInfoResource


@admin.register(VirtualInfo)
class VirtualAdmin(ImportExportModelAdmin):
    list_devtest    = ('area', 'ip', 'os_name', 'cpus', 'mems', 'disk', 'user', 'director', 'status', 'note')
    search_fields   = ('ip', )
    list_filter     = ('area', 'os_name', 'user', 'director', 'isvhost', 'ohost', 'status')
    list_display    = ('area', 'hostname', 'ip', 'os_name', 'loginuser', 'rootpasswd', 'cpus', 'mems', 'disk', 'user', 'director', 'ohost', 'isvhost', 'status', 'note')
    field_add       = (
            ('申请信息', { 'fields': ('area', 'os_name', 'cpus', 'mems', 'disk', 'user', 'note')}),
            )

    def get_fieldsets(self, request, obj=None):
        if self.has_change_permission(request, obj):
            return [(None, {'fields': self.get_fields(request, obj)})]
        if 'add' in request.META['PATH_INFO']:
            return self.field_add
        
    def get_list_display(self, request):
        if not self.has_change_permission(request, obj=None):
            return self.list_devtest
        return self.list_display



@admin.register(vhostInfo)
class VhostInfoAdmin(ImportExportModelAdmin):
    list_devtest    = ('fid', 'ip', 'os_name', 'cpus', 'mems', 'disk', 'user', 'director', 'status', 'note')
    search_fields   = ('ip', 'hostname', 'note')
    list_filter     = ('fid', 'os_name', 'user', 'director')
    list_display    = ('fid', 'hostname', 'ip', 'os_name', 'loginuser', 'rootpasswd', 'cpus', 'mems', 'disk', 'user', 'director', 'status', 'note')
    field_add       = (
            ('申请信息', { 'fields': ('fid', 'os_name', 'cpus', 'mems', 'disk', 'user', 'note')}),
            )

    def get_fieldsets(self, request, obj=None):
        if self.has_change_permission(request, obj):
            return [(None, {'fields': self.get_fields(request, obj)})]
        if 'add' in request.META['PATH_INFO']:
            return self.field_add
    

    def get_list_display(self, request):
        if not self.has_change_permission(request, obj=None):
            return self.list_devtest
        return self.list_display


