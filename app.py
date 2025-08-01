from flask import Flask, request, render_template
import openai
from mn_api_adapter import consultar_expedientes  # Este archivo debes crearlo

app = Flask(__name__)

# Configura tu clave de OpenAI aquí
openai.api_key = "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"  # Reemplaza con tu clave real

@app.route('/', methods=['GET', 'POST'])
def chat():
    respuesta = None
    if request.method == 'POST':
        mensaje = request.form['mensaje']

        # Detecta si es una consulta a MNprogram
        if "expedientes" in mensaje.lower():
            respuesta = consultar_expedientes()
        else:
            # Usa la IA de OpenAI si no es una palabra clave de MNprogram
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un asistente legal conectado a MNprogram."},
                    {"role": "user", "content": mensaje}
                ]
            )
            respuesta = completion.choices[0].message.content

    return render_template('chat.html', respuesta=respuesta)

if __name__ == '__main__':
    app.run(debug=True)