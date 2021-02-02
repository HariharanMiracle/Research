# 2020-016

# Project

Voice Based E-Channeling System and Domain Specific Voice Based AI Training Framework

# Main Objective

To implement an Android Mobile application that has end to end voice assistant capability 
in the E-Channeling sector. And create a domain specific voice assistant that can be customized
to any domain.

# Main Research Question
E-Channeling is a major part in the health care sector which is used by large number of people regardless of their age to channel doctors. Currently this is done using the mobile app for e-channeling , calling the mobile operator or by using the website. Lot of leading telecommunication brands with collaboration of hospitals and government provide this facility. Though they give this service to a certain level almost all of the users are not satisfied with the procedure. The online application is too long and it take time to fill and same goes with the app because it also has multiple screens to navigate to complete the channeling procedure. In Sri Lanka lot of elderly people are not very much familiar with the technology also they are not used to fill digital forms. And for above reasons they are not using the online methods to channel doctors. Some people travel to the hospital to get a channel appointment one day and go to the appointment date on another. Another problem that arise in these scenarios are a lot of people do not have a clear idea about which doctor to channel for their sickness. In the current e-channeling domain there are lot of problems like which are mentioned above.



# Individual Research Question

# Speech To Text - IT17106184 - Weerathunga W.A.H.

Speech To Text Conversion in the Domain Of e-channeling
How to convert
- e-channeling appointment related voice to text ?
- user’s sickness and disease related voice data to text ?
- Medical recommendation request voice data to text?

All of these should be done with a very minimum WER
 
# Rasa NLU - IT17044400 - Hariharan Vasudevan

- Process of receiving the request from the speech to text model, recognizing the right most API function and transferring the request to the back-end.
- What is the most accurate and faster method of analyzing the text and transferring the request to the back-end API?
- Using Natural Language Understanding model to extract the contents. Then using a model to pick up the most accurate back-end API. 

# Deep Neural Network - IT17106016 - Lokugamage G.N.

- How to create a fast an accurate API response to the given e-channeling use case ?
- How to get accurate datasets relavent for the e-channeling domain?
- How to create Neural Netowrks models that give correct outputs through APIs for the
 following scenarios

    - Doctor Recommendation
    - Specialization Recommendation
    - Provide Doctor Details
    - Provide Hospital Details
    - Provide Immediate medical instructions for any kind of situations
    - Provide Health Tips

# Text To Speech - IT17115308 - Yahampath A.D.N.H.

Text To Speech Conversion of the Domain of e-channeling

- How to store recevied output data from the Neural Netowrk ? 
- How to generate relavent natural language data to the recieved user input ? 
- How to get final result in voice which is same as the human speech ? 
- How to create real time conversation output which is in the domain of e-channeling



# Individual Objectives


IT17106184 - Weerathunga W.A.H.

Using PocketSphinx

- Collection of audio datasets
- Preprocessing of the dataset
- Corpus creation
- Create necessary files including acoustic model, dictionary and the language model adapted from the PocketSphinx 
- Create acoustic feature files
- Create language model
- Create dictionary model
- Create acoustic model
- Implement in Android Studio

If Deep Learning Approach Used

- Get an implemented Deep Learning model like DeepSpeech or Wavenet
- Audio Data Processing
- Develop a Corpus that is domain specific to e-channeling
- Train the model with multiple GPUs



IT17044400 - Hariharan Vasudevan

- Understanding the converted text input from voice to text converter.
- Making suitable replies and calling the relevant API functions by considering the extracted features
- Handling the dialog flow management using a well gathered set of data to train the dialog flow model

IT17106016 - Lokugamage G.N.

- Collect custom data set
- Train the deep neural network
- Evaluate accuracy and performance
- Optimize the accuracy and performance

IT17115308 - Yahampath A.D.N.H.

- Create a custom text to speech model.
- Read the text which is given from the DNLP backend and generate the natural language according to that
- Create very relevant reply dialog for given user scenario
- Pass the generate natural language data into the text to speech model and convert the text into very accurate speech dialog
#
#
#
#
#
############################################## IT17044400 - Hariharan Vasudevan ##############################################

1. Installation
This component can work individually and this provides the base for the whole research

* You should have pre installed python, pip, tensorflow and rasa
Follow the below documentation to install the above mentioned components
https://rasa.com/docs/rasa/installation/

* You should pre install eclipse

* You should pre install mysql database

* Clone the repository

* Setting up the springboot back end.
  - Import the sql file (research.sql) in a mysql database.
  - Databse name should be "research".
  - Open the echanelling-service project in eclipse.
  - Change the application.properties file based on your credentials used for the database.
  - Changing port number is not advisable, if you change so you have to change the actions.py file in rasa program.
  - Run the project as springbootapp.

* Setting up the rasa project
  - Go to the Rasa-Chatbot-<largest-number> (eg: Rasa-Chatbot-10) folder, since that is the recent version updated.
  - Change the port Number 9090 in the actions.py file if you have changed the port number in the springboot project.
  
