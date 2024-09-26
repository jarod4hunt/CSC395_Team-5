#!/bin/bash

# Start the Docker containers in detached mode
docker-compose up --build -d

# Wait for a few seconds to ensure the Ollama container is up
sleep 1  # Adjust this time based on how long it takes for your container to start

docker exec -it csc395_team-5-ollama-1 ollama serve 
sleep 5 

# Execute the Ollama command
docker exec -it csc395_team-5-ollama-1 ollama run llama3  # Change the container name if needed
