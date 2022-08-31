import requests
from bs4 import BeautifulSoup

def checkPrice(baseline):
    url = 'YOUR URL HERE'

    headers = {'YOUR USER AGENT HERE'}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    convertedPrice = float(price[:-3])

    if(convertedPrice < baseline):
        sendMail()
        

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YOUR EMAIL', 'YOUR PASSWORD')

    subject = 'Price change.'
    body = f"Check the price here: {url}"

    msg=f"Subject: {subject} \n\n{body}"

    server.sendmail(
        'YOUR FIRST EMAIL',
        'YOUR SECOND EMAIL', 
        msg
    )

    server.quit()

while(True):
    checkPrice()
    time.sleep(3600)
