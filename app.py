from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello World! 🚀 - Auto deployed via GitHub Actions!",
        "status": "success",
        "environment": os.getenv('ENVIRONMENT', 'development')
    })
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/users')
def get_users():
    # 간단한 더미 데이터
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8003))
    app.run(host='0.0.0.0', port=port, debug=False)