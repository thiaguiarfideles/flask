from flask import Flask, jsonify
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
    cursor = cnxn.cursor()

    for row in cursor.execute("select PRODUTOS, NM_PRODUTO, CD_ESTOQUE, DS_ESTOQUE, DS_UNIDADE, QT_ESTOQUE, CD_MULTI_EMPRESA, DS_MULTI_EMPRESA from dbo.Estoque_prontonil"):PRODUTOS, NM_PRODUTO, CD_ESTOQUE, DS_ESTOQUE, DS_UNIDADE, QT_ESTOQUE, CD_MULTI_EMPRESA, DS_MULTI_EMPRESA = row
    rv = cursor.fetchall() 
    Estoque_prontonil =[PRODUTOS, NM_PRODUTO, CD_ESTOQUE, DS_ESTOQUE, DS_UNIDADE, QT_ESTOQUE, CD_MULTI_EMPRESA, DS_MULTI_EMPRESA]
    content = {}
    for result in rv:
          content = {'produtos': result['str(produtos)'], 'nm_produto': result['nm_produto'], 'cd_estoque': result['cd_estoque'], 'ds_estoque': result['ds_estoque'],  'ds_unidade': result['ds_unidade'],'ds_unidade': result['ds_unidade'],'qt_estoque': result['qt_estoque'], 'cd_multi_empresa': result['cd_multi_empresa'], 'ds_multi_empresa': result['ds_multi_empresa']}
          Estoque_prontonil.append(content)
          content = {}
    return jsonify (Estoque_prontonil)
         

     


if __name__ == '__main__':
    app.run(debug=True)
