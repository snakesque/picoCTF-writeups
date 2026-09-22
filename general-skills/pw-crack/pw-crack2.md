# PW Crack 2 (Easy)

## CHallenge
Same like, pw1, provided with two files, `level2.py` and `level2.flag.txt.enc`.
The challenge is to crack the password.

## Approach
The following python snippet was all that's needed to solve this challenge.
```python
def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```

Noticing the `chr(hex-numbers)` syntax tells us that it's a convertion of hex to ASCII.
Converting the if condition gives the following password: `4ec9`.

## Terminal Commands
```
python3 level2.py
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_9701e681}
```

## Flag
`picoCTF{tr45h_51ng1ng_9701e681}`