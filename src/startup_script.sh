#!/bin/bash

# Start the Docker containers in detached mode
docker-compose up --build -d

# Wait for a few seconds to ensure the Ollama container is up
sleep 5 

# Execute the Ollama command
docker exec -it src-ollama-1 ollama run llama3  # Change the container name if needed
