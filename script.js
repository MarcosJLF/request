let url = 'http://127.0.0.1:5000/books';

fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });