# AgIle Recipe Maker

## Introduction
AgIle Recipe Maker is a web application designed to help users generate creative, brand-themed recipes based on a list of ingredients. By leveraging the powerful language model Ollama, this app provides tailored recipes in a fun and engaging format, making meal preparation easier and more enjoyable. Whether you're a foodie looking for inspiration or a brand aiming to showcase your products through recipes, the AgIle Recipe Maker allows users to select a brand, input ingredients, and receive a customized recipe with detailed instructions.

The app is built using Python's Flask framework and integrates with Ollama's AI capabilities to dynamically generate recipes based on user input. It's designed to be lightweight, easily customizable, and scalable for any user or organization.

![Example Image](images/example_output.png)

## Features
- Dynamic Recipe Generation: Users can input a list of ingredients and select a brand to generate a customized recipe using Ollama's AI model.
- Brand-Themed Recipes: The generated recipes include brand-specific information, making it ideal for companies looking to promote their products through engaging recipes.
- Step-by-Step Instructions: Each recipe includes detailed steps, along with measurements and ingredient lists, for easy-to-follow meal preparation.
- Fun and Engaging Output: In addition to the recipe, each output includes a fun tagline and a structured format to enhance the user experience.
- User-Friendly Interface: A simple and clean web interface allows users to easily input their ingredients and brand selections without hassle.
- Error Handling: Provides graceful error messages if there is an issue communicating with Ollama or processing the request.
- Extensible Architecture: Built on Python and Flask, the app can be extended or modified to support additional features, ingredients, or integrations.

## Installation
1) Install Docker and Git:
    - Ask ChatGPT to walk you through the installition steps for your operating system.
    - Make sure you are properly logged into Docker ('docker login')
    
2) Clone this GitHub repository to your machine:
    - Open a terminal window and run 'git clone https://github.com/jarod4hunt/CSC395_Team-5.git'

3) Run the startup script:         
<pre>
    Linux/macOS:                      Windows:                                          
    - cd into CSC395_Team-5/src       - cd into CSC395_Team-5/src
    - run './startup_script.sh'       - run 'docker-compose up --build -d'
                                      - run 'docker exec -it src-ollama-1 ollama run llama3' 
    
    This step will take a while the first time it is ran as the AI model is several GBs of data.
</pre>

4) Open 'localhost:5000' in any browser

5) Once open, the browser will ask for a username and password for simple authentication
    - username: csc395 
    - password: team5 
   

7) Enjoy!

## System Architecture and Data Flow
This section outlines the architecture of the AgIle Recipe Maker and the flow of data within the system. The application is designed to efficiently interact with the Ollama API to generate recipe suggestions based on user input.

Architecture Overview
The system follows a client-server architecture, where the client (web interface) interacts with a Flask backend. The backend processes user requests and communicates with the Ollama API to fetch recipe data. The architecture is modular, allowing for easy scalability and maintenance.

Data Flow
1.  User Input: Users provide ingredients and brand preferences via the web interface.
2. API Request: The Flask server constructs a prompt using the provided information and sends it to the Ollama API.
3. Response Handling: The server receives a response from the API, processes it, and returns the formatted recipe to the user.
4. Display: The recipe is displayed on the client-side, enabling users to view and interact with the suggested recipes.


This architecture ensures a seamless experience for users, allowing for quick and dynamic recipe generation based on their preferences.

![Example Image](images/data_flow.png)


## Contributors
Thanks to the following people who have contributed to this project:
<table>
  <tr>
    <td align="center"><a href="https://github.com/jarod4hunt"><img src="https://avatars.githubusercontent.com/jarod4hunt" width="100px;" alt=""/><br /><sub><b>@jarod4hunt</b></sub></a></td>
    <td align="center"><a href="https://github.com/hartelaneeqa"><img src="https://avatars.githubusercontent.com/hartelaneeqa" width="100px;" alt=""/><br /><sub><b>@hartelaneeqa</b></sub></a></td>
    <td align="center"><a href="https://github.com/nickkeller62"><img src="https://avatars.githubusercontent.com/nickkeller62" width="100px;" alt=""/><br /><sub><b>@nickkeller62</b></sub></a></td>
    <td align="center"><a href="https://github.com/anshi0304"><img src="https://avatars.githubusercontent.com/anshi0304" width="100px;" alt=""/><br /><sub><b>@anshi0304</b></sub></a></td>
    <td align="center"><a href="https://github.com/abdiu1"><img src="https://avatars.githubusercontent.com/abdiu1" width="100px;" alt=""/><br /><sub><b>@abdiu1</b></sub></a></td>
  </tr>
</table>

## License
This project is licensed under the Apache License.
