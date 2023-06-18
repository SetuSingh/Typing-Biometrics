# Typing-Biometrics

This project serves two main purposes: First, it aims to prevent brute force entry attempts. Second, it enables offline user authentication.

The provided Python program allows users to log in to their accounts based on their typing speed or a desired time duration for entering the password.

Brute force attacks are automated and typically involve entering and submitting passwords within milliseconds. By introducing a time variable to the login parameters, any brute force attack that doesn't match the user's typing pattern or password submission speed will be automatically rejected.

In this project, the TIME module is utilized. The time clock starts when the user begins entering the password and stops when they press enter. The recorded time is calculated and stored for future logins. Additionally, the user has the option to introduce a deliberate delay after entering the password to enhance security. For example, if a user chooses to wait for 5 seconds after entering the password, even if someone else knows the correct password, they won't be able to log in because they won't satisfy this additional condition.

To summarize, in this project, time is a crucial factor in ensuring secure user authentication, as it helps defend against brute force attacks and adds an extra layer of protection to the login process.
