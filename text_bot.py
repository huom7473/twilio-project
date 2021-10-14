from twilio.rest import Client
import requests
import json
import datetime


def react(value):
    if value < -50:
        return "What happened???"
    elif value < -25:
        return "Hope you sold..."
    elif value < -10:
        return "Yikes."
    elif value < 0:
        return "Oof."
    elif value == 0:
        return "No way..."
    elif value < 10:
        return "Nice."
    elif value < 25:
        return "Yeeeeeeeeeet."
    else:
        return "To the moooooooooon!"

def get_price():
    btc_price = float(requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD').json()['data']['amount'])

    with open('price_data.txt', 'r+') as f:
        last_price = json.load(f)
        f.seek(0)
        f.write(f'{btc_price:<20}')

    percent_change = ((btc_price-last_price)/last_price)*100

    return f"- -\n\nThe price of BTC is ${btc_price:0.2f}, "\
           f"{'up' if btc_price >= last_price else 'down'} "\
           f"{abs(percent_change):0.2f}% (${abs(btc_price - last_price):0.2f}) from yesterday's "\
           f"price of ${last_price:0.2f}. {react(percent_change)}\n\n"\
           f"Today's date is {datetime.date.today()}."

if __name__ == "__main__":
    account_sid = "ACCOUNT_SID"
    auth_token = "AUTH_TOKEN"
    client = Client(account_sid, auth_token)

    client.messages.create(body=
                           get_price() + "\n\nThis is your daily price check.",
                           from_='+FROM_NUMBER', to='+TO_NUMBER')





