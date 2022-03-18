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

## CI/CD Pipeline
To develop and deploy this application, a full CI/CD Pipeline will be utilised to build, test, deploy, update and maintain the application. There are five main components of the CI/CD Pipeline, which are:
* Project Tracking (Trello)
* Version Control (Git)
* Development Environment
* CI Server
* Deployment Environment
### Project Tracking


