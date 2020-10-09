import calendar

from django.test import TestCase

# Create your tests here.
import time
import datetime
# 获取今天是第几周
this_week = int(time.strftime('%W'))+1
print(this_week)
# this = time.strftime('%W')
# print(this)
# # 获取当前是周几(0-6,0代表周一)
# today=datetime.datetime.now().weekday()
# # 获取指定日期属于当年的第几周
# week=datetime.datetime.strptime('20190825','%Y%m%d').strftime('%W')
# print(week)
# now = datetime.datetime.now()
# today = now
# last_week_start = now - datetime.timedelta(days=today.weekday()+7)
# print(last_week_start)
# 指定时间周期
# ---------------------------------------------------------------------------
# today1 = datetime.datetime.now()
# today2 = datetime.datetime.today()
# print('今天是',today1)
# # 指定时间周期
# oneday = datetime.timedelta(days=1)
# oneweek = datetime.timedelta(days=7)
# # 获取周日的判断条件（周一为0，周日为6,周六为5）
# w6 = calendar.SATURDAY
# w7 = calendar.SUNDAY
# if today1.weekday() != w7: #如果今天不是周日
#     while today1.weekday() != w7:
#         today1-=oneday
# else:
#     today1-=oneweek
# print(today1) # 输出这周的周日，这周的第一天
# last_week_end = today1-oneday
# last_week_start = today1-oneweek
# print("上周周六是",last_week_end)
# print("上周周日是",last_week_start)
# ---------------------------------------------------------------------------
# arr = [4,6,3,5,2,1]
# def bubble_sort(arr):
#     n = len(arr) # 获取arr数组的长度
#     for j in range(0,n-1): # range() 函数可创建一个整数列表，一般用在 for 循环中。
#         print('j=',j)
#         for i in range(0,n-1-j): #
#             print('i=',i)
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1] = arr[i+1],arr[i]
#                 print('第',i+1,'次排序结果',arr)
#             else:
#                 print('第',i+1,'次排序结果',arr)
#
#         print('-------------------------------------')
#
# bubble_sort(arr)
# ----------------------------------------------------------------------
# arr = [5,98,56,48,67,49,23,65,46]
# arr.sort()
# print(arr)


