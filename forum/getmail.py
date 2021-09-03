
import smtplib

def getData(title,data):
	server = smtplib.SMTP(smtp.gmail.com,587)
	email_addr = #email_address
	email_passwd = #email_pass
	server.starttls()
	try:
		server.login(email_addr,email_passwd)
	except Exception as e:
		print('Exception Occured {}'.format(e))
	title = f"{title}"
	message = f"Subject {title}\n\n{data} "
	server.sendmail(email_addr,'contact@apurbaadhikari.com.np',data)
	server.quit()

