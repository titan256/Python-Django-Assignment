# Full-Stack-Software-Fenix
This is the submission for the Fenix Full Stack Software Developer Take Home Assignment

###### Folder Structure
The Assignment has been divided into two folders : 
folder one - for Question 1 (Algorithms) 
folder two/payments - for Question 2. (Integrations)-Django Project


###### Execution for Question 1 (Algorithms):
This was done using conditional logic.

run the below code in the command line:
 *python days_of_power.py 

###### Execution for Question 2

This was broken down in three parts:
* Create a database model class called MomoRequest to store the requests (Framework Django)
* Automatically trigger a collection request whenever a new MomoRequest object is created (Framework Django - Signals)
* Periodically poll the status of any pending payments (Using an asynchronous task queue) and update the MomoRequest with the request status (Framework Django - celery,redis )

* Admin views have been created to ease usage for the application....
