### IMPORTING THE DATA
import nltk

nltk.download("popular")

from utils.getDataSets import getDataSets

import pandas as pd
import numpy as np
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

light = "light"
medium = "medium"
heavy = "heavy"


def normalize_csv(path):
    ### IMPORTING DATA SET
    all_data = pd.read_csv(path)

    ## PROCESSING THE DATA SET
    all_data = all_data[["q", "a"]]
    all_data = all_data.drop_duplicates(subset="q")
    all_data = all_data.dropna()

    return all_data


all_data = normalize_csv(getDataSets(light))

## PROCESSING THE DATA
stopwords_list = stopwords.words("english")
lemmatizer = WordNetLemmatizer()


def my_tokenizer(doc):
    words = word_tokenize(doc)

    pos_tags = pos_tag(words)

    non_stopwords = [w for w in pos_tags if not w[0].lower() in stopwords_list]

    non_punctuation = [w for w in non_stopwords if not w[0] in string.punctuation]

    lemmas = []
    for w in non_punctuation:
        if w[1].startswith("J"):
            pos = wordnet.ADJ
        elif w[1].startswith("V"):
            pos = wordnet.VERB
        elif w[1].startswith("N"):
            pos = wordnet.NOUN
        elif w[1].startswith("R"):
            pos = wordnet.ADV
        else:
            pos = wordnet.NOUN

        lemmas.append(lemmatizer.lemmatize(w[0], pos))

    return lemmas


tfidf_vectorizer = TfidfVectorizer(tokenizer=my_tokenizer)
tfidf_matrix = tfidf_vectorizer.fit_transform(tuple(all_data["q"]))

# tfidf_vectorizer = pickle.load(open("./data/tfidf_vectorizer.pkl", "rb"))
# tfidf_matrix = pickle.load(open("./data/tfidf_matrix.pkl", "rb"))

print("🚀🚀🚀")


def ask_question(question):
    query_vect = tfidf_vectorizer.transform([question])
    similarity = cosine_similarity(query_vect, tfidf_matrix)
    max_similarity = np.argmax(similarity, axis=None)

    result = dict(
        question=question,
        question_closest=all_data.iloc[max_similarity]["q"],
        similarity="{:.2%}".format(similarity[0, max_similarity]),
        answer=all_data.iloc[max_similarity]["a"],
    )

    print("Your question:", question)
    print("Closest question found:", all_data.iloc[max_similarity]["q"])
    print("Similarity: {:.2%}".format(similarity[0, max_similarity]))
    print("Answer:", all_data.iloc[max_similarity]["a"])

    return result


# ask_question("CAN I APPLY FOR JOB IN INEURON?")
