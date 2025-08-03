import joblib
import json
import os
import random
import pandas as pd
from sklearn.preprocessing import StandardScaler
from .serializer import BookMetaSerializer
from .models import Rating_Data, Book_Meta
from rest_framework.response import Response
from django.conf import settings
#The internal logic for the Recommendation function

#Loaded the external model, scaler, best books in a cluster and column structure.
BASE_DIR = settings.BASE_DIR
MODEL_DIR = os.path.join(BASE_DIR, "jupyter_export")
model = joblib.load(os.path.join(MODEL_DIR, "kmeans_model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
book_columns = joblib.load(os.path.join(MODEL_DIR, "book_columns.pkl"))
with open(os.path.join(MODEL_DIR, "cluster_book_map.json")) as f:
    top_books = json.load(f)

#Normalizes the users rating database and sends the matrix to the model.
def find_cluster():
    ratings = Rating_Data.objects.all()
    ratings_df = pd.DataFrame(list(ratings.values()))
    user_item_matrix = ratings_df.pivot_table(index="user_id", columns="book_id", values="rating").fillna(0)
    user_item_matrix = user_item_matrix.reindex(columns=book_columns, fill_value=0)
    scaled_ratings = scaler.transform(user_item_matrix)
    cluster = model.predict(scaled_ratings)[0]
    return cluster

#Gets the user's cluster and return a randomly selected list from the best books
#In that cluster
def recommend():
    cluster = str(find_cluster())
    books_in_cluster = top_books.get(cluster, [])
    choices = random.sample(books_in_cluster, min(len(books_in_cluster), 5))
    books = Book_Meta.objects.filter(
        book_id__in=[int(c) for c in choices]
    )
    return books







