from modules import horoscopes
from modules import dices
from modules import coin

functions_list = {
    'Roll a dice': '{"text": "Usage: @ModuleTestKazikBot !dices", "desc": "!dices"}',
    'Flip a coin': '{"text": "Usage: @ModuleTestKazikBot !coin", "desc": "!coin"}',
    'Daily horoscope': '{"text": "Usage: @ModuleTestKazikBot !horoscopes", "desc": "!horoscopes"}'
}


async def create_answer(module):
    if module == "!dices":
        return await dices.roll_dice()
    elif module == "!horoscopes":
        return await horoscopes.get_horo()
    elif module == "!coin":
        return await coin.coin_flip()
    else:
        return {'Try again': '{"text": "Try again", "desc": "Check available commands", "withImage": "False"}'}
