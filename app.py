import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Análise de Seguro')

@app.route('/predicao', methods=['POST'])
def predicao():

  AGE = request.form['AGE']
  GENDER = request.form['GENDER']
  DRIVING_EXPERIENCE = request.form['DRIVING_EXPERIENCE']
  INCOME = request.form['INCOME']
  VEHICLE_YEAR = request.form['VEHICLE_YEAR']

  array=[[str(AGE), str(GENDER), str(DRIVING_EXPERIENCE), str(INCOME), str(VEHICLE_YEAR)]]

  predicao = model.predict(array)

  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
