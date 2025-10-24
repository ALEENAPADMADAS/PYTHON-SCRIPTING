def caesar_cipher(text,num):
    encrypted=""
    for char in text :
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            encrypted +=chr((ord(char)-base+num)%26+base)
        else :
            encrypted+=char
    return encrypted

                 




message = input("Enter your message :")
shift=int(input("Enter the shift value : "))
print("Encrypted message is : ",caesar_cipher(message,shift))
