from django.shortcuts import render
import pickle
from nltk.corpus import stopwords
import string
from nltk.stem import WordNetLemmatizer



def runserver(request):
    return render(request, "tweet.html")


def prepare(a):
    s=""
    l=[]
    lemmatizer = WordNetLemmatizer()
    stop = stopwords.words('english')
    for i in a.lower().split(" "):
        s=""
        for j in i:
            if j not in string.punctuation:
                s=s+j
        if s!="" and s not in stop and s.isalpha() and s!="user":
            l.append(lemmatizer.lemmatize(s,"v"))
    return(" ".join(l))



def gettweet(request):
    tweet=request.GET['text1']
    s = prepare(tweet)
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(r'C:\\Users\\hp\\' + filename, 'rb'))
    result = loaded_model.predict_proba([s])[:,1]
    if result >= .3:
        msg='Negative'
        row1='dislike'
    else:
        msg="Positive"
        row1='like'
    return render(request, "reply.html",{'row':'Your Tweet  : {}'.format(tweet) ,'row1':row1,'msg1':msg})