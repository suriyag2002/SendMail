import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

# Use your email and app password/generated password here
server.login("suriya.gunasekaran2002@gmail.com", "YourAppOrAccountPassword")

server.sendmail("suriya.gunasekaran2002@gmail.com",    #sender mail
                "isur8388@gmail.com", #receiver mail
                "Subject: Your Subject Here\n\n")    #message and subject

print("Mail sent")
