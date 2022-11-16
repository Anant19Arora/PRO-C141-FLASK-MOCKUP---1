from flask import Flask, jsonify, request
import csv

total_articles = []

total_articles_data = pd.read_csv('article.csv')

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": total_articles[0],
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = total_articles[0]
    liked_articles.append(article)
    total_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = total_articles[0]
    not_liked_articles.append(article)
    total_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()