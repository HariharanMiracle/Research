from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction


def _find_doctors(location: Text, specialization: Text) -> List[Dict]:
    """Returns json of facilities matching the search criteria."""

    if str.isdigit(location):
        full_path = "http://localhost:9090/Doctor/listAllDoctorsByLocation_ZipCodeAndSpecialization?specialization=" + specialization + "&zipcode=" + location
    else:
        full_path = "http://localhost:9090/Doctor/listAllDoctorsByLocationAndSpecialization?specialization=" + specialization + "&location=" + location
        
    print("Full path:")
    print(full_path)
    results = requests.get(full_path).json()
    return results


class DoctorForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of healthcare facilities in a certain city or zip code."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "doctor_form"

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

        results = _find_doctors(location, specialization)
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
            doctor_id = str(r.get("id"))
            name = r["name"]

            payload = "/inform{\"doctor_id\":\"" + doctor_id + "\"}"
            buttons.append(
                {"title": "{}".format(name.title()), "payload": payload})

        if len(buttons) == 1:
            message = "Here is a {} near you:".format(button_name)
        else:
        #     if button_name == "home health agency":
        #         button_name = "home health agencie"
            message = "Here are {} {}s near you:".format(len(buttons),
                                                         button_name)

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_message(message, buttons)

        return []


class FindDoctorDetails(Action):
    """This action class retrieves the address of the user's
    healthcare facility choice to display it to the user."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_doctor_details"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        doctor_id = tracker.get_slot("doctor_id")
        # healthcare_id = tracker.get_slot("facility_id")
        full_path = "http://localhost:9090/Doctor/getDoctorById?doctor_id=" + doctor_id

        print("Full path:")
        print(full_path)

        results = requests.get(full_path).json()
        if results:
            #selected = results[0]
            # if facility_type == FACILITY_TYPES["hospital"]["resource"]:
            
            # regNo = "{}".format(selected["regNo"].title())
            # doctor_name = "{}".format(selected["name"].title())

            regNo = "{}".format(results["regNo"].title())
            doctor_name = "{}".format(results["name"].title())

            return [SlotSet("regNo", regNo), SlotSet("doctor_name", doctor_name)]
        else:
            print("No address found. Most likely this action was executed "
                  "before the user choose a healthcare facility from the "
                  "provided list. "
                  "If this is a common problem in your dialogue flow,"
                  "using a form instead for this action might be appropriate.")

            return [SlotSet("regNo", "not found"), SlotSet("doctor_name", "not found")]


class ActionDoctorSearch(Action):

    def name(self) -> Text:
        return "action_doctor_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        special = tracker.get_slot("specialization")
        address = "300 Company st, Colombo"
        dispatcher.utter_message("Here is the address of the {}:{}".format(special, address))

        return [SlotSet("address", address)]






# class FacilityForm(FormAction):
#     """Custom form action to fill all slots required to find specific type
#     of healthcare facilities in a certain city or zip code."""

#     def name(self) -> Text:
#         """Unique identifier of the form"""

#         return "facility_form"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""

#         return ["facility_type", "location"]

#     def slot_mappings(self) -> Dict[Text, Any]:
#         return {"facility_type": self.from_entity(entity="facility_type",
#                                                   intent=["inform",
#                                                           "search_provider"]),
#                 "location": self.from_entity(entity="location",
#                                              intent=["inform",
#                                                      "search_provider"])}

#     def submit(self,
#                dispatcher: CollectingDispatcher,
#                tracker: Tracker,
#                domain: Dict[Text, Any]
#                ) -> List[Dict]:
#         """Once required slots are filled, print buttons for found facilities"""

#         location = tracker.get_slot('location')
#         facility_type = tracker.get_slot('facility_type')

#         results = _find_facilities(location, facility_type)
#         button_name = _resolve_name(FACILITY_TYPES, facility_type)
#         if len(results) == 0:
#             dispatcher.utter_message(
#                 "Sorry, we could not find a {} in {}.".format(button_name,
#                                                               location.title()))
#             return []

#         buttons = []
#         # limit number of results to 3 for clear presentation purposes
#         for r in results[:3]:
#             if facility_type == FACILITY_TYPES["hospital"]["resource"]:
#                 facility_id = r.get("provider_id")
#                 name = r["hospital_name"]
#             elif facility_type == FACILITY_TYPES["nursing_home"]["resource"]:
#                 facility_id = r["federal_provider_number"]
#                 name = r["provider_name"]
#             else:
#                 facility_id = r["provider_number"]
#                 name = r["provider_name"]

#             payload = "/inform{\"facility_id\":\"" + facility_id + "\"}"
#             buttons.append(
#                 {"title": "{}".format(name.title()), "payload": payload})

#         if len(buttons) == 1:
#             message = "Here is a {} near you:".format(button_name)
#         else:
#             if button_name == "home health agency":
#                 button_name = "home health agencie"
#             message = "Here are {} {}s near you:".format(len(buttons),
#                                                          button_name)

#         # TODO: update rasa core version for configurable `button_type`
#         dispatcher.utter_button_message(message, buttons)

#         return []