from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction

import json

def _find_doctors1(location: Text, specialization: Text) -> List[Dict]:
    """Returns json of facilities matching the search criteria."""

    if str.isdigit(location):
        full_path = "http://localhost:9090/Echannel/listAllDoctorsByZipcodeAndSpecialization?specialization=" + specialization + "&zipcode=" + location
    else:
        full_path = "http://localhost:9090/Echannel/listAllDoctorsByLocationAndSpecialization?specialization=" + specialization + "&location=" + location
        
    print("Full path:")
    print(full_path)
    results = requests.get(full_path).json()
    return results

class Chat_1_doctor_search_form(FormAction):
    """Custom form action to fill all slots required to find 
    the doctor appointment details"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "chat_1_doctor_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["specialization", "location"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"specialization": self.from_entity(entity="specialization",
                                                  intent=["inform",
                                                          "search_provider_specialization_location"]),
                "location": self.from_entity(entity="location",
                                             intent=["inform",
                                                     "search_provider_specialization_location"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        location = tracker.get_slot('location')
        specialization = tracker.get_slot('specialization')

        results = _find_doctors1(location, specialization)
        # button_name = _resolve_name(FACILITY_TYPES, facility_type)
        button_name = specialization

        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find a {} in {}.".format(button_name,
                                                              location.title()))
            return []

        buttons = []
        # limit number of results to 3 for clear presentation purposes

        for r in results[:3]:
            appointmentSlotId = str(r.get("appointmentSlotId"))
            doctorName = str(r.get("doctorName"))
            hospitalName = str(r.get("hospitalName"))
            date = str(r.get("date"))
            time = str(r.get("time"))
            charge = str(r.get("charge"))
            address = str(r.get("address")) 

            details = " Appoitment: Doctor => " + doctorName.title() + ", Hospital => " + hospitalName.title() + ", Date => " + date.title() + ", Time => " + time.title() + ", Charge => " + charge.title() + ", Address => " + address.title() + ""

            payload = "/inform{\"appointmentSlotId\":\"" + appointmentSlotId + "\"}"
            buttons.append(
                {"title": "{}".format(details), "payload": payload})

        if len(buttons) == 1:
            message = "Here is a {} near you:".format(button_name)
        else:
            message = "Here are {} {}s near you:".format(len(buttons),
                                                         button_name)

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_message(message, buttons)

        return []