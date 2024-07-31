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
    

Step 2: Loading Keys

- After creating the files and generating the keys you need to access the codes by reading the files contents

   ```bash
  with open("public.pem", "rb") as f:
   public_key = rsa.PublicKey.load_pkcs1(f.read())
    
  with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
   ```

  Step 3: Encrypting a message

  - Decide on a phrase you'd like to encrypt

  - Your chosen phrase is encoded into bytes using 'message.encode()'
 
  - Your chosen phrase is encrypted by the generated public key with 'rsa.encrypt()'
 
    

   
  
