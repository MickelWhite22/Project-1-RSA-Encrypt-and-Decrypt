import rsa

public_key, private_key = rsa.newkeys(1024)

with open("public.pem", "rb") as f:
   public_key = rsa.PublicKey.load_pkcs1(f.read())
    
with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
    
message = "My phone number is 9174456678"

encrypted_message = open("encrypted.message", "rb").read()

clear_message = rsa.decrypt(encrypted_message, private_key)
print(clear_message.decode())
