from sql_connection import get_sql_connection

connection = get_sql_connection()

def get_all_products():
    cursor = connection.cursor()

    query = ('''select product_id, `name`, products.uom_id ,price_per_unit,uom_name
     from products,uom where products.uom_id = uom.UOM_ID;''')

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )
    cursor.close()
    return response

def insert_product(name, uom_id, price_per_unit):
    cursor = connection.cursor()

    query = ('''INSERT INTO products (name, uom_id, price_per_unit)
                VALUES (%s, %s, %s);''')
    data = (name, uom_id, price_per_unit)
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid








print(get_all_products())
print(insert_product('Oil Bottle', 1, 70))

connection.close()