# Programming Assignment 1: Asterix and the Olympic Games (Winter Olympics Edition)

<center>Due: Friday March 2, 2018, 23:59 hours</center>

### Instructions
- You may work in groups of two for this lab assignment.
- This project has two purposes: first to familiarize you with sockets/RMIs/REST, processes, threads; second to learn the design and internals client-pull and server-push systems.

This repo contains assignment description, starter-code, and other resources for the first lab assignment.
+ Once you are done with your assignment, commit with the message **final**.
+ Points will be given for ease of reproducibility and readability. So try and make it easy for us.
+ Modify this `README` with instructions to run your code. 
+ Comment your code for readability.
+ Source code goes into the `src` directory. Tests go into tests and documentation


## A: The problem
- The year is 50 B.C. Gauls, led by Asterix, look forward to challenging the Romans in the latest edition of the ancient Olympic games. Gauls have made tremendous technological progress since the previous olympics and have finally entered the "smart" stone-age. Every Gaul now has a stone tablet that gives them the latest sports scores of their fellow villagers. Each smart-stone (not to be confused with a smart-phone, which are yet to be invented) is updated by Obelix (a sculpter by profession), who has tasked by the village chief to disseminate the latest scores by engraving them onto each stone tablet. You are tasked to design a distributed system using a client-server architecture to efficiently disseminate latest scores to the villagers.
Assume that there are N tablets, each of which is a client, that needs to be periodically updated with sports scores. (N should be configurable in your system).

	First design a client-pull architecture where each client tablet refreshes the medal tally by periodically pulling the latest data from Obelix's stone server. Additionally a client tablet can also request the current score for an ongoing sports event and receive a response from the server.

	Cacofonix, the village bard, is responsible for providing Obelix's server live updates from the olympic stadium, which he does by singing the scores and thereby sending updated scores to the server. Since Gauls are restful by nature, they have chosen to use the RESTful API for client-sever communications. The RESTful interface provides a simple method for RPC-like communication over HTTP.


    
- Your system should implement the following REST endpoints:
	1. **SERVER_IP:80/getMedalTally/teamName**  
	This should return a json object that contains the number of gold, silver and bronze leafs earned by the specified teamName. Your system should track medal tallies for at least two teams, namely Gual and Rome.
    
	2. **SERVER_IP:80/incrementMedalTally/teamName/medalType/auth_id**  
This increments the medal tally for the specified team, and medalType can be bronze, silver, or gold and the appropriate medal count for that team is incremented. The auth_id variable should be an id unique to Cacofonix used to authorize the action. This should return a success message on successful increment by Cacofonix and a failure message if anyone other than Cacofonix tries to increment the tally.
	3. **SERVER_IP:80/getScore/eventType**  
This should return a json object with the latest score for each team for the specified eventType. Pick at least three winter Olympics events such as stone Curling and stone skating and provide scores for these events.
	4. **SERVER_IP:80/setScore/eventType/rome_score/gaul_score/auth_id**  
This updates the current score for the specified event. The auth_id variable should be an id unique to Cacofonix used to authorize the action. The variables gaul_score and rome_score should be the new score values for each team. This should return a success message on successful update by Cacofonix and a failure message if anyone other than Cacofonix tries to update the score.  

While any stone tablet client can request scores or medal tallies (and can do so concurrently), only the Cacofonix's update process can increment medal tallies and scores in the system. This can be accomplished by sending an authorization id with update requests that you can use to verify permissions. Design each tablet as a separate process, the server is its own process and so is Cacofonix update process. Your client-pull system should be able to handle multiple concurrent requests from different tablets and also concurrent queries and updates. Thus you should implement python threading in the sports server and also use proper synchronization at the server to ensure correctness. You are free to use any server architecture to handle concurrent requests, such as a thread per request model, a pre-spawned pool of threads or event-based architectures.


- Since stone curling is a very popular event among the Gauls, the chief has decreed that a server-push architecture be used to efficiently and immediately disseminate score updates to each tablet. Before a curling event begins, any Gaul interested in receiving push notifications registers with the server. When a curling event is in progress, updates are pushed from the server to all registered tablets whenever any update is received from Cacofonix's update process. 

	**Your system should implement the following interfaces for server-push mode:**
	1. **SERVER_IP:80/registerClient/clientID/eventType**  
This registers a client tablet to receive push updates for the specified eventType.

 	2. **Client_IP:80/pushUpdate/variable1/variable2/variable3/...etc**  
This should be called for all registerd clients and pushes an update of the current state to all registered clients.

	For the push mode, you can implement a separate application to run on the client tablet than the above pull-based application. That is, there is no need to write an integrated client that provides both push and pull functions, although you are certainly allowed (and encouraged) to do so.

- **REST Interface**   
 As noted above, your system should use a REST client/server architecture. This means creating several endpoints that correspond to the interfaces provided above.
	- A sample endpoint for the `getMedalTally(teamName)` interface may be of the following form:  
