from flask import Flask
from datetime import datetime, timezone, timedelta
from requests import get
from time import sleep
from main import Send_Message
from threading import Thread

cookie = 'datr=4xyvY1FGZLGSOsM5RVDgbxOC; sb=4xyvY5kSqkjKLH2ySHm0zc2s; c_user=100075924800901; xs=32%3AHjU6qrosQXW8zA%3A2%3A1672420588%3A-1%3A5149; fr=0FcW89NSGkxa0Pos0.AWWjho3YrHCflxdwZhMk1yIot2I.Bjrxzr.gP.AAA.0.0.Bjrxzr.AWUxd-H3qA8; m_page_voice=100075924800901'
new_yr_msg = "Happy New Year, friends! As we enter 2023, I wish you all the best this new year has to offer. May it be filled with love, laughter, and all your heart's desires. Here's to a year of endless possibilities and endless fun. Let's make 2023 our best year yet! Cheers to a fantastic year."

app=Flask(__name__)
app.config['SECRET_KEY']='thisismysecretkey'
is_done=False

@app.route('/')
def home():
    current_time = datetime.now(timezone(timedelta(hours=6)))
    new_year_time = datetime(year=2023, month=1, day=1, hour=0, minute=0, tzinfo=timezone(timedelta(hours=6)))
    return f'App Running<br>Time Remaining: {new_year_time - current_time}<br>Is Done: {is_done}'

def check_done():
    return get('https://api.countapi.xyz/hit/ytwxbfuyiuqcti/visits').json()['value']

def thread_task():
    global is_done
    while True:
        current_time = datetime.now(timezone(timedelta(hours=6)))
        new_year_time = datetime(year=2023, month=1, day=1, hour=0, minute=0, tzinfo=timezone(timedelta(hours=6)))
        if current_time > new_year_time:
            if check_done() < 2:
                Send_Message('100014913152846', new_yr_msg, cookie)
                Send_Message('100008352752354', new_yr_msg, cookie)
                Send_Message('100077756340708', new_yr_msg, cookie)
                Send_Message('100074400744893', new_yr_msg, cookie)
                Send_Message('100063442311391', new_yr_msg, cookie)
                Send_Message('1151546782', new_yr_msg, cookie)
                is_done=True

        sleep(10)

t=Thread(target=thread_task)
t.setDaemon(True)
t.start()

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
