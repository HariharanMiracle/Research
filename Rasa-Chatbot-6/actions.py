from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction

import json
#
#
#
#
#
# Api connections

def _find_doctors1(location: Text, specialization: Text) -> List[Dict]:
    """Returns json of doctor appointment details matching the search criteria."""

    if str.isdigit(location):
        full_path = "http://localhost:9090/Echannel/listAllDoctorsByZipcodeAndSpecialization?specialization=" + specialization + "&zipcode=" + location
    else:
        full_path = "http://localhost:9090/Echannel/listAllDoctorsByLocationAndSpecialization?specialization=" + specialization + "&location=" + location
        
    print("Full path:")
    print(full_path)
    results = requests.get(full_path).json()
    return results

# Find appointments based on doctor name
# http://localhost:9090/Echannel/listAllDoctorsByDoctorName?doctorName=Dhivya
def _find_doctors2(doctor_name: Text) -> List[Dict]:
    """Returns json of doctor appointment details matching the search criteria."""

    full_path = "http://localhost:9090/Echannel/listAllDoctorsByDoctorName?doctorName=" + doctor_name
        
    print("Full path:")
    print(full_path)
    results = requests.get(full_path).json()
    return results

# Find appointments based on hospital name and specialization
# http://localhost:9090/Echannel/listAllDoctorsByHospitalAndSpecializatiom?specialization=Physician&hospital=Nawaloka
def _find_doctors3(hospitalName: Text, specialization: Text) -> List[Dict]:
    """Returns json of doctor appointment details matching the search criteria."""

    full_path = "http://localhost:9090/Echannel/listAllDoctorsByHospitalAndSpecializatiom?specialization=" + specialization + "&hospital=" + hospitalName
        
    print("Full path:")
    print(full_path)
    results = requests.get(full_path).json()
    return results        
#
#
#
#
#
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
                                                  intent=["inform"]),
                "location": self.from_entity(entity="location",
                                             intent=["inform"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        location = tracker.get_slot('location')
        specialization = tracker.get_slot('specialization')

        results = _find_doctors1(location, specialization)
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

# Displaying appointments for the user - Appointments are based on doctor name
class Chat_2_doctor_search_form(FormAction):
    """Custom form action to fill all slots required to find 
    the doctor appointment details"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "chat_2_doctor_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["doctor_name"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"doctor_name": self.from_entity(entity="doctor_name",
                                                  intent=["inform"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        doctor_name = tracker.get_slot('doctor_name')

        results = _find_doctors2(doctor_name)
        button_name = doctor_name

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

# Displaying appointments for the user - Appointments are based on hospital name
class Chat_3_doctor_search_form(FormAction):
    """Custom form action to fill all slots required to find 
    the doctor appointment details"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "chat_3_doctor_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["hospitalName", "specialization"]

    def slot_mappings(self) -> Dict[Text, Any]:

        return {"hospitalName": self.from_entity(entity="hospitalName",
                                                  intent=["inform"]),
                "specialization": self.from_entity(entity="specialization",
                                                  intent=["inform"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        hospitalName = tracker.get_slot('hospitalName')
        specialization = tracker.get_slot('specialization')

        results = _find_doctors3(hospitalName, specialization)
        button_name = hospitalName

        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find a {} in {}.".format(hospitalName,
                                                              hospitalName.title()))
            return []

        buttons = []
        # limit number of results to 3 for clear presentation purposes

        for r in results[:3]:
            appointmentSlotId = str(r.get("appointmentSlotId"))
            doctorName = str(r.get("doctorName"))
            hospital = str(r.get("hospitalName"))
            date = str(r.get("date"))
            time = str(r.get("time"))
            charge = str(r.get("charge"))
            address = str(r.get("address")) 

            details = " Appoitment: Doctor => " + doctorName.title() + ", Hospital => " + hospital.title() + ", Date => " + date.title() + ", Time => " + time.title() + ", Charge => " + charge.title() + ", Address => " + address.title() + ""

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
#
#
#
#
#
def _make_appointment(patient_name: Text, nic: Text, email_address: Text, contact_number: Text, appointmentSlotId: Text, credit_card: Text, cvv: Text) -> List[Dict]:
    """Appointment making function which retrns the status and message of making appointment"""

    full_path = "http://localhost:9090/Echannel/makeAppointment"
          
    print("Full path:")
    print(full_path)
    results = requests.post(full_path, data={'name': patient_name, 'nic': nic, 'email': email_address, 'contact': contact_number, 'aSlotId': appointmentSlotId, 'creditCardNumber': credit_card, 'cvc': cvv}).json()
    return results


class User_details_form(FormAction):
    """Custom form action to fill all slots required to make 
    an appointment"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "user_details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["patient_name", "contact_number", "email_address", "nic", "credit_card", "cvv"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"patient_name": self.from_entity(entity="patient_name",
                                                  intent=["inform"]),
                "contact_number": self.from_entity(entity="contact_number",
                                             intent=["inform"]),
                "email_address": self.from_entity(entity="email_address",
                                                  intent=["inform"]),
                "nic": self.from_entity(entity="nic",
                                                  intent=["inform"]),
                "credit_card": self.from_entity(entity="credit_card",
                                                  intent=["inform"]),
                "cvv": self.from_entity(entity="cvv",
                                                  intent=["inform"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, Triggering the appointment function"""

        patient_name = tracker.get_slot('patient_name')
        contact_number = tracker.get_slot('contact_number')
        email_address = tracker.get_slot('email_address')
        nic = tracker.get_slot('nic')
        credit_card = tracker.get_slot('credit_card')
        cvv = tracker.get_slot('cvv')
        appointmentSlotId = tracker.get_slot('appointmentSlotId')

        print("patient_name: " + patient_name)
        print("contact_number: " + contact_number)
        print("email_address: " + email_address)
        print("nic: " + nic)
        print("credit_card: " + credit_card)
        print("cvv: " +cvv)
        print("appointmentSlotId: " +appointmentSlotId)

        results = _make_appointment(patient_name, nic, email_address, contact_number, appointmentSlotId, credit_card, cvv)
        status = results.get("status")
        message = str(results.get("message"))

        if status == 0:
            dispatcher.utter_message(
                "Failed!!! " + message)
            return []
        else:
        	dispatcher.utter_message(
                "Success!!! " + message)

        return []
