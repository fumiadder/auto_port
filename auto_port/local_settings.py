
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'root123',  # 数据库用户密码
        'NAME': 'auto_port'  # 数据库名字
    }
}


#  ############################# Django发邮件 #############################
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True  # 是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_USE_SSL = False  # 是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.qq.com'  # 发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 25  # 发件箱的SMTP服务器端口
EMAIL_HOST_USER = '2521532473@qq.com'  # 发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'hlxqpyuxyvntdjef'  # 发送邮件的邮箱密码(这里使用的是授权码)
EMAIL_TO_USER_LIST = ['zhougang@zjaxtynkjyxgs128.wecom.work']   # 此字段是可选的，用来配置收件人列表
