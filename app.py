"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, redirect, jsonify
from models import db, connect_db, Cupcake


app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Halo03117!@localhost:5432/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)


app.config['SECRET_KEY'] = 'cats'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/api/cupcakes')
def list_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupcakes)

@app.route('/api/cupcakes', methods = ["POST"])
def create_cupcakes():
    new_cupcake = Cupcake(
        flavor = request.json["flavor"],
        size = request.json["size"],
        rating = request.json["rating"],
        image = request.json["image"]
    )
    db.session.add(new_cupcake)
    db.session.commit()
    res_json = jsonify(cupcake = new_cupcake.serialize())
    return (res_json, 201)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake.serialize())



