from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(seminar)
#admin.site.register(people)
admin.site.register(news)
admin.site.register(conferences)
admin.site.register(themes)
admin.site.register(banner)
admin.site.register(people_priority)
admin.site.register(about)
admin.site.register(papers)
admin.site.register(papers_categroy)


from guardian.admin import GuardedModelAdmin


###以下是行权限修饰器
from guardian.shortcuts import get_objects_for_user, assign_perm, remove_perm, get_users_with_perms, \
    get_groups_with_perms
@admin.register(people)
class DataAssistantJobAdmin(GuardedModelAdmin):
    # app是否在主页面中显示的话由该函数决定
    def has_module_permission(self, request):
        if super().has_module_permission(request):
            return True
        return self.get_model_objs(request).exists()

    # 在显示数据列表额时候，哪些数据显示，哪些不显示，由该函数控制
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)

        data = self.get_model_objs(request)
        return data
        
    # 内部用来获取某个用户有权限访问的数据行
    def get_model_objs(self, request, action=None, klass=None):
        opts = self.opts
        actions = [action] if action else ['view', 'change', 'delete']
        klass = klass if klass else opts.model
        model_name = klass._meta.model_name
        return get_objects_for_user(user=request.user, perms=[f'{perm}_{model_name}' for perm in actions],
                                    klass=klass, any_perm=True)

    # 用来判断某个用户是否有某个数据行的权限
    def has_perm(self, request, obj, action):
        opts = self.opts
        codename = f'{action}_{opts.model_name}'
        if obj:
            return request.user.has_perm(f'{opts.app_label}.{codename}', obj)
        else:
            return self.get_model_objs(request, action).exists()

    # 是否有查看某个数据行的权限
    def has_view_permission(self, request, obj=None):
        return self.has_perm(request, obj, 'view')

    # 是否有修改某个数据行的权限
    def has_change_permission(self, request, obj=None):
        return self.has_perm(request, obj, 'change')

    # 是否有删除某个数据行的权限
    def has_delete_permission(self, request, obj=None):
        return self.has_perm(request, obj, 'delete')

    # 用户应该拥有他新增的数据行的所有权限
    def save_model(self, request, obj, form, change):
        result = super().save_model(request, obj, form, change)
        if not request.user.is_superuser and not change:
            opts = self.opts
            actions = ['view', 'add', 'change', 'delete']
            [assign_perm(f'{opts.app_label}.{action}_{opts.model_name}', request.user, obj) for action in actions]
        return result
