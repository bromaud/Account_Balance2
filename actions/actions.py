
# This is a custom action which utters "Account Balance"

#from typing import Any, Text, Dict, List

#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher

#class ExtractNameEntity(Action):

#     def name(self) -> Text:
#         return "action_extract_name_entity"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         name_entity = next(tracker.get_latest_entity_values('name'), None)


#         if name_entity:
#             dispatcher.utter_message(text=f"Hello {name_entity}! I confirm your name is on my database, can i have your account number?")

#         else:
#             dispatcher.utter_message(text=f"I am sorry {name_entity}! I can't find your name in my database")

#         return []

#class ExtractAccountNumberEntity(Action):

#    def name(self) -> Text:
#        return "action_extract_account_number_entity"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#        account_number_entity = next(tracker.get_latest_entity_values('account_number'), None)

#        if account_number_entity:
#            dispatcher.utter_message(
#                text=f"I confirm your account number {account_number_entity} tallies with your name on my database, can i have your phone number?")

#        else:
#            dispatcher.utter_message(text=f"I am sorry, this account number {account_number_entity}, does not tally with your name in my database")

#        return []
#class ExtractPhoneNumberEntity(Action):

#    def name(self) -> Text:
#        return "action_extract_phone_number_entity"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#        phone_number_entity = next(tracker.get_latest_entity_values('phone_number'), None)

#        if phone_number_entity:
#            dispatcher.utter_message(text=f"Well done you are now fully verified)

#        else:
#            dispatcher.utter_message(text=f"I am sorry, this phone number {phone_number_entity}, does not tally with your details in my database")

#        return []


#class ActionSayBalance(Action):

#    def name(self) -> Text:
#        return "action_say_balance"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


#        name = tracker.get_slot("name")
#        account_number = tracker.get_slot("account_number")

#        dispatcher.utter_message(text=f"Thank you for your patience! Dear {name} your account number : {account number} has a balance of Rs. 1000.")

#        return []