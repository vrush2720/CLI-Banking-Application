import mysql.connector
Operation = input("").split()

def create():
	connection=mysql.connector.connect(host="localhost",user="root",password="sumeet24",database="banking_app_db")
	cursor=connection.cursor()
	sql1="select Code from banking_app_tb"
	cursor.execute(sql1)
	check=cursor.fetchone()
	for c in check:
		if c == Operation[1]:
			print("Account already exists")
		else:
			sql="insert into banking_app_tb values('%s','%s','%d')"
			cursor.execute(sql %(Operation[1],Operation[2],0))
			print("Account created successfully")
	connection.commit()
	connection.close()

def deposit():
	connection=mysql.connector.connect(host="localhost",user="root",password="sumeet24",database="banking_app_db")
	cursor=connection.cursor()
	sql1="select Code from banking_app_tb"
	cursor.execute(sql1)
	check=cursor.fetchone()
	if Operation[1] not in check:
		print("Account do not exists")
	else:
		sql="update banking_app_tb set Amount='%s' where Code='%s'"
		cursor.execute(sql %(Operation[2], Operation[1]))
		print("Amount deposited successfully")
		connection.commit()
	connection.close()

def withdraw():
	connection=mysql.connector.connect(host="localhost",user="root",password="sumeet24",database="banking_app_db")
	cursor=connection.cursor()
	sql1="select Code from banking_app_tb"
	cursor.execute(sql1)
	check=cursor.fetchone()
	if Operation[1] not in check:
		print("Account do not exists")
	else:
		sql="select amount from banking_app_tb where Code='%s'"
		cursor.execute(sql %(Operation[1]))
		amount=cursor.fetchone()
		final_amount=0
		for at in amount:
			final_amount=int(at)-int(Operation[2])
		print(final_amount)
		sql1="update banking_app_tb set Amount='%s' where Code='%s'"
		cursor.execute(sql1 %(final_amount,Operation[1]))
		connection.commit()
	connection.close()

def balance():
	connection=mysql.connector.connect(host="localhost",user="root",password="sumeet24",database="banking_app_db")
	cursor=connection.cursor()
	sql1="select Code from banking_app_tb"
	cursor.execute(sql1)
	check=cursor.fetchone()
	if Operation[1] not in check:
		print("Account do not exists")
	else:
		sql="select Name, Amount from banking_app_tb where Code='%s'"
		cursor.execute(sql %(Operation[1]))
		data=cursor.fetchone()
		print(data[0]+' '+str(data[1]))
		connection.commit()
	connection.close()

if Operation[0] == "CREATE":
	create()
elif Operation[0] == "DEPOSIT":
	deposit()
elif Operation[0] == "WITHDRAW":
	withdraw()
elif Operation[0] == "BALANCE":
	balance()
else:
	print("invalid action!!!")	
		