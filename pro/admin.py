from django.contrib import admin

# Register your models here.
from .models import ProInfo, TaskInfo, EventInfo
from django.utils import timezone
from .models import FINISHJOB, MIDDLEPRI


class TaskInfoInline(admin.TabularInline):
	model = TaskInfo
	ordering = ('task_status', 'task_mtime' )
	extra = 0


class EventInfoInline(admin.TabularInline):
	model   = EventInfo
	extra   = 0


@admin.register(ProInfo)
class ProInfoAdmin(admin.ModelAdmin):
	inlines	 = (EventInfoInline,)
	list_display	= ('pro_name', 'province', 'pro_ctime', 'pro_link', 'pro_status', 'get_event_status')
	search_fields   = ('pro_name', )
	list_filter		= ('province', )
	ordering		= ('pro_status', )


@admin.register(EventInfo)
class EventInfoAdmin(admin.ModelAdmin):
	inlines		 = (TaskInfoInline,)
	list_display	= ('pro', 'event_name', 'event_ctime', 'event_priority', 'get_task_status')
	search_fields   = ('event_name',)
	list_filter     = ('pro', 'event_priority',)
	ordering		= ('event_priority', 'pro', 'event_ctime')
#	list_editable   = ('event_status', )


@admin.register(TaskInfo)
class TaskInfoAdmin(admin.ModelAdmin):
	ordering	   = ('task_status', 'task_id' )
	list_filter	   =  ('task_status', 'task_mtime')
	list_display   = ('get_pro_name', 'task_id', 'task_name', 'task_status', 'task_mtime', 'task_note')
	list_editable  = ('task_status', )
	search_fields  = ('task_name',)
	date_hierarchy = ('task_mtime')

	def save_model(self, request, obj, form, change):
		obj.save()
		if all([ item.task_status for item in TaskInfo.objects.filter(task_id = obj.task_id) ]):
			obj.task_id.event_priority = FINISHJOB
			obj.task_id.save()
		elif  obj.task_id.event_priority == FINISHJOB:
			obj.task_id.event_priority = MIDDLEPRI
			obj.task_id.save()

