import requests
import json

zodiacs = {
    "aries": "https://farm5.staticflickr.com/4795/38900304020_0e5baa6073_o.jpg",
    "taurus": "https://farm5.staticflickr.com/4787/38900294840_437e248bbe_o.jpg",
    "gemini": "https://farm5.staticflickr.com/4795/25839040287_9f9a647de8_o.jpg",
    "cancer": "https://farm5.staticflickr.com/4796/39815118945_a8f526d52c_o.jpg",
    "leo": "https://farm5.staticflickr.com/4785/40710435551_70de6a5a94_o.jpg",
    "virgo": "https://farm5.staticflickr.com/4776/26838800958_b620a78cfd_o.jpg",
    "libra": "https://farm5.staticflickr.com/4790/40710413431_6d3537a095_o.jpg",
    "scorpio": "https://farm5.staticflickr.com/4773/38900229400_c3e6f6f80f_o.jpg",
    "sagittarius": "https://farm5.staticflickr.com/4792/40710399181_243848ffe3_o.jpg",
    "capricorn": "https://farm5.staticflickr.com/4776/38900194470_108c7f464a_o.jpg",
    "aquarius": "https://farm5.staticflickr.com/4792/25838918497_8d50426e3e_o.jpg",
    "pisces": "https://farm5.staticflickr.com/4793/40710189361_2003097a13_o.jpg"
}


async def get_horo():
    infos = {}
    for entry, value in zodiacs.items():
        params = (
            ('sign', entry),
            ('day', 'today'),
        )
        response = requests.post('https://aztro.sameerkumar.website/', params=params)
        result = json.loads(response.text)
        infos[entry] = '{"text": "' + entry + '\\nLucky number: ' + result['lucky_number'] + '\\nLucky hour: ' + result[
            'lucky_time'] + '\\nYour horoscope: ' + result[
                           'description'] + '", "desc": "Display horoscope for ' + entry + '", "withImage": "True", "imageType": "image/jpeg", "imageUrl": "' + value + '"}'
    return infos
