# from flask import Flask, render_template, request, abort, Response
# app = Flask(__name__)

# # Basic Authentication
# def check_auth(username, password):
#     return username == 'csc395' and password == 'team5'

# def authenticate():
#     return Response(
#         'Could not verify your access level for that URL.\n'
#         'You have to login with proper credentials', 401,
#         {'WWW-Authenticate': 'Basic realm="Login Required"'})

# def requires_auth(f):
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username, auth.password):
#             return authenticate()
#         return f(*args, **kwargs)
#     return decorated

# @app.route('/')
# @requires_auth
# def index():
#     return render_template('delvec_index.html')

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Capture input from the form
    name = request.form['name']
    
    # Process the input and display a response
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
