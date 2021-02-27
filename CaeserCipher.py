import sys
import time

# Please note that sometimes the print functions act as description to what is happening
# Define the operation - encryption or decryption
print("####################################################")
print("                                                    ")
print("Welcome to Alex's Caeser Cipher encoder and decoder!")
print("What operation are you tring to perform (e,d)?")
OP = input()
if OP == 'e':
	print("Let's encrypt your message! Please select a cipher shift between 1 and 25:")
	Key = input()
	K = int(Key)
	if K > 25 or K < 1:
		print("You entered an invalid cipher shift! Please run the program again.")
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
				new_num = (c_num + K) % 26

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
				new_num = (c_num + K) % 26

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
		print("Your cipher shift: ", K)
		time.sleep(3)
		sys.exit()
elif OP == 'd':
	print("Let's decrypt your ciphertext! Do you know the cipher shift (y,n)?")
	K_status = input()
	if K_status == 'y':
		print("Please enter your cipher shift between 1 and 25:")
		Key = input()
		K = int(Key)
		if K > 25 or K < 1:
			print("You entered an invalid cipher shift! Please run the program again.")
			time.sleep(3)
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
					new_num = (c_num - K) % 26

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
					new_num = (c_num - K) % 26

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
			print("Your cipher shift: ", K)
			time.sleep(3)
			exit()

	elif K_status == 'n':
		print("We will try all cipher shifts for you.") 
		print("Now please enter the ciphertext you wish to decrypt:")
		cipher = input()
		x = range(1,26)
		for K in x:

			#Define string that will be filled as we decrypt
			plain = ""
			for c in cipher:

				#Check if character is uppercase
				if c.isupper():

					#Convert to a number between 0 and 25
					c_ascii = ord(c)
					c_num = ord(c) - ord("A") #A would be the smallest so it is associated to 0.

					#Perform desired shift
					new_num = (c_num - K) % 26

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
					new_num = (c_num - K) % 26

					#Convert from number back to character
					new_ascii = new_num + ord("a")
					new_c = chr(new_ascii)

					#Add to plain string
					plain = plain + new_c

				else:

					#Add non-enlish alphabet character as it is
					plain = plain + c

			print("Possible plaintext with shift ", K, " :", plain)

	else:
		print("Wrong status selected, please restart the program and enter y or n in this section.")
		time.sleep(3)
		exit()

else:
	print ("Wrong operation selected, please restart the program and enter e or d.")
	time.sleep(3)
	exit()


