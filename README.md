# CSC395_Team-5

Steps to run application:

    1) Install Docker and Git
        - Ask ChatGPT to walk you through the installition steps for your operating system.
    
    2) Clone this GitHub repository to your machine
        - Open a terminal window and run 'git clone https://github.com/jarod4hunt/CSC395_Team-5.git'

    3) Build the containers
        Run the following commands:
        - 'cd CSC  395_Team-5'              #this makes sure you're in the correct directory
        - 'docker-compose down'             #this removes old containers if you tried this project before
        - 'docker-compose up --build -d     #this builds and runs the containers you need to use the project

    4) Open 'localhost:5000' in any browser

    5) Once open, the browser will ask for a username and password for simple authentication
        - username: csc395
        - password: team5

    6) Enjoy!
