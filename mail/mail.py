import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import json

def send_mail(nombre,apellidos,texto,mail):
    # Configuración
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_usuario = "connectinggrandparents@gmail.com"
    email_password = "ywew ndna vjmd tvlf"

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje["Subject"] = "Nueva reseña / Mensaje"
    mensaje["From"] = email_usuario
    mensaje["To"] = mail

    html = '''\
                <meta charset="utf-8">
      <html>
      <body">
        <h2>'''+nombre+' '+apellidos+'''</h2>
        '''+texto+'''
      </body>
      </html>
      '''

    mensaje.attach(MIMEText(f'''\
    {html}
    ''', "html"))

    # Enviar el correo
    try:
        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()
        servidor.login(email_usuario, email_password)
        servidor.sendmail(email_usuario, [mail], mensaje.as_string())
        servidor.quit()
        return "Correo enviado correctamente."
    except Exception as e:
        return f"Error al enviar el correo: {e}"


    # Contraseña de aplicación: ywew ndna vjmd tvlf
