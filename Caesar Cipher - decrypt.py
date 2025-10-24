def caeser_encrypt(message,shift) :
 encrypted=""
 for char in message :
  if char.isalpha():
    base=ord('A') if char.isupper() else ord('a')
    encrypted+=chr((ord(char)-base+shift)%26+base)
  else :
    encrypted+=char;  
 
 return encrypted        

def caeser_decrypt(encrypted,shift) :
 decrypted=""
 for char in encrypted :
  if char.isalpha():
    base=ord('A') if char.isupper() else ord('a')
    decrypted+=chr((ord(char)-base-shift)%26+base)
  else:
   decrypted+=char  
 return decrypted 

message = input("Enter your message : ")
shift =  int(input("Enter the shift value: "))
encrypted = caeser_encrypt(message,shift)
print("Encrypted message : ",caeser_encrypt(message,shift))
print("Decrypted message : ",caeser_decrypt(encrypted,shift))



