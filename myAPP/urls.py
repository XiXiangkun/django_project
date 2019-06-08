from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path(r'<int:num>/',views.detail),
    path(r'login/',views.login),
    path(r'user/login/',views.login),
    path(r'user/',views.user,name="user"),
    path(r'myself/',views.myself,name="myself"),
    #打卡签到
    path(r'user/signIn/',views.signIn,name="signIn"),
    #工作安排
    path(r'user/workArrangements/',views.workArrangements,name="workArrangements"),
    #加班
    path(r'user/workOvertime/',views.workOvertime,name="workOvertime"),
    #请假
    path(r'user/leaveWork/',views.leaveWork,name="leaveWork"),
    #个人信息
    path(r'user/selfInfo/',views.selfInfo,name="selfInfo"),
    #个人信息修改
    path(r'user/selfInfo/edit/',views.selfInfoEdit),
    path(r'user/selfInfo/sub/',views.generate_qrcode,name='qrcode'),
    path(r'qrform/',views.qrform,name='qrform'),
    path(r'qrform/signIn/',views.signIn),
    #个人信息修改提交
    path(r'user/selfInfo/edit/editSub/',views.editSub,name='editSub'),
    #请假、销假申请提交
    path(r'user/leaveWork/leaveSub/',views.leaveSub,name='leaveSub'),
    #加班申请提交
    path(r'user/workOvertime/overSub/',views.overSub,name='overSub'),
]