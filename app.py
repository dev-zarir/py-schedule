from flask import Flask
from helper import background_thread
from threading import Thread
from datetime import datetime, timezone, timedelta

app=Flask(__name__)
app.config['SECRET_KEY']='somerandomkey'

@app.route('/')
def home():
    current_time=datetime.now(tz=timezone(timedelta(hours=6)))
    birthday_time=datetime(year=2023, month=1, day=14, hour=0, minute=0, tzinfo=timezone(timedelta(hours=6)))

    return f'Server is running<br>Time Remaining: { birthday_time - current_time}'

t1=Thread(target=background_thread)
t1.setDaemon(True)
t1.start()

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)