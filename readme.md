#The purpose of this project
Create a way of using commandline to manage TFS(Team foundation server), provide some most commonly used functionalities such as listing the ticket the user is currently working, change the status of the ticket, show the parents of the ticket, show the children of the ticket and so on

##Configuration
Before using this tool, you need to configure your TFS info in the config.js file

##Config parameter
-------Accessing Setting-------
user: the TFS user
token: the token created for this user to access the database
baseUrl: the TFS domain name that you are going to access
-------Query Setting-------
assignTo: set to only show the ticket assigned to
path: set to only show the ticket that is under this path
fields: specify the fields that you want to show

##Command line
Quick mode
[-l]: list the tickets in the path you specified in the config js
[-t $num *]: list the detail of the specified tickets
Editing mode
[-s $num $num]set the value of the hour of specified ticket number
