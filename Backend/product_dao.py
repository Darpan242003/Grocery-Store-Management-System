import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='grocery')

cursor = cnx.cursor()

query = ("select product_id, `name`, products.uom_id ,price_per_unit,uom_name from products,uom where products.uom_id = uom.UOM_ID;")

cursor.execute(query)

for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
    print(product_id, name, uom_id, price_per_unit, uom_name)

cnx.close()