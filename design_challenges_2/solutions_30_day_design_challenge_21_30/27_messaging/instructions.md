## Add notification functionality using the observer pattern

The observer pattern is a design pattern in which an object, called the subject, maintains a list of its dependents, 
called observers, and notifies them automatically of any state changes, usually by calling one of their methods. 
This pattern is useful in situations where multiple objects need to be informed of changes to the state of another 
object, without tightly coupling them together. It allows for loosely coupled and highly cohesive code that is easily 
maintainable and extendable.


## Challenge

For this challenge you should add a feature to the ticket API to be able to send confirmations to the customer. You 
should design it in such a way that you can easily add different types of confirmation (email, SMS, or both). Switching 
between different confirmation methods should be modular and without changing the code, itself.


## Solution (this should be sent afterwards with your explanation video (if applicable)

To implement the functionality using the observer pattern we create a `Confirmation` class that represents a 
confirmation method (e.g., email or SMS). We then define two concrete `Confirmation` classes, `EmailConfirmation` and 
`SMSConfirmation`, that implement the `send` method to send confirmation messages via email and SMS, respectively. 
The `send` method takes in a `Ticket` instance and sends a confirmation message to the customer associated with that 
ticket.

We also create a `TicketObserver` class that maintains a list of `Confirmation` instances. As long as a new `Ticket` 
instances is created it triggers the appropriate `Confirmation` instance, after creating to send a confirmation message.

To switch between different confirmation methods or email/SMS services, we simply detach the old instance and attach the 
new instance using the `TicketObserver.attach` and `TicketObserver.detach` methods.











