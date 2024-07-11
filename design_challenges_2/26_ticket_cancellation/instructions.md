## Add extra functionality to the events api

Using the ORM improved code we will add some extra functionality to the API.

## Challenge

For this challenge you will need to add some extra functionality to the api. The extra functionality should
implement the following:

1. Add a feature to allow for ticket cancellation. That should be for a single ticket based on its id but also
   in case an event is deleted all the related tickets should be deleted as well.
2. Add a feature to be able to change the name on the ticket.

For both of these features, the api should make sure that the event for which the ticket is for hasn't started yet.

## Solution (this should be sent afterwards with your explanation video (if applicable)

For implementing the extra functionality we added two extra functions in the api app `api_app_orm_added_features.py`,
`update_ticket_customer_name` and `delete_ticket`. We also updated the `delete_event` function to delete all the
tickets related to an event when the event is deleted.

Notice that for the updating of the ticket name functionality we added an extra dataclass `TicketUpdate` that only
contains 1 attribute i.e. the `customer_name` that needs to be updated. This way the request body data is mapped using
that class, before passed into the `update_ticket_customer_name`, so the request body handling inside the endpoint
functions is consistent.

### Important

Remember to delete the database from the local directory after every time you test something to avoid errors.
