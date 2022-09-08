# README

Guide to install the latest version of the Mastermind chatbot.


## Steps

1- Install Python Requirements:
```bash
pip install -r requirements.txt
```

2- Checks the domain, NLU and conversation data for inconsistencies:
```bash
rasa data validate	
```

3- Train the model:
```bash
mkdir models
rasa train
```

4- Run rasa server by loading your trained model to talk to the assistant on the command line
```bash
rasa shell	
```

5- Run actions server:
```bash
cd actions && rasa run actions
```


## Description

- This game is similar to MasterMind Game which is a number game. 
- The chatbot selects a secret number with four different (unique) digits. 
- The object of the game is to guess that secret number. 
- Each guess is answered by the number of digits in the guess number that match or occur in the secret number. 
- You will also be told how many of the digits are in the correct position in the chosen number. 
- Through a process of elimination, you should be able to deduce the correct digits using logic.

- If the chatbot chooses 1234 number and you enter 7438, it will return: 1 CP and 1 IP.

 Explanation: The number contains one digit in a correct position (CP) which is the digit 3 AND one digit but in an incorrect position (IP) which is the digit 4


## Demo

```bash
Your input ->  hello                                                           
Hey! How are you?
Your input ->  great                                                           
Great! Good for you :)
Your input ->  who are you                                                     
I am a bot. I am programmed to play with you MasterMind Game
Your input ->  yes i want to play                                              
Do you want to know more about this game?
Your input ->  yes plz                                                         
This game is similar to MasterMind Game which is a number game. I will select a secret number with four different (unique) digits. The object of the game is to guess that secret number. Each guess is answered by the number of digits in the guess number that match or occur in the secret number. You will also be told how many of the digits are in the correct position in the chosen number. Through a process of elimination, you should be able to deduce the correct digits using logic.
If I chose 1234 number and you enter 7438, I will tell you those infomations: 1 CP and 1 IP. Explanation: The number contains one digit in a correct position (CP) which is the digit 3 AND one digit but in an incorrect position (IP) which is the digit 4
Are you ready to play with me?
Your input ->  yes                                                             
I chose a number
Attempt 1 : Could guess the number?
Your input ->  0123                                                            
Those are your previous attempts:
In 0123 : 0 CP and 1 IP
Attempt 2 : Could guess the number?
Your input ->  4567                                                            
Those are your previous attempts:
In 0123 : 0 CP and 1 IP
In 4567 : 2 CP and 0 IP
Attempt 3 : Could guess the number?
Your input ->  8901                                                            
Those are your previous attempts:
In 0123 : 0 CP and 1 IP
In 4567 : 2 CP and 0 IP
In 8901 : 0 CP and 1 IP
Attempt 4 : Could guess the number?
Your input ->  0187                                                            
Those are your previous attempts:
In 0123 : 0 CP and 1 IP
In 4567 : 2 CP and 0 IP
In 8901 : 0 CP and 1 IP
In 0187 : 0 CP and 0 IP
Attempt 5 : Could guess the number?
Your input ->  3256                                                            
Those are your previous attempts:
In 0123 : 0 CP and 1 IP
In 4567 : 2 CP and 0 IP
In 8901 : 0 CP and 1 IP
In 0187 : 0 CP and 0 IP
In 3256 : 0 CP and 3 IP
Attempt 6 : Could guess the number?
Your input ->  9256                                                            
Those are your previous attempts:
In 0123 : 0 CP and 1 IP
In 4567 : 2 CP and 0 IP
In 8901 : 0 CP and 1 IP
In 0187 : 0 CP and 0 IP
In 3256 : 0 CP and 3 IP
In 9256 : 0 CP and 4 IP
Attempt 7 : Could guess the number?
Your input ->  2596                                                            
Those are your previous attempts:
In 0123 : 0 CP and 1 IP
In 4567 : 2 CP and 0 IP
In 8901 : 0 CP and 1 IP
In 0187 : 0 CP and 0 IP
In 3256 : 0 CP and 3 IP
In 9256 : 0 CP and 4 IP
In 2596 : 2 CP and 2 IP
Attempt 8 : Could guess the number?
Your input ->  2569                                                            
Congratulations! You did a great job! You guessed the number in 7 attempts
Your input ->  thankyou                                                        
You are welcome!
Your input ->  bye                                                             
Bye
Your input ->  i want to play                                                  
Your input ->  how to play again                                               
This game is similar to MasterMind Game which is a number game. I will select a secret number with four different (unique) digits. The object of the game is to guess that secret number. Each guess is answered by the number of digits in the guess number that match or occur in the secret number. You will also be told how many of the digits are in the correct position in the chosen number. Through a process of elimination, you should be able to deduce the correct digits using logic.
If I chose 1234 number and you enter 7438, I will tell you those infomations: 1 CP and 1 IP. Explanation: The number contains one digit in a correct position (CP) which is the digit 3 AND one digit but in an incorrect position (IP) which is the digit 4
Are you ready to play with me?
Your input ->  yes                                                             
I chose a number
Attempt 1 : Could guess the number?
```

