# Made by @fayeezus

import requests
import random

url = 'https://mpirecreative.us5.list-manage.com/subscribe/post?u=e2cf7e6c560758356521baeb3&amp;id=83635a820b'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


def arizona_raffle():
    for number in range(1,10000):
        info = {
            'FNAME': 'Joe',  # first name
            'LNAME': 'Shmoe',  # last name
	        'EMAIL': 'email+{}@gmail.com'.format(random.randint(1,10000)),  # email, don't change end
			'MMERGE3': '6062892345',  # phone number
            'ADDRESS[addr1]': '',  # Address Line 1
			'ADDRESS[addr2]': '',  # Address Line 2 (optional)
			'ADDRESS[city]' : '', #city
			'ADDRESS[state]' : '', #state
			'ADDRESS[zip]' : '', #zipcode
			'ADDRESS[country]' : '', #country value 146 for USA view https://niggabin.com/unevimiluw.js for other countries value
            'MMERGE5': '',  # size values in https://niggabin.com/usitucelic.xml
            'MMERGE4': '',  # for style values in https://niggabin.com/olivoxezef.xml
            'subscribe': "Submit",  # don't change
        }

        req = requests.post(url, data=info, headers=headers, timeout=8)

        if req.status_code == 200:
            print('Arizona Raffle Entry Successful:' + str(number))
        else:
            print('Arizona Raffle Entry Unsuccessful')


if __name__ == '__main__':
    arizona_raffle()
