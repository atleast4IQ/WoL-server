from flask import Flask
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route('/')
def wake_on_lan():
    send_magic_packet('DE:AD:BE:EF:00:00')  # replace with your MAC-Adress
    return 'WOL gesendet!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
