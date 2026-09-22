# PW Crack 3 (Medium)

## Challenge Description
"Can you crack the password to get the flag?

Download the password checker `here`
and you'll need the encrypted `flag`
and the `hash`

in the same directory too.

There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script."

The following is a code snippet from `level3.py`:
```python
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_3_pw_check()


# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]
``` 

## Approach

A brute-force approach was taken to solve this challenge since, this only had 7 possibilites, although the `subprocess` module of python could have been an alternate solution.

The list `pos_pw_list` was used for payload. 

## Terminal Output
```
python3 level3.py 
Please enter correct password for flag: 8799
That password is incorrect

python3 level3.py
Please enter correct password for flag: d3ab
That password is incorrect

python3 level3.py
Please enter correct password for flag: 1ea2
That password is incorrect

python3 level3.py
Please enter correct password for flag: acaf
That password is incorrect

python3 level3.py
Please enter correct password for flag: 2295
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_6f98a49f}

```

## Flag
`picoCTF{m45h_fl1ng1ng_6f98a49f}`