a = input("Enter a sentence: ")

words = a.split()

freqs = {}

for word in words:
	if word in freqs:
		freqs[word] += 1
	else:
		freqs[word] = 1

for word, counter in freqs.items():
	print(f"I found the word {word}: {counter} times")




grades = {"Anna": 18,
	"Stelio": 15,
	"Kosta": 20,
	"Gianni": 20}
students={15:["Stelio"],
	18:["Anna"],
	20:["Kosta", "Gianni"]}

