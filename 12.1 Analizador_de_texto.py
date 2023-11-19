from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    texto = ""
    letras = ["", "", ""]
    cantidad_letras = [0, 0, 0]
    cantidad_palabras = 0
    letra_inicio = ""
    letra_final = ""
    texto_invertido = ""
    buscar_python = False

    if request.method == 'POST':
        texto = request.form['texto']
        letras = [
            request.form['letra1'].lower(),
            request.form['letra2'].lower(),
            request.form['letra3'].lower()
        ]

        cantidad_letras = [texto.count(letra) for letra in letras]

        palabras = texto.split()
        cantidad_palabras = len(palabras)

        letra_inicio = texto[0] if texto else ""
        letra_final = texto[-1] if texto else ""

        palabras.reverse()
        texto_invertido = ' '.join(palabras)

        buscar_python = 'python' in texto

    return render_template('index.html',
                           texto=texto,
                           letras=letras,
                           cantidad_letras=cantidad_letras,
                           cantidad_palabras=cantidad_palabras,
                           letra_inicio=letra_inicio,
                           letra_final=letra_final,
                           texto_invertido=texto_invertido,
                           buscar_python=buscar_python)

if __name__ == '__main__':
    app.run(debug=False)
