# CSC226 Final Project

## Instructions

️Exclamation Marks  ️indicate action items; you should remove these emoji as you complete/update the items which 
  they accompany. (This means that your final README should have no  ️in it!)

**Author(s)**: Beni Shendera, Bright Feitsop

**Google Doc Link**: https://docs.google.com/document/d/1BT4B5kadw3Nl_skQR2FpIa58S7PSUuGdMJjAV-MDu8c/edit?usp=sharing

---

## Milestone 1: Setup, Planning, Design

**Title**: `Bombastic Boa2` 

**Purpose**: `The purpose of the game is to challenge players reaction time and strtegic thinking 
by introduing risk based mechanics into a classic snake game. instead of only growing longer, players must manage their snake size while avoidinghazards like bombs and others. adding a new layer of decision making and difficutly. `

**Source Assignment(s)**: `the source of this assignment came inspired from boustrophedon `

**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:
  
![Don't leave me in your README!](image/ourcrc.jpeg "Image of CRC card as an example. Upload your CRC card(s) in place of this one. ")

**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: Feitsopb
    Branch 2 starting name: oshendera1
```

### References 
Runestone chapters, Google

Throughout this project, you will likely use outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update this 
section as you go. DO NOT forget about it!


## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
Working on the CRC cards for the project helped better understand how to break a program into separate classes and organize responsibilities. At first, it seemed simple to just think of the game as one piece, but creating classes like Snake, Game, Food, and Bomb made it clearer how each part has its own job. like, the Snake handles movement and collisions, while the Game controls the overall flow. This separation makes the program easier to manage and update later.

One thing I noticed is that planning with CRC cards forces you to think ahead. Even though our game will change, having bombs included now helps prepare for future features. It also showed us how classes collaborate with each other, like how the Snake needs to interact with Food to grow and with Bombs to detect danger.

If I were to improve this design, I might simplify or combine some parts at the beginning and then expand later as the game becomes more complex. Overall, this process made us realize that designing before coding can save time and make the program more organized, especially as new features are added.
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `0 - 100%` 75%

️**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
Pretty confident now, we spent lot of time briging newer ideas then what our main idea was and that worked out pretty well for us in terms of being little more creative and different.```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 
Once you hit "Run" in PyCharm, the game window will appear and immediately begin displaying
 a dark, gridded forest floor where your boa is stationed at the bottom. 
 To start the action, simply press any arrow key on your keyboard; the snake will begin moving in that direction,
  and items will start raining from the top of the screen. 
  Your primary goal is to use the Up, Down, Left, and Right keys to navigate the snake toward the falling Red Circles (Fruit) while actively dodging the Grey Squares (Bombs).
   Keep a close eye on the HUD at the top-left to track your score and current wave. Be careful not to let any fruit reach the bottom of the screen or collide with the perimeter walls, 
   as both will result in an immediate "Game Over." If you lose, the screen will display your final score, 
   and you can simply click anywhere on the game window to exit the program.

### Errors and Constraints

Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

### Reflection

Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
Partner 1: **Replace this with your reflection
```

At first i selected because it was the first game in code that came to mind. then more ideas started pouring 
our first design idea wasnt how the code ended. it all changed in during milestone 3 the game just looked kinda of basic for us.
so instead of just screen standing there we came up with what if the screen moves. this was while i was watching soccer higjlights
neymar was dribbling through players and i was like oh crap we can do this with the snake so what if the snake dribles throught bombs
and thats where the rain fall idea came from in my brain its defenders coming randomly to defend the player with the ball to score a goal 
which the player with the ball is the snake and if the snake beats the first defender aka first bomb the next defender is ready and knows your move..
i learned a lot the biggest for me was debuging step by step and actaully fixing the code and learning what was wrong with the code and learning how to do more than what you have ideally
the hardest part was being debuging and fiding the right codes. 
knowing what i know now i would try to be a lot more creative then this at some point during this code i was playing around and wanted to have bombs as actuall immages of bombs and fruits as 
actually images of fruits both random and 8 of each.after trying to do it my brain told me with the time we have i should just stick to what we have. and i guess since were using turles it was a lot harder and i ddint wnat somehting i liked to make 
both me and my partner start all over.
working with my partner made it a lot easier hes good at seeing both point of views and just open to listening to new ideas and change 
which was huge for us because if he wasnt a person thats easy to work with we would not end up with the idea we ended with. so shout out to bright 
for being open to new ideas and making my first ever parther projects a good expeirnce witouth givng me headche.

```
Partner 2: **Replace this with your reflection
```
we brainstormed on an idea, and came up with a snake game, which we had to then make it different, from what everyother person has had in the past. finding a way to make it special was the harder part. 
the initial design was just a regular snake game, but along the way, we came up with a new idea, of making thoings fall from the upper screen downward. the initial design was not so much different from the design we are currently working on.
i learned that ideas can be changed while working on projects. i learned that i need to be fluid and open up for more ideas as i code through whatever i am doing. 
the hardest part for me was debugging the code, and then coming up with new creative ideas of making some objects come down randomly. 
next time, i will break the code even further, making good use of functional decomposition and top-down design. 
i did a good job with him. it was hectic, filled with moments of me having to remind him of our project a couple times. but overall, it was a great experience.  
---