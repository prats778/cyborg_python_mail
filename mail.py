import smtplib,csv

EMAIL_ADDRESS = 'dav.pratyush@gmail.com'#give your own email id here
EMAIL_PASSWORD = input("enter your email password and press enter: \n")
message = """Subject: Your certficate

Hi, your certificate is here {link}"""

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
   smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD )
   with open("info.csv") as file:
   	reader = csv.reader(file)
   	next(reader)
   	count = 0
   	for email_id, link in reader:
   		smtp.sendmail(
   			EMAIL_ADDRESS,
   			email_id,
   			message.format(link=link),
   			)
   		count = count + 1
   		print("mail has been sent to candidate no. {count} {email_id} \n".format(count=count,email_id=email_id))
print("all emails have been successfully delivered to {count} candidates".format(count=count))
   		