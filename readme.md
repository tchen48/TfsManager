#The purpose of this project
Create a  command line app for developers using TFS. The provide some most commonly used functionalities such as listing the tickets that user is currently working on, changing the status of the ticket, showing the parents of the ticket, showing the children of the ticket and so on

##Configuration
Before using this tool, you need to configure your TFS, and put your credentials and other pre-setting info in the config.js file

##Config parameter
-------Accessing Setting-------<br />
user: the TFS user <br />
token: the token created for this user to access the database<br />
baseUrl: the TFS domain name that you are going to access<br />
-------Query Setting-------<br />
assignTo: set to only show the ticket assigned to<br />
path: set to only show the ticket that is under this path<br />
fields: specify the fields that you want to show<br />

##Command line
Quick mode<br />
[-l]: list the tickets in the path you specified in the config js<br />
[-t $num *]: list the detail of the specified tickets<br />
Editing mode
[-s $num $num]set the value of the hour of specified ticket number<br />
