import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="simrin",
    database="nikki"
)
cursor=db.cursor()
#
# sql="INSERT INTO students VALUES (%(id)s, %(name)s)"
# val={"id":14,
#      "name":"Layla"}
#
# cursor.execute(sql, val)
#
# db.commit()

# sql="SELECT sname, age, rating FROM sailors"
# cursor.execute(sql)
#
# for sname, age, rating in cursor:
#     print("The age of %s is %s. The rating of the sailor is %s" %(sname, age, rating))


sql="SELECT * FROM students WHERE student_id>%s"
val=7
cursor.execute(sql, (val,))
print(cursor.fetchall())

