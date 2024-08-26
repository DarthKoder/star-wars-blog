# <Star-Wars-Discussion-Blog>

# Star Wars Discussion Blog

Star Wars Discussion Blog is an online blog for star wars fans to create posts and comment on posts and discuss their thoughts and opinions on the franchise.

Anybody can access it, register by creating an account and login to start discussing. This can be done via desktop, tablet or mobile as the site is responsive. 

All users will need to go through a registration process before they can participate. They will the need to login with a authenticated user profile to either post or comment, they will also be able to edit or delete any post they themselves have created.

![Narth Vaders Question Raiders | Star Wars Edition](/assets/img/star-wars-quiz-game-start-screen.png)
 
[View Narth Vaders Question Raiders | Star Wars Edition project here](https://github.com/DarthKoder/Star-Wars-Question-Raider)
- - -
## Table of Contents
### [User Experience (UX)](#user-experience-ux-1)
* [Rationale](#rationale-1)
* [User Stories](#user-stories)
### [Database Schema](#database-schema)
* [User Table](#user-table)
* [Post Table](#post-table)
* [Comment Table](#comment-table)
### [CRUD Functionality](#crud-functionality)
* [Create](#create)
* [Read](#read)
* [Update](#update)
* [Delete](#delete)
### [Features](#features)
* [Existing Features](#existing-features)
### [Features Left to Implement](#features-left-to-implement-1)
### [Design](#design-1)
### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
* [Validation Results](#validation-results)
* [Manual Testing](#manual-testing)
* [Lighthouse Report](#lighthouse-report)
### [Deployment and local development](#deployment-and-local-development-1)
* [GitHub Pages](#github-pages)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Local Clone](#local-clone)
### [Credits](#credits-1)
### [Acknowledgements](#acknowledgements-1)
---
## Rationale

## User Experience (UX)

### Rationale

This website is designed for star wars fans to create posts and comment on posts and discuss their thoughts and opinions.

The aim is to cater to all fans of the genre, whether they are die hard fans or new fans with questions or opinions. The site is there to enable people to discuss their thoughts and opinions with like-minded individuals help people learn more about Star Wars. It is to help people have fun while also be intuitive and informative at the same time.

There is clear and simple intuitive buttons as guidance to help the user along their way, such as a "Register", "Login", "Logout", "Home", "Create Post", "Edit Post", "Delete Post" and so on. You also recieve flash messages on the page when achieving somwething such as creating a post or comment, editing and so on. There is also a modal that pops up as defensive programming to ensure there is confirmation when deleting a post or comment. 

Once registered, the user must input their username/email along with a password to begin participating in the discussions, there is also a 'remember me' checkbox to remember the users id from the database, this is all to create a more personal experience.

To help inspire the user and bring them into the Star Wars universe for their experience, I have used familiar star wars related colours and fonts to help make the user feel immersed and really connect with the Star Wars theme. 

### User Stories

 * First-time visitor goals
    * Have fun when posting & reading others blogs and comments.
    * Bring pleasure to the user with familiar Star Wars immersion.
    * Easily navigate throughout the site.
    * Be able to complete registration and login easily with the intuitive design.
    
 * Returning visitor goals
    * Be able to have variety with other peoples posts/comments of thoughts and opinions.
    * Have the opportunity to get involved with all sorts of different conversations with other interested individuals.
    * Enjoy the familiar aesthetic.

 * Frequent user goals
    * Always being able to navigate their way.
    * Have the opportunity to get more and more information within the genre and discuss all and everything they wanted relating to star wars.
    * Enjoy the familiar aesthetic.
    * Review the posts and any added comments added by other users at all times.
    * Review any updates to their own or others posts.
    
- - -

## Database Schema

* The database schema consists of three main tables:

* User: Stores user credentials and related information.
* Post: Stores blog posts created by users.
* Comment: Stores comments on blog posts.

See the Flowchart For the Schema here: ![Flow Chart - Star Wars Blog](/starwars_blog/static/img/starwars-blog-schema-flowchart.png)

### User Table

* id: Primary key
* username: Unique username for login
* email: Optional email for login
* password_hash: Hashed password

### Post Table

* id: Primary key
* title: Title of the post
* body: Content of the post
* timestamp: Date and time of creation
* user_id: Foreign key linking to the User table
* film_name: Optional field for the name of the Star Wars film
* film_num: Optional field for the episode number
* year_of_release: Optional field for the year the film was released
* favourite_character: Optional field for the user's favorite character

### Comment Table

* id: Primary key
* body: Content of the comment
* timestamp: Date and time of creation
* post_id: Foreign key linking to the Post table
* user_id: Foreign key linking to the User table

- - -

## CRUD Functionality

### Create
   * Create a user profile by registering      
   * Once logged in, Create posts and comments      

### Read
   * Read usernames for password check
   * Read username to check if user exists
   * Read posts created by yourself and others
   * Read comments created by yourself and others      
   * Read information an all posts such as user crteated, timstamps and the optional features         

### Update
   * 'Remember me' functionality
   * Functionality to edit owned posts 
   * Functionality to update posts with comments

### Delete
   * Functionality to delete owned posts
   * Functionality to delete owned comments

- - - 

## Features

* Genre Based: This website is targeting people who interested in Star Wars.
* Emersion: The user can enjoy the Star Wars aesthetic whist having good discussions with other fans.
* Intuitive: They can use the intuitive design to navigate through the game with ease, whether on a mobile, tablet or desktop computer.
* User Authentication: Users can register, log in, and log out securely.
* Blog Post Creation: Authenticated users can create, edit, and delete blog posts.
* Comments: Users can comment on blog posts.
* Responsive Design: The application is styled using MaterializeCSS for a modern and responsive user interface.
* Secure Password Handling: User passwords are securely hashed using Werkzeug's password hashing utilities.
* Favorite Features: Users can mention their favorite characters Star Wars in their posts.
* Database: The database will store information regarding the users id and passwords, can remember their ids, posts and comments.

### Existing Features

* Site Logo
    * This is the websites logo to show what it is all about and can be seen as constant throught the game and series.
    * I have used the Star Wars sith red #ff0000 for the logo which turns white #fff when hovered over.

    ![Site Title/Logo](/starwars_blog/static/img/starwars-blog-logo.png)

* Navbar & Sidenav Logo
    * This is the websites navbar to be used for navigation around the site, When on mobile it will be a sidebar.
    * I have used the Star Wars jedi blue #007bce for this that turn Star Wars Yerllow #feda4a when hovered over.
    * When NOT logged in, the navbar/sidebar will show the options 'Home', 'Login', 'Register' which will take you to the associated pages.
    * When logged in, the navbar/sidebar will show the options 'Home', 'Create Post', 'Logout' which will take you to the associated pages or log the user out.
    * The sidebar will have a menu icon on the top left hand side of the screen when on a mobile device.

    ![Navbar](/starwars_blog/static/img/star-wars-blog-navbar.png)

    ![Sidebar](/starwars_blog/static/img/star-wars-blog-sidebar.png)

    ![Sidebar Icon](/starwars_blog/static/img/star-wars-blog-sidebar-icon.png)

* Register Screen 
    * The Register Screen is the screen that come after clicking the "Register" button on the navbar/sidenav.
    * It has a form to fill out to create a username and password along with your email address.
    * This is where the user will add their information to the database and create their profile.
    * This will allow the user to login and create posts and comment on posts.
    * There is a reactive button that will submit the form when complete, this has a hover function to help with UX.
    * You will recieve a flash message at the top of the screen when successfully registered.


    ![Register Screen](/starwars_blog/static/img/star-wars-blog-register.png)

* Login Screen 
    * The Login Screen is the screen that come after clicking the "Login" button on the navbar/sidenav.
    * It has a form to fill out with a username/email and password.
    * This is where the user will authenticate their information with the database and login to their profile.
    * This will allow the user to create posts and comment on posts.
    * There is a reactive button that will submit the form when complete, this has a hover function to help with UX.
    * There is a 'Remember Me' checkbox also which will remember the users username and automatically populate it if the page is reloaded.


    ![Login Screen](/starwars_blog/static/img/star-wars-blog-login.png)

* Main Homepage
    * It is the opening screen to the site.
    * This has the Navbar, Site logo, Page Heading, User Posts & Comments along with the 'Create Post' button.
    * This page will also show the 'Edit' and 'Delete' button on owned posts when the authenticated user is logged in.
    * It uses familliar fonts such as the "Star Wars" font and then "Orbitron", to give it more of a Star Wars feel and space like immersion.
    * It contains a reactive buttons to allow easy navigation to Create Post, Edit Post, Delete Post. This button also has a hover effect to let the user know the button can be activated.
    * I have used colours associated with Star Wars such as sith red #ff0000, the famous Star Wars yellow #feda4a, Jedi green #239400, Jedi blue #007bce along with a contrasting white #fff, all on the space style black #000000 and #222 for card contrast. These colours are to help make the user feel immersed and really connect with the Star Wars theme. 
    * There is a 'READ MORE' button which will take to to the full post screen witch has all the post information and comments related to that post.

    ![Main Homepage](/starwars_blog/static/img/star-wars-blog-index.png)

* Post Screen 
    * The Post Screen is the screen that come after clicking the "READ MORE" button on the posts on the homepage/index.
    * It will show the post title, post description and all of the filled out optional fields, timestamp, comments.
    * If logged in you will see the option to comment, otherwise it will ask you to login to comment.
    * If logged in and you own the post it will show you the 'Edit Post', 'Delete Post' and 'Delete Comment' buttons, these are all reactive buttons when hovered over.

    ![Post Screen](/starwars_blog/static/img/star-wars-blog-post.png)

* Edit Post Screen 
    * The Edit Post Screen is the screen that come after clicking the "Edit Post" button on an owned post on the homepage/index when logged in.
    * It will show the post title, post description and all of the filled out optional fields, timestamp that can all be edited.
    * There will be an 'Update Post' button which will submit the changes, you will recieve a flash message at the top of the screen when successfully updated.
    

    ![Edit Post Screen](/starwars_blog/static/img/star-wars-blog-edit-post.png)

    ![Edit Post Success Message](/starwars_blog/static/img/star-wars-blog-edit-success-msg.png)

* Delete Post/Comment Screen 
    * The Delete Edit Post Screen is the screen that come after clicking the "Delete Post" button on an owned post on the homepage/index when logged in.
    * Once clicked, the button will initiate a pop up modal that will ask for confirmation of the deletion.
    * You will recieve a flash message at the top of the screen when successfully deleted.
    * This is the same scenario for comment deletion.
    

    ![Delete Button](/starwars_blog/static/img/star-wars-delete-btn.png)

    ![Delete Post/Comment Screen](/starwars_blog/static/img/star-wars-blog-post.png)

    ![Delete Post Modal](/starwars_blog/static/img/star-wars-blog-delete-post-modal.png)

    ![Delete Message](/starwars_blog/static/img/star-wars-blog-delete-msg.png)

- - -

## Error Pages

### 404 Page

In the event of a page not found the error handler will render a page with a link back to the homepage.

- - -

## Features Left to Implement

* Like/Dislike System: Implement a feature to like or dislike posts and comments.
* Profile Pages: Add user profile pages that display a user's posts and favorite Star Wars content.
* Advanced Search: Enable users to search by film name, character, and more.
* Email Notifications: Implement email notifications for comments and likes on posts.
* Search Functionality: Users can search for specific posts by title or content.
* Favorite Features: Users can mention their favorite movies, and scenes from Star Wars in their posts.

## Design

 * Colour Scheme
    * Primary colours used on the website: ![Color Scheme](/starwars_blog/static/img/star-wars-blog-clour-palette.png)

 * Typography
    * 'Orbitron' font is the main font used throughout the site with the addition of "Star Wars". These all have sans-serif as its fallback font, in case the imported fonts dont load for any reason.
    * The main logo uses the 'Star Wars' font.
    * "Star Wars" have been used in the page titles and "Orbitron" has been used for the paragraph text. 

 * Wireframes
    * Figma: Easy to create, uses and shares detailed images whilst also effective.
    * Please find my wireframes here: [Figma: Star-wars-blog](https://www.figma.com/design/v0S3A7Z9lYm8i7cmwbVV4X/Star-wars-blog?node-id=0-1&t=ZNw5ISooLO2AKF2b-1)

- - -

## Bug fixes 

* One issue I came across was getting the optional post fields to display if filled out as thewy kept appearing as 'none'. 
   - After rigorous testing and trial and error, I realised that I had the code for this in the wrong function in routes.py thjat was not saving the correct values to the post request handler and to also run if statements in the html. 

* Another bug I had was that, while testing, was the "Remember Me" check box was being ticked but not remembering the usernam on a page reload.
   - This was due having the code wrong, so I implemented some javascript to take over and auto populate the field with the users username.

* The biggest issue I had was trying to get postgresql and all the other dependencies to work together initially.
   - I had to review alot of the versions and update and migrate alot after doing alot of research to get it all to function and connect.

* There were alot of minor code and syntax issues I faced but I m,anaged to research them and fix them along the way.
   - I feel that I learned alot from these minor issues about coding with python and using the other dependencies and how they work. 

- - -

## Technologies Used

 * [HTML5](https://en.wikipedia.org/wiki/HTML5)
 * [CSS3](https://en.wikipedia.org/wiki/CSS) 
 * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
 * [Python: The core programming language.](https://en.wikipedia.org/wiki/Python_(programming_language))
 * [Flask: The web framework used to build the application.](https://flask.palletsprojects.com/en/3.0.x/)
 * [Flask-SQLAlchemy: An ORM used for database interactions.](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
 * [Flask-Migrate: Used for database migrations.](https://flask-migrate.readthedocs.io/en/latest/)
 * [Flask-Login: Used for handling user authentication.](https://flask-login.readthedocs.io/en/latest/)
 * [PostgreSQL: The relational database management system used to store data.](https://www.postgresql.org/)
 * [Jinja2: The templating engine used for rendering HTML](https://jinja.palletsprojects.com/en/3.1.x/)

- - -

## Frameworks, Libraries & Programs Used

 * [Visual Studio Code](https://visualstudio.microsoft.com/)
    * Desktop version to write and edit the code. 
 * [Github](https://github.com/)
    * Deployment of the website and storing the files online.
    * Version control.
 * [Google Fonts](https://fonts.google.com/)
    * Import main fonts the website.
 * [CDNFonts](https://www.cdnfonts.com/)
    * Import main fonts the website.
 * [MaterializeCSS 1.0.0: A CSS framework for styling and responsiveness.](https://materializecss.com/)
    * Used for its helpful responsive layouts and components such as modals and sidenav.
 * [Heroku](https://www.heroku.com/home)
    * Used to deploy the website.

- - -

## Testing

The W3C Markup Validator and W3C CSS Validator services were used to validate every page of the project, to ensure there were no errors.

 * [W3C Markup Validtor](https://validator.w3.org/)
 * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
 * [JS Lint](https://www.jslint.com/)
 * [JS Hint](https://www.jshint.com/)

### Validation results

<details>
<summary>index.html
</summary>

![Index.html validation result](/starwars_blog/static/img/Index.html-lighthouse-report.png)
</details>

<details>
<summary>style.css
</summary>

![CSS validation result](/assets/img/sw-quiz-css-validator-results.png)
</details>

<details>
<summary>style.css
</summary>

![JavaScript validation result](/assets/img/)
</details>

### Manual Testing

* The website was tested on Google Chrome & Microsoft Edge.
* The website was viewed on a desktop computer and Moto G Power mobile phone.
* A large amount of manual testing was done to ensure all buttons are working correctly.
* A large amount of manual testing was done to ensure that the logic behind the game worked and the user experience is fulfilled.
* A large amount of manual testing was done to ensure that there were no bugs hindering the game and any progression.
* Family and friends were asked to review the website for a better understanding of the user experience.
* Dev Tools was used to test how the site looks on various screen sizes.
* Dev Tools Lighthouse was use to test the performance accessibility, best prectices and SEO of each page.
* JS Lint was used to ensure there are no major issues with the script.

### Lighthouse Report

#### Desktop analysis
<details>
<summary>Home Page
</summary>

![Homepage Screen Lighthouse Report (index.html)](/starwars_blog/static/img/Index.html-lighthouse-report.png)
</details>

<details>
<summary>Create Post Page
</summary>

![Create Post Screen Lighthouse Report (index.html)](/starwars_blog/static/img/create-post-lighthouse-report.png)
</details>

<details>
<summary>Edit Post Page
</summary>

![Edit Post Screen Lighthouse Report (index.html)](/starwars_blog/static/img/edit-post-lighthouse-report.png)
</details>

<details>
<summary>Register Post Page
</summary>

![Register Screen Lighthouse Report (index.html)](/starwars_blog/static/img/register-lighthouse-report.png)
</details>

<details>
<summary>Login Page
</summary>

![Login Screen Lighthouse Report (index.html)](/starwars_blog/static/img/login-lighthouse-report.png)
</details>

#### Mobile analysis
<details>
<summary>Home Page
</summary>

![Starting Screen Mobile Lighthouse Report (index.html)](/assets/img/sw-quiz-start-mobile-lighthouse.png)
</details>

<details>
<summary>Home Page
</summary>

![Question Screen Mobile Lighthouse Report (index.html)](/assets/img/sw-quiz-question-mobile-lighthouse.png)
</details>

---

## Deployment and local development

### GitHub Pages

GitHub Pages used to deploy live version of the website.
1. Log in to GitHub and locate [GitHub Repository Hunter Kitchen Design](https://github.com/DarthKoder/Star-Wars-Question-Raider)
2. At the top of the Repository(not the main navigation) locate "Settings" button on the menu.
3. Scroll down the Settings page until you locate "GitHub Pages".
4. Under "Source", click the dropdown menu "None" and select "Main" and click "Save".
5. The page will automatically refresh.
6. Scroll back to locate the now-published site [link](https://github.com/DarthKoder/Star-Wars-Question-Raider) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [GitHub Repository Star Wars Question Raider](https://github.com/DarthKoder/Star-Wars-Question-Raider)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.

### Local Clone

1. Log in to GitHub and locate [GitHub Repository Star Wars Question Raider](https://github.com/DarthKoder/Star-Wars-Question-Raider)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

---

## Credits

### Code
 * Understanding some JavaScript concepts and code needed for certail aspects of the game [W3schools](https://www.w3schools.com/)
 * The README template was helpfully provided by my mentor Mitko at Code Institute [Lunar-Escape](https://github.com/Thomas-Tomo/Lunar-Escape)

### Content

 * All content was written by the developer.
 * [Color contrast checker](https://coolors.co/contrast-checker/112a46-acc8e5) was used to decide which colours would be used for the website.

### Media 

 * [Pexels](https://www.pexels.com/) free stock photos & videos, royalty free images & videos.

---

## Acknowledgements
 * My mentor Mitko for helping me with ideas for the game and ways to build it. 
 * W3schools for the information online needed to help me build this game. 
 * Slack community for encouragement and information.
 * My motivation for this project was my love for Star Wars and wanted to build something for the community. 