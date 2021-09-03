import smtplib
import random
import requests

def getData(mail):
	code = random.randint(100000, 999999)
	server = smtplib.SMTP("smtp.gmail.com",587)
	title = "Minerva User Verification"
	data = f'''
Hey user,
	We welcome you to be the teacher of our platform. 
   
	Verification Code : {code}
 
Regards,
Minerva
 	'''
	email_addr = "ashjoes2212@gmail.com"
	email_passwd = "LeoMessi"
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

def check_github(username):
    res = requests.get("https://github.com/" + username)
    return res.status_code != 404
