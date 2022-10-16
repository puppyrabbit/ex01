import pymysql

db=pymysql.connect(host="localhost",user="root",password="1103",charset="utf8")
print(db)

cursor=db.cursor()
cursor.execute('USE exam;')

cursor.execute('INSERT INTO itemSales (date,userNo,itemCode,salesCount) VALUES ("2022-08-07","a4","b1","3")')
cursor.execute('INSERT INTO itemSales (date,userNo,itemCode,salesCount) VALUES ("2022-08-06","a4","b2","2")')
cursor.execute('INSERT INTO itemSales (date,userNo,itemCode,salesCount) VALUES ("2022-08-07","a2","b1","2")')
cursor.execute('INSERT INTO itemSales (date,userNo,itemCode,salesCount) VALUES ("2022-08-07","a1","b2","4")')
cursor.execute('INSERT INTO itemSales (date,userNo,itemCode,salesCount) VALUES ("2022-08-07","a3","b3","5")')
cursor.execute('INSERT INTO itemSales (date,userNo,itemCode,salesCount) VALUES ("2022-06-07","a3","b1","10")')
cursor.execute('INSERT INTO itemSales (date,userNo,itemCode,salesCount) VALUES ("2022-06-27","a3","b2","8")')
cursor.execute('INSERT INTO itemSales (date,userNo,itemCode,salesCount) VALUES ("2022-08-01","a1","b3","7")')

cursor.execute('INSERT INTO User (userNo,regDate) VALUES ("a1","2022-08-07")')
cursor.execute('INSERT INTO User (userNo,regDate) VALUES ("a2","2022-08-01")')
cursor.execute('INSERT INTO User (userNo,regDate) VALUES ("a3","2022-07-07")')
cursor.execute('INSERT INTO User (userNo,regDate) VALUES ("a4","2022-06-07")')

cursor.execute('INSERT INTO D_item (itemCode,itemName,itemPrice) VALUES ("b1","도란검","350")')
cursor.execute('INSERT INTO D_item (itemCode,itemName,itemPrice) VALUES ("b2","삼위일체","3300")')
cursor.execute('INSERT INTO D_item (itemCode,itemName,itemPrice) VALUES ("b3","암흑의인장","300")')



db.commit()
db.close()