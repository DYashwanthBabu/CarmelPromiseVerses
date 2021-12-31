from flask import Flask
from flask import request
from flask import render_template, jsonify
import pandas as pd
import random

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

    return render_template('Home.html')

@app.route("/promise_verse", methods=['GET', 'POST'])
def promise_verse():
    # allStock = pd.read_csv('NIFTY50_all.csv')
    # stock_symbols=allStock.Symbol.unique()
    if(request.method =='POST'):
        filename = request.form
        namesList = []
        valuesList = []
        counter = 0
        df = pd.read_csv("let.csv")
        for i in filename.keys():
            counter +=1
            ranNum = random.randint(0,171)
            li = df.loc[ranNum].tolist()
            verse = li[0] + ": "+li[1] 
            namesList.append(filename[i])
            valuesList.append(verse)
        return render_template('PromiseVerse.html', key=namesList, val=valuesList, count =counter)

    return render_template('NPromiseVerse.html')

if __name__ == '__main__':
    app.run(debug=True)