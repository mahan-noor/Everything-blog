## Author
Ismahan Abey

## Description
* A web application made using Python's Flask that allows a user to create blog posts on their account and allow other users to view


## installation
1. cloning the repo https://github.com/mahan-noor/Everything-blog.git

2. move to the folder and also install whats in the requirements
   * cd E-blog
   * pip install -r requirements.txt

3. exporting configuration
  * export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

4. running the app
   * python3.8 manage.py server

5. app in the browser
   * http://127.0.0.1:5000/


## Features
 * A landing page with a list of all the posted blogs.
 * A display of random quotes.
 * A link to create a new blog posts.
 * A navigation bar with options to sign-in, navigate to your profile, sign-out and navigate * back to the home-page.
 * A link to navigate to the full blog post.
 * An option to delete the post once on the full blog post.
 * An option to comment on the blog post.

## Behaviour Driven Development (BDD)
* Behaviour => Page loads, landing page with a list of all the posted blogs appears.	
* Input =>The user, after signing-up or signing-into their account as a writer, can click on write a log  and submit their own blogs.	
* Output =>The blog-post they create is added to the list of blog posts in the landing page.




## Technology used
   * Python3.8
   * Flask
   * Bootstrap
   * CSS
   * Heroku

## Known bugs
  * There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact info
 * if you have any query email me at ismahanabey@gmail.com
 
 ## Licence
  * MIT LICENCE
  * Copyright (c) 2021 Ismahan Abey
