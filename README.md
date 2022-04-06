# QA-Core-Practical-Project
Repository for the QA DevOps Core Practical Project. 

## Table of Contents
* [Project Brief](#Project-Brief)
* [Project Planning](#Project-Planning)
  * [Risk Assessment](#Risk-Assessment)
  * [Entity Diagram](#Entity-Diagram)
  * [Microservice Architecture](#Microservice-Architecture)
* [CI/CD Pipeline](#CICD-Pipeline)
  * [Project Tracking](#Project-Tracking)
  * [Version Control](#Version-Control)
    * [Versions](#Versions)
  * [CI Server](#CI-Server)
* [App Design](#App-Design)
  * [Virtual Machines](#Virtual-Machines)

## Project Brief
To produce an application, consisting of four microservices, all interacting with one another to generate objects using a defined logic. 
The application was to be produced and maintained using a fully automated CI/CD Pipeline, with the full technology stack being:
* Kanban Board (Trello) for project tracking
* Git (with the use also of Github) for version control
* Jenkins acting as the CI server
* Ansible for configuration management
* Google Cloud Platform as the cloud platform
* Docker as the containerisation tool
* Docker Swarm for container orchestration
* NGINX as the reverse proxy

## Project Planning
### Risk Assessment
Prior to the commencement of the project, a Risk Assessment Table was produced. This outlines any risks that have been considered prior to the commencement of working on the actual project. This table will be updated throughout the project to accommodate any new risks that may have arisen or need to be considered. Any updates will be made to the table and reassesed throughout the span of the entire project. They will also be evaluated after the project to ensure that no errors/risks will occur to the live application. The risk assessment table from prior to the commencement of the project can be seen below, with the key for this table below that. 
![Risk Assessment Table](/Readme-Images/Risk-Assessment.png)
![Risk Assessment Table Key](/Readme-Images/Risk-Assessment-Key.png)

Users will not be submitting any information (personal information) into the application, and so the main focus of the risk assessment and risk assessment table was the operational risks. Operational risks are the risks which are associated solely on the building/creating of the application and deployment of the application. As seen from the table above, each of the different risks was assigned a Probablity and Impact score both before and after the control variable that will be used. This is done to quantify the risk and act as a guide throughout the development of the application. 

The screenshot below shows the Risk Assessment Table during the project working sprint, having been updated with any additional risks and the other risks re-evaluated. 
![Risk Assessment During](/Readme-Images/risk-assessment-during.png)

### Entity Diagram
For this project, a database will be used to save and persist data. This data will be a history of the planning cards that have been generated. The database for this project will be simple, consisting of one table (playingCards table), which will store the data for the playing cards id, the value of the playing card ("Ace", ..., "King") and the suit of the playing card ("Hearts", "Diamonds", "Spades" and "Clubs"). The image below shows an ED of the table/database for this project. The database also stores the date in which the card was generated, so that on the history webpage it will show the cards that have been generated along with the date that someone generated them cards.  

![ED](/Readme-Images/ED.drawio.png)

### Microservice Architecture
For development purposes, the database will be stored within a `sqlite` database, however the end goal of the application is that have the data is stored within a MySQL database on a server that is accessible from the entire application. The diagram below shows the microservice architecture diagram, outlining how the application is built. 

![Microservices Architecture](/Readme-Images/microservices_architecture.drawio.png)

## CI/CD Pipeline
To develop and deploy this application, a full CI/CD Pipeline will be utilised to build, test, deploy, update and maintain the application. There are five main components of the CI/CD Pipeline, which are:
* Project Tracking (Trello)
* Version Control (Git)
* Development Environment
* CI Server
* Deployment Environment

### Project Tracking
Project tracking was used to keep track of all of the required tasks for this project. The software used to perform project tracking was Trello. Here, a board had been created for the sprint project/sprint, which included a project backlog (which is a list of tasks that will need to be completed throughout the lifespan of the project), sprint backlog (which is a list of tasks which need to be completed within the designated sprint timeline), In Progress (which is where a task is moved to when it is being worked on), In Review (where the task has been completed but needs a final check before being pushed to the dev branch for example), Completed (when a task is fully completed) and Pushed to Main (which will house all of the sprints tasks that have been completed and push up to the main branch on the Github repository). The image below shows how the Trello board looked at the start of the project.
![Trello Board Start](/Readme-Images/Trello-Board-Start.png)
Here is also a link to the full Trello board: [Trello Board](https://trello.com/b/AS9evaBO/qa-core-practical-project)

The screenshot below shows how a task looks on the Trello board, with the user stories that relate to that task and any todo items that may also need completing to fully finish that task within the sprint. The next screenshot also shows what it looked like at the end of the sprint with the user stories completed. 
![Service 1 Trello start](/Readme-Images/service_1_start.png)
![Service 1 Trello end](/Readme-Images/service_1_end.png)

The screenshot below is from the Trello board closer to the end of the sprint/project. As you can see the project tasks have been moved to completed, and once pushed to main they will be moved over to the pushed to main section of the Trello board. 
![Trello near end](/Readme-Images/Trello_near_end.png)

### Version Control
Version Control allows for the application to be stored remotely, meaning that no work can be lost as long as it has been pushed up onto the designated repository. The Version Control system that has been used for this application is Git, utilising GitHub for accessing and reading the information that has been stored within the repository. Version Control also allows for the application to be rolled back to it's last working state should any bugs, or errors, be added and pushed up to the repository. 
In this application a Feature-Branch model of Version Control has been adopted. The Feature-Branch model essential creates new branches for each of the different features that are being worked on at any time. For example, if working on the Unit Testing, you would create a new branch off of the development branch, write the tests and make sure there are no errors, and then create a pull request back to the development branch. This method ensures that there is always a fully working version of the software that can be rolled back to. The image below shows an example of the Feature-Branch network diagram from the start of this project, and how it had been utilised thus far. 
![Feature-Branch Model Start](/Readme-Images/Network-Diagram-Start.png)

Further on down the project line, the feature branch model looked more like the screenshot below. This captures how new branches were created, merged with development branches and finally sent back into the production main branch ready for deployment. 
![Feature-Branch Model During](/Readme-Images/Feature-branch-model-example.png)

#### Versions
Only once the development branch has had all features pull-requested onto it, and it has been tested that there are no errors can a version be made. The creation of versions will consist of creating a new pull-request from the development branch back to the main branch. In this process, the CI/CD Pipeline will also perform automated tests through the use of Jenkins to add a final fail safe that there will be no errors in the live environment. The CI/CD Pipline will then be able to build the application and deploy it live to the end users. 

### CI Server
Jenkins was used for the CI server for this project. A Github webhook was created, so that whenever any code was pushed or pull requested onto the main branch of the repository, Jenkins would clone the repository down onto the server, and execute the pipeline script (found within the Jenkinsfile). This would run the main stages of the application, which included the testing, building and deploying stages. The pipeline would also execute the post build actions, which in this case was to archive the artifacts, which were the testing coverage html reports folder. 

The first stage of the Jenkins pipeline was testing. Within this stage, each of the different APIs are tested to ensure that there are no bugs or unexpected errors when deploying the application. Should any of the tests fail, then the Jenkins pipeline will skip the next steps and not deploy the application should anything fail. The screenshots below show the final stage of the pipeline which saves the html coverage report for each of the different tests (front-end, cardvalue-api, cardsuit-api and card-api). 
![front-end coverage report](/Readme-Images/front-end_cov.png)

![cardvalue-api coverage report](/Readme-Images/cardvalue_api_coverage.png)

![cardsuit-api coverage report](/Readme-Images/cardsuit_api_coverage.png)

![card-api coverage report](/Readme-Images/card-api_cov.png)

The next stage of the pipeline is the building stage. Within this stage, the Docker images from the docker-compose.yaml file. I.e., all of the APIs, database and NGINX. The final step of this stage is to push the images to Dockerhub, where they can be retrieved. 

The final stage of the pipeline is the deploying stage. In this stage the application is deployed onto the swarm-manager/swarm-workers and can be accessed via the web-browser from the IP address for the swarm-manager virtual machine. 

## App Design
In response to the brief, I have chosen to develop a random card generator. This utilises a microservice architecture as follows:
* Service 1 (front-end):
  * This is the service which the end user interacts with. Service 1 sends `GET` and `POST` requests to the other services (services 2, 3 & 4) to generate a random card and an image of that random card. The service also adds the card that has been generated to a mysql database and will display the history of the cards generated. 
* Service 2 (cardvalue-api):
  * This service receives HTTP GET requests from service 1 (front-end) and responds with a randomly selected card value/symbol from a list of card values (`[A, 2, 3, ..., K]`) using Random.choice(). 
* Service 3 (cardsuit-api):
  * This service receives HTTP GET requests from service 1, and responds with a randomly selected card suit from a list of card suits (`[Spades, Diamonds, Clubs, Hearts]`), again using Random.choice(). 
* Service 4 (card-api):
  * This service receives HTTP POST requests from service 1, which provides to it a randomly generated value/symbol and a randomly generated suit. Service 4 then creates a deck for the cards images to be stored in, creates a image key based on the symbol and suit which has been sent and gathers that image from the card deck, using the key as a reference for which one to collect. 

In addition to these main four services, a reverse proxy using NGINX was implemented and used. NGINX service listens on port 80 from the host machine and performs a proxy pass, which directs traffic from port 80 to port 5000 on the front-end container, which is where the app is accessible. The images below show the front-end in action:
![App working](/Readme-Images/action_1.png)
![App working](/Readme-Images/action_2.png)
![App working](/Readme-Images/action_3.png)
![App working](/Readme-Images/action_4.png)

The original design for the application was to have the home page display a random string of the cards thats has been generated. This can be seen in the screenshot below. Whenever the webpage is refreshed, or the "Generate New Card" button is clicked, the card text being displayed will change for a randomly generated card value and suit. This can be seen in the screenshot below:
![Original design for the application](/Readme-Images/original_design.png)

I then redesigned the application to also include an image of the card that has been generated. This is done through the use of a static folder which houses all of the different card images. An image key is then generated which is used to find the correct image in the "card deck", which is a python dictionary. This card image is then displayed through the use of the index.html webpage, which gets the `url_for` the static folder and adds the filename of the card that has been generated. This can be seen in the screenshot below:
![New design with image](/Readme-Images/new_design_w_card_image.png)

The next design phase was to create a history of the cards that had been generated, store them in a database and display the full history of the cards that had been generated on another web page. The home page would also be changed to show the last five cards that have been drawn. This design change can be seen in the screenshots below:
![Home page with five card history](/Readme-Images/home_5_card_history.png)

![History page with card history from database](/Readme-Images/history_webpage.png)


### Virtual Machines
I have setup the following virtual machines. These were all created on Google Cloud Platform (GCP), and then Ansible was used to configure each of these virtual machines. The virtual machines that were setup were as follows: 
* dev
* instance-1
* jenkins
* swarm-manager
* swarm-worker
The dev branch is used to make changes to the application itself. Within Ansible, the setup for this branch is to clone down the working repository from GitHub, which can then be used with VSCode to make changes to the web application. This is also helpful when working towards a rolling update, where you can work on the application, make a change and then push that to the Jenkins server to deploy. 
The instance-1 virtual machine was used as the Asnible server. This is where the code for the configuration is held. Here, there is a playbook, inventory and roles which are used to configure each of the differenet virtual machines ready to deploy the web application. The first step is to export the mysql root password, and then run the following `ansible-playbook -i inventory.yml playbook.yml -e mysql_root_password=${mysql_root_password}`. 
The jenkins virtual machine was initially configured manually, by installing Jenkins and setting up the admin user. Once this was done, Ansible could then do some more configuration for the virtual machine by adding the Jenkins user to the Docker group. 
The swarm-manager and the swarm-worker are where the Docker swarm is running, with the swarm-worker joined onto the swarm-manager. The application is viewed by the end user from the swarm-manager virtual machine. 

The image below shows these virtual machines on GCP. 
![GCP VMs](/Readme-Images/virtual_machines.png)

An SQL instance was also created, which is where the mysql database is held. This gets configured to have a database called `card_db`, which has a table called `cards`. This is then connected to from the application and used to store all of the details of the cards that are generated from the front-end of the application. The screenshot below shows the mysql instance, with the database and table. 
![mysql instance](/Readme-Images/mysql_instance.png)

## Future Improvements
In the future, this application could be extended to function more like a game, such as black jack, where a user can generate a number of randomly generated cards with the aim of getting a score of 21. This could also be even further extended to allow for different types of card games to be played and would therefore increase the usability and the likelyhood of a returning user base. The application could also be further improved by using a locally hosted Nexus repository, which would speed up the deployment stage, as all of the different images would then not have to be collected from the Dockerhub site.