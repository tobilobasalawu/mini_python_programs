import requests   #To access a URL and pull out data from the site
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.co.uk/Veno-Scorp-Gaming-Bundle-Set/dp/B0BDMV65L3/ref=sr_1_4?crid=26JIKCFTS05W2&dib=eyJ2IjoiMSJ9.n-kGti1DZUbAdS_Gc8KlJ2Mtii3nTeb3eK_dScGen4bTYc_VGqMUKl_7sxA0ijW_UQD8TsGkj2RKJ3hon_coH_Q-iuUIpij4eaAivMVsvg_W5ovmZZKaR_MEJkDpg0mLWgs-Q-PcfMH_XrkWxWAItnfcITEJ25NuHXjsEu-djy42eCW6hfI5L6ylOXf66u3FSF6OiuYG2unpDO5vZQxhHl6OWFszI8Mm2VvTWfeNnaA.YH9ZA_dqprXbzhY5Uw9PofRjTWs68GNbdYFcj2zPLWc&dib_tag=se&keywords=pc+coding&qid=1712952315&sprefix=pc+coding%2Caps%2C245&sr=8-4"

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}
#Gives us info on our broswer

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser') #To pull out individual data

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(class_= "a-price-whole").get_text()
    converted_price = float(price[0:5])

    if converted_price < 1.700:
        send_mail()

    print(converted_price)
    print(title.strip())
    
    if converted_price > 1.700:
        send_mail()
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('tobisal.dev@gmail.com', 'gzqd wgrm gbtw myfd')
    
    subject = 'Price fell down'
    body = 'check the amazon link https://www.amazon.co.uk/Veno-Scorp-Gaming-Bundle-Set/dp/B0BDMV65L3/ref=sr_1_4?crid=26JIKCFTS05W2&dib=eyJ2IjoiMSJ9.n-kGti1DZUbAdS_Gc8KlJ2Mtii3nTeb3eK_dScGen4bTYc_VGqMUKl_7sxA0ijW_UQD8TsGkj2RKJ3hon_coH_Q-iuUIpij4eaAivMVsvg_W5ovmZZKaR_MEJkDpg0mLWgs-Q-PcfMH_XrkWxWAItnfcITEJ25NuHXjsEu-djy42eCW6hfI5L6ylOXf66u3FSF6OiuYG2unpDO5vZQxhHl6OWFszI8Mm2VvTWfeNnaA.YH9ZA_dqprXbzhY5Uw9PofRjTWs68GNbdYFcj2zPLWc&dib_tag=se&keywords=pc+coding&qid=1712952315&sprefix=pc+coding%2Caps%2C245&sr=8-4'
    
    msg = f"Subject : {subject}\n\n{body}"
    
    server.sendmail(
        'tobisal.dev@gmail.com',
        'oluwatobilobasalawu1234@gmail.com',
        msg
        )
    print('Hey EMAIL has been sent')
    
    server.quit()
    
while True:
    print(check_price())
    time.sleep(60 * 60 * 60)