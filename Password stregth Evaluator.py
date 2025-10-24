#Mini Project: Build Your Own Password Strength Evaluator
#Requirements:
#• 	Ask the user for a password
#• 	Check for:
#• 	Length ≥ 8
#• 	Mix of letters and numbers
#• 	Presence of special characters ()
#• 	Print feedback: Weak, Medium, Strong

#Wrong if len(password)<8:
#    print("Weak")
#elif password.isalnum():
#    print("Medium")
#else :    
#   any(char in "!@#$%^&*" for char in password)
#   print("Strong")%

password = input("Enter your password: ")

has_special=any(char in "!@#$%^&*" for char in password)
has_number=any(char.isdigit() for char in password)
has_letters=any(char.isalpha() for char in password)

if len(password)<8:
    print("Weak:too short!!")
elif has_special and has_number and has_letters:
    print("Strong!!")
elif has_number and has_letters:
    print("Medium")
else:
    print("Weak:Only letters or numbers or special characters,add all 3 types")
