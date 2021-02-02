# This file is to train the actions.py
# This is the model which is used to deal with the back-end functions and the user inputs
# This model is already trained with the samples

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



def _find_first_aid_tip(cause: Text) -> List[Dict]:
    url = 'https://d0259b50553a.ngrok.io/instructions'
    # url = 'https://api.example.com/api/dir/v1/accounts/9999999/orders'
    headers = {'Content-Type' : 'application/json'}
    r = requests.post(url, data={'input': cause}, headers=headers)
    print(r.text)
    return r


# Find appointments based on specialization and location
# http://localhost:9090/Echannel/listAllDoctorsByZipcodeAndSpecialization?specialization=cardiologist&location=Colombo
# http://localhost:9090/Echannel/listAllDoctorsByZipcodeAndSpecialization?specialization=cardiologist&zipcode=000010
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
# http://localhost:9090/Echannel/listAllDoctorsByDoctorName?doctorName=Hariharan
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

# Login function
# Post function => http://localhost:9090/Echannel/login
def _login(username: Text, password: Text) -> List[Dict]:
    """Registration"""

    full_path = "http://localhost:9090/Echannel/login"
          
    print("Full path:")
    print(full_path)
    results = requests.post(full_path, data={'id': '0', 'username': username, 'password': password, 'nic': '', 'email': '', 'contact': ''}).json()
    return results

# Registration function
# Post function => http://localhost:9090/Echannel/register
def _registration(username: Text, password: Text, nic: Text, email: Text, contact_number: Text) -> List[Dict]:
    """Registration"""

    full_path = "http://localhost:9090/Echannel/register"
          
    print("Full path:")
    print(full_path)
    results = requests.post(full_path, data={'id': '0', 'username': username, 'password': password, 'nic': nic, 'email': email, 'contact': contact_number}).json()
    return results

