from flask import Flask, render_template, request
import os
import re
import math
from collections import defaultdict

app = Flask(__name__)

DATA_DIR = "data"
STOPLIST = "stoplist.txt"


def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())


def load_stopwords():
    with open(os.path.join(DATA_DIR, STOPLIST)) as f:
        return set(line.strip() for line in f)


def create_index():
    stopwords = load_stopwords()
    docs = {}
    index = defaultdict(dict)
    df = defaultdict(int)

    doc_id = 0

    for file in os.listdir(DATA_DIR):
        if file == STOPLIST:
            continue

        path = os.path.join(DATA_DIR, file)
        if os.path.isfile(path):
            doc_id += 1
            docs[doc_id] = file

            with open(path) as f:
                words = tokenize(f.read())

            words = [w for w in words if w not in stopwords and w.startswith('c')]

            freq = defaultdict(int)
            for w in words:
                freq[w] += 1

            for w, count in freq.items():
                index[w][doc_id] = count
                df[w] += 1

    return docs, index, df


docs, index, df = create_index()
N = len(docs)


def search(query):
    words = tokenize(query)
    scores = defaultdict(float)
    detail = defaultdict(list)

    for w in words:
        if w not in index:
            continue

        idf = math.log(N / (1 + df[w]))

        for doc_id, tf in index[w].items():
            score = tf * idf
            scores[doc_id] += score

            detail[doc_id].append({
                "word": w,
                "tf": tf,
                "idf": round(idf, 3),
                "score": round(score, 3)
            })

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked, detail


def highlight(text, words):
    for w in words:
        text = re.sub(f"({w})", r"<mark>\1</mark>", text, flags=re.IGNORECASE)
    return text


@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    query = ""
    index_view = index

    if request.method == "POST":
        query = request.form["query"]
        ranked, detail = search(query)

        for doc_id, score in ranked:
            path = os.path.join(DATA_DIR, docs[doc_id])
            with open(path) as f:
                content = f.read()

            snippet = highlight(content[:200], tokenize(query))

            results.append({
                "doc": docs[doc_id],
                "score": round(score, 3),
                "detail": detail[doc_id],
                "content": snippet
            })

    return render_template("index.html",
                           results=results,
                           query=query,
                           index=index_view)


if __name__ == "__main__":
    app.run(debug=True)