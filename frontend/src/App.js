import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [books, setBooks] = useState([]);
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [search, setSearch] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/api/books/')
      .then(response => setBooks(response.data))
      .catch(error => console.error(error));
  }, []);

  const handleAddBook = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/books/', { title, author })
      .then(response => setBooks([...books, response.data]))
      .catch(error => console.error(error));
    setTitle('');
    setAuthor('');
  };

  const handleDeleteBook = (id) => {
    axios.delete(`http://localhost:8000/api/books/${id}/`)
      .then(() => setBooks(books.filter(book => book.id !== id)))
      .catch(error => console.error(error));
  };

  const handleSearch = (e) => {
    setSearch(e.target.value);
    axios.get(`http://localhost:8000/api/books/?author=${e.target.value}`)
      .then(response => setBooks(response.data))
      .catch(error => console.error(error));
  };

  return (
    <div>
      <h1>My Library</h1>
      <form onSubmit={handleAddBook}>
        <input type="text" value={title} onChange={e => setTitle(e.target.value)} placeholder="Title" required />
        <input type="text" value={author} onChange={e => setAuthor(e.target.value)} placeholder="Author" required />
        <button type="submit">Add Book</button>
      </form>
      <input type="text" value={search} onChange={handleSearch} placeholder="Search by author" />
      <ul>
        {books.map(book => (
          <li key={book.id}>
            {book.title} by {book.author}
            <button onClick={() => handleDeleteBook(book.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
