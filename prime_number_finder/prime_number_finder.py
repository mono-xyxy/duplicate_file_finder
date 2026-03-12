num = int(input("Enter Number: "))

prime = True

for i in range(2,num):
    if num%i==0:
        prime = False
        break

print("Prime" if prime and num>1 else "Not Prime")