from flask import Flask, render_template, request, redirect

app = Flask(__name__)

militares = [
    {"numero":"201","nome":"Moreira","cafe":1,"almoco":1,"janta":1},
    {"numero":"207","nome":"Ferreira","cafe":0,"almoco":1,"janta":0},
    {"numero":"211","nome":"De Almeida","cafe":1,"almoco":1,"janta":1},
    {"numero":"217","nome":"Muniz","cafe":1,"almoco":1,"janta":1},
    {"numero":"220","nome":"Moser","cafe":0,"almoco":1,"janta":1},
]

@app.route("/")
def inicio():
    return render_template("index.html", militares=militares)


@app.route("/adicionar", methods=["POST"])
def adicionar():

    militar = {
        "numero": request.form["numero"],
        "nome": request.form["nome"],
        "cafe": 1 if "cafe" in request.form else 0,
        "almoco": 1 if "almoco" in request.form else 0,
        "janta": 1 if "janta" in request.form else 0
    }

    militares.append(militar)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
