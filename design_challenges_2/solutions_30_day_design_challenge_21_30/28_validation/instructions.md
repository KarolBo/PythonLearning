## Add validation for events and tickets

Data validation is something you definitely need when users fill in data into a system. This will sanitize your data,
preventing weird and unpredictable behavior later on that might cause very difficult and complicated bugs.


## Challenge

For this challenge you should add some validation checks for both the event and the tickets in our api. You should add 
at least the following checks:
1. The `available_tickets` upon event creation can not be negative
2. The `end_date` of an event can not be before the `start_date`
3. The `customer_email` should be valid

Hint: Since we are using pydantic classes for the `EventCreate` and `TicketCreate`, it would be nice if you used 
pydantic's in build validation functionality.


## Solution (this should be sent afterwards with your explanation video (if applicable)

Check the `EventCreate` and `TicketCreate` classes in the `api_app_validator.py` to see the implementation.
Try changing the `event_data` and `ticket_data` in the `use_api.py` to check that the validation works.











