from flask import Flask
import requests 
from bs4 import BeautifulSoup 
from google.cloud import language_v1

app = Flask(__name__)

@app.route("/")
def hello_world():
    URL = "http://www.values.com/inspirational-quotes"
    r = requests.get(URL) 
    
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
    return soup.prettify()

@app.route("/gcp")
def gcp():
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    text = "I fucking hate you"
    document = language_v1.types.Document(
        content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    # print(f"Text: {text}")
    return f"Sentiment: {sentiment.score}, {sentiment.magnitude}"