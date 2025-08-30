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
    return response

print(get_all_products())