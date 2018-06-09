#launches the webapp on a specified host and port
from flask import Flask
from alcoholism import app

if __name__=='__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        threaded=True
    )

