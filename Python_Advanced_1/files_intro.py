with open('pi_digits.txt') as file:
    lines = file.readlines()

pi = ""
for i in lines:
    pi = pi + i.strip()

bday = input("Give your bday in the format mmddyy: ")
if bday in pi:
    print("Your birthday is in the first one million pi digits!")
else:
    print("Your birthdate is not in the pi digits!")