# Installation Instructions

#### Virtual Environment

Setting up virtual environment

```
virtualenv --python=python3.9 flaskgit add
source flask/bin/activate
```

#### Running Client App

Setting up virtual environment

```
pip install -r requirements.txt 
```

Change Host IP in client app/app.py to server IP

host = "http://Server IP:80"

Run Client Flask App

First cd to client folder

```
python3 app.py 
```

#### Running Server App

```
flask run --host=0.0.0.0 --port=8080
```



#### Problem

Servers can recognize clients and their data stored on server’s storage.
This leads to security concerns where the server providers can maliciously retrieve or sell the data.


#### Solution

Encrypt the client message and generate ID for the message on the client side before sending to server.
Server has no clue of the actual client’s identity/message stored on the database.
Other clients can request the data using the message ID from the server.
