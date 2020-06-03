from django.contrib import admin

# Register your models here.
from .models import ProInfo, TaskInfo, EventInfo
from django.utils import timezone
from .models import FINISHJOB, MIDDLEPRI
from django.contrib import messages
from datetime import date


class TaskInfoInline(admin.TabularInline):
    model = TaskInfo
    ordering = ('task_status', 'task_ftime' )
    fieldsets = [(None, {'fields':['task_name','task_dealer', 'task_ftime', 'task_nice', 'task_status', 'task_note']})]
    readonly_fields = ('task_nice',)
    extra = 0


class EventInfoInline(admin.TabularInline):
    model   = EventInfo
    extra   = 0


@admin.register(ProInfo)
class ProInfoAdmin(admin.ModelAdmin):
    inlines     = (EventInfoInline,)
    list_display    = ('pro_name', 'province', 'pro_ctime', 'pro_link', 'get_event_status')
    search_fields   = ('pro_name', )
    list_filter        = ('province', )


@admin.register(EventInfo)
class EventInfoAdmin(admin.ModelAdmin):
    inlines         = (TaskInfoInline,)
    list_display    = ('pro', 'event_name', 'event_priority', 'get_task_status')
    search_fields   = ('event_name',)
    list_filter     = ('pro', 'event_priority',)
    ordering        = ('event_priority', 'pro')
    list_editable   = ('event_priority', )

    def save_model(self, request, obj, form, change):
        if '/add/' in request.META['PATH_INFO']:
            pass
        else:
            for item in TaskInfo.objects.filter(task_id = obj.id):
                if item.task_ftime >= item.task_mtime:
                # 如果在规定时间内完成任务.
                    item.task_nice = True
                else:
                    item.task_nice = False
                item.save()
        obj.save()


@admin.register(TaskInfo)
class TaskInfoAdmin(admin.ModelAdmin):
    ordering       = ('task_status', 'task_ftime')
    list_filter    = ('task_id__pro', 'task_id', 'task_status', 'task_dealer', 'task_mtime')
    list_display   = ('get_pro_name', 'task_id', 'task_dealer', 'task_name', 
            'task_status', 'task_stime', 'task_mtime', 'task_ftime', 'task_nice', 'task_note')
    list_editable  = ('task_status', )
    search_fields  = ('task_name',)
    date_hierarchy = ('task_mtime')
    readonly_fields = ('task_nice', )

    def save_model(self, request, obj, form, change):
        if '/add/' in request.META['PATH_INFO']:
            obj.task_dealer_id = request.user.num
        elif request.user.is_superuser or obj.task_dealer_id == request.user.num:
            if obj.task_ftime >= date.today():
                # 如果在规定时间内完成任务
                obj.task_nice = True
            else:
                obj.task_nice = False
        else:
            messages.error(request, "you cannot change other staff task message!")
            messages.set_level(request, messages.ERROR)
            return
        obj.save()

