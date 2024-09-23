from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ollama-endpoint', methods=['POST'])
def ollama_endpoint():
    data = request.json
    query = data.get('query')  # Extract the 'query' from the JSON data

    # Process the query with Ollama (replace this with your actual Ollama logic)
    response = process_with_ollama(query)

    return jsonify({"response": response})

def process_with_ollama(query):
    # Simulate processing the query
    # Replace this with your actual Ollama processing logic
    return f"Processed response for: {query}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)  # Choose an appropriate port
