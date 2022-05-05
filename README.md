# DjangoSpeedrunAnyPercent

## Description

Project name: Daniil CMS  
Technologies: Django, DRF  
Idea: CMS for various services with the sale of goods.  
This CMS has an authorization module, a permission layer. There is also a logging module at the database level.  
Adult content layer. Architecture of not deletable models. Main entities: Category, Item, Images, Reviews, Order.  
The system can be integrated as a backend engine for mobile applications or web applications. There is a built-in admin module for moderators.   
The architecture is built on Scalable and Portable application. The engine can be used for various purposes, from a blog to a store.  


## Setup
```sh
git clone https://github.com/Sens3ii/DjangoSpeedrunAnyPercent.git  
python3 -m venv env  
source env/bin/activate  

pip install -r requirements.txt
./manage.py runserver
```
Also you should create postgresql database and add credentials in .env  
