## doctor search happy path
* greet
  - utter_how_can_i_help
* search_provider{"facility_type":"doctor", "doctor_type":"Cardiologists"}
  - action_facility_search
  - slot{"details":"Dr.Dilshan De Silva specialized as a Cardiologist"}
* thanks
 - utter_goodbye

## search doctor + doctor_type
* greet
  - utter_how_can_i_help
* search_provider{"facility_type":"doctor"}
 - utter_ask_doctor_type
* inform{"doctor_type":"cardiologist"}
 - action_facility_search
 - slot{"details":"Dr.Dilshan De Silva specialized as a Cardiologist"}
* thanks
 - utter_goodbye

## happy_path
* greet
  - find_facility_type
* inform{"facility_type": "aaaa-a11a"}
  - facility_form
  - form("name": "facility_form")
  - form("name": null)
* inform{"facility_id": 0001}
 - find_doctor_details
 - utter_details
* thanks
  - utter_goodbye

## happy_path_multi_requests
* greet
  - find_facility_types
* inform{"facility_type": "aaaa-a11a"}
  - facility_form
  - form("name": "facility_form")
  - form("name": null)
* inform{"facility_id": 0001}
 - find_doctor_details
 - utter_details
* search_provider{"facility_type": "aaaa-a11a"}
  - facility_form
  - form("name": "facility_form")
  - form("name": null)
* inform{"facility_id": 0001}
 - find_doctor_details
 - utter_details
* thanks
  - utter_goodbye

## happy_path2
* search_provider{"doctor_type":"cardiologist", "facility_type":"aaaa-a11a"}
  - facility_form
  - form("name": "facility_form")
  - form("name": null)
*inform{"facility_id": 0001}
 - find_doctor_details
 - utter_details
* thanks
  - utter_noworries

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

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