
import smtplib
import random

def getData(mail):
	code = random.randint(100000, 999999)
	server = smtplib.SMTP(smtplib.gmail.com,587)
	title = "Minerva User Verification"
	data = f'''
		Hey user,
			We welcome you to be the teacher of our platform. 
   
			Verification Code : {code}
 	'''
	email_addr = "erikduke182@gmail.com"
	email_passwd = "alpha-vega"
	server.starttls()
	try:
		server.login(email_addr,email_passwd)
	except Exception as e:
		print('Exception Occured {}'.format(e))
	title = f"{title}"
	message = f"Subject {title}\n\n{data} "
	server.sendmail(email_addr,mail,data) 
	server.quit()
	return code

