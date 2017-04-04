from flask import Flask, jsonify, request
app = Flask(__name__)

countries = [{'name' : 'Singapore'},
             {'name' : 'Malaysia'},
             {'name' : 'Thailand'}
             #Creating a list of array

@app.route('/', methods=['GET'])
             def test():
             return jsonify({'countries' : countries})

@app.route('/countries/<string:name>', methods={['GET'])
             def returnOne(name):
             countries = [countries for countries in countries if countries['name'] == name]
             return jsonify({'countries' : countries[0]})
             
@app.route('/countries', methods=['POST'])
             def addOne():
             countries = {'name' : request.json['name']}
             
             countries.append(countries)
             return jsonify({'countries' : countries})
             #return value countries with the value of countries
             #POST request (BODY SECTION: create a new value
                                        #{'name' : "Korea"}

@app.route('/countries/<string:name>', methods={['PUT'])
             def editOne(name):
             countries = [countries for countries in countries if countries['name'] == name]
             countries[0]['name'] = request.json['name']
             return jsonify({'countries' : countries[0]})
             #return json version of the dictionary
             #PUT request url/countries/Thailand
             #{'name' : "Japan"}

             
@app.route('/countries/<string:name>', methods={['DELETE'])
             def removeOne(name):
             countries = [countries for countries in countries if countries['name'] == name]
             countries.remove(countres[0])
             return jsonify({'countries' : countries[0]})
             #DELETE request
             #url/countries/Malaysia

if __name__ == '__main__':
             app.run(debug=True, port=8080)
             #run app on port 8080 in debug mode
