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

### Entity Diagram
For this project, a database will be used to save and persist data. This data will be a history of the planning cards that have been generated. The database for this project will be simple, consisting of one table (playingCards table), which will store the data for the playing cards id, the value of the playing card ("Ace", ..., "King") and the suit of the playing card ("Hearts", "Diamonds", "Spades" and "Clubs"). The image below shows an ED of the table/database for this project. 

![ED](/Readme-Images/ED.drawio.png)

### Microservice Architecture
For development purposes, the database will be stored within a `sqlite` database, however the end goal of the application is that have the database stored within a MySQL database on a server that is accessible from the entire application. The diagram below shows the microservice architecture diagram, outlining how the application is built. 

![Microservices Architecture]()

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

### Version Control
Version Control allows for the application to be stored remotely, meaning that no work can be lost as long as it has been pushed up onto the designated repository. The Version Control system that has been used for this application is Git, utilising GitHub for accessing and reading the information that has been stored within the repository. Version Control also allows for the application to be rolled back to it's last working state should any bugs, or errors, be added and pushed up to the repository. 
In this application a Feature-Branch model of Version Control has been adopted. The Feature-Branch model essential creates new branches for each of the different features that are being worked on at any time. For example, if working on the Unit Testing, you would create a new branch off of the development branch, write the tests and make sure there are no errors, and then create a pull request back to the development branch. This method ensures that there is always a fully working version of the software that can be rolled back to. The image below shows an example of the Feature-Branch network diagram from the start of this project, and how it had been utilised thus far. 
![Feature-Branch Model Start](/Readme-Images/Network-Diagram-Start.png)
#### Versions
Only once the development branch has had all features pull-requested onto it, and it has been tested that there are no errors can a version be made. The creation of versions will consist of creating a new pull-request from the development branch back to the main branch. In this process, the CI/CD Pipeline will also perform automated tests through the use of Jenkins to add a final fail safe that there will be no errors in the live environment. The CI/CD Pipline will then be able to build the application and deploy it live to the end users. 
### CI Server
Jenkins was used for the CI server for this project. A Github webhook was created, so that whenever any code was pushed or pull requested onto the main branch of the repository, Jenkins would clone the repository down onto the server, and execute the pipeline script (found within the Jenkinsfile). This would run the main stages of the application, which included the testing, building and deploying stages. The pipeline would also execute the post build actions, which in this case was to archive the artifacts, which were the testing coverage html reports folder. 

TALK ABOUT EACH OF THE DIFFERENT PIPELINE STAGES HERE!

## App Design
