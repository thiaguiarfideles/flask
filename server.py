from flask import Flask, jsonify
# from requests import Response
import pyodbc
import json
app = Flask(__name__)

@app.route('/',methods=['GET'])
def table():
    server = 'DESKTOP-10BH6IJ' 
    database = 'master' 
    username = 'sa' 
    password = 'masterkey' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    resultado =[]
    cursor = cnxn.cursor()

    ## você sabe o que isso aqui faz? isso ai roda a query do sql server 
    ## não, faz mais que isso rodar a query é só cursor.execute, então pode tirar 
    #pois é né


    # for row in cursor.execute("select PRODUTOS, NM_PRODUTO, CD_ESTOQUE, DS_ESTOQUE, DS_UNIDADE, QT_ESTOQUE, CD_MULTI_EMPRESA, DS_MULTI_EMPRESA from dbo.Estoque_prontonil"):PRODUTOS, NM_PRODUTO, CD_ESTOQUE, DS_ESTOQUE, DS_UNIDADE, QT_ESTOQUE, CD_MULTI_EMPRESA, DS_MULTI_EMPRESA = row
        # resultado.append(row)
    cursor.execute("select PRODUTOS, NM_PRODUTO, CD_ESTOQUE, DS_ESTOQUE, DS_UNIDADE, QT_ESTOQUE, CD_MULTI_EMPRESA, DS_MULTI_EMPRESA from dbo.Estoque_prontonil WITH(NOLOCK)")
    
    rv = cursor.fetchall() 

    Estoque_prontonil =[]

    for result in rv:
          # content = {'produtos': result[0], 'nm_produto': result['nm_produto'], 'cd_estoque': result['cd_estoque'], 'ds_estoque': result['ds_estoque'],  'ds_unidade': result['ds_unidade'],'ds_unidade': result['ds_unidade'],'qt_estoque': result['qt_estoque'], 'cd_multi_empresa': result['cd_multi_empresa'], 'ds_multi_empresa': result['ds_multi_empresa']}}
          content = {'produtos': result[0], 'nm_produto': result[1], 'cd_estoque': result[2], 'ds_estoque': result[3],  'ds_unidade': result[4],'qt_estoque': result[5], 'cd_multi_empresa': result[6], 'ds_multi_empresa': result[7]}
          # 
          Estoque_prontonil.append(content)
          content = {}
    return jsonify(prontonil=Estoque_prontonil)

if __name__ == '__main__':
    app.run(debug=True)
