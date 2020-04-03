Used bootstrap to implement layouts and used an e-commerce bootstrap template 
for the home, product and checkout page which we changed around to suit needs. 
Used crispy forms to make buttons and text areas neater, and used Django 
authentication to provide the user authorisation functionalities. We also 
implemented a Bing Maps API to show location of our store. 

Instructions for deploying:

1) First, access our GitHub repository by cloning it: 

git clone https://github.com/craigd00/mobile_store

2) Then, create a Python virtual environment (preferably using anaconda powershell), 
and install the requirements.txt file so that the packages we have installed save

conda create <name of env>

conda activate <name of env>

pip install -r requirements.txt

3) Then, populate the database, using our population script

python population_script.py

4) It should now be working if you run the server and copy the address

python manage.py runserver