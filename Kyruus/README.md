# README #

The goal is to spend 90 minutes and build out the flow to create an appointment against a doctor. Doctors don't have tightly controlled schedules; they're very unlike yours & my Google calendars. Doctors explicitly open up certain times during the day, and patients can book only into those free areas.

This is like seeing a movie at the theater. You can't arbitrarily see a movie at any time; there are published start times, and you get tickets. 

Therefore this problem is to:
1) Create a way to model a doctor's free times (availability)
2) Create a way to book an appointment against that free time

This repository contains the outlines of a web API.

We've built two skeletons for this project. One uses a SQL database (sqlite, without an ORM), 
and one is entirely in-memory using data structures that mimic a database.

Decide which skeleton you'd like to use, and extend it (we do prefer the SQL version).

### IMPORTANT !!!!!

If you do this as a "take home", prior to your interview, do not spend too much time on it.

We're happy to do this entirely on-site, during your interview, as a paired programming exercise in Python.

We're also happy to do this as a code review, where you do it at home in the language of your choice and we review it in-person. In this case, we prefer Python, but it's even more important that you do it in a language in which you're very comfortable.

If you were to do it entirely on-site, you'd only have 90 minutes. Therefore, it's fine to aim for the same amount of time at home.

Part of the exercise is to see what tradeoffs you make, and explain them when talking through the solution. How did you prioritize what to build first? What, if anything, would you do differently if you had to put this code into production?

Note: if you would like to do it in something other than Python, please do it as a take-home, but still aim for the 90 minute mark.

### Problem statement

We would like to build a simple service for managing doctors and their schedules. 
Requirements:

* For each doctor we would initially like to store the following:
    * id
	* name
	* locations - represented as a collection of address strings
	* schedule - weekly schedule indicating the hours they are available each day of the week
* CRUD operations for doctors
* Ability to book an appointment with a doctor (a tuple of (doctor, location, time))
* Ability to get all appointments for a doctor
* Ability to cancel an appointment with a doctor

Expectations/assumptions:

* The API will be internally-facing and used by other applications/services that we trust
* The API will be single-tenant (it only contains data for a single hospital)
* A doctor is available at any of their locations for any of their available times
* A doctor can only have one appointment at a time
* A doctor can travel instantaneously between locations
* No UI/front-end is expected

#### Prerequisites

* [Python 2.7](https://www.python.org/downloads/)
* [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* [git](https://git-scm.com/downloads)
* [flask 1.0.2](http://flask.pocoo.org/)

	
# Running things

## Database version

* Create (or reset) the database: `./init_database.sh`
* Run the server: `./run_in_database.sh`

In another terminal, run things like `curl http://localhost:5000/doctors`

Run tests with `pytest in_database`

## In-memory version

* Run the server: `./run_in_memory.sh`

In another terminal, run things like `curl http://localhost:5000/doctors`

Run tests with `pytest in_memory`

#### Extra questions ####

Below are a few questions which expand the scope of the service. Please pick one and describe your approach.

* What are some real-world constraints to booking appointments that would add complexity to this API and how would they impact the design.
* How would our design change if this API was opened up to external users?
* What concerns are there with multi-tenant data management and how could we modify the design to increase data security?

#### Suggestions ####

* Start simple 
* Document your assumptions and their impact on the design
* Stub out areas that are not related to core functionality and describe their expected behavior
* You may choose any means of persistence (ex: database, third-party service, etc.) or choose to exclude it (e.g. in-memory only). We recognize that integrating with a persistence layer may be time-consuming and by omitting it, more time can be allocated to service development.
* You may use any third-party libraries you feel are appropriate

### Who do I talk to? ###
* If you have any questions prior to your interview, please reach out to your designated Kyruus recruiting contact and he/she will get back to you as soon as possible.
* If you have any feedback on the interview question after you're done, let us know, we're always looking into improving the interview process. Thanks!
