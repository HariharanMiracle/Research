## happy path
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
    - utter_goodbye

<!-- ## search doctor happy path 1
* greet
  - utter_greet
* search_provider_specialization_location{"specialization":"cardiologist", "location":"Colombo"}
  - action_doctor_search
  - slot{"address":"300 Company st, Colombo"}
* thanks
  - utter_goodbye -->

<!-- ## search doctor + location
* greet
  - utter_greet
* search_provider_specialization_location{"specialization":"cardiologist"}
  - utter_ask_location
* inform{"location":"Colombo"}
  - action_doctor_search
  - slot{"address":"300 Company st, Colombo"}
* thanks
  - utter_goodbye -->

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