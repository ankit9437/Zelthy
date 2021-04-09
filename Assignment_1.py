import smtplib              #Python Library

print("Subject?")
sub=input()                 #Used to take subject
print("Body?")  
message = input()           #Used for taking message for email
print("Recipient")
receivers_mail = input()    #Used to take receiver's mail
print("Sender's Mail?")
sender_mail= input()        #Used to take sender's mail
try:    
   password = input('Enter the password')       #Enter password of sender's email ID 
   smtpObj = smtplib.SMTP('gmail.com',587)    
   smtpObj.login(sender_mail,password)    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")             #If the email is sent successfullt
except Exception:    
   print("Error: unable to send email")         #If the email is not successful