

def Parse_steam(URL):
    import requests
    from bs4 import BeautifulSoup
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'accept': 'text/css,*/*;q=0.1',
        'l':'russian',
        'Accept-Language': 'ru, ru - RU'}
    cookies = {'birthtime': '568022401'}
    try:
        html = requests.get(URL, headers=HEADERS,cookies=cookies)
    except:
        return 0
    if html.status_code == 200:
        html = html.text

        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find('div', class_='game_purchase_action_bg')
        items = str(items)
        if 'discount_final_price' in items:
            percent = items.find('discount_pct')
            percent = items[percent+14:percent+19]
            for item in percent:
                if item not in '1234567890':
                    percent = percent.replace(item,'')
            percent_int = int(percent)
            percent = '-'+percent+'%'
            orig_price = items.find('discount_original_price')
            orig_price = items[orig_price+20:orig_price+36]
            for item in orig_price:
                if item not in '1234567890':
                    orig_price = orig_price.replace(item,'')
            orig_price_int = int(orig_price)
            orig_price = orig_price+' Руб'
            final_price_int = round(orig_price_int*(1-(percent_int/100)))
            return [percent_int,orig_price_int,final_price_int]

        elif 'Бесплатно' in items:
            free = 'Бесплатно'
            return free

        else:
            price = items.find('game_purchase_price price')
            if price == -1:
                return 0
            price = items[price+55:price+80]
            for item in price:
                if item not in '1234567890':
                    price = price.replace(item,'')
                if price == '':
                    return 0

            return int(price)

    else:
        print('Error')
        return False
