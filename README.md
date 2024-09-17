# Point > Point
## Milestone Project 4:  *full-stack site e-Commerce site.* 

DISCLAIMER: This is a project for Code Institute, to demonstrate an understanding full-stack site based around business logic used to control a centrally-owned dataset.

![MockUps](#)

## Live Project 

[View live project here](#)

## Repository 

[Locate project repository here](https://github.com/JJBR13/Justin-Brown-Milestone-Project4)

## Contents 

- [Ideology](#ideology)
- [User Experience](#user-experience)
    + [User Stories](#user-stories)
- [Design](#design)
    + [Wireframes](#wireframes)
    + [Database](#database)
    + [Colour Palette](#colour-pallete)
    + [Typography](#typography)
- [Current Features](#current-features)
    + [Responsive On All Devices](#responsive-on-all-devices)
- [Future Releases](#future-releases)
- [Languages Used](#languages-used)
- [Testing](#testing)
- [Deployment](#deployment)
    + [Project Creation](#project-creation)
    + [Cloning Repo](#cloning-repo)
    + [Danjgo](#django)
    + [ElaphantSQL](#elaphantsql)
    + [Heroku](#heroku)
    + [Stripe](#stripe)
- [References, Credit, Frameworks & Programs](#references-credit-frameworks-programs)
    + [References](#references)
    + [Credit](#credit)
    + [Frameworks](#frameworks)
    + [Programs](#programs)

## Ideology

The purpose of this website is to provide a fully functional e-commerce platform tailored for solo youth travelers seeking their next adventure. Built with Django and Python, the site allows users to explore all the unique travel experiences offered by Point > Point. Visitors can browse destinations, discover the exciting activities awaiting them, and book unforgettable, once-in-a-lifetime trips, all designed specifically for young, solo travelers eager to explore the world. 

## User Experience 

### User Stories 

## Design 
 
### Wireframes

### Database

### Colour Pallete

### Typography

## Current Features

### Pages
#### Favicon
#### Home
#### All Tours
#### About 
#### Contact Us
#### Profile & Profile Managemnet 
#### Profile: Admin users 
#### Bag 
#### Checkout 
#### Secure checkout 
#### Responsive messages
#### Error Page 

### Responsive On All Devices

## Future releases

## Languages Used

- [HTML5](https://www.w3schools.com/whatis/whatis_html.asp)
- [CSS3](https://www.w3schools.com/whatis/whatis_css.asp)
- [JavaScript](https://www.w3schools.com/whatis/whatis_js.asp)
- [Python](https://www.python.org/doc/)

## Testing 

### Stripe

### Dummy Card Information

The following test card details were used for testing Stripe:

Card Number: 4242 4242 4242 4242
Date: 0424
CVC: 242
Postcode: 42424

## Deployment 

### Project Creation 

## Cloning Repo 

 1. Locating repository, clicking on the "New" button.
 2. Click the Code button, select clone with HTTPS, SSH or the GitHub CLI and copy the link.
 3. Open the terminal in your preferred IDE. Change the working directory to the target location for the cloned repository.
 4. In the terminal, type 'git clone' followed by the copied URL.
 5. Install the packages from the requirements.txt file by running pip3 install -r requirements.txt in the terminal.

## Django: 

 1. In the terminal enter, pip3 install 'django<4'.
 2. Then enter, django-admin startproject your project name
 3. You will see the django project folder, including settings.py and urls.py.
 4. Back to the terminal, enter touch .gitignore.
 5. In the .gitignore file enter, *.sqlite3 and *.pyc and pycache
 6. Run the project by entering python3 manage.py runserver to check it is running well. Your page should show a rocket with 'The install worked successfully! Congratulations!' below it.
 7. Back in the terminal CTRL + C to quit the server.
 8. Migrate: enter, python3 manage.py migrate.
 9. Create a superuser: enter, python3 manage.py createsuperuser. Provide username, email (or skip this by hitting enter) and password.

- Adding the Chrome extension "GitPod" created an online coding platform, enabling the use of bash terminals throughout the project. The below "git commands" were used: 

1. git add . - This command for multiple files to the staging area before commiting. 
2. git commit -m "Message explaining upadate" - This command explained changes that were done to the repository. 
3. git push - This command was used to push all committed changes to the GitHub Repository. 

## ElaphantSQL
 1. Navigate to ElephantSQL.com and select create a new instance.
 2. Select - free database plan.
 3. Set up your plan 
 4. Give it the same name as your project 
 5. Select region closest to you 
 6. Click review and then Create instance.
 7. Return to the ElephantSQL dashboard
 8. Click on the database instance name for this project
 9. In the URL section, copy the database URL to your clipboard

## Heroku

## Stripe
 1. Navigate to Stripe website 
 2. Register for a Stripe account.
 3. Go to 'API Keys' to view public and secret key.
 4. In the apps .env file, add STRIPE_PUCLIC_KEY AND STRIPE_SECERET_KEY.
 5. Copy in public and secret keys from Stripe.
 6. Go to Heroku and open the app.
 7. Click 'settings' and 'Reveal Config Vars'
 8. Add the STRIPE_PUCLIC_KEY AND STRIPE_SECERET_KEY with their keys from Stripe.

## References, Credit, Frameworks & Programs

### References 

- [Flat icon](https://www.flaticon.com/): 
    - All icons used for the site.

- [Git](https://git-scm.com/): 
    - Used for version conterol.

- [GitHub](https://docs.github.com/en/get-started): 
    - Was used to store the project.

- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/): 
    - Used to inspect site pages and there elements to help debug issues with layouts and try differnt CSS styles.
    
- [Google Fonts](https://fonts.google.com/) 
    - Used to import fonts into style.css. 

- [Hex to RGBA Converter](https://rgbacolorpicker.com/)
    - Used to convert hex to rgba.

- [Loading Animation](https://css-loaders.com/classic/): 
    - Loading animation while payment is pending.

- [Profile tab structure](https://codepen.io/rockteam/pen/WrpXBN ): 
    - Used on profile page to create tab for perosnal details & Order history. 

- [Unicorn Revealer](https://chromewebstore.google.com/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-US&utm_source=ext_sidebar): 
    - Used to aid with diagnosis & applying css.

### Credit

- [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/f5880efee43b3b9ea1276a09ca972f4588001c59)
    - A lot of the core code was taken from the 'Boutique Ado' walkthrough project on Code Institute.

- [Code Institute](https://codeinstitute.net/): 
    - For all the lecture/ learning content provided. 

- [Manu at Bristol Collge](https://codeinstitute.net/): 
    - For all the support and pointers. 

### Frameworks

- [Bootstrap](https://getbootstrap.com/)
    - Documentation and layout of the site.

- [Heroku](https://id.heroku.com/login): 
    - Used as hosting platform to deploy the project.

### Programs 

- [Balsamiq](https://balsamiq.com/)
   - Allowed the creation of wireframes.

- [Canva](https://www.canva.com/login)
   - Allowed the creation logos & Unquie sitewide touches.
