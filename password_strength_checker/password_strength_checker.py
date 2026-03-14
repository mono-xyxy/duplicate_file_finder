import re

print("Password strength checker")
password = input("Enter your password")

score =0

# check length
if len(password)>=8:
    score+=1

# check lowercase
if re.search(r"[a-z]",password):
    score+=1

# check uppercase
if re.search(r"[A-Z]",password):
    score+=1

# check digits
if re.search(r"[0-9]",password):
    score+=1

# check special characters
if re.search(r"[!@#$%^&*(),.?\]",password):
    score+=1

print("\n password strength result: ")

if score==5:
    print("Strong Password ✅")
elif score >= 3:
    print("Medium Password ⚠️")
else:
    print("Weak Password ❌")