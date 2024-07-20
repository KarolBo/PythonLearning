## Change connection to database architecture to be handled by context manager

Context managers in Python are objects that define a runtime context within which certain 
operations can be performed. The most common use case for context managers is to ensure that 
resources are properly managed, such as closing a file after it has been read or written to, 
releasing a lock after it has been acquired, or closing a connection to a database after operations
have been performed.

Context managers are typically implemented using a "with" statement in Python, 
which allows you to define a block of code that will be executed within the context of 
the manager.

## Challenge

For this challenge, you need to refactor the events api to use a context manager to handle database
connection instead of the `get_db` function.



## Solution (this should be sent afterwards with your explanation video (if applicable)










