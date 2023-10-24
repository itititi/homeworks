from datetime import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///advertisements.db'
db = SQLAlchemy(app)


class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    owner = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Advertisement {self.title}>'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'


@app.route('/advertisement/<int:id>', methods=['GET'])
def get_advertisement(id):
    advertisement = Advertisement.query.get(id)
    if advertisement is None:
        return jsonify({'error': 'Advertisement not found'}), 404
    return jsonify({
        'id': advertisement.id,
        'title': advertisement.title,
        'description': advertisement.description,
        'created_date': advertisement.created_date,
        'owner': advertisement.owner
    }), 200


@app.route('/advertisement', methods=['POST'])
def create_advertisement():
    title = request.json.get('title')
    description = request.json.get('description')
    owner = request.json.get('owner')

    if not title or not description or not owner:
        return jsonify({'error': 'Missing required parameters'}), 400

    advertisement = Advertisement(title=title, description=description, owner=owner)
    db.session.add(advertisement)
    db.session.commit()

    return jsonify({
        'id': advertisement.id,
        'title': advertisement.title,
        'description': advertisement.description,
        'created_date': advertisement.created_date,
        'owner': advertisement.owner
    }), 201


@app.route('/advertisement/<int:id>', methods=['DELETE'])
def delete_advertisement(id):
    advertisement = Advertisement.query.get(id)
    if advertisement is None:
        return jsonify({'error': 'Advertisement not found'}), 404
    db.session.delete(advertisement)
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)