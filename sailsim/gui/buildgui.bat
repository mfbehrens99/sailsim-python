call .env\Scripts\activate.bat
pyside6-uic sailsim\gui\main.ui > sailsim\gui\qtmain.py
autoflake -i --remove-all-unused-imports sailsim\gui\qtmain.py
autopep8 -i -a sailsim\gui\qtmain.py
rem pause
