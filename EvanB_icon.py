print("\nHello and welcome. You may use this program to display your icon.\n\nYou will be prompted to enter ten lines of TEN ones and zeros. \n")
row_name_list = ["one", "two" , "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
icon_row_list = []

def create_icon():
	# loop through all ten rows
	for row in row_name_list:
		# get input for each row
		row_input = input("Please enter ten characters (zeros and ones only, please!) for row " + row + ": ")
		# test to see if each row is 10 characters long
		if len(row_input) == 10:
			row_input_list=list(row_input)
			# test to see if each character is a 1 or a 0
			for inp in row_input_list:
				if (inp != "0") and (inp != "1"):
					print("You failed to enter ONLY ten ones and zeros. Please try again.")
					# restart the program if the test fails
					create_icon()
			icon_row_list.append(row_input)
		else:
			print("You failed to enter ten ones and zeros. Please try again.")
			# if the length test fails, restart the program
			create_icon()
	return icon_row_list
	
def display_icon():
	# print the icon
	for row in icon_row_list:
		print(row)

def scale_icon():
	# see if the user would like to scale the icon
	scaled_rows = input("Would you like to scale your icon? (yes/no) ")
	if scaled_rows.lower() == "yes":
		scaling_int=int(input("Choose an integer by which to scale? "))
		for row in icon_row_list:
			scaled_list = []
			combined_list = []
			row_list=list(row)
			# print(row_list)
			for char in row_list:
				num_row = char[:]*scaling_int
				scaled_list.append(num_row)
			print(*scaled_list, sep="")
			print(*scaled_list, sep="")
			print(*scaled_list, sep="")
			print(*scaled_list, sep="")
			print(*scaled_list, sep="")
	elif scaled_rows.lower() == "no":
		print("Keep it simple, then.")


def invert_icon():
	invert_rows = input("Would you like to invert the icon? (y/n) ")
	if invert_rows.lower() == "yes":
		for row in icon_row_list:
			print(row[::-1])
	elif invert_rows.lower() == "no":
		print("Keep it simple, then.")
	else:
		invert_icon()




create_icon()
display_icon()
scale_icon()
invert_icon()
	


