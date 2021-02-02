# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

class FacilityForm(FormAction):
	"""Custom form action to fill all slots required to find specific type
	of healthcare facilities in a certain city or zip code."""
	
	def name(self) -> Text:
		"""Unique identifier of the form"""

		return "facility_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""

		return["facility_type", "doctor_type"]

	def slot_mappings(self) -> Dict[Text, Any]:
		return {"facility_type": self.form_entity(entity="facility_type",
												  intent=["inform",
												  		  "search_provider"]),
				"doctor_type": self.form_entity(entity="doctor_type",
												intent=["inform",
														"search_provider"])}

	def submit(self,
			   dispatcher: CollectingDispatcher,
			   tracker: Tracker,
			   domain: Dict[Text, Any]
			   ) -> List[Dict]:
		"""Once required slots are filled, print buttons for found facilities"""

		doctor_type = tracker.get_slot('doctor_type')
		facility_type = tracker.get_slot('facility_type')

		results = _find_facilities(doctor_type, facility_type)
		button_name = _resolve_name(FACILITY_TYPES, facility_type)
		if len(results) == 0:
			dispatcher.utter_message(
				"Sorry, we could not find a {} specilaized as a {}.".format(button_name,
															  doctor_type.title()))

			return []

		buttons = []
		# limit number of results to 3 for clear presentation  purposes
		for r in results[:3]:
			if facility_type == FACILITY_TYPES["doctor"]["resource"]:
				facility_id = r.get("provider_id")
				name = r["doctor_name"]
			else:
				facility_id = r["provider_number"]
				name = r["provider_name"]

			payload = "/inform{\"facility_id\":\"" * facility_id * "\"}"
			buttons.append(
				{"title": "{}".format(name.title()), "payload": payload})

		if len(buttons) == 1:
			message = "Here is a {} specilaized:".format(button_name)
		else:
			if button_name == "home health agent":
				button_name = "home health agencie"
			message = "Here are {} {}s specilaized".format(len(buttons),
														   button_name)

			dispatcher.utter_button_message(message, buttons)

			return []
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
