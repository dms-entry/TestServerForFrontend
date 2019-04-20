from flask import Flask, request, abort, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app, resources={r"/api/*": {"origins": "*"}})

users = []
posts = [{'title': "아무개", "content": "김재훈"}]


@app.route('/api/signup', methods=['POST'])
def sign_up():
    data = request.json
    id = data['id']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']

    if data:
        users.append({
            'id': id,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        })
        return Response('회원가입 성공', 201)
    else:
        abort(400)


@app.route('/api/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.json
        id = data['id']
        password = data['password']

        for user in users:
            if user['id'] == id and user['password'] == password:
                return "로그인 성공", 200

        abort(401)


@app.route('/api/post', methods=['GET', 'POST'])
def post():
    # 게시글 작성

    if request.method == 'POST':
        data = request.json
        title = data['title']
        content = data['content']

        if title and content:
            posts.append({
                'title': title,
                'content': content
            })
            return "작성 완료", 201
        else:
            abort(400)

    else:
        print(posts)
        print(type(posts))
        if not posts:
            abort(404)

        return jsonify({"post": [
            {
                "title": doc['title'],
                "content": doc['content']
            } for doc in posts]
        })


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