`serverIP:80/getMedalTally/teamName`  
	- Clients can make this api call to the server and will receive back a json object of the following form:  
		```
		{
  			"medals": {
    			"bronze": 0, 
    			"gold": 2, 
    			"silver": 5
  			}
		}  
		```
	- This can be extended to update scores and register clients for push mode.
	- While we recommend using GET requests for simplicity, feel free to use PUT/POST requests if you find them easier to use.
	- While python web frameworks such as Django or Flask make is simple to write web application using REST interfaces, in this case, you should write your own code rather than using a python web framework. However, you are encouraged to use a simple library such as [RESTArt](https://restart.readthedocs.io/en/latest/)  to implement the REST interface. In addition, you should use Python Threads interface (see [Python 3 Threading](https://docs.python.org/3/library/threading.html) or [Python 2 Threading](https://docs.python.org/2/library/threading.html)) to implement a multi-threaded sports server to handle concurrent requests. Of course, an event-based server with non-blocking I/O can also be used for concurrency if you so wish.



- Other requirements:
	1. For your multi-threaded server, be aware of the thread synchronizing issues to avoid inconsistency, race conditions or deadlock in your system.
	2. No GUIs are required. Simple command line interfaces and textual output of scores and medal tallies are fine.
	3. A secondary goal of this and subsequent labs is to make you familiar with modern software development practices. Familiarity with source code control systems (e.g., git, mercurial, svn) and software testing suites is now considered to be essential knowledge for a Computer Scientist. In this lab, you will use github for a source code control repository. You will need to create a free student github account and work on this project using a repository that we have created using github classroom. Please make sure you use multiple commits and provide detailed commit messages. You will be evaluated on your use of effective commits. Instructions for doing so as well as as pointers to a git tutorial are here.
	4. A related goal is to ensure you properly test you code. You can create specific scenarios and/or inputs to test your code and verify that it works as expected. Unit testing frameworks are fine to use here, but do keep in mind that this is a distributed application with peers running on different machines. So testing is more complex in this setting. For the purposes of the lab, you should write three tests of your choice either using a testing framework or using your own scripts/inputs to test the code. The tests and test output should be submitted along with your code.
	
	We do not expect elaborate use of github or testing frameworks - rather we want you to become familiar with these tools and start using them for your lab work (and other programs you write).

## B. Evaluation and Measurement
1. Deploy at least 6 clients, a server and an update process. They can be setup on the same machine (different directories) and have the client tablets make several requests and provide the output as part of your submission. Do the same for the server push mode.
2. Next deploy the clients and the server such that at least some of the processes are on different machines and demonstrate that your system works over a network for both client-pull and server-push modes. You are free to develop your solution on any platform, but please ensure that your programs compile and run on the [edlab machines](http://www-edlab.cs.umass.edu/) (See note below).
3. Conduct a few experiments to evaluate the behavior of your system under different scenarios. Change the rate at which updates are requested, or change the number of clients and measure the latencies to get a reply. In the server push mode, measure how long it takes for the server to push out an update to N clients for different values of N. Report any insights, if any, from your experiments, as to which strategies succeed the best.

## C. What you will submit
- When you have finished implementing the complete assignment as described above, you will submit your solution in the form of a zip file that you will upload into moodle. **Please also upload everything to your github repo and tag it with `lab1_final_submission`**.
- Each program must work correctly and be **documented**. The code file you commit to github should contain:
	1. An electronic copy of the output generated by running your program. Print informative messages when a client or server receives and sends key messages and the scores/medal tallies.
	2. A separate document of approximately two pages describing the overall program design, a description of "how it works", and design trade-offs considered and made. Also describe possible improvements and extensions to your program (and sketch how they might be made). You also need to describe clearly how we can run your program - if we can't run it, we can't verify that it works.
	3. A program listing containing in-line documentation.
	4. A separate description of the tests you ran on your program to convince yourself that it is indeed correct. Also describe any cases for which your program is known not to work correctly.
	5. A separate description of the tests you ran on your program to convince yourself that it is indeed correct. Include the testing code you constructed, describe the tests, inputs and outputs of the tests (and how the output shows that the test was a success). Also describe any cases for which your program is known not to work correctly.
	6. Performance results: Include a results of experiments you ran.
	7. Performance results.


## D. Grading policy for all programming assignments
1. Program Listing  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;works correctly ------------- 50%  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in-line documentation -------- 15%  
2. Design Document  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quality of design and creativity ------------ 10%  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;understandability of doc ------- 10%  
3. Use of github with checkin comments --- 5%
4. Thoroughness of test cases and test output---------- 10%

**Grades for late programs will be lowered 12 points per day late.**


### Note about edlab machines
- We expect that most of you will work on this lab on your own machine or a machine to which you have access. However we will grade your submission by running it on the EdLab machines, so please keep the following instructions in mind.
- You will soon be given accounts on the EdLab. Read more about edlab and how to access it [here](http://www-edlab.cs.umass.edu/).
- Although it is not required that you develop your code on the edlab machines, we will run and test your solutions on the edlab machines. Testing your code on the edlab machines is a good way to ensure that we can run and grade your code. Remember, if we can't run it, we can't grade it.
- There are no visiting hours for the edlab. You should all have remote access to the edlab machines. Please make sure you are able to log into and access your edlab accounts.

### Stumped?
- Who are the Gauls? Read about them on [Wikipedia](http://en.wikipedia.org/wiki/Asterix).
- Stumped on how to proceed? Review the comic book [Asterix at the Olympic Games](http://en.wikipedia.org/wiki/Asterix_at_the_Olympic_Games) from your local library. Better yet, ask the TA or the instructor by posting a question on the Piazza 677 questions. General clarifications are best posted on Piazza. Questions of a personal nature regarding this lab should be asked in person or via email.

