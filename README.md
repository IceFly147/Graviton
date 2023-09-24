# Learnova.co


#### How to clone this repositary

- First Fork this Repository:

  <img src="https://github.com/IceFly147/Learnova.co/assets/100683747/ab66ff97-d0eb-44e5-ae10-244cb351ed47" width="500px"/>

- Hit create fork without changing any settings:

  <img src="https://github.com/IceFly147/Learnova.co/assets/100683747/9209da65-dd9b-440b-9d6a-afe483c1fdff" width="500px"/>

- Then clone the repositary to your local machine by running ` git clone https://github.com/[Your_Username]/Learnova.co.git`.
- Make Sure to replace [Your_Username] with your github username.
- In the above case the terminal prompt should display

  <img src="https://github.com/IceFly147/Learnova.co/assets/100683747/813fd274-506d-4e10-97ba-184a6798ba0a" width="500px"/>
  
- run `pip install virtualenv` then run `python -m venv env` to create make sure to run this command in the folder in which the project file in located in.
- This will create a virtual enviroment which will need to be activated via `./env/Scripts/activate.ps1`
- Then run `python -m pip install -r requirements.txt`
- All the packages will now be installed, to run the server type `python manage.py runserver`.This should give a local host link which will direct to the web app.
