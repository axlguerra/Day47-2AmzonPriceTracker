import bs4
from bs4 import BeautifulSoup
import requests
import smtplib

price_level = 20.00

URL = 'https://www.amazon.com/Professional-Mahogany-HUAWIND-Hawaiian-Beginners/dp/B07J4NZ2N6/ref=sr_1_3_sspa?crid=3OG776SJP9OX1&amp&keywords=guitar&amp&qid=1649378717&amp&sprefix=guita%2Caps%2C172&amp&sr=8-3-spons&amp&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSEc0MFlaWjJFUkVMJmVuY3J5cHRlZElkPUEwODQwMTc3MTNaUE1BT0NTREFVNCZlbmNyeXB0ZWRBZElkPUEwNzk1MjU1N0lXM0xHSFBSUVRDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&amp&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

r = requests.get(URL,
        headers=headers)  # , proxies=proxies)

content=r.content



soup = BeautifulSoup(content, 'html.parser')

price = soup.find('span', class_='a-offscreen').getText()

# print(soup)




article_price_float = float(price.split('$')[1])

title = soup.find(id="productTitle").get_text().strip()


MY_EMAIL = ''
MY_PASSWORD = ''



if article_price_float < price_level:

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Amazon article...;.!\n"
                f"The current price for the article you are trackin: {title} is  at ${article_price_float} dollars\n"
                f" and at this moment is {article_price_float - price_level} dollars cheaper than usual \n"
                f"click the link: \n {URL} "
        )

