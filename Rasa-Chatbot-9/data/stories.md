## chat for first aid tip 
* greet
  - utter_greet
* mood_unhappy  
  - first_aid_tip_form
  - form{"name": "first_aid_tip_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## doctor appointment happy path path 01
* greet
  - utter_greet
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
## doctor appointment happy path path 02
* greet
 - utter_greet
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
## doctor appointment happy path path 03
* greet
 - utter_greet
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
## doctor appointment happy path path 04
* greet
 - utter_greet
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

<!-- ## doctor appointment happy path path 01
* greet
  - utter_greet
* search_provider{"facility":"doctor"}
  - utter_ask_specialization
* inform{"specialization":"cardiologist"}
  - utter_ask_location
* inform{"location":"Colombo"}
  - utter_ask_patient_name
* inform{"patient_name":"Hariharan"}
  - utter_ask_contact_number
* inform{"contact_number":"0776318136"}
  - utter_ask_email_address
* inform{"email_address":"hariharansliit@gmail.com"}
  - utter_ask_nic
* inform{"nic":"991133992V"}
  - utter_ask_credit_card
* inform{"credit_card":"2222111122221111"}
  - utter_ask_cvv
* inform{"cvv":"002"}
  - utter_test -->

## happy path 1
* greet
  - utter_greet
* mood_great
  - utter_happy
* goodbye
  - utter_goodbye

<!-- ## sad path 1 -->
<!-- * greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy -->

<!-- ## sad path 2 -->
<!-- * greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye -->

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot