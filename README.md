# Full Stack Software Challenge
This is the submission for the Fenix Full Stack Software Developer Take Home Assignment

###### Folder Structure
The Assignment has been divided into two folders : 
folder one - for Question 1 (Algorithms) 
folder two/payments - for Question 2. (Integrations)-Django Project


###### Execution for Question 1 (Algorithms):
This was done using conditional logic.
run the below code in the command line
 * python days_of_power.py 

###### Execution for Question 2

This was broken down in three parts:
* Create a database model class called MomoRequest to store the requests (Framework Django)
* Automatically trigger a collection request whenever a new MomoRequest object is created (Framework Django - Signals, MTN MoMoAPI)
* Periodically poll the status of any pending payments (Using an asynchronous task queue) and update the MomoRequest with the request status (Framework Django - celery,redis, MTN MoMo Api )
* Admin views have been created to ease usage for the application....
* Intergration with MoMo API have been placed in the mtn.py in the momo app folder and Header Settings have been placed in the settings.py
* Asychronous task queues have been placed in the tasks.py
* Test API:  ./manage.py test
