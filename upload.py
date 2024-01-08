from pyrubi import Client
import os
import requests
from datetime import datetime
import datetime



bot = Client(session="amir")
guid_admin = "u0E5Kwm05bf24b106b3006ea425b1f65"


while True:
	try:
		for ms in bot.on_message():
			text = ms.text
			guid = ms.object_guid
			msg_id = ms.message_id
			print(text)
			
			
			if text =='/start' and guid == guid_admin:
				bot.send_text(guid,""" بــه ربــات اپــلودر و دانــلودر خــوش آمــدید🤖
لــطفا /help را ارســال کنید""",msg_id)
				
			elif text.startswith("-")and guid == guid_admin:
				name = text[1 : ].strip()
				bot.send(guid,"ok")
				bot.send_text(guid,"لــینک پــستی کــہ میــخاهیــد دانــلود یا اپلــود شــود ارســال کنید")
			elif text.startswith('post: ')and guid == guid_admin:
				link_dan = text[6 : ].strip()
				print(link_dan)
				info_link = bot.get_link_from_app_url(link_dan)
				bot.send_text(guid,'لــینک پســت با موفقیــت دریافــت شــد😚',msg_id)
				bot.send_text(guid,"لــینک چــنلــی کــہ مــیخاهیــد اپ شــود ارســال کــنیــد.")
					
			elif text.startswith("link: ")and guid == guid_admin:
				id = text[6 : ].strip()
				guid_ch = bot.join_chat(id)['channel']['channel_guid']
				bot.send_text(guid,'گــوید چنل دریــافت شــد  لــطفا مطمعن بــاشید که اوت در کــانــال ادمیــن باشــد😟😯')
				bot.send_text(guid,'''برای اپلود کردن  file یا video را ارسال کنید ''')
			elif text =="file"and guid == guid_admin:
				bot.send_text(guid,"آپــلود شــروع شــد😚 ")
				dan = bot.download(info_link['link']['open_chat_data']['object_guid'],info_link['link']['open_chat_data']['message_id'],save=True)
				
				bot.send_file(guid_ch,f'{name}')
				bot.send_text(guid,"بــا مــوفقیــت آپــلود شــد😚 ")
				os.remove(name)
				
				
			elif text =="video"and guid == guid_admin:
				bot.send_text(guid,"آپــلود شــروع شــد😚 ")
				dan = bot.download(info_link['link']['open_chat_data']['object_guid'],info_link['link']['open_chat_data']['message_id'],save=True)
				bot.send_video(guid_ch,f'{name}')
				bot.send_text(guid,"بــا مــوفقیــت آپــلود شــد😚 ")
				os.remove(name)
				
			#
	except:continue
