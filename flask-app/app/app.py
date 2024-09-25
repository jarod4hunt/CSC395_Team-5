import requests
from flask import Flask, render_template, request, Response, jsonify
from functools import wraps
import json

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
            "model": "llama3",
            "prompt": user_input
        }
        
        response = requests.post(ollama_url, json=data)

        # Print raw response for debugging
        print("Status Code:", response.status_code)  # Print the status code
        
        if response.status_code == 200:
            try:
                # Handle the chunked response
                raw_responses = response.text.strip().splitlines()
                for line in raw_responses:
                    parsed_line = json.loads(line)
                    partial_response = parsed_line.get('response', '')
                    ollama_response += partial_response  # Append partial response to the overall response
                    print("Partial response:", partial_response)  # Print each chunk of the response

                    # Check if done flag is true
                    if parsed_line.get('done', False):
                        break

            except ValueError as e:
                # Handle the case where JSON parsing fails
                ollama_response = f"Error parsing JSON: {str(e)}"
        else:
            ollama_response = f"Error communicating with Ollama: {response.status_code} {response.text}"

    except requests.exceptions.RequestException as e:
        ollama_response = f"Request failed: {str(e)}"

    # Return a JSON response for the JavaScript to handle
    return jsonify({'response': ollama_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
