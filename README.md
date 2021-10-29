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



