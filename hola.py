from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def url_principal():
	return render_template("templates.html")


@app.route("/music")
def music():
	return render_template("musica.html")

@app.route("/pasatiempo")
def pasatiempo():
	return render_template("pasatiempos.html")

@app.route("/cachos")
def cachos():
	return render_template("cachos.html")

@app.route("/contacto")
def contacto():
	return render_template("cont.html")
	

if __name__ == "__main__":
		app.run(debug=True)