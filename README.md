Currency Crawling

--------------------
**INSTALATION**
--------------------

1- clone the project -> 
git clone https://github.com/sepide1371/CurrencyCrawling

2- create a virtual environment -> 
virtualenv venv

3- install required packages(in root of project) -> 
pip install -r requirements.txt

3- run project(in root of project) -> 
python manage.py runserver

4- run redis -> redis-server

5- run following command for start celery worker -> celery -A currency_crawling worker --pool=solo -l info

6- run following command for start celery beat -> celery -A currency_crawling beat -l info


--------------------
**SUPER USER INFOS**
--------------------
test super user info -> 
username: "admin"
password: "123"


--------------------
**POST MAN COLLECTION**
--------------------
postman collection file uploaded in root of project

--------------------
**ATTENTION**
--------------------
all of api uses oauth2-

for get token call -> http://127.0.0.1:8000/oauth/token/

and set body like this:
```
    {
    "client_id":"bBOCOhs7N8CiT1s3GvYdkRM3PSPlW8TlykuAABG0",
    "grant_type": "password",
    "username":"admin",
    "password": "123"
    }
```

and for use refresh token set body like this:
```
{
    "client_id":"bBOCOhs7N8CiT1s3GvYdkRM3PSPlW8TlykuAABG0",
    "grant_type":"refresh_token",
    "refresh_token": "hCdYPWty9gKFRNIbPQccIdWclCkgpZ"
}
```