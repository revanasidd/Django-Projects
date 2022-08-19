import smtplib
sender="shubham247341@gmail.com"
reciever='ds299676@gmail.com'
password=input("please enter your password: ")
msg="Hey, This is my test message"

server=smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender,password)
print("login successfully!!")
server.sendmail(sender,reciever,msg)
print("Email has been sent to", reciever)