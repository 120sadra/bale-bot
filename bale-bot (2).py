from bale import Bot, CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton, MenuKeyboardMarkup, MenuKeyboardButton
#ایمپورت کردن و قابلیت هاش  python-bale-bot
client = Bot(token="yor token")
#توکن بات رو وارد میکنیم

@client.event
# ایونت رو فرا میخونیم تا بتونیم تابع بسازیم 
async def on_ready():
	print(client.user, "bot ready !")
#تابع on-ready برای نمایش فعال بودن بات در کنسول و اطلاعات بات در کنسول نمایش میدهد
@client.event
async def on_message(message: Message):
#تابع مسیج برای وارد کردن مقدار های پیامی و کیبورد سازی
	if message.content.lower() == "/start":
#شزط برای ورود ستارت چه کاری را انجام دهد
		reply_markup = InlineKeyboardMarkup()
#کیبورد مارکاپبرای ساخت کیبورد در متغیر میریزیم 
		reply_markup.add(InlineKeyboardButton(text="نرم 1", url="your lurl"))
		reply_markup.add(InlineKeyboardButton(text="فصل اول", url="your lurl"),row=2)
#اضافه کردن دکمه به منو و متن دادن بهش بجی آدرس یو آر ال میتوان call back data اضافه کرد
		reply_markup.add(InlineKeyboardButton(text="فصل دوم", url="your lurl"),row=2)
#row هم میشه ردیف
		reply_markup.add(InlineKeyboardButton(text="فصل سوم", url="your lurl"),row=3)
		reply_markup.add(InlineKeyboardButton(text="فصل چهارم", url="your lurl"),row=3)
		reply_markup.add(InlineKeyboardButton(text="فصل پنجم", url="your lurl"),row=4)
		reply_markup.add(InlineKeyboardButton(text="فصل ششم", url="your lurl"),row=4)
		reply_markup.add(InlineKeyboardButton(text="فصل هفتم", url="your lurl"),row=5)
		reply_markup.add(InlineKeyboardButton(text="فصل هشتم", url="your lurl"),row=5)
  
		reply_markup.add(InlineKeyboardButton(text="نرم 2", url="your lurl"),row=6)
		reply_markup.add(InlineKeyboardButton(text="فصل اول", url="your lurl"),row=7)
		reply_markup.add(InlineKeyboardButton(text="فصل دوم", url="your lurl"),row=7)
		reply_markup.add(InlineKeyboardButton(text="فصل سوم", url="your lurl"),row=8)
		reply_markup.add(InlineKeyboardButton(text="فصل چهارم", url="your lurl"),row=8)
		reply_markup.add(InlineKeyboardButton(text="فصل پنجم", url="your lurl"),row=9)
		reply_markup.add(InlineKeyboardButton(text="فصل ششم", url="your lurl"),row=9)
		reply_markup.add(InlineKeyboardButton(text="فصل هفتم", url="your lurl"),row=10)
		reply_markup.add(InlineKeyboardButton(text="فصل هشتم", url="your lurl"),row=10)

		reply_markup.add(InlineKeyboardButton(text="طراحی الگوریتم", url="your lurl"),row=11)
		reply_markup.add(InlineKeyboardButton(text="فصل اول", url="your lurl"),row=12)
		reply_markup.add(InlineKeyboardButton(text="فصل دوم", url="your lurl"),row=12)
		reply_markup.add(InlineKeyboardButton(text="فصل سوم", url="your lurl"),row=13)
		reply_markup.add(InlineKeyboardButton(text="فصل چهارم", url="your lurl"),row=13)
		reply_markup.add(InlineKeyboardButton(text="فصل پنجم", url="your lurl"),row=14)
		reply_markup.add(InlineKeyboardButton(text="فصل ششم", url="your lurl"),row=14)
		reply_markup.add(InlineKeyboardButton(text="فصل هفتم", url="your lurl"),row=15)
		reply_markup.add(InlineKeyboardButton(text="فصل هشتم", url="your lurl"),row=15)
  
		reply_markup.add(InlineKeyboardButton(text="برنامه سازی پیشرفته ", url="your lurl"),row=16)
		reply_markup.add(InlineKeyboardButton(text="فصل اول", url="your lurl"),row=17)
		reply_markup.add(InlineKeyboardButton(text="فصل دوم", url="your lurl"),row=17)
		reply_markup.add(InlineKeyboardButton(text="فصل سوم", url="your lurl"),row=18)
		reply_markup.add(InlineKeyboardButton(text="فصل چهارم", url="your lurl"),row=18)
		reply_markup.add(InlineKeyboardButton(text="فصل پنجم", url="your lurl"),row=19)
		reply_markup.add(InlineKeyboardButton(text="فصل ششم", url="your lurl"),row=19)
		reply_markup.add(InlineKeyboardButton(text="فصل هفتم", url="your lurl"),row=20)
		reply_markup.add(InlineKeyboardButton(text="فصل هشتم", url="your lurl"),row=20)
  
		reply_markup.add(InlineKeyboardButton(text="مبانی برنامه نویسی ", url="your lurl"),row=21)
		reply_markup.add(InlineKeyboardButton(text="فصل اول", url="your lurl"),row=22)
		reply_markup.add(InlineKeyboardButton(text="فصل دوم", url="your lurl"),row=22)
		reply_markup.add(InlineKeyboardButton(text="فصل سوم", url="your lurl"),row=23)
		reply_markup.add(InlineKeyboardButton(text="فصل چهارم", url="your lurl"),row=23)
		reply_markup.add(InlineKeyboardButton(text="فصل پنجم", url="your lurl"),row=24)
		reply_markup.add(InlineKeyboardButton(text="فصل ششم", url="your lurl"),row=24)
		reply_markup.add(InlineKeyboardButton(text="فصل هفتم", url="your lurl"),row=25)
		reply_markup.add(InlineKeyboardButton(text="فصل هشتم", url="your lurl"),row=25)
		#reply_markup.add(InlineKeyboardButton(text="package algoritm", url="your lurl"), row=2)
		#reply_markup.add(InlineKeyboardButton(text="گروه استاد راهنما", url="your link9"), row=2)
		await message.reply(
#برای نمایش مسیج از کد بالا استفاده میکنیم
			f"*خوش آمدید {message.author.first_name}\nبرای دریافت چنل های استاد کلمه!لیست کانال های استاد! وارد کنید*",
			components=reply_markup
		)
#در کد زیر هم اگر مسیج مساوی چیزی داده باشیم باشه باکس زیر رو میسازه و فقط اسم هارو میده بهش
	elif message.content == "لیست کانال های استاد":
		await message.reply(
			f"* خدمت شما{message.author.first_name}\nاز منوایجاد شده انتخال کنید*",
			components=MenuKeyboardMarkup().add(MenuKeyboardButton('package git hub')).add(MenuKeyboardButton('package git hub'))
		)
#در این قسمت اسم هایی که دادیم در کد بالا رو بهش آدرس میدیم
	elif message.content in [
		'package git hub',
		'package git hub'
	]:
		await message.reply(
			"{} is {}".format(message.content, {" package git hub ": 'url link', " package git hub": 'your lurl/github'}[message.content]),
			components=MenuKeyboardMarkup() # برای حذف منیو کیبورد
		)

@client.event
async def on_callback(callback: CallbackQuery):
	if callback.data == "classes in this term":
		await callback.message.reply(
			
   )
  

client.run()
#اجرای کلاینت