# Make an appointment function
# Post function => http://localhost:9090/Echannel/makeAppointment
def _make_appointment(patient_name: Text, appointmentSlotId: Text, credit_card: Text, cvv: Text, username: Text) -> List[Dict]:
    """Appointment making function which retrns the status and message of making appointment"""

    full_path = "http://localhost:9090/Echannel/makeAppointment"
          
    print("Full path:")
    print(full_path)
    results = requests.post(full_path, data={'name': patient_name, 'aSlotId': appointmentSlotId, 'creditCardNumber': credit_card, 'cvc': cvv, 'username': username}).json()
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

            details = " Appoitment id ["+appointmentSlotId+"] : Doctor => " + doctorName.title() + ", Hospital => " + hospitalName.title() + ", Date => " + date.title() + ", Time => " + time.title() + ", Charge => " + charge.title() + ", Address => " + address.title() + ""

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

        return ["name"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"name": self.from_entity(entity="name",
                                                  intent=["inform"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        doctor_name = tracker.get_slot('name')



        results = _find_doctors2(doctor_name)
        button_name = doctor_name

        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find a {} in {}.".format(button_name,
                                                              location.title()))
            return [SlotSet("name", None)]

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

            details = " Appoitment id ["+appointmentSlotId+"]: Doctor => " + doctorName.title() + ", Hospital => " + hospitalName.title() + ", Date => " + date.title() + ", Time => " + time.title() + ", Charge => " + charge.title() + ", Address => " + address.title() + ""

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

        return [SlotSet("name", None)]
#
#
#
#
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

            details = " Appoitment id ["+appointmentSlotId+"]: Doctor => " + doctorName.title() + ", Hospital => " + hospital.title() + ", Date => " + date.title() + ", Time => " + time.title() + ", Charge => " + charge.title() + ", Address => " + address.title() + ""

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
class User_details_form(FormAction):
    """Custom form action to fill all slots required to make 
    an appointment"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "user_details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["name", "credit_card", "cvv"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"name": self.from_entity(entity="name",
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

        patient_name = tracker.get_slot('name')
        username = tracker.get_slot('username')
        credit_card = tracker.get_slot('credit_card')
        cvv = tracker.get_slot('cvv')
        appointmentSlotId = tracker.get_slot('appointmentSlotId')

        print("patient_name: " + patient_name)
        print("credit_card: " + credit_card)
        print("cvv: " +cvv)
        print("appointmentSlotId: " +appointmentSlotId)

        results = _make_appointment(patient_name, appointmentSlotId, credit_card, cvv, username)
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
#
#
#
#
#
class first_aid_tip_form(FormAction):
    """Custom form action to fill all slots required to find 
    the first aid tip"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "first_aid_tip_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["cause"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"cause": self.from_entity(entity="cause",
                                                  intent=["firstaid"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        cause = tracker.get_slot('cause')

        # response = json from API
        # response['data'] ----> SPECIALIZATION OR INSTRUCTIONS

        # results = _find_first_aid_tip(cause)
        # results = "### Null ###"
        # print("result => ")
        # print(results)
        button_name = cause

        # if len(results) == 0:
        #     dispatcher.utter_message(
        #         "Sorry, we could not find a first aid tip for {}.".format(button_name))
        #     return []

        buttons = []
        # # limit number of results to 3 for clear presentation purposes
        display = "text"
        
        message = "First aid tip: {}".format(display)
        # message = "First aid tip for {} is {}".format(button_name, results.text)

        # # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_message(message, buttons)

        return []
#
#
#
#
#
class login_form(FormAction):
    """Custom form action to fill all slots required to make 
    an registration"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "login_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["username", "password"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"username": self.from_entity(entity="username",
                                                  intent=["inform"]),
                "password": self.from_entity(entity="password",
                                                  intent=["inform"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, Triggering the appointment function"""

        username = tracker.get_slot('username')
        password = tracker.get_slot('password')
        var_none = tracker.get_slot('var_none')

        print("username: " + username)
        print("password: " + password)

        results = _login(username, password)
        status = results.get("status")
        message = str(results.get("message")) 

        if status == 0:
            dispatcher.utter_message(
                "Failed!!! " + message)
            return [SlotSet("username", var_none), SlotSet("password", var_none), SlotSet("login_auth", "0"), FollowupAction("login_form")]
        else:
        	dispatcher.utter_message(
                "Loggged in successfully!!! How can I help you?")

        return [SlotSet("login_auth", "1")]
#
#
#
#
#
class specialization_form(FormAction):
    """Custom form action to fill all slots required to find 
    the specialization form"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "specialization_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["symptoms"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"symptoms": self.from_entity(entity="symptoms",
                                                  intent=["inform"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        symptoms = tracker.get_slot('symptoms')
        print(symptoms)

        # response = json from API
        # response['data'] ----> SPECIALIZATION OR INSTRUCTIONS

        # results = _find_first_aid_tip(cause)
        # results = "### Null ###"
        # print("result => ")
        # print(results)
        button_name = symptoms

        # if len(results) == 0:
        #     dispatcher.utter_message(
        #         "Sorry, we could not find a first aid tip for {}.".format(button_name))
        #     return []

        buttons = []
        # # limit number of results to 3 for clear presentation purposes
        display = "text"
        
        message = "Specialization: {}".format(display)
        # message = "First aid tip for {} is {}".format(button_name, results.text)

        # # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_message(message, buttons)

        return []
#
#
#
#
#
class registration_form(FormAction):
    """Custom form action to fill all slots required to make 
    an registration"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "registration_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["username", "password", "nic", "email_address", "contact_number"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"username": self.from_entity(entity="username",
                                                  intent=["inform"]),
                "password": self.from_entity(entity="password",
                                             intent=["inform"]),
                "nic": self.from_entity(entity="nic",
                                                  intent=["inform"]),
                "email_address": self.from_entity(entity="email_address",
                                                  intent=["inform"]),
                "contact_number": self.from_entity(entity="contact_number",
                                                  intent=["inform"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, Triggering the appointment function"""

        username = tracker.get_slot('username')
        password = tracker.get_slot('password')
        nic = tracker.get_slot('nic')
        email_address = tracker.get_slot('email_address')
        contact_number = tracker.get_slot('contact_number')
        var_none = tracker.get_slot('var_none')

        print("username: " + username)
        print("password: " + password)
        print("nic: " + nic)
        print("email_address: " + email_address)
        print("contact_number: " + contact_number)

        results = _registration(username, password, nic, email_address, contact_number)
        status = results.get("status")
        message = str(results.get("message"))

        if status == 0:
            dispatcher.utter_message(
                "Failed!!! " + message)
            return [SlotSet("username", var_none), SlotSet("password", var_none), SlotSet("nic", var_none), SlotSet("email_address", var_none), SlotSet("contact_number", var_none), SlotSet("register_auth", "0"), FollowupAction("registration_form")]
        else:
        	dispatcher.utter_message(
                "Registered successfully!!! How can I help you?")

        return []