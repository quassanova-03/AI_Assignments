# TURING TEST + CAPTCHA IMPLEMENTATION

## Overview
This project demonstrates the concepts of Turing Test and CAPTCHA system by implementing a simple CAPTCHA verification system using Python(Flask) and HTML. The system generates distorted CAPTCHA images that humans can recognise but automated bots find difficult to solve.

## What is the Turing Test?
Proposed originally by Alan Turing in 1950, the Turing Test, is a method to determine whether a machine can exibit a level of intelligence equivalent to a human.

In the test:  
- A human judge communicates with both a human and a machine.  
- The judge does not know which participant is the machine.  
- If the judge cannot reliably distinguish the machine from the human, the machine is said to have passed the Turing Test.

## What is CAPTCHA?
CAPTCHA : Completely Automated Public Turing test to tell Computers and Humans Apart

It is a security mechanism used by websites to prevent automated bots from performing actions such as:

- creating fake accounts  
- spamming forms  
- scraping data  
- brute-force login attempts

The idea behind CAPTCHA is closely related to the concept of the Turing Test. Here, instead of testing whether machines can behave like humans, it tests whether users behave like humans instead of bots.
This project implements a text-based CAPTCHA system with image distortion.

## Project Structure
```
AI_Assignments/
|
└─ Captcha/
   │
   ├── captcha_app.py        # Main Flask application
   │
   ├── templates/
   │   └── Captcha.html      # Web interface
   │
   └── static/
       └── captcha.png       # Generated CAPTCHA image
```

## How the system works
1. The Flask server starts and hosts a webpage.  
2. A random CAPTCHA string is generated.  
3. The program creates an image containing the CAPTCHA text.  
4. Characters are randomly rotated and spaced.  
5. Noise lines and dots are added to increase difficulty.  
6. The image is displayed on the webpage.  
7. The user enters the CAPTCHA text.  
8. The server compares the input with the generated CAPTCHA.
   If the values match :
       Access Granted
   Otherwise :
       Incorrect CAPTCHA
9. A new CAPTCHA is generated after each attempt.

## How to run the project
1. Install dependencies
   ```
   pip install flask pillow
   ```
   or
   ```
   py -m pip install flask pillow
   ```
2. Navigate to the project folder
   ```
   cd Captcha
   ```
3. Run the flask application
   ```
   py captcha_app.py
   ```
4. Open the application in a browser
   Go to :
   ```
   http://127.0.0.1:5000
   ```
   The CAPTCHA verification page will appear.

## Project Features
This implementation includes:
- Random CAPTCHA generation (letters and numbers)  
- Character rotation and distortion  
- Random spacing between characters  
- Noise lines across the image  
- Random noise dots  
- Web-based CAPTCHA display  
- User input validation  
- CAPTCHA regeneration after each attempt

These distortions make it difficult for automated programs to reliably recognize the text.

## Technologies Used
Python  
Flask (web server framework)  
Pillow [PIL] (for CAPTCHA image generation)  
HTML (for the user interface)
