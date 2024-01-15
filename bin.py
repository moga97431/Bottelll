import os , sys
os.system("pip install requests")
os.system("pip install random")
os.system("clear")
import random , requests
ahmd="1234567980"
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
id = ("")

tok = ("")

while True:
	bin1 = "3"+str("". join(random.choice(ahmd)for i in range(5)))
	bin2="4"+str("". join(random.choice(ahmd)for i in range(5)))
	bin3="5"+str("". join(random.choice(ahmd)for i in range(5)))
	all=[bin1, bin2, bin3]
	bin=random.choice(all)
	url= f"https://lookup.binlist.net/"+bin
	k=requests.get(url)
	if "country"in k.text:
			name = k.json()["country"]["name"]
			emoji = k.json()["country"]["emoji"]
			scheme = k.json()["scheme"]
			country = k.json()["country"]["currency"]
			emoji = k.json()["country"]["emoji"]
			txt_L=f""" 
☆ʜɪ ʟ ɴᴇᴡ ʙɪɴ 💙  
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉┉ ┉ ┉  
◇𝙱𝙸𝙽🎟 : {bin}  
Country🚬: {name} {emoji}  
NeTwOrK🗿 : {scheme}  
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉┉ ┉ ┉  
⌯ 𝐃𝐄𝐕: @id_MoDeM"""
			print(F+txt_L)
			tele = f"""https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={txt_L}"""
			requests.get(tele)
	else:
		print(Z+f"Bad Bin ⇨ {bin}")
