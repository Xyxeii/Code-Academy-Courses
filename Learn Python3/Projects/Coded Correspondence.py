import string
ascii = string.ascii_lowercase

def decode_message(msg, cipher):
	decoded_msg = []
	for i in msg:
		if i in ascii:
			if (ascii.index(i) + cipher) > len(ascii) - 1:
				decoded_msg.append(ascii[(ascii.index(i) + cipher) - len(ascii)])
			else:
				decoded_msg.append(ascii[ascii.index(i) + cipher])
		else:
			decoded_msg.append(i)
	return ''.join(decoded_msg)

def secret_message(msg, cipher):
	coded_msg  = []
	for i in msg:
		if i in ascii:
			if (ascii.index(i) - cipher) < 0:
				coded_msg.append(ascii[(len(ascii)) - (cipher - ascii.index(i))])
			else:
				coded_msg.append(ascii[ascii.index(i) - cipher])
		else:
			coded_msg.append(i)
	return ''.join(coded_msg)


def vCoder(msg, keyword):
	decoded_msg = []
	keycode = []
	#testlist = []
	#keycodeIndex = 0
	while len(keycode) < len(msg):
		for i in keyword:
			keycode.append(i)
	for l in range(len(msg)):
		if msg[l] in ascii:
			#cipher = ascii.index(msg[l]) + ascii.index(keycode[keycodeIndex])
			#testlist.append(keycode[keycodeIndex])
			cipher = ascii.index(msg[l]) + ascii.index(keycode[l])
			#print(ascii.index(msg[l]), ascii.index(keycode[l]), cipher)
			if cipher > len(ascii) - 1:
				#print(msg[l], ascii.index(msg[l]), keycode[l], ascii.index(keycode[l]), cipher, cipher - len(ascii))
				decoded_msg.append(ascii[(cipher - len(ascii))])
			else:
				decoded_msg.append(ascii[cipher])
		else:
			#keycodeIndex -= 1
			decoded_msg.append(msg[l])
		#keycodeIndex += 1
	return ''.join(decoded_msg)

def vDecoder(msg, keyword):
	decoded_msg = []
	keycode = []
	#testlist = []
	#keycodeIndex = 0
	while len(keycode) < len(msg):
		for i in keyword:
			keycode.append(i)
	for l in range(len(msg)):
		if msg[l] in ascii:
			#cipher = ascii.index(msg[l]) - ascii.index(keycode[keycodeIndex])
			#testlist.append(keycode[keycodeIndex])
			cipher = ascii.index(msg[l]) - ascii.index(keycode[l])
			#print(ascii.index(msg[l]), ascii.index(keycode[l]), cipher)
			if cipher < 0:
				#print(msg[l], ascii.index(msg[l]), keycode[l], ascii.index(keycode[l]), cipher, cipher - len(ascii))
				decoded_msg.append(ascii[len(ascii) + cipher])
			else:
				decoded_msg.append(ascii[cipher])
		else:
			#keycodeIndex -= 1
			decoded_msg.append(msg[l])
		#keycodeIndex += 1
	return ''.join(decoded_msg)

def bruteForce(msg):
	for i in range(len(ascii)):
		print(i, decode_message(msg, i))


message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
mymessage = "Huo Vyixqb! I cqdqwut je tusetu oekh cuiiqwu!"

message2 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
message3 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

no_shift_value = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

vcmessage = "dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!"

# bruteForce(no_shift_value)
# print(decode_message(no_shift_value, 7))

#print(decode_message(message3, 14))
# print(decode_message(mymessage, 10))
# print(secret_message('Hey Vishal! I managed to decode your message!', 10))
#print(ascii)
#print(vDecoder(vcmessage, 'friends'))
print(vCoder('These projects are too easy!', 'python'))
print(vDecoder('Tfxzs ephqspiq hfr rhv rpqr!', 'python'))