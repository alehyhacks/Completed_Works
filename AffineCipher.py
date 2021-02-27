import time
import math
import array

# Please note that sometimes the print functions act as description to what is happening
# Define the operation - encryption or decryption
print("####################################################")
print("                                                    ")
print("Welcome to Alex's Affine Cipher encoder and decoder!")
print("What operation are you tring to perform (e,d)?")
OP = input()

# Putting all possible a values into a list
a_list = [1,3,5,7,9,11,15,17,19,21,23,25]
if OP == 'e':
	print("Let's encrypt your message! Your key is of the form (a,b).")
	print("Please select a to be one of the following: 1,3,5,7,9,11,15,17,19,21,23,25")
	a_input = input()
	a = int(a_input)
	if a not in a_list:
		print("You entered an invalid a! Please run the program again.")
		time.sleep(5)
		exit()
	else:
		print("Please select b to be between 0 and 25 inclusive:")
		b_input = input()
		b = int(b_input)
		if b < 0 or b > 25:
			print("You entered an invalid b! Please run the program again.")
			time.sleep(5)
			exit()
		else:
			#Define string that will be filled as we encrypt
			cipher = "" 
			print("Now please enter your message. Note that only english alphabet characters will get encoded:")
			plain = input()
			for c in plain:

				#Check if character is uppercase
				if c.isupper():

					#Convert to a number between 0 and 25
					c_ascii = ord(c)
					c_num = ord(c) - ord("A") #A would be the smallest so it is associated to 0.

					#Perform desired shift
					new_num = (c_num*a + b) % 26

					#Convert from number back to character
					new_ascii = new_num + ord("A")
					new_c = chr(new_ascii)

					#Add to cipher string
					cipher = cipher + new_c

				#Check if character is lowercase
				elif c.islower():

					#Convert to a number between 0 and 25
					c_ascii = ord(c)
					c_num = ord(c) - ord("a") #a would be the smallest so it is associated to 0.

					#Perform desired shift
					new_num = (c_num*a + b) % 26

					#Convert from number back to character
					new_ascii = new_num + ord("a")
					new_c = chr(new_ascii)

					#Add to cipher string
					cipher = cipher + new_c

				else:

					#Add non-enlish alphabet character as it is
					cipher = cipher + c


			print("Your plaintext: ", plain)
			print("Your ciphertext: ", cipher)
			print("Your cipher Keypair: (", a, ",", b, ")")
			time.sleep(3)
			exit()
