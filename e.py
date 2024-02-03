import os
import requests 
import telebot 
from telebot import types
import datetime

id = 5497242163

tok = '6406574208:AAFzkKOHtAsFauTmhG8tsJcMK4Y1cd-X3jA'
zzk=0
bot = telebot.TeleBot(tok)
@bot.message_handler(commands=['start'])
def start(message):
 global zzk
 zzk+=1
 nm = message.from_user.first_name
 id2 = message.from_user.id
 userk = message.from_user.username
 zxu = datetime.datetime.now()
 tt=f'''
عضو يستخدم البوت…
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
ـــــــــــــــــــــــــــــــــــــــ
ـ @P_W_7'''

 key = types.InlineKeyboardMarkup()
 bot.send_message(5000568348, f"<strong>{tt}</strong>",parse_mode="html",reply_markup=key)
 

 
 add = types.InlineKeyboardButton(text ="دریافت ایمیل جدید", callback_data = 'ansh')
 A= types.InlineKeyboardButton(text ="البـريد الـوارد ", callback_data = 'A')
 
 K= types.InlineKeyboardButton(text ="حذف حساب", callback_data = 'AK')
 

 fr = message.from_user.first_name
 maac = types.InlineKeyboardMarkup()
 maac.row_width=2
 maac.add(add,A,K)
 bot.send_message(message.chat.id,f"<strong>اهلا بك : | {fr} | في بـوت انشـاء بريد وهمي لاستقبال الاكواد والرسائل للحصول على معلوماتك [ /info ]</strong>",parse_mode="html",reply_markup=maac)
@bot.callback_query_handler(func=lambda call:True)
def st(call):
 
 
 if call.data== 'ansh':
            nc1 = types.InlineKeyboardMarkup(row_width=2)
            Az = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='ارسـل كـلمه انشاء',reply_markup=nc1)
            bot.register_next_step_handler(Az,zd2)
           
           
           
 elif call.data =="A":
	  nc1 = types.InlineKeyboardMarkup()
	  zd1 = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='ارسـل كلـمه اسـتلام',reply_markup=nc1)
	  bot.register_next_step_handler(zd1,OZ)


 elif call.data =="AK":

  nc1 = types.InlineKeyboardMarkup(row_width=2)
  MC = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='هل حـذف حسـابك القديم؟',reply_markup=nc1)
  bot.register_next_step_handler(MC,k3)

def zd2(message):
 id2 = str(message.from_user.id)
 ms =(message.text)
 if 'انشاء' in ms:
 	try:
	 	os.system(f'rm -rf token{id2}.txt')
	 	bot.send_message(message.chat.id, f"<strong>جـاري انـشاء ايـميل</strong>",parse_mode="html",reply_markup=types.InlineKeyboardMarkup())
	 	url = 'https://mob2.temp-mail.org/mailbox'
	 	he = {
	'Host': 'mob2.temp-mail.org',
	'accept': 'application/json',
	'accept-encoding': 'gzip',
	'user-agent': '3.33',
	'content-length': '0',
	}
	
	 	r = requests.post(url,headers=he).json()
	 	email=r['mailbox']
	 	token=r['token']
	 	try:
	 		with open(f'token{id2}.txt', 'a') as (zaidno):
	 			zaidno.write(f'{token}')
	 		z=f"""
	 تـم انشـاء بريـد بنـجاح
	 ـــــــــــــــــــــــــــــــــــــــ
	 الايميل : {email}
	ـــــــــــــــــــــــــــــــــــــــ
	يمكـن الان ارسال كود على البريد واستلامه من قسم الاستلام للرجوع
	/start""" 
	 
	 		bot.send_message(message.chat.id, f"<strong>{z}</strong>",parse_mode="html",reply_markup=types.InlineKeyboardMarkup())
	 	except:pass
 	except:
 		key = types.InlineKeyboardMarkup()
 		bot.send_message(message.chat.id, f"<strong> ❗لقد حدث خطأ ماا</strong>",parse_mode="html",reply_markup=key)
 else:
  key = types.InlineKeyboardMarkup()
  bot.send_message(message.chat.id, f"<strong> ❗ارسـلت الكـلمه بشـكل خـطأ</strong>",parse_mode="html",reply_markup=key)
	 
	 
def OZ(message):
    try:
	    za=0
	    id2=message.chat.id
	    tx =(message.text)
	    if 'استلام'in tx:
	    	try:
		    	token = open(f"token{id2}.txt","r").read()
		    	url2='https://mob2.temp-mail.org/messages'#@P_W_7
		    	he2 = {
	'Host': 'mob2.temp-mail.org',
	'accept': 'application/json',
	'accept-encoding': 'gzip',
	'content-length': '0',
	'user-agent': '3.33',
	'authorization': token, #توكن الايميل المنشئ
	'if-modified-since': 'Thu, 25 Jan 2024 11:47:16 GMT',
	}
		    	r2 = requests.get(url2,headers=he2).json()
		    	bot.send_message(message.chat.id, f"<strong>{r2}</strong>",parse_mode="html",reply_markup=types.InlineKeyboardMarkup())
	
	    	except:pass
    except:
    	bot.send_message(message.chat.id, f"<strong>❗ليـس لـديك حسـاب بالـبوت</strong>",parse_mode="html",reply_markup=types.InlineKeyboardMarkup())


		 						 				
def k3(message):
 mg=message.chat.id
 try:
 	os.system(f'rm -rf token{mg}.txt')
 	key = types.InlineKeyboardMarkup()
 	bot.send_message(message.chat.id, f"<strong>تـم حـذف حسـابك القـديم</strong>",parse_mode="html",reply_markup=key)
 except:
 	key = types.InlineKeyboardMarkup()
 	bot.send_message(message.chat.id, f"<strong>ليس لديك حساب اساساً</strong>",parse_mode="html",reply_markup=key)	
	
@bot.message_handler(commands=["info"])
def inf(message):
    global zzk
    zzk+=1
    zxu = datetime.datetime.now()
    nm = message.from_user.first_name
    id2 = message.from_user.id
    userk = message.from_user.username
    bio = bot.get_chat(message.from_user.id).bio
    
    ttg=f'''
رتبتك هي عضو 🥰 
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
بايو المستخدم : {bio}
ـــــــــــــــــــــــــــــــــــــــ
ـ @P_W_7'''
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"<strong>{ttg}</strong>",parse_mode="html",reply_markup=key) 	


while True:
	try:
		bot.infinity_polling()
	except:
		pass
