## Greeting story
* greet
    - utter_greet

## Greeting story
* deny
    - utter_sorry

## happy path
* inform
    - flight_booking_form
    - form{"name": "flight_booking_form"}
    - form{"name": null}
* affirm
    - utter_slots_values

## happy path
* inform{"from": "Milan"}
    - flight_booking_form
    - form{"name": "flight_booking_form"}
    - form{"name": null}
* affirm
    - utter_slots_values

## happy path
* inform{"to": "Milan"}
    - flight_booking_form
    - form{"name": "flight_booking_form"}
    - form{"name": null}
* affirm
    - utter_slots_values

## happy path
* inform{"time": "Tuesday"}
    - flight_booking_form
    - form{"name": "flight_booking_form"}
    - form{"name": null}
* affirm
    - utter_slots_values

## happy path
* inform{"from": "Milan", "to": "Milan"}
    - flight_booking_form
    - form{"name": "flight_booking_form"}
    - form{"name": null}
* affirm
    - utter_slots_values

## happy path
* inform{"from": "Milan", "time": "Tuesday"}
    - flight_booking_form
    - form{"name": "flight_booking_form"}
    - form{"name": null}
* affirm
    - utter_slots_values

## happy path
* inform{"to": "Milan", "time": "Tuesday"}
    - flight_booking_form
    - form{"name": "flight_booking_form"}
    - form{"name": null}
* affirm
    - utter_slots_values

## happy path
* inform{"from": "Milan", "to": "Milan", "time": "Tuesday"}
    - flight_booking_form
    - form{"name": "flight_booking_form"}
    - form{"name": null}
* affirm
    - utter_slots_values