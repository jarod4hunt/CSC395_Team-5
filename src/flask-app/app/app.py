import requests
from flask import Flask, render_template, request, Response, jsonify
from functools import wraps
import json

app = Flask(__name__)

# Basic Authentication - ignore this
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
# End of Authentication - ignore this

# Main web page - blank input field
@app.route('/', methods=['GET'])
@requires_auth
def index():
    return render_template('index.html')

# Stream Ollama response line by line
def stream_ollama_response(prompt):
    ollama_url = "http://ollama:11434/api/generate"
    data = {
        "model": "llama3",
        "prompt": prompt
    }

    try:
        with requests.post(ollama_url, json=data, stream=True) as response:
            if response.status_code == 200:
                for chunk in response.iter_lines():
                    if chunk:
                        try:
                            parsed_line = json.loads(chunk.decode('utf-8'))
                            partial_response = parsed_line.get('response', '')
                            yield partial_response  # Yield each chunk of the response
                            print("Partial response:", partial_response)

                            if parsed_line.get('done', False):
                                break
                        except ValueError:
                            yield f"Error parsing JSON: {chunk}"
            else:
                yield f"Error communicating with Ollama: {response.status_code} {response.text}"
    except requests.exceptions.RequestException as e:
        yield f"Request failed: {str(e)}"

# Runs user input and returns output
@app.route('/submit', methods=['POST'])
@requires_auth
def submit():
    user_input = request.form.get('user_input')  # Get ingredients from form

    template = """Please give me a recipe in the following format:

    Recipe Title:

    Fun Tagline:

    Ingredient list:
        - ingredient 1 + measurement
        - ingredient 2 + measurement
        - etc....

    Instructions:
        Step 1)
        Step 2)
        etc....    

    with these ingredients:  
    """
    prompt = template + user_input  # this is what gets sent to Ollama as input

    return Response(stream_ollama_response(prompt), content_type='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
