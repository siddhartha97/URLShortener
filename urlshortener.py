import mysql.connector


obj = mysql.connector.connect(user = "*****", password = "******",host = "127.0.0.1",database = "********");



cursor = obj.cursor()

insertval = """INSERT INTO mytable
                    (id,urlstring) 
                    VALUES (%s,%s)"""



input_string = raw_input("Enter the link: ")

val = (0,input_string) #the value

cursor.execute(insertval,val) #inserting

string = [input_string]

sql = "select id from mytable where urlstring in (%s)"

in_p  =', '.join(map(lambda x: "%s",string))

sql = sql % in_p

cursor.execute(sql,string)

row = cursor.fetchone()


#add base 62 val;

x = row[0]

val_store = []

while(x):

    val_store.append(x%62)
    x = x/62


val_store.reverse()



s = ""
for x in val_store:

    sql1 = "select alph from bijective where hashval in (%s)"
    in_p1 = ','.join(map(lambda y: "%s",[x]))
    sql1 = sql1 % in_p1
    cursor.execute(sql1,[x])
    row1 = cursor.fetchone()
    s+=str(row1[0])


print "Siddhartha's url shortener is: sidy.short/"+s

obj.commit()

cursor.close()

obj.close()



