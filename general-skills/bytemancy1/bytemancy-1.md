# Bytemancy 1

## Challenge Description
An app.py source code was provided with the following code.
```python
while(True):
  try:
    print('⊹──────[ BYTEMANCY-1 ]──────⊹')
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print()
    print('Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.')
    print()
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print('⊹─────────────⟡─────────────⊹')
    user_input = input('==> ')
    if user_input == "\x65"*1751:
      print(open("./flag.txt", "r").read())
      break
    else:
      print("That wasn't it. I got: " + str(user_input))
      print()
      print()
      print()
  except Exception as e:
    print(e)
    break
```
The challenge was to provide ASCII decimal of 101 1751 times to the input function.
Decimal 101 = hex 0x65 (`hex`) = ASCII(`'e'`).
It was expected to be done, using python and not tirelessly copy pasting "\x65" 1751 times.

## Approach
Initial approach was to type python command like `python3 -c "print('\x65' * 1751)"`.
But `input()` reads raw keystrokes as literal text from the start.
So a different approach was taken writing a `flag.py` script, also attached in this folder.

```python
# flag.py
from pwn import *

# for a remote instance
io = remote('foggy-cliff.picoctf.net', 61974)

io.sendline(b'\x65' * 1751)
print(io.recvall().decode())
```

Line by line break-down of `flag.py`:
This uses CTF framework pwntools. [Reference: pwntools docs]("https://docs.pwntools.com/en/latest")
```python
from pwn import *
```
This imports everything from pwntools library (functions, classes like remote, process, context).

```python
io = remote('foggy-cliff.picoctf.net', 61974)
```
Here, the syntax for `remote()` is `remote("host", port)`.
This opens a TCP connection to a remote host and port, it returns a connection object (`io`), which can be used to send or recieve data, similar to a socket but with methods built in (timeouts, buffering, logging, etc.)

```python
io.sendline(b'\x65' * 1751)
```
This is the key action:
`b'\x65'` is a python bytes literal representing a single raw byte with hex value `0x65`.
It is multiplied like this `* 1751`, which repeats that byte 1751 times, producing a byte object of length 1751, all identical `0x65`.
`io.sendline(...)` sends that data to the connection and appends a newline (`\n`).
This would mimic what would happen if you type `0x65` 1751 times and pressed Enter, since `input()` reads until newline.

```python
print(io.recvall().decode())
```
`io.recvall()` reads all available data from the connection until it closes, this is where it captures the flag.
`decode()` converts the raw bytes response in human-readable Python `str`, assuming the challenge kept it compatible.
`print(...)` displays the decoded output in the terminal.

## Terminal Output
```
$ python3 flag.py 
[+] Opening connection to foggy-cliff.picoctf.net on port 61974: Done
[+] Receiving all data: Done (424B)
[*] Closed connection to foggy-cliff.picoctf.net port 61974
⊹──────[ BYTEMANCY-1 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==> picoCTF{h0w_m4ny_e's???_7dbc095c}
```

### Flag
`picoCTF{h0w_m4ny_e's???_7dbc095c}`