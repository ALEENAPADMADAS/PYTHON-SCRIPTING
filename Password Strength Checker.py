password = input("Enter your password : ")
if len(password)<8:
 print("Weak Password:Too Short")
elif password.isnumeric():
 print("Weak Password:Only Numbers")
elif password.isalpha():
 print("Weak Password:Only Letters")
else:
 print("Strong Password!") 

