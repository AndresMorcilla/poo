from mailAutomation import EmailSender

# ⚙️ Datos del remitente
usuario = "t4yl0r.4l1s0n.sw1ft.shake.it.off@gmail.com" # ignore el correo profe :)
contraseña = "obxs caxi bqco dviq"  # Contraseña de aplicación

# ✉️ Crear objeto y enviar
correo = EmailSender(usuario, contraseña)
correo.enviar_mail(
    destinatario="agmorillofigueroa@escuelasproa.edu.ar",
    asunto="title",
    mensaje="Hello World!"
)
