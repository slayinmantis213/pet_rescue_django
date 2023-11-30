# Creature Classes
## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- I undertook this project because I remember enjoying Tamogatchi as a kid and I thought it would be an engaging challenge to make something like it while learning to use Django.
- Inspired by classic Tamogatchi and games like Webkins and Neopets, Creature Classes is a browser game about rescuing and rehabilitating mystical creatures.
- User spends gifts to collect pets and can interact with pets to acquire more gifts and progress pet experience level with an end goal of collecting feathers by "releasing" maximum level pets.


## Technologies Used
- Python Django -- scalable, streamlined queries, good learning experience
- HTML, CSS, Bootstrap -- intuitive navigation and interactive UI
- SQLite3 -- one-to-many relationship between users and pets
- HTML validations and server-side validations with Bcrypt hashing for secure login


## Features
- Existing user logs in and is redirected to dashboard:

<img src="img\login-gif.gif" alt="login-to-dashboard-gif"/>

- User can spend 5 "gifts" to "rescue" a pet:

<img src="img\rescue-gif.gif" alt="rescue-pet-gif"/>

- When "rescuing" pets user is given 3 random pets to choose from with only their avatar photo and type.  User must choose one.
- All 12 pet types have different ranges for these statistics and a rarity weighting to match with the rarest pets having the best statistics.

- User can change the pet's name from the dashboard:

<img src="img\edit-name-gif.gif" alt="edit-name-gif"/>

- Upon confirmation, user is redirected to the "visit" screen where the pet is displayed along with its name, stats, and a gif to indicate its mood: 


<img src="img\pet-screen-gif.gif" alt="pet-screen-gif"/>

- Pets have a simple stat block with current level, health, energy, happiness, and experience.
- Users can influence these statistics by interacting with the pet via either the "train" or "play" actions so long as the pet has energy.
- "Train" awards high experience, but reduces energy, health and happiness.
- "Play" awards a small amount of experience, increased health and happiness, and has a high chance of giving the player a "gift".
- Users can visit any pet in their collection from the dashboard:

<img src="img\visit-gif.gif" alt="visit-gif"/>

- User is also rewarded with gifts for "releasing" or deleting pets: when pet is released, it awards an amount of gifts equal to its current level.
- Upon releasing a pet at maximum level, user is awarded with a feather, the current endgame incentive:

<img src="img\get-feather-gif.gif" alt="get-feather-gif"/>


## Screenshots

<img src="img\celestial-SC.png" alt="screenshot-of-celestial-dragon" width=1200/>

- This is a Celestial Dragon.  They are the rarest of the bunch and I think they look pretty cool.  It takes some luck to find one though!

<img src="img\help-screen.png" alt="screenshot-of-help-page" width=1200/>

- This is the "Help" page.  Newly registered users are redirected to this page before they see the dashboard.  Any user can revisit the "Help" page from the dashboard.


## Project Status
In Progress


## Room for Improvement
TODO:
- Polish front-end aesthetic
- More functionality for pet over-time progression
- Time differential calculations should be expanded and made more integral
- Reduce reliance on rerouting
- Add filter menu or search bar to make it easier to navigate pet list.
- Add many-to-many for friend system

## Acknowledgements
- Many thanks to [Benji Hix](https://github.com/benji-hix) for taking time out of his project week to make a logo for me.
- Thanks to Google images for all of the pictures for the different pets.
- Thanks to TA Lucky from Python stack at Coding Dojo for helping get time calculations working.

## Contact
[LINKEDIN](https://www.linkedin.com/in/joshua-bliek/)


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->