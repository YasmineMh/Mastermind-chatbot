from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import logging
from random import randrange


# logger variable for tracking
logger = logging.getLogger(__name__)


def check_unique_digits(attempt_number):
    if (
        attempt_number[0] not in attempt_number[1:] and
        attempt_number[1] not in attempt_number[2:] and
        attempt_number[2] not in attempt_number[3:]
    ):
        return True
    return False


# Create a custom action for attempt field
class AskForAttempt(Action):
    def name(self) -> Text:
        return "action_ask_attempt"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        attempts = tracker.get_slot("attempts")

        if attempts is None:
            attempts = []

        dispatcher.utter_message(
            text="Attempt {} : Could guess the number?".format(len(attempts) + 1)
        )

        return [SlotSet("attempts", attempts)]


class ValidateFormGame(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_game"

    def validate_attempt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `attempt` value."""

        chosen_number = tracker.get_slot("chosen_number")
        attempts = tracker.get_slot("attempts")
        previous_cp = tracker.get_slot("previous_cp")
        previous_ip = tracker.get_slot("previous_ip")

        # if attempts is None:
        #     attempts = []
        if previous_cp is None:
            previous_cp = []
        if previous_ip is None:
            previous_ip = []

        attempts.append(slot_value)

        if chosen_number == slot_value:
            return {"attempt": "win"}

        elif len(attempts) == 10:
            return {"attempt": "loose"}

        else:

            if not slot_value.isdigit():
                dispatcher.utter_message(
                    text="The number must only contain digits from 0 to 9"
                )
                return {"attempt": None}

            if len(slot_value) != 4:
                dispatcher.utter_message(
                    text="The number must contain 4 digits from 0 to 9"
                )
                return {"attempt": None}

            if not check_unique_digits(slot_value):
                dispatcher.utter_message(
                    text="The number must contain 4 different (unique) digits."
                )
                return {"attempt": None}

            incorrect_position = 0
            correct_position = 0

            for i in range(0, 4):
                if slot_value[i] == chosen_number[i]:
                    correct_position += 1
                elif slot_value[i] in chosen_number:
                    incorrect_position += 1
            previous_cp.append(correct_position)
            previous_ip.append(incorrect_position)

            dispatcher.utter_message(text="Those are your previous attempts:")

            for index, i in enumerate(attempts):
                dispatcher.utter_message(
                    text="In {attempt} : {correct_position} CP and {incorrect_position} IP".format(
                        attempt=i,
                        correct_position=previous_cp[index],
                        incorrect_position=previous_ip[index],
                    )
                )
            return {
                "attempt": None,
                "attempts": attempts,
                "previous_cp": previous_cp,
                "previous_ip": previous_ip,
            }


# Submit submit_form_game form
class SubmitFormGame(Action):
    def name(self) -> Text:
        return "submit_form_game"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        slots = []
        attempt = tracker.get_slot("attempt")
        attempts = tracker.get_slot("attempts")
        chosen_number = tracker.get_slot("chosen_number")

        if attempt == "win":
            dispatcher.utter_message(
                text="Congratulations! You did a great job! You guessed the number in {} attempts".format(
                    len(attempts)
                )
            )

        else:
            dispatcher.utter_message(
                text="Unfortunately, you lost by completing your 10 attempts without guessing the number! The number that I chose was {}".format(
                    len(chosen_number)
                )
            )

        slots.append(SlotSet("attempt", None))
        slots.append(SlotSet("attempts", []))
        slots.append(SlotSet("previous_cp", []))
        slots.append(SlotSet("previous_ip", []))
        return slots


class ActionGenerateNumber(Action):
    def name(self) -> Text:
        return "action_generate_number"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        chosen_number = ""

        list_numbers = [i for i in range(0, 10)]

        for i in range(0, 4):
            randomInt = randrange(10 - i)
            chosen_number += str(list_numbers[randomInt])
            list_numbers.remove(list_numbers[randomInt])

        logger.info(
            "The generated number for this round is : {chosen_number}".format(
                chosen_number=chosen_number
            )
        )
        dispatcher.utter_message(text="I chose a number")

        return [SlotSet("chosen_number", chosen_number)]
