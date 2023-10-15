from flask import Flask, request, jsonify
app = Flask(__name__)

books_list = [
  {
    "id": 0,
    "author": "Chinua Achebe",
    "language": "English",
    "title": "Things Fall Apart",
  },
  {
    "id": 1,
    "author": "Hans Christian Andersen",
    "language": "Danish",
    "title": "Fairy tales",
  },
  {
    "id": 2,
    "author": "Samuel Beckett",
    "language": "French, English",
    "title": "Molloy, Malone Dies, The Unnamable, the triology",
  },
  {
    "id": 3,
    "author": "Giovanni Boccaccio",
    "language": "Italian",
    "title": "The Decameron",
  },
  {
    "id": 4,
    "author": "Jorge Luis Borges",
    "language": "Spanish",
    "title": "Ficciones",
  },
  {
    "id": 5,
    "author": "Emily Bront",
    "language": "English",
    "title": "Wuthering Heights",
  },
]

@app.route('/books', methods=['GET'])
def get_books():
  if len(books_list) > 0:
      return jsonify(books_list)
  else:
    return 'Nothing Found', 404
  
@app.route('/books', methods=['POST'])
def create_book():
  new_author = request.form['author']
  new_lang = request.form['language']
  new_title = request.form['title']
  iD = books_list[-1]['id']+1

  new_book = {
    'id': iD,
    'author': new_author,
    'language': new_lang,
    'title': new_title,
  }

  books_list.append(new_book)

  return jsonify(books_list), 201

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
  for book in books_list:
    if book['id'] == id:
      return jsonify(book)

  return 'Nothing Found', 404
    
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
  for book in books_list:
    if book['id'] == id:
      book['author'] = request.form['author']
      book['language'] = request.form['language']
      book['title'] = request.form['title']
      updated_book = {
        'id': book['id'],
        'author': book['author'],
        'language': book['language'],
        'title': book['title'],
      }

      return jsonify(updated_book)

  return 'Nothing Found', 404
    

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
  for index, book in enumerate(books_list):
    if book['id'] == id:
      books_list.pop(index)
      return jsonify(books_list)

  return 'Nothing Found', 404

if __name__ == '__main__':
  app.run()