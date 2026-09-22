# PW Crack 1 (Easy)

## Challenge Description
"Can you crack the password to get the flag?

Download the password checker `here`
and you'll need the encrypted `flag`
in the same directory too."

## Approach
Upon viewing the password checker `.py` file: `level1.py`.
```python
# level1.py
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################


flag_enc = open('level1.flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "691d"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()
```

The password is given on the if condition, below the user input: `if( user_pw == "691d"):`

## Terminal Commands
```
python3 level1.py
Please enter correct password for flag: 691d
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_56891419}
```

## Flag
`picoCTF{545h_r1ng1ng_56891419}`