# Feedback-Automation

This is simple python script for automating 
your Feedback survey with out Login_Credentials (ID and Password).
This script uses a session_cookie to automate your survey in a minute.
Manually giving Feedback would take nearly 20 minutes.
Follow some steps and get this done in a minute and SAVE YOUR TIME.


## Steps to follow

1.Open your firefox browser. 2. Login in your HUB using your login_credentials.
 3. Right click and inspect any element and then click on network tab.
  4.Refresh the page again then you can see an index file under the file tab in the network tab.
  5.Click on it you will find Cookies and copy the cookie called session_id_hub copy the value
  then open new tab in the browser and paste it in the input field of url: (https://take-survey-feed.herokuapp.com/welcome)
  and click on submit
  if you see aplication error don't worry go back and paste the cookie again and submit
 as there is a timeout limit for scripts on server it throws an application error.
 exactly it throws that error 2 times after in 3rd attempt you see a Thank you message and the survey is done.. 
  

NOTE : Don't logout hub from previous tab untill your survey get completed 
 

