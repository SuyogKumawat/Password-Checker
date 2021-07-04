import requests
import hashlib
import sys 

def request_api_data(query_character):
	url='https://api.pwnedpasswords.com/range/' + query_character
	res=requests.get(url)
	# print(res)
	if res.status_code !=200:
		raise RuntimeError(f'Error Fetching:{res.status_code},check the api and try again')
	return res

# def read_res(response):              #read api response in text form
# 	print(response.text)
def get_password_leaks_counts(hashes,hash_to_check):     #now we will match a tail that matches the given password and the we know the count
	hashes=(line.split(":") for line in hashes.text.splitlines())
	for h, count in hashes:
		if h==hash_to_check:
			return count
	return 0
		# print(h, count)

def pwned_api_check(password):
	sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char,tail=sha1password[:5],sha1password[5:]
	response=request_api_data(first5_char)
	# print(response)
	# return read_res(response)           #now we will send to the api and see what response we get
	return get_password_leaks_counts(response,tail)

# pwned_api_check('123')      #output shown how many time each passwords hacked now we will match a tail
 # that matches the given password and the we know the count

def main(args):
 	for password in args:
 		count=pwned_api_check(password)
 		if count:
 			print(f'                                Your Password:{password} was found and breached {count} times...\n                                You should probably change your password')
 		else:
 			print(f'                                Your Password:{password} was not found \n                                Strong Password!!! You can set this Password')
 	return 'done!'
 	
if __name__=="__main__":
	main(sys.argv[1:])
	##OR
	# sys.exit(main(sys.argv[1:]))