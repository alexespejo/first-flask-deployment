from flask import Flask
import requests 
from bs4 import BeautifulSoup 

app = Flask(__name__)

@app.route("/")
def hello_world():
    URL = "http://www.values.com/inspirational-quotes"
    r = requests.get(URL) 
    
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
    return soup.prettify()