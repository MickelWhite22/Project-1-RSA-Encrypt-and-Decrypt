#Asymmetric encryption using RSA

Goal: Create a simple RSA asymmetric encryption using python

# RSA Encryption 

This project demonstrates the use of RSA keys to encrypt a message using Python. The `rsa` library is used to handle the RSA encryption and decryption process.

## Prerequisites

- Python 3.x
- `rsa` library

You can install the `rsa` library using pip:

```bash 
pip install rsa
```

## Files
- 'public.pem and private.pem': Scripts to generate and save accessible RSA keys.

- 'encrypt_message.py': Script to load RSA keys and encrypt the message. 

## Explanation

Step 1: Generate and Save RSA Keys

- Import the RA library

- Using the 'rsa.newkeys(1024)' function I can generate the keys according to the desired bit length

- Create and name the files you will use to store the keys. In this case I simply named them 'public.pem' and 'private .pem'

- Here I defined my standards by using Public Key Format One and Privacy-Enhanced Mail.

  ```bash
  import rsa

  public_key, private_key = rsa.newkeys(1024)

  with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))
    
  with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM")) ```
    

Step 2: Loading keys

- After creating the files and generating the keys you need to access the codes by reading the files contents

   ```bash
  with open("public.pem", "rb") as f:
   public_key = rsa.PublicKey.load_pkcs1(f.read())
    
  with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
   ```

Step 3: Encrypting a message

- Decide on a phrase you'd like to encrypt and put it under the variable message

- Your chosen phrase is encoded into bytes using 'message.encode()'
 
- Your chosen phrase is encrypted by the generated public key with 'rsa.encrypt()'


   ```bash
 
  message = "My phone number is 9174456678"

   encrypted_message = rsa.encrypt(message.encode(), public_key)

  ```

Step 4: Save newly encrypted message

- Create a file to save the encrypted message. In this case, i used 'encrypted.message'.

  ```bash

  with open("encrypted.message", "wb") as f:
    f.write(encrypted_message)
   ```
# RSA Decryption
Now we are going to use the generated private key to decrypt the public key encrypted phrase chosen earlier.

## Explanation

Step 1: Reading the encrypted message 

- Before decrypting the message, you need to open the 'encrypted.message' file in read-binary mode. You can do this by storing it under the 'encrypted_message' variable to prevent excessive lines of code. Remember that this file contains your phrase in encrypted form using the public key.

   ```bash
  encrypted_message = open("encrypted.message", "rb").read()
   ```
- Create a new variable called 'clear_message' and use the 'rsa.decrypt()' function to decrypt the 'encrypted message' using the 'private_key'.

 ```bash
  clear_message = rsa.decrypt(encrypted_message, private_key)
  ```
- If you print 'clear_message' without decoding it, you will get the message returned in bytes. Use the '.decode()' function to convert it to a string.

 ```bash
  print(clear_message.decode())
  ```

## Summary

- Key loading: The code searches for previously saved RSA asymmetric encryption keys from files.

- Reading Encrypted Data: The code reads an encrypted message from the public key files.

- Decrypting Data: The encrypted message is decrypted using the private key.

- Results: The decrypted message is converted from bytes to a string and displayed in the console.
