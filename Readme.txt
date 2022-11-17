# CLI-Banking-application
Database file(MySQL 8.0): bank_app_db.sql
Application file(Python 3.8): bank_app.py

For configuring Mysql database edit mysql server root password in application file (replace "mysqlpass" with your mysql server password)
line of code: 5, 20, 35,56

STEPS:
1] Log into Mysql Command Line Interface and execute "source [path of database file]" eg. "source E:\bank_app_db.sql"
2] Open Command Line Interface and enter " pip install mysql-connector-python "
3] Type "bank_app.py" and enter
4] For account creation: 
   Type "[Action] [Account code] [Account holder name]" eg. CREATE a01 vrushali
5] For depositing amount:
   Type "[Action] [Account code] [Amount to be deposited]" eg. DEPOSIT a01 7000
6] For withdrawing amount:
   Type "[Action] [Account code] [Amount to be withdraw]" eg. WITHDRAW a01 7000
7] For checking balance: 
   Type "[Action] [Account code] " eg. BALANCE a01
