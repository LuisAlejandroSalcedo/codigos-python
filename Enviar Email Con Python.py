 import smtplib 
    
from email.MIMEText import MIMEText 

emisor = "copia el mail de origen" 
receptor = "copia el mail de destino" 
    
# Configuracion del mail 
mensaje = MIMEText("Este correo ha sido enviado desde Python") 
mensaje['From']=emisor 
mensaje['To']=receptor 
mensaje['Subject']="Mi primer correo desde Python" 
    
# Nos conectamos al servidor SMTP de Gmail 
serverSMTP = smtplib.SMTP('smtp.gmail.com',587) 
serverSMTP.ehlo() 
serverSMTP.starttls() 
serverSMTP.ehlo() 
serverSMTP.login(emisor,"ingresa la contraseña de tu correo con el que deseas enviar un mail") 
    
# Enviamos el mensaje 
serverSMTP.sendmail(emisor,receptor,mensaje.as_string()) 
    
# Cerramos la conexion 
serverSMTP.close()
