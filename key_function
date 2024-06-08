import os
from hashlib import sha256

def bytes_split(obj:bytes,sec:int = 32):
	return[obj[i:i+sec] for i in range(0,len(obj),sec)]
		
def SHA256(s:bytes):
	obj = sha256()
	obj.update(s)
	return obj.digest()
		
def bxor(b1, b2): # use xor for bytes
	result = b""
	for b1, b2 in zip(b1, b2):
		result += bytes([b1 ^ b2])
	return result
		
def bytes_comb(obj:list):
	b = b''
	for i in obj:
	b += i
	return b
		
IV = os.urandom(32)
		
def Encode(bm:bytes,IV:bytes):
	mlist = bytes_split(bm)
	group_num = len(mlist)
	clist = []
	for i in mlist:
		key = SHA256(IV)
		c = bxor(i,key)
		clist.append(c)
		IV = SHA256(c)
	return bytes_comb(clist)
		
def Decode(c:bytes,IV:bytes):
	clist = bytes_split(c)
	mlist = []
	for i in clist:
		key = SHA256(IV)
		m = bxor(i,key)
		mlist.append(m)
		IV = SHA256(i)
	return bytes_comb(mlist)
