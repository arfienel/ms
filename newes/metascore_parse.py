

def Parse(URL):
    import requests
    from bs4 import BeautifulSoup
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'accept': '*/*'}
    html = requests.get(URL, headers=HEADERS)
    if html.status_code == 200:
        html = html.text

        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='metascore_w xlarge game positive')
        if items == []:
            items = soup.find_all('div', class_='metascore_w xlarge game mixed')
        if items == []:
            items = soup.find_all('div', class_='metascore_w xlarge game negative')
        items = str(items)
        items = items.replace(items[0:items.find('span')+5],'').replace(items[items.find('</'):],'')

        return int(items)

    else:
        print('Error')
        return False


