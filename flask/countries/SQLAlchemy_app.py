from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Configurando a SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Criando o objeto SQLAlchemy
db = SQLAlchemy(app)

# Marshmallow para serialização e desserialização
ma = Marshmallow(app)

# Modelo para a tabela countries
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(100))
    capital = db.Column(db.String(100))

# Schema para o modelo Country
class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Country
        load_instance = True

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)

@app.route("/countries", methods=['GET'])
def get_countries():
    countries = Country.query.all()
    result = countries_schema.dump(countries)
    return jsonify(result), 200

@app.route("/countries", methods=['POST'])
def add_country():
    if request.is_json:
        country = request.get_json()
        new_country = Country(country_name=country['country_name'], capital=country['capital'])
        db.session.add(new_country)
        db.session.commit()
        return country_schema.dump(new_country), 201
    return {"error": "A requisição deve ser JSON"}, 415

@app.route("/countries/<int:id>", methods=['GET'])
def get_country(id):
    country = Country.query.get(id)
    if country is not None:
        return country_schema.dump(country), 200
    else:
        return {"error": "País não encontrado"}, 404

@app.route("/countries/<int:id>", methods=['PUT'])
def update_country(id):
    country = Country.query.get(id)
    if country is not None:
        if request.is_json:
            data = request.get_json()
            country.country_name = data['country_name']
            country.capital = data['capital']
            db.session.commit()
            return country_schema.dump(country), 200
        else:
            return {"error": "A requisição deve ser JSON"}, 415
    else:
        return {"error": "País não encontrado"}, 404

@app.route("/countries/<int:id>", methods=['DELETE'])
def delete_country(id):
    country = Country.query.get(id)
    if country is not None:
        db.session.delete(country)
        db.session.commit()
        return {"message": "País deletado com sucesso"}, 200
    else:
        return {"error": "País não encontrado"}, 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=8090)
