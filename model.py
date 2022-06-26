### IMPORTING THE DATA
from typing import Dict
import nltk

nltk.download("popular")

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


def normalize_csv(path):
    ### IMPORTING DATA SET
    all_data = pd.read_csv(path)

    ## PROCESSING THE DATA SET
    all_data = all_data[["q", "a"]]
    all_data = all_data.drop_duplicates(subset="q")
    all_data = all_data.dropna()

    return all_data


class Kira:
    all_data = normalize_csv("./data/dat2.csv")

    ## PROCESSING THE DATA
    stopwords_list = stopwords.words("english")
    lemmatizer = WordNetLemmatizer()

    def my_tokenizer(self, doc):
        words = word_tokenize(doc)

        pos_tags = pos_tag(words)

        non_stopwords = [w for w in pos_tags if not w[0].lower() in Kira.stopwords_list]

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

            lemmas.append(Kira.lemmatizer.lemmatize(w[0], pos))

        return lemmas

    tfidf_vectorizer = TfidfVectorizer(tokenizer=my_tokenizer)
    tfidf_matrix = tfidf_vectorizer.fit_transform(tuple(all_data["q"]))

    def ask_question(self, question):
        query_vect = Kira.tfidf_vectorizer.transform([question])
        similarity = cosine_similarity(query_vect, Kira.tfidf_matrix)
        max_similarity = np.argmax(similarity, axis=None)

        result = dict(
            question=question,
            question_closest=Kira.all_data.iloc[max_similarity]["q"],
            similarity="{:.2%}".format(similarity[0, max_similarity]),
            answer=Kira.all_data.iloc[max_similarity]["a"],
        )

        print("Your question:", question)
        print("Closest question found:", Kira.all_data.iloc[max_similarity]["q"])
        print("Similarity: {:.2%}".format(similarity[0, max_similarity]))
        print("Answer:", Kira.all_data.iloc[max_similarity]["a"])

        return result


# ask_question("CAN I APPLY FOR JOB IN INEURON?")
