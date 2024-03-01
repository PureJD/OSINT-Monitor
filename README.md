# OSINT Flagging Monitor Tool
### This is a tool devised for use within OSINT investigations in which a website is under investigation and updates to the site are expected and need to be recorded.
![Tech globe](https://media.istockphoto.com/id/1405728317/vector/global-network-connection-world-map-point-and-line-composition-concept-of-global-business.jpg?s=612x612&w=0&k=20&c=u_DZ9MwU6DFC0-TVD4qnZFmHDu2PoWYhDzppUaijv-c=)

### - In the program code the user is required to set the email address they wish to recieve notifications on as well as the website they wish to be observed. 

### - The code performs the following;
- Attends the web page selected and captures the HTML using the Requests Library and stores the HTML in a variable.
- The code will then wait for a set period (adjustable) and once again visit the website, it will save the HTML into a new variable and compare the two.
- If the HTML is the same the program will repeat the above step until stopped or a change is detected.
- If a change is detected the program will create an HTML file containing the code with a timestamp, compose an email, attach the HTML code and send the email notification to the selected address (The user's address).
- The code will then continue for changes and record the HTML and send emails for every subsequent change. 
![Notification view](https://github.com/PureJD/OSINT-Monitor/blob/main/Screenshot.png?raw=true)

# Items of note
#### The code has been aimed at Google due to the fact Google does change and a notification will be sent immediately to demonstrate the program's capabilities. The program has also been tested on my personal site, on which I made a change to the HTML and recieved a notification. 

#### The email address used to send the notifications has been created solely for this purpose. This address contains no personal information of any kind and can be used by others or changed to your own outlook address. 

![GitHub Logo](https://github.com/github.png)