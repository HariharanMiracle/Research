<!-- ## happy path
* greet
    - utter_greet
* search_provider_specialization_location{"specialization":"cardiologist"}
    - doctor_form
    - form{"name": "doctor_form"}
    - form{"name": null}
* inform{"doctor_id": 1}
    - find_doctor_details
    - utter_doctor_details
* thanks
    - utter_goodbye -->

## chat query doctor
* greet
  - utter_greet
* search_provider{"facility":"doctor"}
  - chat_1_doctor_search_form
  - form{"name": "chat_1_doctor_search_form"}
  - form{"name": null}
* inform{"appointmentSlotId": 1}
  - utter_goodbye


## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot