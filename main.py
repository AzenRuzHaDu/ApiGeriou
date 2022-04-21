from flask import Flask
import pandas as pd


app = Flask(__name__)

@app.route("/api/<name>", methods=['GET'])

def getCity(name):
    print(name)
    data = pd.read_csv('data_base.csv', index_col='fra')
    dic = data.loc[name, 'bre']
    print(dic)
    return {'nom breton': dic}, 200

if __name__ == '__main__' :
    app.run(debug=True)
    print('api start')