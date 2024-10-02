## Introduction
Ollama Recipe Builder is a web application designed to help users generate creative, brand-themed recipes based on a list of ingredients. By leveraging the powerful language model Ollama, this app provides tailored recipes in a fun and engaging format, making meal preparation easier and more enjoyable. Whether you're a foodie looking for inspiration or a brand aiming to showcase your products through recipes, the Ollama Recipe Builder allows users to select a brand, input ingredients, and receive a customized recipe with detailed instructions.

The app is built using Python's Flask framework and integrates with Ollama's AI capabilities to dynamically generate recipes based on user input. It's designed to be lightweight, easily customizable, and scalable for any user or organization.

## Features
...
## Installation
1) Install Docker and Git:
    - Ask ChatGPT to walk you through the installition steps for your operating system.
    - Make sure you are properly logged into Docker ('docker login')
    
2) Clone this GitHub repository to your machine:
    - Open a terminal window and run 'git clone https://github.com/jarod4hunt/CSC395_Team-5.git'

3) Run the startup script:          
    Linux/macOS:                    Windows:                        
    - cd into CSC395_Team-5/src     - cd into CSC395_Team-5/src
    - run './startup_script.sh'     - run 'docker-compose up --build -d'
                                    - run 'docker exec -it src-ollama-1 ollama run llama3'  

**This step will take a while the first time it is ran as the AI model is several GBs of data.
**Subsequent runs will start up very fast.

4) Open 'localhost:5000' in any browser

5) Once open, the browser will ask for a username and password for simple authentication
   - username: csc395
    - password: team5

6) Enjoy!

## Screenshots
...
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
