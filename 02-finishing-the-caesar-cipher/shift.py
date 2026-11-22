ALPHABET_SIZE = 26

message: str = input("Message: ")   #AB$78
key:int = int(input("Key:"))

ciphertext =" "

#Encryption loop
for character in message:
    if "A" <= character <= "Z":
       shifted = ord(character) + key
       if shifted > ord("Z"):
           shifted -= ALPHABET_SIZE
       ciphertext += chr(shifted)
    else:
       ciphertext += character

print ("Ciphertext:" , ciphertext)

plaintext =" "

#Decryption loop
for character in ciphertext:
    if "A" <=character <= "Z":
        shifted:int = ord(character) - key
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)
    else:
        plaintext +=character


print("Plaintext:", plaintext)

#check if the message equal to plain text

#assert message == plaintext, "The encryption-decryption loop doesn't close"

