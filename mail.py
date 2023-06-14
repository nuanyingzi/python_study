import smtplib
import email.utils
from email.mime.text import MIMEText

# 创建邮件
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'zhongtao1024@gmail.com'))
msg['From'] = email.utils.formataddr(('Author',
                                      '852947475@qq.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(True)  # 展示与服务器的交互信息
try:
    server.sendmail('852947475@qq.com',
                    ['zhongtao1024@gmail.com'],
                    msg.as_string())
finally:
    server.quit()
