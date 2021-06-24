import smtplib as s

ob = s.SMTP("smtp.gmail.com",587)
ob.starttls()

ob.login("pkumarp1998@gmail.com","Accenture@@55")
print("h1")
subject = "Sending email using python"
body = "This is a working email sender software using python script"

message = "Subject:{}\n\n{}".format(subject,body)
#print(message)
listOfAddress = ["pkumarp1998@gmail.com","pkumarpatel100298@gmail.com"]
#"pandey299prakash@gmail.com"
ob.sendmail("pkumarp1998@gmail.com",listOfAddress,message)

print("Sent successfully")
ob.quit()