# pindrop
This application has 2 parts. 
1. REST server that serves user requests
2. Service that runs perpetually in background collecting the statistics

SYNOPSIS:
I have used Flask micro-framework to create a RESTFul API. 
I have used psutil library to get the stats of the machine

INSTALL:
pip install flask and other dependencies (which get installed along with flask)
pip install psutil

TO RUN:
./application.py

EXAMPLE:
http://127.0.0.1:5000/api/stats/memory/now?stat_type=free
Other API can be seen in application.py
