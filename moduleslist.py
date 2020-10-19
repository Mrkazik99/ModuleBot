from modules import horoscopes
from modules import dices

functions_list = {
    'Roll a dice': '{"text": "Usage: @ModuleTestKazikBot !dices", "desc": "!dices"}',
    'Daily horoscope': '{"text": "Usage: @ModuleTestKazikBot !horoscopes", "desc": "!horoscopes"}'
}


async def create_answer(module):
    if module == "!dices":
        return await dices.roll_dice()
    if module == "!horoscopes":
        return await horoscopes.get_horo()
    else:
        return {'Try again': '{"text": "Try again", "desc": "Check available commands", "withImage": "False"}'}
