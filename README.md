# Password Checker
This is a program that allows you to enter a password and it will tell you whether that password has ever been leaked. 

## Usage
Simply run the checkmypass.py file. The program will ask you to input a password and upon entering, it will tell you if that password has been leaked and if it has, it will tell you how 
many times it's been leaked. The program runs in a loop so it will keep on asking for your password until you enter "/q" which tells the program to exit.

## How it works
The entered password gets passed into the apiCheck method. There it gets hashed using the SHA1 algorithm and gets split into 2 pieces - the first 5 characters, and the remainder of the hash.
From there the program calls requestData, which requests data from the API using only the first 5 characters of our password. The method returns a response which gets passed to 
passwordLeakCount as an argument along with the remainder of the hash. In passwordLeakCount, the response from the API is looped over and the remainder of the hash is compared to the remainder 
of each hash returned by the API. Finally if a match is found, the program returns that a match has been found along with the count of how many times it's been leaked.
