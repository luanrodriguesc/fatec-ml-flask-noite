import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Analise de Seguro')

@app.route('/predicao', methods=['POST'])
def predicao():

  gp = float(request.form['gp'])
  pts = float(request.form['pts'])
  fg = float(request.form['fg'])
  ft = float(request.form['ft'])
  reb = float(request.form['reb'])
  ast = float(request.form['ast'])
  stl = float(request.form['stl'])
  blk = float(request.form['blk'])
  tov = float(request.form['tov'])

  predicao = model.predict([[gp, pts, fg, ft, reb, ast, stl, blk, tov]])
  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
