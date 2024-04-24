# CE-Final-Project
Project Goals:
1.	Make a game, that has a falling block, with a character at the bottom, that can move left and right. 
2.	Make coins fall from the sky for points. Make the character able to select the coins. 
3.	Make walls falling kill the character when hit.
4.	Have, a restart button on-screen/ game over message/ score. 
5.	Add a timer, that pops up for how long the player lasted. 
Player Instructions:
1.	Move Charlie, with the left and right arrows. 
2.	Press, and restart to play the game. 
technologies and techniques:
1.	First import pygame, random, and time
2.	Use pygame. Sprite class to interact with the other sprites 
3.	Use the __init__() in almost every def, to initialize the attributes, of the picture, and position of the picture
4.	Then use update () for coins, and wall, to restart the falling after falling off the screen
5.	Make a class for block, wall, coin, game. 
6.	The game class sets up the game with the initialization, also with a create wall, create-coin, and restate game (which is the restart button),
7.	The Run class is a loop that takes the input of the user, and checks for collisions, and runs all the sprites, putting everything on the screen. 
Citations:

•	galangpiliang. "Coin Icon." 2016. https://opengameart.org/content/coin-icon. Accessed March 29, 2024.
•	Twopiharris. "Charlie” 2022. https://github.com/twopiharris/BSU-CS120/blob/main/firstGame/Charlie.png Accessed March 20, 2024.
•	Sketchepedia. "Golden Coin." 2021. Freepik, https://www.freepik.com/free-ai-image/free-photo-good-friday-background-with-jesus-christ-cross_40380546.htm#query=game%20art&position=0&from_view=keyword&track=ais&uuid=94699576-a174-4a3a-b2ca-c1a62728a663. Accessed April 22, 2024.
•	
Description of your process:
o	What did you learn?
o	Where did you get stuck?
o	What would you like to improve?
o	How would you do things differently next time?
o	How far did you stray from the game design document?
o	How did you stay on track?

I learned a whole bunch, on this project, one of the main ones being how to make an object fall. And so that some objects have are ability to hit and give you points, and other objects stop the game. Also, how to restart a game and, hit messages to pop up on the screen. The thing that I struggled on and got stuck a few times was, getting the messages to pop up on the screen, in the right place, time, or color. I just couldn’t figure that out for a long time but figured it out. The hardest part of this code is getting the restart button to work, I could get it to come up on the screen, but it never worked, a got it. I would like to improve the game by adding levels and making the walls not so random, so Charlie doesn’t get trapped. With no way out. I think the only thing I would do differently, is find a different way for the wall to be span and off out. With different pictures on the walls. That’s the only thing I would do differently. I went kind of far away from the game design document, I couldn’t figure out a solid horizontal wall with a gap in it, and they turned out into just random wall chunks. I stayed on track, by adding a score system, with a timer, and a restart button, with a character that moves left and right at the bottom of the screen. 

