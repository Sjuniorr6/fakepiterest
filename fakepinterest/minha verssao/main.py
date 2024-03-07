from flask import Flask ,render_template, url_for

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('homepage.html')

@app.route('/perfil/<usuario')
def perfil(usuario):
    return render_template('perfil.html', usuario = usuario)

if __name__ == "__main__":
    app.run(debug=True)