from modules import horoscopes
from modules import dices
from telethon import TelegramClient, events

functions_list = {
    'Daily horoscope': '!horoscopes',
    'Roll a dice': '!dices'
}


async def create_answer(module):
    if module == "!dice":
        return await dices.roll_dice()
    if module == "!horoscopes":
        return await horoscopes.get_horo()
