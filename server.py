from flask import Flask, jsonify, simplejson
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

    cursor.execute("select * from dbo.Estoque_prontonil") 
    row = cursor.fetchone() 
    html= '<table border="1" style="width:50%"><tr><th>PRODUTOS</th><th>NM_PRODUTO</th><th>CD_ESTOQUE</th><th>DS_ESTOQUE</th><th>DS_UNIDADE</th><th>QT_ESTOQUE</th><th>CD_MULTI_EMPRESA</th><th>DS_MULTI_EMPRESA</th></tr>'
    while row: 
        html += '<tr><td>'+str(row.PRODUTOS)+'</td><td>'+str(row.NM_PRODUTO)+'</td><td>'+str(row.CD_ESTOQUE)+'</td><td>'+str(row.DS_ESTOQUE)+'</td><td>'+str(row.DS_UNIDADE)+'</td><td>'+str(row.QT_ESTOQUE)+'</td><td>'+str(row.CD_MULTI_EMPRESA)+'</td><td>'+str(row.DS_MULTI_EMPRESA)+'</td></tr>'
        row = cursor.fetchone()
    html+= '</table>'
    return = PCT.objects.filter(code__startswith='a').values('PRODUTOS', 'NM_PRODUTO')
return JsonResponse({'results': list(results)})


if __name__ == '__main__':
    app.run(debug=True)