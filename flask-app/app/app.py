from flask import Flask, render_template, request, abort, Response
app = Flask(__name__)

# Basic Authentication
def check_auth(username, password):
    return username == 'csc395' and password == 'team5'

def authenticate():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET', 'POST'])
@requires_auth
def index():
    name = None
    greeting = None
    
    if request.method == 'POST':
        name = request.form['name']
        greeting = f'Hello, {name}!'
    
    return render_template('index.html', name=name, greeting=greeting)
   

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


