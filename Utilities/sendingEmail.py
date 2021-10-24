import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("testexample65@gmail.com","shafi_FORu65")
server.sendmail("testexample65@gmail.com","ershafaat@gmail.com","Hello how are you")
server.quit()