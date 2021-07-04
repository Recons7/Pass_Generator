import random
import string
import pyfiglet
import sys, time, os

from termcolor import colored 

os.system('clear')

banner = pyfiglet.figlet_format("pwd >< gen")

print(colored(banner, "magenta"), "\n")

developer = colored("\n\t   >> Developed By Suraj Sharma <<\n\n", "yellow")

for about_dev in developer:
	sys.stdout.write(about_dev)
	sys.stdout.flush()
	time.sleep(0.01)

print(colored("\n\n"+"#"*50, "green"))

def password_generator():
		
		try:
			
			length = int(input("\n\n\nEnter length for your password : "))
			
			patterns = int(input(colored("\n\n\nEnter how many passwords : ", "blue")))
		
		
			lower  = string.ascii_lowercase
			
			upper = string.ascii_uppercase
			
			digits = string.digits
			
			punc = string.punctuation
			
			combination = (lower+upper+punc+digits)
			
			
			print(colored("\n\n\n"+"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈{Passwords}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈", "cyan"))
			
			for i in range(1, patterns+1):
				
				strong_pwd = random.sample(combination, length)
				
				joint_pwd = ''.join(strong_pwd)
				
				print(colored("\n\n\nPassword => ", "yellow"), end="")
				
				print(colored(f"{joint_pwd}", "green"))
			print(colored("\n\n\n"+"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈{Passwords}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈", "cyan"))
			
		except Exception as error:
			
			print(colored("\n\n\nPlease Enter Correct Value...\n", "red"))
		
	
		password_generator()
		
password_generator()
		
		
