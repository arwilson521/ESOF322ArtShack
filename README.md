# ESOF322ArtShack
Austin Wilson

ESOF 322

#How to use
Download the program folder.
run interface.py
upload art into the art folder and run it through the seller tab.

## File descriptions
### Program
**Holds the main files including art and the database**
### Models
**Holds the system models**

## Preface
  ###  Version 0.0.2
  Changelog:
  Added everything.
  ### Introduction:
  Welcome to version 0.0.2 of the Artshack system. This program is developed to ease the process between the artists selling art and the users buying art
  ### Current Features:
  **SuperUser**
  Able to make changes to art listings. Admin only 
  **Artist**
  can list art
  **Buyer**
  Can bid on art and purchase art
  **Browser**
  Can look at art
  ### Future Features
  Ability to feature art
  ### Limitations:
  Ugly interface
## Introduction
  This system is used to hold, store, and display art in a reasonable manner. it allows users to buy, sell, or look at art.
## Glossary
  
## user requirement definitions
  This system is designed to automate certain workflows for each seperate user
  ### SuperUser:
  Remove art
  Approve art
  Mark art as sold
  

  ### Buyer:
  Buy art
  View art
   
  ### Seller:
  Sell art

  ### Looker:
  browse art
## System Architecture
  ### Overview
  The art shack system uses front end, back end and databases which allows for large scalability. The program can handle multiple interactions from multiple users
  ### Front end
  This provides the user interface which allows users to interact with the program.
  The program is built in python and is meant to be used on primarily browsers but allows limited functionality on browsers and mobile phones
  ### Back end
  This provides the operations and data flow behind the scenes
  This part of the program is written in python
  ### Database
  This contains persistent data such as the orders in the system.
  This part of the program is written in sqllite (python branch of sql with a local database!)
## System Models
  
The program starts from the main menu where they choose a role. the system then sends them to the appropriate page. Each user has its own functions listed above that they will be able to accomplish