* Training the model
  - Go to command prompt
  - cd into the Rasa-Chatbot-<largest-number> (eg: Rasa-Chatbot-10) folder
  - Run the command "rasa train"
  - After training is completed
  - Run the command "rasa run actions"
  - Again cd into the Rasa-Chatbot-<largest-number> (eg: Rasa-Chatbot-10) folder from a differnt command prompt tab
  - Run the command "rasa shell"

"NOW YOU CAN TALK TO YOUR CHATBOT"



2. Tasks completed with logs
########################################## Second commit ##########################################
Since Rasa framework is a very huge file, I have uploaded only the scripts
Back-end services will be updated
Basic NLU is working fine:3 <3

Task completed
* Basic NLU trained
* Actions file first action in construction
* Basic doctor handling crud with springboot # This will be overidden by my other members services while integration, this is just a support work.
## 12/04/2020 GIT LAB Pushing date
## 06/04/2020 Actual completion of tasks

Refer to Rasa-Chatbot
##############################################################################################################################

########################################## Third commit ##########################################
Task completed
* Application which can trace the address of an hospital for a sample has been completed.
* Connected to a back-end from an external API from: https://data.medicare.gov/Home-Health-Compare/Home-Health-Care-Agencies/6jpm-sxkc
* 100% worked as expected
## 26/04/2020 GIT LAB Pushing date
## 23/04/2020 Actual completion of tasks

Refer to Rasa-Chatbot-1
These codes were extracted from: https://github.com/RasaHQ/rasa-masterclass/tree/master/episode8
##############################################################################################################################

########################################## Fourth commit ##########################################
Task completed
* Application which can trace dummy doctors from the springboot Backend API has been completed
* Rasa NLU trained
* Rasa core trained
* 100% worked as expected
## 26/04/2020 GIT LAB Pushing date
## 24/04/2020 Actual completion of tasks

Refer to Rasa-Chatbot-2
##############################################################################################################################

########################################## Fifth commit ##########################################
Task completed
* Db design completed with dummy data
## 27/04/2020 GIT LAB Pushing date
## 27/04/2020 Actual completion of tasks

Refer to sql_db
##############################################################################################################################

########################################## Sixth commit ##########################################
Task completed
* Completed the db for our purpose chatbot
* Completed the backend services
* Back end tested and 100% worked as expected
## 28/04/2020 GIT LAB Pushing date
## 28/04/2020 Actual completion of tasks

Refer to sql_db
Refer to echanelling-service
##############################################################################################################################

>>> Intermediate push when my laptop crashed due to over heat

########################################## Seventh commit ##########################################
Task completed
* Appointment making successfull
## 08/05/2020 GIT LAB Pushing date
## 08/05/2020 Actual completion of tasks

Refer to Rasa-Chatbot-4
##############################################################################################################################

########################################## Eighth commit ##########################################
Task completed
* Backend Springboot project updated
* Database updated
* Appointment making successfull
* missing part added
* combining all the backend and rasa bot
## 09/05/2020 GIT LAB Pushing date
## 09/05/2020 Actual completion of tasks

Refer to Rasa-Chatbot-4
Refer to sql_db
Refer to echanelling-service
##############################################################################################################################

########################################## Ninth commit ##########################################
Task completed
* Bug fixation
* channeling updates
## 03/07/2020 GIT LAB Pushing date
Refer to Rasa-Chatbot-5
Refer to echanelling-service
https://drive.google.com/file/d/1h2DVgGLLnY952dWbRmsFnMJeWdPoUh2u/view?usp=sharing => link for the video
##############################################################################################################################

########################################## Tenth commit ##########################################
Task completed
* Training more chat flows
* Searching appointment by doctor name is done
* Searching appointment by hospital name and specialization is done
* Searching appointment by specialization and location is done
## 29/08/2020 GIT LAB Pushing date
## 15/08/2020 Actual completion of tasks
Refer to Rasa-Chatbot-6
##############################################################################################################################

########################################## Eleventh commit ##########################################
Task completed
* Training more chat flows
* Searching appointment by doctor name is done
* Searching appointment by hospital name and specialization is done
* Searching appointment by specialization and location is done
* Some bugs are cleared
## 29/08/2020 GIT LAB Pushing date
## 22/08/2020 Actual completion of tasks
Refer to Rasa-Chatbot-7
##############################################################################################################################

########################################## Twelfth commit ##########################################
Task completed
* Handling wrong chat message
## 05/09/2020 GIT LAB Pushing date
## 05/09/2020 Actual completion of tasks
Refer to Rasa-Chatbot-8
##############################################################################################################################

########################################## Thirteenth commit ##########################################
Task completed
* Integration
## 17/10/2020 GIT LAB Pushing date
## 30/10/2020 Actual completion of tasks
Refer to Rasa-Chatbot-9
##############################################################################################################################

########################################## Fourteenth commit ##########################################
Task completed
* Automatic form filling or remembarance
* New functions in springboot-api
* Sql db update
## 05/11/2020 GIT LAB Pushing date
## 05/11/2020 Actual completion of tasks
Refer to Rasa-Chatbot-10
Refer to echanneling-service
Refer to sql_db
Refer to Chat-comparisons
##############################################################################################################################