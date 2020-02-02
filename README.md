# Django-1
实现基于sqlit数据库的增删
用到的第三方库

- asgiref         :3.2.3 
- Django         :1.11.7 
- pip                :19.0.3 
- PyMySQL    :0.9.3 
-  pytz              :2019.3 
- setuptools     :40.8.0 
- sqlparse        :0.3.0
#### 班级和学生级联显示

1. 班级列表，班级列表可点击： <img src="https://github.com/thinkforanameissohard/Django-1/blob/master/image/image-20200202193352583.png" />
2. 点击之后显示本班的所有学生：<img src="https://github.com/thinkforanameissohard/Django-1/blob/master/image/image-20200202193913136.png" />
3. 要求：
   1. 路径全都使用反向解析
   2. 在学生列表页面添加点击事件
      1. 点击学生可以进入学生详情
      2. 在详情中，存在删除按钮，点击删除
      3. 在学生列表最后面，添加输入窗口，可以添加学生
