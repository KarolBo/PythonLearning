## Create test code for function with side effects (without changing code)

Although test driven development (TDD) has some strong advantages when it comes to code integrity and maintainability, there are quite
some cases that you will need to write tests for code that has been written already (either by you or others)
and cannot/should not be changed or refactored. 
 
In this case that is the code of the events API we have created. Since APIs, 
are almost always designed with a universal architecture and structure, an attempt to refactor its components only for 
the sake of testing, might create more problems that it solves.

Being able to write test code for existing software, is equally useful to writing tests together with the code itself.

## Challenge

For this challenge you need to create test to check if the `create_events` function works as it is supposed to.
That is to create an event in the database through a POST method. As you can see this is a function with side effects,
since it affects the system itself outside its scope. 

You have to assume that the `create_events` function should not be modified at all, since this might compromise the 
cohesion and consistency of the whole api and eventually break it.

HINT 1: For writing the test you can combine the functionality of `FastAPI` library with its testing capabilities.

HINT 2: When running the test script it will/should create a testing database `test.db` for the testing purposes, so that
the production database is not affected. 


## Solution (this should be sent afterwards with your explanation video (if applicable)

In the `test.py` you can see the implementation of the test script. Using testing functionality of FastAPI, 
we create a `TestClient` object which we use to create an event using the post method. 
We then fetch back the event created in the db and check if everything is as it should be.








