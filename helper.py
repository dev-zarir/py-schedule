from mechanize import Browser
from requests import get
from datetime import datetime, timezone, timedelta
from time import sleep

# Required Info
target_id='100063442311391'
wish_msg="Happy birthday, Nazia! I hope this special day is as amazing as you are. You deserve all the love, laughter, and birthday cheer that comes your way. I'm so grateful to have you as a friend and I can't wait to see all the amazing things you'll accomplish in the year ahead. Here's to another year of friendship, growth, and endless memories. May your birthday be as special as you are!"
cookie='wd=1366x615; fr=0LWH2JUC0zv8yUWoj.AWWLhiwgIoc9BUvPQxQbx7K6XfU.Bjt9kl.xf.AAA.0.0.Bjt938.AWUfygvdLMA; sb=Jdm3Y6wXlI8cPMcdpWhvSGXm; datr=Jdm3YzGKkDqXX8uzEjo7SoMr; c_user=100075924800901; xs=39%3ADdy1ToEAVlJkEQ%3A2%3A1672993075%3A-1%3A4472; usida=eyJ2ZXIiOjEsImlkIjoiQXJvMjIzNjFlZnJza3IiLCJ0aW1lIjoxNjcyOTk2NzY0fQ%3D%3D; m_page_voice=100075924800901'

# Sending Function
def Send_Message(target_id, msg, cookie):
    br=Browser()
    br.set_handle_robots(False) # Skip Robot Blocking
    br.set_header('Cookie', cookie) # Login with cookie

    br.open(f'https://mbasic.facebook.com/messages/read/?fbid={target_id}')
    br._factory.is_html=True

    br.select_form(nr=1)
    br.form['body']=msg # Writing the msg
    br.submit() # submit form

def check_if_done_already():
    return get('https://api.countapi.xyz/hit/gruygb2qiuycbyct4/visits').json()['value']

def background_thread():
    while True:
        current_time=datetime.now(tz=timezone(timedelta(hours=6)))
        birthday_time=datetime(year=2023, month=1, day=14, hour=0, minute=0, tzinfo=timezone(timedelta(hours=6)))
        if current_time > birthday_time:
            if check_if_done_already() < 2:
                Send_Message(target_id, wish_msg, cookie) # Sending Message
        sleep(10)
        # Sleeping so server will not crash......
