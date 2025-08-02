# 📚 Book Recommendation API

## 1. Overview
A Django REST API for managing a personal book library and getting machine‑learning‑based recommendations.  
Users can add books, rate them, search, and get tailored recommendations powered by a KMeans clustering model trained on 5,000 users.
The repository for the Machine-Learning Model can be found here: https://github.com/Jason-Govender/ML-Book-Recommender

---

## 2. Features
- ➕ **Add a book**
- ❌ **Remove a book**
- 🔍 **Search for books**
- ⭐ **Rate a book**
- 🗑 **Remove a rating**
- 📄 **List all books**
- 📊 **List all ratings**
- 🤖 **Recommend books** based on similar users’ reading patterns

---

## 3. Tech Stack
- **Backend**: Django REST Framework
- **Database**: SQLite
- **Machine Learning**: scikit‑learn (KMeans clustering, StandardScaler)
- **Language**: Python 3.13
- 
## 4. API Endpoints

| Method   | Endpoint                     | Description                       |
|----------|------------------------------|-----------------------------------|
| **POST** | `/books/add/`                | Add a new book                    |
| **GET**  | `/books/`                    | List all books                    |
| **DELETE** | `/books/<pk>/`             | Remove a specific book            |
| **GET**  | `/books/search/?q=<term>`    | Search for books                  |
| **POST** | `/ratings/add/`              | Add a rating                      |
| **DELETE** | `/ratings/<pk>/`           | Remove a rating                   |
| **GET**  | `/ratings/`                  | List all ratings                  |
| **GET**  | `/recommend/`                | Get book recommendations          |

## 6. Machine Learning

- **Algorithm**: KMeans clustering
- **Clusters**: 50
- **Dataset**: 5,000 users
- **Preprocessing**: StandardScaler for feature normalization
- **Logic**: 
  - Assigns each user to a cluster based on their ratings.
  - Recommendations are drawn from the top‑rated books in the user’s cluster.
  

