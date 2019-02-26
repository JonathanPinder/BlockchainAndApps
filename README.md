# Brute Force
![If it Ain't Broke, Break It](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIvG6gLpbjz5Yf1PXgcgRyddhG3SWkaIcX1YxEQt-jFuEUF_a9)

This program allows you to experiment with brute-forcing understanding how vulnerable passwords are that are SHA-1 encrypted. Especially passwords that are common by Jonathan Pinder

![Get A Real Password](http://images.jagran.com/pass_B_20116.jpg)

Let's get into it!

To run this program you must have Python 2.7 downloaded. Please see: https://www.python.org/download/releases/2.7/
**IMPORTANT** Please keep a note of where your Python 2.7 download is if you don't keep the default option.

If you downloaded Python 2.7 with default setting it is located in;
    `C:/python27/python.exe`
    
#Getting Started
###Step One: Download the zipped file
1. Click clone/download
2. Select "Download ZIP"
3. Locate where your zipped file is in your directory and unzip it, it should be called "BlockchainAndApps-master"
4. When asked where to extract the file put 
`C:\Users\{YOUR COMPUTER NAME}\Documents\LetsGetItCracking`
5. For the duration of this tutorial ,we will assume that {YOUR COMPUTER NAME} is jpinder1

###Step Two: Get it Cracking
1. Go to your command prompt, if you are on windows click the Windows button and type "cmd" and click enter
2. type `"cd C:/Users/{YOUR COMPUTER NAME}/Documents/LetsGetItCracking/BlockchainAndApps-master"` and click enter
3. You should now be in the directory with the downloaded files, Great!
4. You must run the program with Python 2.7
5. You must specify the program to be ran (there are 2)
6. The format for user input is `C:/python27/python.exe {program_name} {final_hash} {definition of problem} {salted_hash}`
7. definition of problem can be: hashonly, salted, or complex
8. If there is no salted hash put "null"

###Step Three: Solving Your first SHA-1 Hash

*testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3*
1. Ensure you are still in your cmd window from Step Two
2. Type the following
`C:/python27/python.exe crackinghashes.py b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 hashonly null`
3. Press Enter
4. You should get the following output
*This is the hash for the password letmein
It only took 16 tries!
It took0.1360661 seconds to complete!*

###Step Four: Solving your second SHA-1 Hash

*medium hacker hash:801cdea58224c921c21fd2b183ff28ffa910ce31*
1. While still in the cmd window from Step Three
2. Type the following
`C:/python27/python.exe crackinghashes.py 801cdea58224c921c21fd2b183ff28ffa910ce31 hashonly null`
3. Press Enter
4. You should get the follow output:
*This is the hash for the password vjhtrhsvdctcegth
It only took 999968 tries!
It took1.4036156 seconds to complete!*

###Step Five: Solving your first salted Hash

Here is the hash given: *ece4bb07f2580ed8b39aa52b7f7f918e43033ea1*

However, there is a salted hash *f0744d60dd500c92c0d37c16174cc58d3c4bdd8e* that is concatenated before hashing with another word to produce the final hash we are given: *ece4bb07f2580ed8b39aa52b7f7f918e43033ea1*. Here's how we'll solve it:

1. Ensure you are still in the cmd window from Step Four
2. Type the following:
`C:/python27/python.exe crackinghashes.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 salted f0744d60dd500c92c0d37c16174cc58d3c4bdd8e`
***IT IS VERY IMPORTANT THAT YOU REMEMBER THE SYNTAX FOR THIS PROGRAM `C:/python27/python.exe {program_name} {final_hash} {definition of problem} {salted_hash}`***






    



