!pip install flask_ngrok
from flask_ngrok import run_with_ngrok
from flask import Flask, render_template,request
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/', methods = ['GET', 'POST'])
def text():
 global tokens
 global speech
 global verb
 global noun
 if request.method == 'POST':
   sentence = request.form['sentence'] #accept sentence input
   tokens = nltk.word_tokenize(sentence) #tokenized the sentence
   speech = nltk.pos_tag(tokens) #analyse as part iof speech
   verb = [word for (word, pos) in nltk.pos_tag(tokens) if(pos[:2] == 'VB')] #extract the verb
   noun = [word for (word, pos) in nltk.pos_tag(tokens) if(pos[:2] == 'NN')] #extract the noun
 return render_template('text.html',tokens=tokens, speech=speech, verb=verb, noun=noun)

app.run()