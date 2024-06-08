import key_fuction
import os

if __name__ == '__main__':
	bm = os.urandom(125000)
    IV = os.urandom(32)
    c = Encode(bm, IV)
	m = Decode(c, IV)
	if m == bm:
		print('Success!')
		print('m:',m)
		print('c:',c)
	else:
		print('Error!')
