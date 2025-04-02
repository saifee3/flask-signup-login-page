from flask import request, jsonify, render_template
from models import User, db

def init_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.get_json()
        if not all([data.get('username'), data.get('email'), data.get('password')]):
            return jsonify({"error": "All fields are required"}), 400
        if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
            return jsonify({"error": "Username or email already exists"}), 400

        user = User(username=data['username'], email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        if not all([data.get('email'), data.get('password')]):
            return jsonify({"error": "Email and password are required"}), 400
        user = User.query.filter_by(email=data['email'], password=data['password']).first()
        if not user:
            return jsonify({"error": "Invalid email or password"}), 400
        return jsonify({"message": "Login successful", "username": user.username}), 200
