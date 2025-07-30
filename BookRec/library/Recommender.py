import joblib
import json
import os
import random
import pandas as pd
from serializer import BookMetaSerializer
from .models import Rating_Data, Book_Meta
from rest_framework.response import Response

from django.conf import settings
BASE_DIR = settings.BASE_DIR
MODEL_DIR = os.path.join(BASE_DIR, "jupyter_export")
model = joblib.load(os.path.join(MODEL_DIR, "kmeans_model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
with open(os.path.join(MODEL_DIR, "cluster_book_map.json")) as f:
    top_books = json.load(f)

def find_cluster(request):
    ratings = Rating_Data.objects.filter(user_id=int(request.session["user_id"]))
    ratings_df = pd.DataFrame(list(ratings.values()))
    user_item_matrix = ratings_df.pivot_table(index="user_id", columns="book_id", values="rating").fillna(0)
    scaled_ratings = scaler(user_item_matrix)
    cluster = model.predict(scaled_ratings)[0]
    return cluster

def recommend(request):
    cluster = find_cluster(request)
    choice = random.choice(top_books.get(cluster))
    book = Book_Meta.objects.filter(book_id=int(choice.book_id)).first()
    serializer = BookMetaSerializer(book)
    return Response(serializer.data)







