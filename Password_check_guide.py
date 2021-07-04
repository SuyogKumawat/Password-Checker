"""Complete Guide of Password checker"""

import requests
import hashlib     #built in python module 

# url='https://api.pwnedpasswords.com/range/' +'password123'
# url='https://api.pwnedpasswords.com/range/' +'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'       #HAshed version of password123

# url='https://api.pwnedpasswords.com/range/' +'CBFDA'               #using the k anonymity technique:
#' it allows that somebody to receive information about us yet still dont know who we are '   
# so we used above first 5 character of hashed version
# res=requests.get(url)
# print(res)

def request_api_data(query_character):
	url='https://api.pwnedpasswords.com/range/' +'query_character'
	res=requests.get(url)
	print(res)
	if res.status_code !=200:
		raise RuntimeError(f'Error Fetching:{res.status_code},check the api and try again')
	return res


def pwned_api_check(password):
	#check password if ir exists in API response
	# print(password.encode('utf-8'))                #outputs b'123'
	# print(hashlib.sha1(password.encode('utf-8')))     # it outputs <sha1 HASH object @ 0x0000022CA23C9AA8>
	# print(hashlib.sha1(password.encode('utf-8')).hexdigest())        #returned as a string object of double length  
	# 40bd001563085fc35165329ea1ff5c5ecbdbbeef
	# print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())      #Uppercase
	# When we not use  encode utf-8
	# print(hashlib.sha1(password).hexdigest().upper())        #TypeError: Unicode-objects must be encoded before hashing
	sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	return sha1password            #now we will send to the api and see what response we get
pwned_api_check('123')