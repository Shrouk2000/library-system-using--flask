from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from app.models import Book
from app.forms import BookForm
import os
from werkzeug.utils import secure_filename

bp = Blueprint('main', __name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')

@bp.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@bp.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_detail.html', book=book)

@bp.route('/create', methods=['GET', 'POST'])
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        if form.cover_photo.data:
            filename = secure_filename(form.cover_photo.data.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            form.cover_photo.data.save(filepath)
        else:
            filename = None
        
        new_book = Book(
            title=form.title.data,
            cover_photo=filename,
            number_of_pages=form.number_of_pages.data,
            description=form.description.data
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('book_form.html', form=form)

@bp.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        if form.cover_photo.data:
            filename = secure_filename(form.cover_photo.data.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            form.cover_photo.data.save(filepath)
        else:
            filename = book.cover_photo
        
        book.title = form.title.data
        book.cover_photo = filename
        book.number_of_pages = form.number_of_pages.data
        book.description = form.description.data
        db.session.commit()
        return redirect(url_for('main.book_detail', book_id=book.id))
    return render_template('book_form.html', form=form)

@bp.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('main.index'))
