import requests
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
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET'])
@requires_auth
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
@requires_auth
def submit():
    user_input = request.form.get('user_input')  # Get user input from form
    ollama_response = ""

    try:
        # Make a request to the Ollama container
        ollama_url = "http://ollama:11434/api/generate"
        data = { 
            "model": "gemma2:2b",
            "prompt": user_input
        }
        
        response = requests.post(ollama_url, json=data)
        
        # Print raw response for debugging
        print("Raw response:", response.text)  # Print the raw response
        
        if response.status_code == 200:
            ollama_response = response.json().get('response', 'No response from Ollama')
        else:
            ollama_response = f"Error communicating with Ollama: {response.status_code} {response.text}"

    except ValueError as e:
        ollama_response = f"Error parsing JSON: {str(e)}"
    except requests.exceptions.RequestException as e:
        ollama_response = f"Request failed: {str(e)}"

    # Return a JSON response for the JavaScript to handle
    return jsonify({'response': ollama_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
