from flask import Flask, render_template, request, jsonify
from google.cloud import language_v1
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
client = language_v1.LanguageServiceClient()

@app.route('/', methods=['GET', 'POST'])
def reverse_input():
    if request.method == 'POST':
        # Get input values from the form
        input_text = request.form['input1']

        document = language_v1.types.Document(
            content=input_text, type_=language_v1.types.Document.Type.PLAIN_TEXT
        )
        sentiment = client.analyze_sentiment(
           request={"document": document}
        ).document_sentiment

        # Render the template with reversed inputs
        return render_template('result.html', sentiment_anal=f"Sentiment: {sentiment.score}, {sentiment.magnitude}")

    # Render the initial form
    return render_template('index.html')

@app.route('/json_example/<input_param>', methods=['GET'])
def json_example(input_param):
    # You can perform any processing on the input_param here if needed
    # For simplicity, let's just return it as JSON
    response_data = {'input_param': input_param}
    return jsonify(response_data)

@app.route("/anal_sentiment/<input_param>")
def gcp(input_param):
    # The text to analyze
    text = input_param 
    document = language_v1.types.Document(
        content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    return {"sentiment": sentiment.score}

@app.route("/testing_api/<param>")
def testing_api(param):
    return {"params": f"params: {param}"} 