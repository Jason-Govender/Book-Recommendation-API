import joblib
import json
import os

from django.conf import settings
BASE_DIR = settings.BASE_DIR
MODEL_DIR = os.path.join(BASE_DIR, "jupyter_export")
model = joblib.load(os.path.join(MODEL_DIR, "kmeans_model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
with open(os.path.join(MODEL_DIR, "cluster_book_map.json")) as f:
    top_books = json.load(f)
