import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.ebay.com/itm/Apple-Watch-Series-4-44mm-A1978-GPS-Space-Gray-Aluminum-Black-Sport-Band-INC/164063196101?epid=19028318361&_trkparms=ispr%3D1&hash=item2632edb3c5:g:TQ0AAOSwTEteOIud&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qVViPQMKXguLtOufn5twSue4u8aKA4gOG%2FLqhD4EUMGfX5nqCsjQFAqqPYXyfQ%2Fl6zlBEor3xMt0b3mi%2F2IrhJA0qnI3Ow4Zktu0OUaOWJu3mmHoZe57cSJIwkwov0wl%2FpbA0JXOYQcfCaSCuK0ZUiNovSbjzIkGjtAxKgI7IFJOXTuF3SYBbHnfsrkVq6WrPCiyw1JT%2BrVrmTrXaTzcGB3JLcRQ%2BaMFfT9%2BkFYRiYTNIdNcuXqq0g1dYhxMuWn2RQmGnJE2C1YQ2xA8%2Boufx5%2Bfh%2BqlYDkPw7OTXZoLfPgC7ZmQ8nzgF3h4X7ACI0dihCB7U6IrAeBl6I1d9BeMXwqN46ib%2Br8KhKbT93ICuVp0xfJcBYXhJ3WjmT4mj5%2F%2FAdy6zBDDezqVU0afn5SnaRNG4o62SWyFrvKu7Ouju8M9lqTnOZdMdbvxukc8rbkeyHWttEUJGA%2F5gmSZUP79%2BLiHDUaUsSv3ZahWRnOaHcS%2FZoe88t4LwbJOoKi9OfFu0ZSvUo%2FN9FlbxX0woNTxDmyiFxhBy%2BamwGrmlAKNvAC6%2FYLaj56OFb6rnPbEj5mR0K70c%2F8kwXjsyZYsUgWSmnJRpDuIrkJwF36hh%2Bt9PBNmVqhlnDvPwUjxl%2FsGiH%2FuYTGUG2gv7ZI1NMGDW7la7siqLOnLmOtiR29SHo8pdbRTzAiQIU4bjNSYycSYmu8nCQWIG%2BNcPlAn4EPJjfURj%2BlTTZ7f6e4WVHq7NZs%2FjCwKg%3D%3D&checksum=164063196101a687a4ea76f84e429e746a5fb57b04d4'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 OPR/67.0.3575.53'}

# Check the price


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    product_title = soup.find(id="itemTitle").get_text()
    product_price = soup.find(id="prcIsum").get_text()

    modified_product_title = product_title[16:-21]
    modified_price = int(product_price[4:7])

    print(modified_product_title)
    print(modified_price)

    if(modified_price < 379):
        send_email()


def send_email():
    # The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon. ... If specified, local_hostname is used as the FQDN of the local host in the HELO/EHLO command. Otherwise, the local hostname is found using socket.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # ehlo command sent by an email server to identify itself when connecting to another email server to start the process of sending an email
    server.starttls()
    server.ehlo()

    # Enter your own email and password
    server.login('spiderman@gmail.com', 'yuepwzblztknipk')

    subject = "Yeah Baby ! Price Fell Down!! "
    body = " Check the Link : https://www.ebay.com/itm/Apple-Watch-Series-4-44mm-A1978-GPS-Space-Gray-Aluminum-Black-Sport-Band-INC/164063196101?epid=19028318361&_trkparms=ispr%3D1&hash=item2632edb3c5:g:TQ0AAOSwTEteOIud&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qVViPQMKXguLtOufn5twSue4u8aKA4gOG%2FLqhD4EUMGfX5nqCsjQFAqqPYXyfQ%2Fl6zlBEor3xMt0b3mi%2F2IrhJA0qnI3Ow4Zktu0OUaOWJu3mmHoZe57cSJIwkwov0wl%2FpbA0JXOYQcfCaSCuK0ZUiNovSbjzIkGjtAxKgI7IFJOXTuF3SYBbHnfsrkVq6WrPCiyw1JT%2BrVrmTrXaTzcGB3JLcRQ%2BaMFfT9%2BkFYRiYTNIdNcuXqq0g1dYhxMuWn2RQmGnJE2C1YQ2xA8%2Boufx5%2Bfh%2BqlYDkPw7OTXZoLfPgC7ZmQ8nzgF3h4X7ACI0dihCB7U6IrAeBl6I1d9BeMXwqN46ib%2Br8KhKbT93ICuVp0xfJcBYXhJ3WjmT4mj5%2F%2FAdy6zBDDezqVU0afn5SnaRNG4o62SWyFrvKu7Ouju8M9lqTnOZdMdbvxukc8rbkeyHWttEUJGA%2F5gmSZUP79%2BLiHDUaUsSv3ZahWRnOaHcS%2FZoe88t4LwbJOoKi9OfFu0ZSvUo%2FN9FlbxX0woNTxDmyiFxhBy%2BamwGrmlAKNvAC6%2FYLaj56OFb6rnPbEj5mR0K70c%2F8kwXjsyZYsUgWSmnJRpDuIrkJwF36hh%2Bt9PBNmVqhlnDvPwUjxl%2FsGiH%2FuYTGUG2gv7ZI1NMGDW7la7siqLOnLmOtiR29SHo8pdbRTzAiQIU4bjNSYycSYmu8nCQWIG%2BNcPlAn4EPJjfURj%2BlTTZ7f6e4WVHq7NZs%2FjCwKg%3D%3D&checksum=164063196101a687a4ea76f84e429e746a5fb57b04d4 "

    msg = f"subject: {subject}\n\n {body}"

    server.sendmail(
        'spiderman@gmail.com',
        'hulk@outlook.com',
        msg
    )

    print('You can buy it now!! EMAIL HAS BEEN SENT !')

    server.quit()


while True:
    check_price()
    time.sleep(86400)  # 60 * 60 * 24
