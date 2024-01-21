# TMCompanion
This is a Web-App Companion for the popular board game Terraforming Mars

# Goals
The goal of this Web-App is to provide a useful interface for Terraforming Mars.
Calculations in this game can sometimes be difficult or inconvenient to track.
This app attempts to solve those issues with easy to use interfaces.

# Features
Home Page - This is a landing page for the TMCompanion Website. On this page is also a link to a random image search which will display images relevant to the mars theme.

Megacredit Calculator - This page is a Calculator for Megacredits which are a currency used very often in this game.

Resource Tracker - This page is a tracker for the different resources in the game. It also automates the production phase.

Scoring - This page automates the end of game scoring

Player Reference - This page displays a useful player reference card.

Rule Book - This page displays the entire rule book for the game

# Files

## layout.html
In layout.html is the basis for most of the website layout. At the top is displayed the apps title and a list of available pages on the website.
On the top right of layout is a button called "Reset Game". This button when clicked will reset all of the locally stored values used within the site.
The Block Content within the section is where the templates for the other pages will be inserted.

## index.html
This is the file for the homepage of the website. This page is fairly simplistic. It has a welcome message as well as the link to the random image search.

## megacredit-calculator.html
This page contains the megacredit calculator.
There is a paragraph object which contains the current value of megacredits that the user has.
Below that is a form with an input field and two buttons.
The input field takes a number of megacredits the user would like to add or subtract.
The two buttons (add and subtract) trigger a function which adds the value in the input field to the users megacredits.

When a user first visits this page, their megacredits value is initiated at 0.

## resource-tracker.html
This page handles storing each of the users resources as well as automating the production phase.
On this page is a list of Resources.
Each resource has an Amount input field, a Production input field, and a Set Button.
The input fields double as displays for the users current Amount and Production Values.
When the user presses a Set Button, the corresponding Resources Amount and Production are stored locally.

Since Megacredits exist both here and in the Megacredits Calculator, both pages are using the same value. So megacredits can be set via this resource page or the calculator page.
The benefit the calculator page has over the resource page for megacredits is that you can actually do a calculation with the calculator instead of needing to just set a specific value as it is here in the resource tracker page.

The "Production Phase" button at the bottom automates the production phase from Terraforming Mars. In Terraforming Mars when production phase happens, the player needs to quite a few different operation such as:
Converting Energy To Heat
Gaining Resources based on Production for every Resource.
This Production Phase button saves a lot of time. Instead of needing to do each resource on at a time, you simply press this button and it calculates how many resources you would have after production phase.

## scoring.html
This pages automates the scoring for the end of a Terraforming Mars Game.
In Terraforming Mars, scoring can be quite tedious, you need to get the scores for each of the scoring categories and then add them all up and then you have to repeat for each player. Then you have to compare the players scores to see who won.

While with this app, you still need to type in the scores for each individual category for each player however, the calculations including who won is all done for you.

At the top of this page is a Player Selection Box. You simply type in the number of players who are participating and then a number of forms is generated below that corresponding to the number of players.

Below the player Forms is a button called "Submit Scores". When you press this button, all the calculations are done and it displays a message.

If there is a winner, the name of the winner is displayed.
If there is a tie for first place, the name of all the tied players are displayed.

In Terraforming Mars, there is actually a tie breaker which is the person with the most megacredits wins. I have not implemented this as it is very easy to check.
This page also does not currently support single player scoring.

## player-reference.html
This page displays a few images that act as a player reference card. The original game doesn't actually come with very useful player reference cards. 
These cards are not as detailed as a full rule-book but they provide you with enough reminder information while playing to hopefully prevent you from needing to actually look up rules in the rule-book.

## rule-book.html
This page contains a PDF viewer for the entire games rule book.
Currently not working on Mobile.

## app.py
This is the flask server configuration. This simply contains GET routes to each of the available pages on the website.
If there was server side data on the website I would have needed to do most of the above calculations within this file.
Since I opted instead to have all of the data stored locally on the client, I handled all of the calculations using javascript in their respective pages.
