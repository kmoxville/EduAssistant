from flask import  render_template, request, redirect, url_for, flash, session
import sqlite3 as sql
from login import app, login_required
from src.database.db_model import db

@app.route("/")
@app.route("/index")
@login_required
def index():
    con = sql.connect(db)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from questions where id<>1")
    data = cur.fetchall()
    return render_template("index.html", datas=data)


@app.route("/add_question", methods=['POST', 'GET'])
@login_required
def add_question():
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        key_words = request.form['key_words']
        con = sql.connect(db)
        cur = con.cursor()
        cur.execute(f"insert into questions(question,answer, key_words) values (?,?, ?)",
                    (question, answer, key_words))
        con.commit()
        flash('question added', 'success')
        return redirect(url_for("index"))
    return render_template("add_question.html")


@app.route("/edit_question/<string:id>", methods=['POST', 'GET'])
@login_required
def edit_question(id):
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        key_words = request.form['key_words']
        con = sql.connect(db)
        cur = con.cursor()
        cur.execute(
            "update questions set question=?,answer=?, key_words=? where id=?", (question, answer, key_words,id))
        con.commit()
        flash('question updated', 'success')
        return redirect(url_for("index"))
    con = sql.connect(db)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from questions where id=?", (id,))
    data = cur.fetchone()
    return render_template("edit_question.html", datas=data)


@app.route("/delete_question/<string:id>", methods=['GET'])
@login_required
def delete_question(id):
    con = sql.connect(db)
    cur = con.cursor()
    cur.execute("delete from questions where id=?", (id,))
    con.commit()
    flash('question deleted', 'warning')
    return redirect(url_for("index"))


@app.route("/menu")
@login_required
def menu():
    con = sql.connect(db)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("""select a.id as id,
    m.name as name, 
    m.url as url, 
    a.answer as answer 
    from menu as m 
    join answers as a on a.menu_id=m.id  
    join users as u on u.id=a.author_id """)
    data = cur.fetchall()
    return render_template("menu.html", datas=data)


@app.route("/delete_menu/<string:id>", methods=['GET'])
@login_required
def delete_menu(id):
    con = sql.connect(db)
    cur = con.cursor()
    cur.execute("delete from answers where id=?", (id,))
    con.commit()
    cur.execute("delete from menu where id=?", (id,))
    con.commit()
    flash('menu deleted', 'warning')
    return redirect(url_for("menu"))


@app.route("/edit_menu/<string:id>", methods=['POST', 'GET'])
@login_required
def edit_menu(id):
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        answer = request.form['answer']
        con = sql.connect(db)
        cur = con.cursor()
        cur.execute("update menu set name=?,url=? where id=?", (name, url, id))
        con.commit()
        cur.execute("update answers set answer=? where id=?", (answer, id))
        con.commit()
        flash('menu updated', 'success')
        return redirect(url_for("menu"))
    con = sql.connect(db)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("""select a.id as id,
    m.name as name, 
    m.url as url, 
    a.answer as answer 
    from menu as m 
    join answers as a on a.menu_id=m.id  
    join users as u on u.id=a.author_id  where a.id=? """, (id,))
    data = cur.fetchone()
    return render_template("edit_menu.html", datas=data)


@app.route("/add_menu", methods=['POST', 'GET'])
@login_required
def add_menu():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        answer = request.form['answer']
        con = sql.connect(db)
        cur = con.cursor()
        cur.execute(f"insert into menu(name,url) values (?,?)", (name, url))
        con.commit()
        cur.execute("""select max(id) from menu""")
        max_id = cur.fetchone()
        print(max_id[0])
        cur.execute(f"insert into answers (menu_id,author_id,answer) values (?,?,?)", (max_id[0], 1, answer))
        con.commit()

        flash('menu added', 'success')
        return redirect(url_for("menu"))
    return render_template("add_menu.html")


if __name__ == '__main__':
    app.secret_key = 'zzzzz1221'
    app.run(debug=True)
