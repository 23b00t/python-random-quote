import random
def eris():
	usrin = input("To generate two random quotes press 1, to add quotes to the library press 2: ")
	try:
		numin = int(usrin)
	except ValueError:
		print("Invalid input")
  
	if numin == 1:  
		f = open("quotes.txt")
		quotes = f.readlines()
		f.close()

		count = 0
		while (count < 1):
			last = len(quotes) - 1
			rnd = random.randint(0, last)
			rndd = random.randint(0, last)
			if rndd != rnd: 
				print(quotes[rnd])
				print(quotes[rndd], end='')
				count = 1
			else: 
				count = 0

	elif numin == 2:
		count = 0
		while (count < 1):
			quotein = input("Please enter a quote to add: ")
			f = open("quotes.txt", "a", newline='\n')
			f.write(quotein)
			f.close()
			usrin1 = input("If you want to add more quotes press 1, to stop press 2: ")
			try:
				numin1 = int(usrin1)
			except ValueError:
				print("Invalid input")
			if numin1 == 1:
				count = 0
			else:
				count = 1
		
	else:
		print("Invalid input")
    
if __name__ == "__main__":
	eris()

