"""
优秀 90分以上
良好 80-90
一般 70-80
及格 60-70
不及格 <60
"""

score = float(input('请输入成绩:'))
if score >= 90:
    print("成绩为优秀")
elif score >= 80:
    print('成绩为良好')
elif score >= 70:
    print('成绩为一般')
elif score >= 60:
    print('成绩为及格')
else:
    print('成绩为不合格')
