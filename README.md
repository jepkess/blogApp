Blog-App
#### Author
Vincent Kipkirui 

## Description
Its a personal blogging website where i can create and share the opinions.Also it allows others users to view and comment on my opinion posted.As a user he or she can log into the website and subscribed.

## Setup and installations
1. Clone Project to your machine
2. Activate a virtual environment on terminal: `source venv/bin/activate`
3. On your terminal run `python3.8 manage.py server`


  
## Specifications
1. user Authentication
 
### Prerequisites
* python3.8
* virtual environment
* pip
#### Clone the Repo and rename it to your suitable name of your choice.
git clone `https://github.com/jepkess/blogApp.git`

#### Initialize git and add the remote repository
1. git init 

2. git remote add origin https://github.com/jepkess/Pitch-App.git



#### Create  the virtual environment and activating it.
1. python3.8 -m venv virtual (creating the environment)
2. source virtual/bin/activate (activating)
#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`
#### Make and run migrations
bash
python3.8 manage.py check
python manage.py make migrations 
python3.8 manage.py sqlmigrate 
python3.8 manage.py migrate

#### Run the app
bash
python3.8 manage.py runserver

Open [localhost:5000](http://127.0.0.1:5000)
## Testing the Application
`python3.8 manager.py test`
## Technologies used
1.  python 3.8 version
2. Flask
3.  Boostrap
4.  HTML
5. CSS

## live link
[live](https://bloggapplication.herokuapp.com)


### Licence
This project is under the  [MIT](LICENSE.md) licence