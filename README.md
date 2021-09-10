# Typing-Biometrics

This project was meant for 2 purposes:
  1st: Defeat BruteForce entry.
  2nd: Authorize  user offline.
  
The python program provided allows user to login into the account based on their typing speed or desired time duration to enter the password.

Bruteforce attacks are automated attacks and hence they enter and submit password withing milli-seconds. So now that we have added this time variable to our login paramaters, any brute force attack will be automatically discarded as it won't match the typing pattern/ password submission speed of the user.

In this project i took advantage of TIME module. 

Time clock starts when user starts entering password and stops when user hits enter. Time take in calculates and recorded for fututre logins.
Here user can wait for desired amount of time after enetering password to make it more secure. For ex: Lets say a user decides to wait for 5 seconds after entering the passsword,later on if any other person tries to login into his or her account even after knowing the exact password , they won't be able to as we have added one more condition to satisfy!

"TIME ISN'T THE MAIN THING,IT'S THE ONLY THING" - Miles Davis
