from telethon.sync import TelegramClient, events
import config
import time
import re

api_id = config.API_ID
api_hash = config.API_HASH

INVOICE = "/send BALANCE @AnotherAccUserName"

with TelegramClient("session-name" , api_id, api_hash) as client:
   print("Started.")
   @client.on(events.NewMessage(from_users="lntxbot"))
   async def handler(event):
        try:
            if(event.chat_id == 738657014):
                text = (event.message.message)
                regex = "You've lost"
                match = re.search(regex , text)
                if(match):
                    await client.send_message(entity = 738657014 , message = INVOICE)
        except Exception as e:
            pass
   client.run_until_disconnected()
