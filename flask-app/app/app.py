from flask import Flask, render_template, request, Response

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
    user_input = ""
    ollama_response = ""
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        ollama_response = ollama(user_input)
    return render_template('index.html', user_input=user_input, ollama_response=ollama_response)

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input')
    ollama_response = ollama(user_input).replace('\n', '<br>')
    return render_template('index.html', user_input=user_input, ollama_response=ollama_response)

# Get Ollama response 
def ollama(user_input):
    try:
        # Simulate calling Ollama and returning a response based on input
        response = """ Recipes from Ollama with your ingredients: 
        pizza
        """
        return response.replace('\n', '<br>')
    except:
        return "There was an error contacting Ollama"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
