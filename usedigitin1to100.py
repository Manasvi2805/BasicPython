#write a code to input number from user and check & print how many time that digit use in 1 to 100.

num = input("Enter a number : ")
count = 0

for i in range(1, 101):
    if num in str(i):
        count += 1
        print(i)
print("-"*40)
print("The digit",num, "is used", count, "times between 1 and 100.")
