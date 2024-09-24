# CSC395_Team-5

Steps to run application:                   #These steps are for Ubuntu linux. Different operating systems may require modified commands. 

    1) Install Docker                       #If you already have Docker installed you can skip this step
        Run these commands:
            - sudo apt update
            - sudo apt install apt-transport-https ca-certificates curl software-properties-common
            - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
            - echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
            - sudo apt update
            - sudo apt install docker-ce
            - docker --version
            - sudo systemctl enable docker
            - sudo systemctl start docker
            - sudo usermod -aG docker ${USER}
            - su - ${USER}

    Docker should now be installed and you should have permissions to make and run containers
    
    2) Clone this GitHub repository to your machine

    3) Open a terminal window and cd into ~/CSC395_Team-5

    4) Run the following commands:
        - 'docker-compose down'             #this removes old containers if you tried this project before
        - 'docker-compose up --build        #this builds and runs the containers you need to use the project

    5) Open 'localhost:5000' in any browser

    6) Enjoy!
