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
    ingredients = None
    greeting = None
    
    if request.method == 'POST':
        ingredients = request.form['name']
        greeting = f'Finding recipes with {ingredients}!'
    
    return render_template('index.html', name=ingredients, greeting=greeting)
   
#Get Ollama response 
def ollama():

    return

#Extra Credit - Get Response from other AIs
def AI2(): return
def AI3(): return


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


