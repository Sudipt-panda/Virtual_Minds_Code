This is task 6.

Requirements for the task:
-Install Docker
-Install Docker-compose

Steps to exceute:
-Open command prompt from this folder
-Enter 'docker-compose up' command to build the docker images for the database and the app. 

Now the app is running on the localhost server in port 8080. You can access the app from your browser with the url 'http://localhost:8080/getvalues/"userId"'. 
Give the desierd userID in the above mentioned URL, to obtian the amount of advertisements the user has seen.
The database can be accessed directly (with mysql client 5.7) using the command 'mysql --host=127.0.0.1 --post=3200 -u root -p