elif OP == 'd':
	print("Let's decrypt your ciphertext! Your key is of the form (a,b).")
	print("Do you know a? (y,n)")
	a_status = input()
	if a_status == 'y':
		print("Please enter a:")
		a_input = input()
		a = int(a_input)
		if a not in a_list:
			print("You entered an invalid a! Please run the program again.")
			time.sleep(5)
			exit()
		else:
			#Find Modular Multiplicative Inverse of a by guessing
			for x in range(1, 26):
				if ((x * a) % 26 == 1):
					a_inverse = x

			print("Do you know b? (y,n)")
			b_status = input()
			if b_status == 'y':
				print("Please enter b:")
				b_input = input()
				b = int(b_input)
				if b < 0 or b > 25:
					print("You entered an invalid b! Please run the program again.")
					time.sleep(5)
					exit()
				else:

					#Define string that will be filled as we decrypt
					plain = "" 
					print("Now please enter the ciphertext you wish to decrypt:")
					cipher = input()
					for c in cipher:

						#Check if character is uppercase
						if c.isupper():

							#Convert to a number between 0 and 25
							c_ascii = ord(c)
							c_num = ord(c) - ord("A") #A would be the smallest so it is associated to 0.

							#Perform desired shift
							new_num = a_inverse*(c_num - b) % 26

							#Convert from number back to character
							new_ascii = new_num + ord("A")
							new_c = chr(new_ascii)

							#Add to plain string
							plain = plain + new_c

						#Check if character is lowercase
						elif c.islower():

							#Convert to a number between 0 and 25
							c_ascii = ord(c)
							c_num = ord(c) - ord("a") #a would be the smallest so it is associated to 0.

							#Perform desired shift
							new_num = a_inverse*(c_num - b) % 26

							#Convert from number back to character
							new_ascii = new_num + ord("a")
							new_c = chr(new_ascii)

							#Add to plain string
							plain = plain + new_c

						else:

							#Add non-enlish alphabet character as it is
							plain = plain + c

					print("Your ciphertext: ", cipher)
					print("Your plaintext: ", plain)
					print("Your cipher Keypair: (", a, ",", b, ")")
					time.sleep(3)
					exit()

			if b_status == 'n':
				print("We will try every possible b for you!")
				print("Now please enter the ciphertext you wish to decrypt:")
				cipher = input()
				#Define string that will be filled as we decrypt
				y = range(0,26)
				for b in y:
					plain = "" 
					for c in cipher:

						#Check if character is uppercase
						if c.isupper():

							#Convert to a number between 0 and 25
							c_ascii = ord(c)
							c_num = ord(c) - ord("A") #A would be the smallest so it is associated to 0.

							#Perform desired shift
							new_num = a_inverse*(c_num - b) % 26

							#Convert from number back to character
							new_ascii = new_num + ord("A")
							new_c = chr(new_ascii)

							#Add to plain string
							plain = plain + new_c

						#Check if character is lowercase
						elif c.islower():

							#Convert to a number between 0 and 25
							c_ascii = ord(c)
							c_num = ord(c) - ord("a") #a would be the smallest so it is associated to 0.

							#Perform desired shift
							new_num = a_inverse*(c_num - b) % 26

							#Convert from number back to character
							new_ascii = new_num + ord("a")
							new_c = chr(new_ascii)

							#Add to plain string
							plain = plain + new_c

						else:

							#Add non-enlish alphabet character as it is
							plain = plain + c

					print("Your possible plaintext with b = ",b, " :", plain)

			else:
				print("Wrong status selected, please restart the program and enter y or n in this section.")
				time.sleep(3)
				exit()

	elif a_status == 'n':
		print("We will try all a and b values for you.") 
		print("Now please enter the ciphertext you wish to decrypt:")
		cipher = input()
		for a in a_list:
			#Find Modular Multiplicative Inverse of a by guessing
			for x in range(1, 26):
				if ((x * a) % 26 == 1):
					a_inverse = x

			print("*********SECTION WITH a = ",a, " :")
			print(" ") #empty line
			y = range(0,26)
			for b in y:
				plain = "" 
				for c in cipher:

					#Check if character is uppercase
					if c.isupper():

						#Convert to a number between 0 and 25
						c_ascii = ord(c)
						c_num = ord(c) - ord("A") #A would be the smallest so it is associated to 0.

						#Perform desired shift
						new_num = a_inverse*(c_num - b) % 26

						#Convert from number back to character
						new_ascii = new_num + ord("A")
						new_c = chr(new_ascii)

						#Add to plain string
						plain = plain + new_c

					#Check if character is lowercase
					elif c.islower():

						#Convert to a number between 0 and 25
						c_ascii = ord(c)
						c_num = ord(c) - ord("a") #a would be the smallest so it is associated to 0.

						#Perform desired shift
						new_num = a_inverse*(c_num - b) % 26

						#Convert from number back to character
						new_ascii = new_num + ord("a")
						new_c = chr(new_ascii)

						#Add to plain string
						plain = plain + new_c

					else:

						#Add non-enlish alphabet character as it is
						plain = plain + c

				print("Your possible plaintext with b = ",b, " :", plain)
			print(" ") #empty line

	else:
		print("Wrong status selected, please restart the program and enter y or n in this section.")
		time.sleep(3)
		exit()

else:
	print ("Wrong operation selected, please restart the program and enter e or d.")
	time.sleep(3)
	exit()
