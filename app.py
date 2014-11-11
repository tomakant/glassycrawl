from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
import random
import requests
import ipdb
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud

# Initialize your app and load your pickled models.
#================================================
# init flask app
app = Flask(__name__)
Bootstrap(app)

# load the model you pickled in build_model.py
model = pickle.load(open('data/my_model.pkl', 'r'))

# load the vectorized you pickled in build_model.py
tfidf = pickle.load(open('data/my_vectorizer.pkl', 'r'))

df = pd.read_csv('data/glass_reviews.csv')
df['company'] = df['_pageUrl'].apply(lambda x: x.split('/')[4].split('-Reviews')[0].replace('-',' '))



# Homepage with form on it.
#================================================
@app.route('/')
def index():
    return render_template('my_template.html')
    

@app.route('/wordcloud', methods=['POST'])
def featurize():
    n = 100   # number of articles per topic
    employer = request.form['user_input']
    ftopic = df[df['company']==employer].head(n)
    text = list(ftopic['cons'].values)
    text = " ".join(text)
    text = re.sub('[^\w\s]+', ' ', text).replace('\n', ' ')
   # tokenize into words
    tokens = [word.lower() for sent in sent_tokenize(text) \
             for word in word_tokenize(sent)]
   # remove stopwords

   # some extra stop words not present in stopwords
    stop = stopwords.words('english')
    stop += ['said', 'would', 's', 'also', 'U', 'mr', 're', 'may', 'one', 'two', 'buy', 'much', \
            'take', 'might', 'say', 'new', 'year', 'many','etc', 'll']
    stop += str(employer)

    tokens = [token for token in tokens if token not in stop]
   # remove words less than three letters
    tokens = [word for word in tokens if len(word) >= 2]
    string = " ".join(tokens)
    wordcloud = WordCloud(font_path='/Library/Fonts/Arial Rounded Bold.ttf').generate(string)
    plt.figure(figsize=(50,30))
    plt.imshow(wordcloud)
    plt.axis("off")
    name = 'static/' +str(employer) + '.png'
    pic = plt.savefig(name, bbox_inches='tight',transparent = True)

    return render_template('template_wordcloud.html', pic = name, employer=employer)

# def wordcloud():
    
#     # vectorizer_pros = TfidfVectorizer(ngram_range=(1, 2), stop_words='english', analyzer = 'word')

#     # df2 = df[df.company==employer]
#     # pros = df2['pros']
#     # vectorized_pros = vectorizer_pros.fit_transform(pros)
#     # sum_words_pros = np.sum(vectorized_pros.toarray(),axis=0)
#     # sort_pros = np.argsort(sum_words_pros)[::-1][0:40]
#     # list_pros = []
#     # for i in sort_pros:
#     #    list_pros.append(vectorizer_pros.get_feature_names()[i])
# return render_template('template_wordcloud.html', list_pros=list_pros, company=employer)    



# Once submit is hit, pass info into model, return results.
#================================================
@app.route('/predict', methods=['POST'])
def predict():

    # get data from request form
    data = request.form['user_input']

    # convert data from unicode to string
    data = str(data)

    # vectorize our new data
    features = tfidf.transform([data])

    # make prediction based on new data
    pred = model.classes_[np.argsort(model.predict_proba(features))]

    frame = pd.read_csv('data/glass_reviews.csv')
    frame['company'] = frame['_pageUrl'].apply(lambda x: x.split('/')[4].split('-Reviews')[0].replace('-',' '))
    # return a string format of that prediction to the html page

    # return "Here are the top ten companies by " + str.title(data) + ": " + str(pred[0][::-1][:10]) 

    return render_template('template_predict.html', title=str.title(data), 
        p1=str(pred[0][::-1][0]),
        p2=str(pred[0][::-1][1]),
        p3=str(pred[0][::-1][2]),
        p4=str(pred[0][::-1][3]),
        p5=str(pred[0][::-1][4]),
        p6=str(pred[0][::-1][5]),
        p7=str(pred[0][::-1][6]),
        p8=str(pred[0][::-1][7]),
        p9=str(pred[0][::-1][8]),
        p10=str(pred[0][::-1][9])
        )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
