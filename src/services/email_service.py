import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_correo(destinatario, nueva_password):

    remitente = "TU_CORREO@gmail.com"

    contraseña = "TU_PASSWORD_DE_APLICACION"

    asunto = "Recuperación de contraseña"

    mensaje = f"""
Hola.

Tu nueva contraseña es:

{nueva_password}

Ya puedes iniciar sesión.
"""

    msg = MIMEMultipart()

    msg["From"] = remitente
    msg["To"] = destinatario
    msg["Subject"] = asunto

    msg.attach(
        MIMEText(
            mensaje,
            "plain"
        )
    )

    try:

        servidor = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        servidor.starttls()

        servidor.login(
            remitente,
            contraseña
        )

        servidor.send_message(msg)

        servidor.quit()

        return True

    except Exception as e:

        print("ERROR CORREO:", e)

        return False