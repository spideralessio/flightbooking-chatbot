# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_core_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
import random
import pyrfc3339

DUCKLING_HOST = "http://0.0.0.0:8000/parse"

class FlightBookingForm(FormAction):

    def name(self) -> Text:
        return "flight_booking_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["from", "to", "time"]

    

    # def valitime_from(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Valitime cuisine value."""
    #     oks = ["tuesday"]
    #     if value.lower() in oks:
    #         return {"time": value}
    #     else:
    #         # utter submit template
    #         dispatcher.utter_message(template="utter_not_found")
    #         return {"time": None}

    # def valitime_to(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Valitime cuisine value."""
    #     oks = ["tuesday"]
    #     if value.lower() in oks:
    #         return {"time": value}
    #     else:
    #         # utter submit template
    #         dispatcher.utter_message(template="utter_not_found")
    #         return {"time": None}

    def valitime_time(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Valitime cuisine value."""
        time = pyrfc3339.parse(value)
        def suffix(d):
            return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

        def custom_strftime(format, t):
            return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


        return {"time": custom_strftime("%A, {S} %d, %Y at %H:%M", time)}
        # items = json.loads(requests.post(DUCKLING_HOST, data={"locale":"en", "text":value}).text)
        # items = [item for item in items if item["dim"] == "time"]
        # if len(items) == 1:
            
        # else:
        #     dispatcher.utter_message(template="utter_time_error")
        #     return {"time": None}


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        dispatcher.utter_message(template="utter_submit")


            
        return []


