from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Crie um DataFrame de exemplo
dados = pd.read_csv('Dados/df_score_bairros.csv')

# Endpoint para retornar a idade com base no nome
@app.route('/<bairro>', methods=['GET'])
def info_por_bairro(bairro):
    # Filtra as linhas do DataFrame onde o nome do bairro corresponde ao valor especificado
    filtro_bairro = dados[dados['BAIRRO'] == bairro]
    
    if not filtro_bairro.empty:
        regiao = filtro_bairro.iloc[0]['REGIÃO']
        total = int(filtro_bairro.iloc[0]['TOTAL'])
        furtos = int(filtro_bairro.iloc[0]['FURTOS'])
        lesao = int(filtro_bairro.iloc[0]['LESAO'])
        roubos = int(filtro_bairro.iloc[0]['ROUBOS'])
        acidente_transito = int(filtro_bairro.iloc[0]['ACIDENTES_TRANSITO'])
        estupro = int(filtro_bairro.iloc[0]['ESTUPRO'])
        homicidio = int(filtro_bairro.iloc[0]['HOMICIDIO'])
        tent_homicidio = int(filtro_bairro.iloc[0]['TENT_HOMICIDIO'])
        
        # Filtra as linhas do DataFrame onde a região é a mesma, excluindo o bairro atual
        filtro_regiao = dados[(dados['REGIÃO'] == regiao) & (dados['BAIRRO'] != bairro)]
        
        # Encontra os dois bairros com o menor total na mesma região
        bairros_menor_total = filtro_regiao.nlargest(2, 'TOTAL')
        
        # Converte os resultados para um formato JSON
        resultado1 = {
            'Total': total,
            'Regiao': regiao,
            'BAIRRO': bairro,
            'ocorrencias': {
                'Furtos': furtos,
                'Lesao': lesao,
                'Roubos': roubos,
                'Acidente Transito' : acidente_transito,
                'Estupro': estupro,
                'Homicidio': homicidio,
                'Tentativa Homicidio': tent_homicidio 
            }
        }
        resultado2 = {
            'Bairros com MAIOR indice de segurança': bairros_menor_total[['BAIRRO', 'TOTAL']].to_dict(orient='records')
        }
        return jsonify(resultado1,resultado2)
    else:
        return jsonify({'erro': 'BAIRRO não encontrado'})

if __name__ == '__main__':
    app.run(debug=True)
