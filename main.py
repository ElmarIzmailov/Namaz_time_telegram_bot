import requests
import telebot
from bs4 import BeautifulSoup
from telebot import types

from var_main import *

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    
    item = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("🕋 Namaz Time", callback_data=namaz_time)
    item2 = types.InlineKeyboardButton("🌆 Today's Weather ", callback_data=day_temperature)
    item3 = types.InlineKeyboardButton("🌌 Today Which Holiday Day", callback_data=which_day)
    item4 = types.InlineKeyboardButton("💰 Bitcoin", callback_data=bitcoin)
    item5 = types.InlineKeyboardButton("📲 Admin", callback_data=admin)
    
    item.row(item1)
    item.row(item2, item3)
    item.row(item4, item5)
    
    bot.send_message(message.chat.id, f"👋 Hello  {message.from_user.first_name}", reply_markup=item)
    


@bot.callback_query_handler(func=lambda call: True)
def prossec(call):
   
# back
    if call.data == back:

        try:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("🕋 Namaz Time", callback_data=namaz_time)
            item2 = types.InlineKeyboardButton("🌆 Today's Weather ", callback_data=day_temperature)
            item3 = types.InlineKeyboardButton("🌌 Today Which Holiday Day", callback_data=which_day)
            item4 = types.InlineKeyboardButton("💰 Bitcoin", callback_data=bitcoin)
            item5 = types.InlineKeyboardButton("📲 Admin", callback_data=admin)
        
            item.row(item1)
            item.row(item2, item3)
            item.row(item4, item5)
    
            bot.send_message(call.message.chat.id, f"👋 Hello  {call.from_user.first_name}", reply_markup=item)
        
        
        except:
            bot.send_message(call.message.chat.id, "😔 No Information click on button /start")

    
    
    # 🕋 Namaz Time
    elif call.data == namaz_time:

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
            resp = requests.get('https://namozvaqti.uz/', headers=headers).text
            soup = BeautifulSoup(resp, "html.parser")
            
            bomdod = soup.find("p", class_="time", id="bomdod")
            quyosh = soup.find("p", class_="time", id="quyosh")
            peshin = soup.find("p", class_="time", id="peshin")
            asr = soup.find("p", class_="time", id="asr")
            shom = soup.find("p", class_="time", id="shom")
            xufton = soup.find("p", class_="time", id="hufton")
            
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("<- back", callback_data=back)
            item.row(item1)
            
            bot.send_message(call.message.chat.id, f"☀️ Quyosh Time      {quyosh.get_text()}\n\n"
                                                   f"🌄 Bomdod Time     {bomdod.get_text()}\n\n"
                                                   f"🏙 Peshin Time        {peshin.get_text()}\n\n"
                                                   f"🌆 Asr Time              {asr.get_text()}\n\n"
                                                   f"🎇 Shom Time          {shom.get_text()}\n\n"
                                                   f"🌃 Xufton Time         {xufton.get_text()}\n\n", reply_markup=item)


                    
        except:
            bot.send_message(call.message.chat.id, "😔 No Information click on button /start")
    

    # admin 
    elif call.data == admin:
        kivy = bot.send_message(call.message.chat.id, "If you have any suggestions or complaints please write !!")
        bot.register_next_step_handler(kivy, get_admin)
        


    # 🌆 Today's Weather
    elif call.data == day_temperature:

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
            resp = requests.get('https://www.weather-atlas.com/en/uzbekistan/asaka#:~:text=The%20current%20temperature%20(20%3A23,C%20(82.4%C2%B0F)',headers=headers).text
            soup = BeautifulSoup(resp, "html.parser")
            
            tempeterure = soup.find("li", class_="fs-2")
            info_weather = soup.find("ul", class_="list-unstyled lh-sm mb-0")

            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("<- back", callback_data=back)
            
            item.row(item1)

            bot.send_message(call.message.chat.id, f"🌡️ Asaka {tempeterure.get_text()}\n\n"
            f"{info_weather.get_text()}", reply_markup=item)

        except:
            bot.send_message(call.message.chat.id, "😔 No Information click on button /start")

    
    
    # 🌌 Today Which Holiday Day
    elif call.data == which_day:

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
            resp = requests.get('https://nationaltoday.com/what-is-today',headers=headers).text
            soup = BeautifulSoup(resp, "html.parser")
            
            day = soup.find("h3", class_="holiday-title")

            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("<- back", callback_data=back)
            item.row(item1)
            
            bot.send_message(call.message.chat.id, f"😉 Today {day.get_text()} !", reply_markup=item)
        
        except:
            bot.send_message(call.message.chat.id, "😔 No Information click on button /start")
    
    elif call.data == bitcoin:
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
            resp = requests.get('',headers=headers).text
            soup = BeautifulSoup(resp, "html.parser")
            
            bit = soup.find_all("span", class_="pclqee")

            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("<- back", callback_data=back)
            item.row(item1)
            
            bot.send_message(call.message.chat.id, f"😉 Today bitcoin price {bit.get_text()} !", reply_markup=item)
        
        except:
            bot.send_message(call.message.chat.id, "😔 No Information click on button /start")

def get_admin(message):
    bot.send_message(5371294058, message.text)
    
    item = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("<- back", callback_data=back)

    item.row(item1)
    bot.send_message(message.chat.id, "🙏 Thanks for the feedback", reply_markup=item)


@bot.message_handler(content_types=["text"])
def get_text(message):
    bot.delete_message(message.chat.id, message.message_id)




bot.polling(none_stop=True)