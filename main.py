from flask import Flask,jsonify,request
import csv

all_articles=[]
with open("articles.csv",encoding='utf-8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]

liked_articles=[]
not_liked_articles=[]

app=Flask(__name__)

@app.route('/get-articles')

def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":'success'
    })

@app.route('/liked-articles',methods=['POST'])

def liked_article():
    global all_articles
    movie=all_articles[3]
    all_articles=all_articles[1:]
    liked_articles.append(movie)
    return jsonify({
        "data":liked_articles,
        "status":"success"
    }),200


@app.route('/not-liked-articles',methods=['POST'])

def not_liked_article():
    global all_articles
    movie=all_articles[6]
    all_articles=all_articles[1:]
    not_liked_articles.append(movie)
    return jsonify({
        "data":not_liked_articles,
        "status":"success"
    }),200



if __name__=='__main__':
    app.run(debug=True)    