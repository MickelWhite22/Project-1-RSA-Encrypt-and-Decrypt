# Importing RSA library.
import rsa

# Specifying the length of the generated keys in bits.
public_key, private_key = rsa.newkeys(1024)

#Create separate files where the generated keys will be held.
# with open("public.pem", "wb") as f:
   # f.write(public_key.save_pkcs1("PEM"))
    
# with open("private.pem", "wb") as f:
   # f.write(private_key.save_pkcs1("PEM"))

# After the files are created to prevent the keys from regenerating, I delete the previous code and use the same algorithm so the keys will be in my script. 
with open("public.pem", "rb") as f:
   public_key = rsa.PublicKey.load_pkcs1(f.read())
    
with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# This is the message that will be encrypted and sent over the network   
message = "My phone number is 9174456678"

# Passing the message through the encryption algorithm and encode it into bits
encrypted_message = rsa.encrypt(message.encode(), public_key)

with open("encrypted.message", "wb") as f:
    f.write(encrypted_message)
