from Katil import Saurabh as Stark
from telethon import events, Button

PM_START_TEXT = """
**Hi {}**
I Am A Bot Who Works For @KatilXspam And Can Detect Spammers In Your Groups Can Protect Goups From Them.

**Click The Below Button For Getting Help Menu!**
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name),
 buttons=[
          [
            Button.inline("Commands", data="help"), 
            Button.url("Support", "https://t.me/KatilXUpdates")
          ]
         ]
     )
       return

    if event.is_group:
       await event.reply("**Hehe Am Alive Baby💔**")
       return
