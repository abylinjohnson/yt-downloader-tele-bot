import os
import telebot
import shortuuid
from pytube import YouTube 
bot = telebot.TeleBot('your bot api')

SAVE_PATH = 'videos'

def ytdownload(link):
    try:
        id = shortuuid.uuid()  
        yt = YouTube(link)
        title = yt.title
        yt.title = id
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
        print("video downloaded")
        return(title, id)
    except: 
        print("Some Error!")
        return('error','error')
    

@bot.message_handler(commands=['get'])
def greet(message):
    msg = message.text.split()
    if len(msg) > 1:
        title, id = ytdownload(msg[1])
        id = "CxebctD8YRWfDff8rTNrdu"
        if id != 'error':
            video = open('videos/CxebctD8YRWfDff8rTNrdu.mp4', 'rb')
            print('opened video')
            bot.send_video(chat_id=message.chat.id, video=video, supports_streaming=True)

bot.infinity_polling()
