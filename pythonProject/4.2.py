import re
def clean_data(data):
    cleaned_data = []
    for item in data:
        item = ' '.join(item.split())
        item = re.sub(r'[^\w\s]', '', item)
        item = item.title()
        cleaned_data.append(item)
    return cleaned_data

dirty_data = ["  Газпром   ", "    Роснефть ! ", "ЛУКоЙл№",
               "Сургутнефтегаз", "           Сбербанк ?",
                "транснефть", "$МосЭнерго@"]
cleaned_data = clean_data(dirty_data)
for item in cleaned_data:
    print(item)