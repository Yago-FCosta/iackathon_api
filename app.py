from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Crie um DataFrame de exemplo
dados = pd.read_csv('df_score_bairros.csv')

dados= dados.sort_values(by = 'BAIRRO')

# Endpoint para retornar a idade com base no nome
@app.route('/', methods=['GET'])
def mostrar_tabela():
    # Converte o DataFrame em uma lista de dicionários
    dados_dict = dados.to_dict(orient='records')
    
    # Retorna os dados em JSON
    return jsonify(dados_dict)

if __name__ == '__main__':
    app.run(debug=True)
