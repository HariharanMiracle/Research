<!-- This file is to train the stories model -->
<!-- This is the model which is used to deal with the dialogue -->
<!-- This model is already trained with the samples -->

## chat for first aid tip new user
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* mood_unhappy  
  - first_aid_tip_form
  - form{"name": "first_aid_tip_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## chat for first aid tip old user
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* mood_unhappy  
  - first_aid_tip_form
  - form{"name": "first_aid_tip_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path path 01 new user
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

## doctor appointment happy path path 01 old user
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

<!-- Make a doctor appointment using doctor's name  -->
## doctor appointment happy path path 02 new user
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* inform{"facility": "doctor", "name": "Dhivya"}
  - chat_2_doctor_search_form
  - form{"name": "chat_2_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path path 02 old user
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* inform{"facility": "doctor", "name": "Dhivya"}
  - chat_2_doctor_search_form
  - form{"name": "chat_2_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

<!-- Make a doctor appointment using hospital name 01  -->
## doctor appointment happy path path 03 new user
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

## doctor appointment happy path path 03 old user
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

<!-- Make a doctor appointment using hospital name 02  -->
## doctor appointment happy path path 04 new user
* greet
 - utter_greet
* affirm
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
* inform{"specialization": "cardiologist", "hospitalName": "Nawaloka"}
 - utter_test
  - chat_3_doctor_search_form
  - form{"name": "chat_3_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path path 04 old user
* greet
 - utter_greet
* deny
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* inform{"specialization": "cardiologist", "hospitalName": "Nawaloka"}
 - utter_test
  - chat_3_doctor_search_form
  - form{"name": "chat_3_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
* thanks
  - utter_goodbye  

  <!-- - utter_test -->