from flask import Flask, render_template, request, Response, jsonify
from functools import wraps

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
    @wraps(f)  # This will preserve the original function's name
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
        user_input = request.form.get('user_input')  # For standard form submission
        ollama_response = ollama(user_input)
    return render_template('index.html', user_input=user_input, ollama_response=ollama_response)

@app.route('/submit_json', methods=['POST'])
@requires_auth
def submit_json():
    # Get JSON data from the request
    data = request.get_json()
    user_input = data.get('user_input', '')  # Get the user input from the JSON data
    ollama_response = ollama(user_input)  # Process input with the ollama function
    # Return a JSON response
    return jsonify({'message': ollama_response})

# Get Ollama response 
def ollama(user_input):
    try:
        # Simulate calling Ollama and returning a response based on input
        response = """ Recipes from Ollama with your ingredients: 
        pizza
        """
        return response.replace('\n', '<br>')
    except Exception as e:
        return f"There was an error contacting Ollama: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
