from django.urls import path

from . import views

urlpatterns = [
    path('', views.gologin, name='gologin'), # 首页显示登录页
    path(r'login',views.login,name='login'), # 登录函数
    path(r'info.html',views.info,name='info'), # 进入用户信息页面,获取信息
    path(r'go_changePassword.html',views.go_changePassword,name='go_changePassword'), #进入修改用户密码页面
    path(r'changePassword.html',views.changePassword,name='changePassword'), #修改用户密码
    path(r'add.html',views.add,name='add'), # 进入添加用户页面
    path(r'addUser',views.addUser,name='addUser'), # 添加新用户
    path(r'userList.html',views.userList,name='userList'), # 所有用户
    path(r'findUser.html',views.findUser,name='findUser'), # 模糊搜索用户
    path(r'deleteUser',views.deleteUser,name='deleteUser'), # 删除单条用户信息
    path(r'selectDelUser',views.selectDelUser,name='selectDelUser'), # 批量删除用户信息
    path(r'goModify',views.goModify,name='goModify'), # 进入修改用户页面
    path(r'modifyUser',views.modifyUser,name='modifyUser'), # 修改用户信息
    path(r'addReport.html',views.addReport,name='addReport'), # 进入添加周报页面
    path(r'createReport',views.createReport,name='createReport'), # 新增周报
    path(r'myReport.html',views.show_myReport,name='show_myReport'), # 进入“我的周报”
    path(r'thisWeek.html',views.thisWeek,name='thisWeek'), # 进入本周周报
]