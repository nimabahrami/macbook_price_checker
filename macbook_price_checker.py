import requests 
from bs4 import BeautifulSoup
import smtplib

URL = "https://sazgarhamrah.com/pro-series/1743-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%D9%BE%D9%84-apple-macbook-pro-mpxq2-2017.html"
headers = {
    "User-Agent": '#search my user agent on google'
}

def check_price():
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content , 'html.parser')
    title = soup.find(id = "our_price_display").get_text()
    price = title.strip().split(' ')
    final_price = int(price[0].replace(',',''))
    if final_price << 13340000:
        send_mail()
    print(final_price)
    print('macbook is getting cheaper and cheaper')

def send_mail():
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('# your email', '# your google app password')
    subject = 'hey youre 1 step closer to buy a macbook'
    body = 'check the price baby check it: https://sazgarhamrah.com/pro-series/1743-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%D9%BE%D9%84-apple-macbook-pro-mpxq2-2017.html'
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
    '#your email (from)', 
    '#your email (to)',
    msg)
    print('hey the email has been sent!')
    
check_price()
