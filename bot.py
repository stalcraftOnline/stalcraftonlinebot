#Импорт пакетов
#from posix import EX_OSFILE
import discord
import asyncio
import os
from dotenv import load_dotenv
import sys
import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver

web = webdriver.Firefox(executable_path='geckodriver.exe')

web.get('https://stalcraft.net')
#========================================


#Для того чтобы не сливать токен своего бота в исходном коде на Github мы будем грузить его из файла окружающией среды (.env).
load_dotenv()

TOKEN = os.getenv('TOKEN')
#========================================


#Блок бота Discord
class MyClient(discord.Client):
    #Приветствие от бота в консоль при его инициализации.
    async def on_ready(self):
        def getOnline():
            html = web.page_source
            soup = BeautifulSoup(html, 'html.parser')
            onlinestr = soup.find(class_="sub-logo logo-img-mp").text
            onlinews = onlinestr.replace("  ", "")
            online = onlinews.replace('\n',"")
            return online
        while True:
            print(getOnline())
            await self.change_presence(activity=discord.Streaming(name=f'{getOnline()}',url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
            await asyncio.sleep(15)
            web.refresh()
    #========================================

    #Блок бота где он принимает все сообщения.
    async def on_message(self, message):

        #Введение переменных для упрощения моей работы.
        msg = message.content
        args = msg.split(' ')
        command = args[0]
        guild = message.guild
        user = message.author
        channel = message.channel
        admin = user.guild_permissions.administrator
         #========================================
    #========================================
        #sql.execute("DELETE FROM roles WHERE rolename = 'None'")

#Запуск бота
client = MyClient()
client.run(TOKEN)
#========================================

#856203715584458782
#856203715584458782