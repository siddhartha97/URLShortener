x = input("Enter the number: ")

val_store = []

while(x):
    val_store.append(x%62)
    x = x/62

val_store.reverse()

#print (val_store)

for x in val_store:
    print x
