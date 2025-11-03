import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(nombre, apellidos, texto, mail):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_usuario = "connectinggrandparents@gmail.com"
    email_password = "ywew ndna vjmd tvlf"

    mensaje = MIMEMultipart()
    mensaje["Subject"] = "Nueva reseña / Mensaje"
    mensaje["From"] = email_usuario
    mensaje["To"] = mail

    html = f"""
    <html>
    <body>
        <h2>{nombre} {apellidos}</h2>
        <p>{texto}</p>
    </body>
    </html>
    """
    mensaje.attach(MIMEText(html, "html"))

    try:
        # 👇 Límite de tiempo en la conexión (muy importante)
        with smtplib.SMTP(smtp_server, smtp_port, timeout=5) as servidor:
            servidor.starttls()
            servidor.login(email_usuario, email_password)
            servidor.sendmail(email_usuario, [mail], mensaje.as_string())
        return "Correo enviado correctamente."
    except smtplib.SMTPAuthenticationError:
        return "Error: credenciales SMTP inválidas o bloqueadas por Gmail."
    except smtplib.SMTPConnectError:
        return "Error: no se pudo conectar al servidor SMTP."
    except Exception as e:
        return f"Error inesperado al enviar el correo: {e}"
