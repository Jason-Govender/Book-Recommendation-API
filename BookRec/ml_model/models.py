from django.db import models
import joblib
import json
import os

from django.conf import settings
BASE_DIR = settings.BASE_DIR
MODEL_DIR = os.path.join(BASE_DIR, "jupyter_export")


