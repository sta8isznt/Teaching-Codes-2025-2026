names = []
for i in range(5):
    name = input("Enter a name: ")
    age = int(input("Enter the age: "))
    if age > 10:
        names.append(name)

for i in names:
    print(f"Hello {i}")