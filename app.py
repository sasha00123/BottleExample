import json

from bottle import route, run, request, template

from models import Book


@route("/create")
def create():
    return """
        <form action='/create' method='POST'>
            Title: <input type='text' name='title' /> 
            <input value='Создать!' type='submit' />
        </form> 
    """


@route("/create", method='POST')
def do_create():
    Book.create(title=request.forms.get('title'))
    return """The book was created! <br>
            <a href='/create'>Create more.</a> <br>
            <a href='/list'>Look all</a>"""


@route('/list')
def lst():
    books = Book.select()
    return template("""
            <ul>
                % for book in test:
                    <li>{{ book.title }}</li> 
                % end
            </ul>
    """, books=books)


run(host='localhost', port=80, debug=True)
