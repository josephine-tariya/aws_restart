import getpass

users = ['james', 'mary', 'jane']
pins = ['1234', '2222', '3333']
amounts = [1500, 2200, 3050]
count = 0

# while loop checks existance of the enterd username
print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome to TANGO Bank                  *")
print("*                                                                          *")
print("****************************************************************************")
while True:
	user = input('\nPlease enter your name: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
		print('----------------')
		print('****************')
		print('Username does not exist')
		print('****************')
		print('----------------')

# comparing pin
while count < 3:
	print('------------------')
	print('******************')
	pin = getpass.getpass('Please input your pin: ')
	password_length = len(pin)
	password_hide = ('*' * password_length)
	print('******************')
	print('------------------')
	if pin.isdigit():
		if user == 'james':
			if pin == pins[0]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('Pin is incorrect. Try again. ')
				print('***********')
				print('-----------')
				print()

		if user == 'mary':
			if pin == pins[1]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('Pin is incorrect. Try again ')
				print('***********')
				print('-----------')
				print()
				
		if user == 'jane':
			if pin == pins[2]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('Pin is incorrect. Try again')
				print('***********')
				print('-----------')
				print()
	else:
		print('------------------------')
		print('************************')
		print('Please enter a four-digit pin: ')
		print('************************')
		print('------------------------')
		count += 1
	
# in case of a valid pin- continuing, or exiting
if count == 3:
	print('-----------------------------------')
	print('***********************************')
	print('You have incorrectly typed your pin 3 times.')
	print('!!!!!Your card has been locked. Please contact customer care!!!!!')
	print('***********************************')
	print('-----------------------------------')
	exit()

print('-------------------------')
print('*************************')
print('You have succesfully logged in! ')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')	
print('Hello', str.capitalize(users[n]),', Welcome to Tango Bank ATM System')
print('**************************')
print('----------TANGO BANK-----------')

# Main menu
while True:
	#os.system('clear')
	print('-------------------------------')
	print('*******************************')
	response = input('Please select: \n(S) for Statement \n(W) to Withdraw \n(D) to Deposit  \n(P) to Change pin \n(Q) to Quit \n: ')
	print('*******************************')
	print('-------------------------------')
	valid_responses = ['s', 'w', 'd', 'p', 'q']
	response = response.lower()
	if response == 's':
		print('---------------------------------------------')
		print('*********************************************')
		print(str.capitalize(users[n]), 'Your current balance is Ksh.', amounts[n])
		print('*********************************************')
		print('---------------------------------------------')
		
	elif response == 'w':
		print('---------------------------------------------')
		print('*********************************************')
		userWithdraw = int(input('How much would you like to withdraw? : '))
		print('*********************************************')
		print('---------------------------------------------')
		if userWithdraw%1 != 0:
			print('------------------------------------------------------')
			print('******************************************************')
			print('Please enter an amount in multiples of Ksh. 100')
			print('******************************************************')
			print('------------------------------------------------------')
		elif userWithdraw > amounts[n]:
			print('-----------------------------')
			print('*****************************')
			print('Transaction unsuccessful. You balance is insufficient. Please try a lower amount.')
			print('*****************************')
			print('-----------------------------')
		else:
			amounts[n] = amounts[n] - userWithdraw
			print('-----------------------------------')
			print('***********************************')
			print('Transaction successful. Your new balance is Ksh. ', amounts[n])
			print('***********************************')
			print('-----------------------------------')
			
	elif response == 'd':
		print()
		print('---------------------------------------------')
		print('*********************************************')
		userDeposit = int(input('How much would you like to deposit? '))
		print('*********************************************')
		print('---------------------------------------------')
		print()
		if userDeposit%100 != 0:
			print('----------------------------------------------------')
			print('****************************************************')
			print('Please enter an amount in multiples of Ksh. 100')
			print('****************************************************')
			print('----------------------------------------------------')
		else:
			amounts[n] = amounts[n] + userDeposit
			print('----------------------------------------')
			print('****************************************')
			print('Transaction successful. Your new balance is Ksh.', amounts[n])
			print('****************************************')
			print('----------------------------------------')
	elif response == 'p':
		print('-----------------------------')
		print('*****************************')
		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
		print('*****************************')
		print('-----------------------------')
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
			print('------------------')
			print('******************')
			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
			print('*******************')
			print('-------------------')
			if new_ppin != new_pin:
				print('------------')
				print('************')
				print('Error! Pins do not match!')
				print('************')
				print('------------')
			else:
				pins[n] = new_pin
				print('You have succesfully changed your pin!')
		else:
			print('-------------------------------------')
			print('*************************************')
			print('    Please enter a 4-digit pin. \nYou must not use an old pin!')
			print('*************************************')
			print('-------------------------------------')
	elif response == 'q':
		print("Thankyou for visiting TANGO Bank")
		break
	else:
			continue
