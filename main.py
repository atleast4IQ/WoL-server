from flask import Flask
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route('/<mac_address>')
def wake_on_lan(mac_address):
    try:
        send_magic_packet(mac_address)
        return f'WOL to {mac_address} sent! <script>window.close()</script>'
    except Exception as e:
        return f'Error: {str(e)}', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
