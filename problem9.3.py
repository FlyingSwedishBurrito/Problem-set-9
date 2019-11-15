def encrypt(text,k): 
    result = "" 

    for i in range(len(text)): 
        c = text[i] 
  
        if (c.isupper()): 
            result += chr((ord(c) + k -65) % 26 + 65) 
  
        else: 
            result += chr((ord(c) + k - 97) % 26 + 97) 
  
    return result 


  
text = input("Enter message that you want to be encrypted: ")
k = int(input("Enter the cypher shift (key): "))

k = k % 26 #makes cypher work with any integer value

print ("Plain Text: " + text)

text = encrypt(text,k)
print ("Cipher: " + text)

text = encrypt(text,-k)
print ("De-excryption: " + text)