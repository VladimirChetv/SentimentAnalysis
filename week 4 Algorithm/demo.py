from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request

app = Flask(__name__)

print("Preparing classifier")
start_time = time.time()
classifier = SentimentClassifier()
print("Classifier is ready")
print(time.time() - start_time, "seconds")


@app.route('/')
@app.route('/', methods=["POST", "GET"])
def hello(text='', prediction_message=''):
    if request.method == 'POST':
        text = request.form['text']
        prediction_message = classifier.get_prediction_message(text)
    return render_template('hello.html', text=text, prediction_message=prediction_message)


@app.errorhandler(404)
def not_found(e):
   return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=False)
