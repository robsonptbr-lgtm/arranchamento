from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def conectar():
    banco = sqlite3.connect("arranchamento.db")
    banco.row_factory = sqlite3.Row
    return banco


def criar_banco():
    banco = conectar()

    banco.execute("""
    CREATE TABLE IF NOT EXISTS militares (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero TEXT,
        nome TEXT,
        dia TEXT,
        cafe INTEGER,
        almoco INTEGER,
        janta INTEGER
    )
    """)

    banco.commit()
    banco.close()


@app.route("/")
def inicio():

    banco = conectar()

    militares = banco.execute(
        "SELECT * FROM militares"
    ).fetchall()

    banco.close()

    return render_template(
        "index.html",
        militares=militares
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():

    banco = conectar()

    banco.execute("""
    INSERT INTO militares
    (numero, nome, dia, cafe, almoco, janta)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        request.form["numero"],
        request.form["nome"],
        request.form["dia"],
        1 if "cafe" in request.form else 0,
        1 if "almoco" in request.form else 0,
        1 if "janta" in request.form else 0
    ))

    banco.commit()
    banco.close()

    return redirect("/")


@app.route("/excluir/<int:id>")
def excluir(id):

    banco = conectar()

    banco.execute(
        "DELETE FROM militares WHERE id=?",
        (id,)
    )

    banco.commit()
    banco.close()

    return redirect("/")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    banco = conectar()

    if request.method == "POST":

        banco.execute("""
        UPDATE militares SET
        numero=?,
        nome=?,
        dia=?,
        cafe=?,
        almoco=?,
        janta=?
        WHERE id=?
        """,
        (
            request.form["numero"],
            request.form["nome"],
            request.form["dia"],
            1 if "cafe" in request.form else 0,
            1 if "almoco" in request.form else 0,
            1 if "janta" in request.form else 0,
            id
        ))

        banco.commit()
        banco.close()

        return redirect("/")


    militar = banco.execute(
        "SELECT * FROM militares WHERE id=?",
        (id,)
    ).fetchone()

    banco.close()

    return render_template(
        "editar.html",
        militar=militar
    )


criar_banco()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )