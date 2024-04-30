import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formatdate

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment=None):
    smtp_server = 'smtp.163.com'
    smtp_port = 465  # 使用 SSL/TLS 连接的 SMTP 端口号

    # 创建 MIME 文档
    message = MIMEMultipart()
    message['From'] = 'tcsendmail@163.com'
    message['To'] = 'onion@163.com'
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))  # 添加邮件正文

    if attachment:
        # 添加附件
        with open(attachment, 'rb') as file:
            part = MIMEApplication(file.read(), Name=attachment)
        part['Content-Disposition'] = f'attachment; filename="{attachment}"'
        message.attach(part)

    try:
        # 连接 SMTP 服务器
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)  # 登录邮箱

            # 发送邮件
            server.sendmail(sender_email, recipient_email, message.as_string())

        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败：{e}")

# 使用示例
if __name__ == "__main__":
    sender_email = 'tcsendmail@163.com'
    sender_password = 'ZRKHLLTHHIAYSUBN'
    recipient_email = 'onion@163.com'
    subject = 'Test Email with Attachment'
    body = 'This is a test email sent from Python.'
    attachment_path = '/tmp/1.txt'  # 替换为你的附件路径，可选

    send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path)
