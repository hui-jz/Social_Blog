# 电子邮件
from flask_mail import Mail
from flask_mail import Message


# 邮箱配置
app.config['MAIL_SERVER'] = 'smtp.163.com'  # SMTP服务器
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # 接收存储用户名的变量 MAIL_USERNAME
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # 接收存储密码的变量 MAIL_PASSWORD
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <18056170605@163.com>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
mail = Mail(app)


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr