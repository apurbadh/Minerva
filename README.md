# Minerva
A platform for sharing selfmade courses, quizes to other in the platform

## How to Run ?

### From python on host machine
To run this app from python on the host machine run the following commands

#### For Windows
```
python -m pip install -r requirements.txt
python manage.py runserver
```
#### For Linux/Mac
```
python3 -m pip install -r requirements.txt
python3 manage.py runserver
```

### Using virtualenv

#### For Windows
```
./venv/Scripts/activate
python manage.py runserver
```
#### For Linux
```
source venv/bin/activate
python3 manage.py runserver
```

### Using Docker
 ```
 docker-compose up -d
 ```
