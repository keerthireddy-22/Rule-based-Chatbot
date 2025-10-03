# Rule-based-Chatbot
A Simple Rule-Based Chatbot using if-elif-else statements

This Python script, named rule_based_chatbot.py, sets up a simple, rule-based chatbot called "Rule-Bot."

The entire application runs within the chatbot() function, which starts by printing an introductory message. The heart of the program is the continuous conversation loop, created using while True, which allows the bot to repeatedly take input from the user. For effective matching, the script immediately converts the user's input to lowercase and removes any leading or trailing spaces.

The decision-making process relies entirely on the if-elif-else structure:

Exit Check (if): The script first checks a critical condition: if the user types "quit," "exit," or "bye," the bot prints a farewell and uses the break statement to terminate the while True loop and end the program.

Rule Checks (elif): If the input is not an exit command, the script proceeds down a list of elif (else if) statements. Each one checks if a specific keyword, such as "hello," "weather," or "python," is present in the user's message. If a keyword is found, the bot delivers the corresponding pre-programmed response.

Default Response (else): If the user's input does not contain any of the keywords defined in the rules, the program hits the final else block, which serves as a catch-all, letting the user know the input wasn't understood.

This architecture ensures the chatbot remains active until explicitly told to quit, providing relevant responses only when specific keywords trigger its built-in rules.
