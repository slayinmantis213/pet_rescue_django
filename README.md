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

## General Information
- Inspired by classic Tamagotchi and games like Webkins and Neopets, Creature Classes is a browser game about rescuing and rehabilitating mystical creatures.
- I undertook this project because I remember enjoying Tamagotchi as a kid, and I thought it would be an engaging challenge to make something like it while learning to use Django.
- Users spend gifts to collect pets. They can interact with their pets to acquire more gifts and progress their pet's experience level. The ultimate goal is to collect feathers by "releasing" maximum level pets.

[Return to Table of Contents](#table-of-contents)

## Technologies Used
- Python Django -- scalable, streamlined queries, good learning experience
- HTML, CSS, Bootstrap -- intuitive navigation and interactive UI
- SQLite3 -- one-to-many relationship between users and pets
- HTML validations and server-side validations with Bcrypt hashing for secure login

[Return to Table of Contents](#table-of-contents)

## Features
- Existing users log in and are redirected to the dashboard:

![Login to Dashboard](img\login-gif.gif)

- Users can spend 5 "gifts" to "rescue" a pet:

![Rescue Pet](img\rescue-gif.gif)

- When "rescuing" pets, the user is given 3 random pets to choose from with only their avatar photo and type. The user must choose one.
- All 12 pet types have a rarity weighting with the rarest pets having the best statistics.

- Users can change the pet's name from the dashboard:

![Edit Name](img\edit-name-gif.gif)

- Upon confirmation, the user is redirected to the "visit" screen where the pet is displayed along with its name, stats, and a gif to indicate its mood: 

![Pet Screen](img\pet-screen-gif.gif)

- Pets have a simple stat block with current level, health, energy, happiness, and experience.
- Users can influence these statistics by interacting with the pet via either the "train" or "play" actions as long as the pet has energy.
- "Train" awards high experience but reduces energy, health, and happiness.
- "Play" awards a small amount of experience, increased health and happiness, and has a high chance of giving the player a "gift".
- Users can visit any pet in their collection from the dashboard:

![Visit](img\visit-gif.gif)

- Users are also rewarded with gifts for "releasing" or deleting pets: when a pet is released, it awards an amount of gifts equal to its current level.
- Upon releasing a pet at maximum level, the user is awarded with a feather, the current endgame incentive:

![Get Feather](img\get-feather-gif.gif)

[Return to Table of Contents](#table-of-contents)

## Screenshots

![Celestial Dragon](img\celestial-SC.png)

- This is a Celestial Dragon. They are the rarest of the bunch and I think they look pretty cool. It takes some luck to find one though!

![Help Page](img\help-screen.png)

- This is the "Help" page. Newly registered users are redirected to this page before they see the dashboard. Any user can revisit the "Help" page from the dashboard.

[Return to Table of Contents](#table-of-contents)

## Project Status
In Progress

[Return to Table of Contents](#table-of-contents)

## Room for Improvement
TODO:
- Polish front-end aesthetic
- More functionality for pet over-time progression
- Time differential calculations should be expanded and made more integral
- Reduce reliance on rerouting
- Add a filter menu or search bar to make it easier to navigate the pet list.
- Add many-to-many for friend system

[Return to Table of Contents](#table-of-contents)

## Acknowledgements
- Many thanks to [Benji Hix](https://github.com/benji-hix) for taking time out of his project week to make a logo for me.
- Thanks to Google images for all of the pictures for the different pets.
- Thanks to TA Lucky from Python stack at Coding Dojo for helping get time calculations working.

[Return to Table of Contents](#table-of-contents)

## Contact
[LINKEDIN](https://www.linkedin.com/in/joshua-bliek/)