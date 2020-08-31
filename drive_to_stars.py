# Stairway to STARS
# Last Modified: 29.4.2020 ; chrome version is 81 now and program works
import imaplib
import time
import re
from selenium import webdriver

SRS_URL = "https://stars.bilkent.edu.tr/srs"

# User configuration
STUDENT_ID = "your_id_here" 
SRS_PASSWORD = "srs_password"
MAIL_HANDLE = "your_mail_address_here"
MAIL_PASSWORD = "email_password"

def login_srs(explorer, id_, srs_password, mail_address, mail_pwd):
	explorer.get(SRS_URL)

	# Fill in the blanks
	user_name, pswd, _ = browser.find_elements_by_tag_name("input")
	user_name.send_keys(id_)
	pswd.send_keys(srs_password)

	login_button = browser.find_element_by_tag_name("button")
	login_button.click()
	time.sleep(1.2)

	# Next step is to have the verification code and enter it
	v_code = read_from_mail(mail_address, mail_pwd)
	if v_code is None:
		raise ValueError("Unable to detect the verification code.")

	# Find the verification code input field and fill in
	vcode_inp = explorer.find_element_by_tag_name("input")
	vcode_inp.send_keys(v_code)

	# click to verify and all the way to SRS!
	verify_button = explorer.find_element_by_tag_name("button")
	verify_button.click()

def read_from_mail(mail_address, password):
	"""
	Somewhat specific email-reader function that returns the verification code
	for STARS system, designed considering the structure of the verification code e-mails.
	"""

	# Entering to the server, mail and inbox
	mail = imaplib.IMAP4_SSL("mail.bilkent.edu.tr")
	mail.login(mail_address,password)
	mail.select("inbox")

	# Get all the mails in inbox (their "id"s)
	_, msg_nums = mail.search(None, "ALL")
	mail_ids = msg_nums[0]
	id_list = mail_ids.split()

	# Retrieval of the latest email
	last = id_list[-1]
	_, data = mail.fetch(last, "(RFC822)")
	content = str(data[0][1])

	# The Verification Code, finally
	regex = re.compile(r"Code: (\d+)")
	result = regex.search(content)
	code = int(result.group(1)) if result is not None else None

	return code

if __name__ == "__main__":
	# The chrome driver is of version 81
	driver_path = r"chromedriver.exe"
	browser = webdriver.Chrome(executable_path=driver_path)

	login_srs(explorer=browser, id_=STUDENT_ID, srs_password=SRS_PASSWORD,
				mail_address=MAIL_HANDLE, mail_pwd=MAIL_PASSWORD)