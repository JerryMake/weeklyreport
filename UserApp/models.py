from django.db import models


class User(models.Model):
    # 用户表实例
    id = models.AutoField(verbose_name='id',primary_key=True)
    userCode = models.CharField(max_length=30,verbose_name='用户账号')
    userPassword = models.CharField(max_length=30,verbose_name='用户密码')
    logo = models.ImageField(upload_to='')
    userName = models.CharField(max_length=30,verbose_name='用户名称')
    role = models.CharField(max_length=10,verbose_name='用户角色')
    createTime = models.CharField(max_length=30,verbose_name='创建时间')
    department = models.CharField(max_length=30,verbose_name='部门')
    def __unicode__(self):
        return u'User:%s'%self.id

    class Meta():
        # 实体连接user表
        db_table = 'user'

class Report(models.Model):
    # 周报表实例
    id = models.AutoField(verbose_name='id',primary_key=True)
    department = models.CharField(max_length=30,verbose_name='部门')
    reporter = models.CharField(max_length=10,verbose_name='周报填写人')
    this_week_completed = models.TextField(max_length=1200,verbose_name='本周完成的计划工作')
    this_week_not_completed = models.TextField(max_length=1200,verbose_name='本周未完成的计划工作')
    last_reson = models.CharField(max_length=10,verbose_name='上周未完成原因')
    next_week_plan = models.CharField(max_length=225,verbose_name='下周工作计划')
    need_help = models.CharField(max_length=255,verbose_name='需要公司协调的事项')
    createTime = models.DateTimeField(verbose_name='周报创建时间',auto_now_add=True)
    week_number = models.CharField(max_length=10,verbose_name='周数')

    def __str__(self):
        return u'Report:%s'%self.id

    class Meta():
        db_table = 'report'