<!-- This file is to train the stories model -->
<!-- This is the model which is used to deal with the dialogue -->
<!-- This model is already trained with the samples -->

<!-- Make a doctor appointment using doctor's name  -->
## doctor appointment happy path 02 new user v1
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* inform{"facility": "doctor", "name": "Vino"}
  - chat_2_doctor_search_form
  - form{"name": "chat_2_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 02 new user v2
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* search_provider{"facility": "doctor", "name": "Vino"}
  - chat_2_doctor_search_form
  - form{"name": "chat_2_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 02 old user v1
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* inform{"facility": "doctor", "name": "Vino"}
  - chat_2_doctor_search_form
  - form{"name": "chat_2_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 02 old user v2
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* search_provider{"facility": "doctor", "name": "Vino"}
  - chat_2_doctor_search_form
  - form{"name": "chat_2_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

<!-- Make a doctor appointment using specialization and location  -->
## doctor appointment happy path 01 new user v1
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* inform{"facility":"doctor"}
  - chat_1_doctor_search_form
  - form{"name": "chat_1_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 01 new user v2
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* inform{"name":"doctor"}
  - chat_1_doctor_search_form
  - form{"name": "chat_1_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 01 new user v3
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* search_provider{"name":"doctor"}
  - chat_1_doctor_search_form
  - form{"name": "chat_1_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 01 new user v4
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* search_provider{"facility":"doctor"}
  - chat_1_doctor_search_form
  - form{"name": "chat_1_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 01 old user v1
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* inform{"facility":"doctor"}
  - chat_1_doctor_search_form
  - form{"name": "chat_1_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 01 old user v2
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* inform{"name":"doctor"}
  - chat_1_doctor_search_form
  - form{"name": "chat_1_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 01 old user v3
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* search_provider{"name":"doctor"}
  - chat_1_doctor_search_form
  - form{"name": "chat_1_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 01 old user v4
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* search_provider{"facility":"doctor"}
  - chat_1_doctor_search_form
  - form{"name": "chat_1_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

<!-- Make a doctor appointment using hospital name 01  -->
## doctor appointment happy path 03 new user v1
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* inform{"facility": "doctor", "hospitalName": "Nawaloka"}
  - chat_3_doctor_search_form
  - form{"name": "chat_3_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 03 new user v2
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* search_provider{"facility": "doctor", "hospitalName": "Nawaloka"}
  - chat_3_doctor_search_form
  - form{"name": "chat_3_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 03 old user v1
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* inform{"facility": "doctor", "hospitalName": "Nawaloka"}
  - chat_3_doctor_search_form
  - form{"name": "chat_3_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye  

## doctor appointment happy path 03 old user v2
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* search_provider{"facility": "doctor", "hospitalName": "Nawaloka"}
  - chat_3_doctor_search_form
  - form{"name": "chat_3_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye  

<!-- Make a doctor appointment using hospital name 02  -->
## doctor appointment happy path 04 new user v1
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* inform{"specialization": "cardiologist", "hospitalName": "Nawaloka"}
  - chat_3_doctor_search_form
  - form{"name": "chat_3_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 04 old user v2
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* inform{"specialization": "cardiologist", "hospitalName": "Nawaloka"}
  - chat_3_doctor_search_form
  - form{"name": "chat_3_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 04 new user v2
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* search_provider{"specialization": "cardiologist", "hospitalName": "Nawaloka"}
  - chat_3_doctor_search_form
  - form{"name": "chat_3_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path 04 old user v2
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* search_provider{"specialization": "cardiologist", "hospitalName": "Nawaloka"}
  - chat_3_doctor_search_form
  - form{"name": "chat_3_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

<!-- firstaid health tip chat -->
## health tips user v1
* greet
 - utter_greet
* firstaid{"cause": "chest pain"}
  - first_aid_tip_form
  - form{"name": "first_aid_tip_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

<!-- specialization chat -->
## specialization user v1
* greet
 - utter_greet
* inform{"symptoms": "headache"}
  - specialization_form
  - form{"name": "specialization_form"}
  - form{"name": null}
* thanks
  - utter_goodbye