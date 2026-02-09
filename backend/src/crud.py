import psycopg2
import uuid

DATABASE_URL = "postgresql://postgres:ramyap06@localhost:5432/food_app"

def row_to_dict(row):
    return {
        "id": row[0],
        "name": row[1],
        "dining_hall_id": row[2],
        "calories": row[3],
        "protein": row[4],
        "carbs": row[5],
        "fats": row[6],
    }

def post(item_dict: dict):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        query = """
            INSERT INTO items (id, name, dining_hall_id, calories, protein, carbs, fats)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id, name, dining_hall_id, calories, protein, carbs, fats;
        """
        item_id = str(uuid.uuid4())

        cursor.execute(query, (
            item_id,
            item_dict["name"],
            item_dict["dining_hall_id"],
            item_dict["calories"],
            item_dict["protein"],
            item_dict["carbs"],
            item_dict["fats"],
        ))
        item = cursor.fetchone()
        connection.commit()
        if item is None:
            return None
        return row_to_dict(item)

    finally:
        if connection:
            cursor.close()
            connection.close()


def get(item_id: str):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE id = %s"
        cursor.execute(query, (item_id,))
        item = cursor.fetchone()
        if item is None:
            return None
        return row_to_dict(item)
    finally:
        if connection:
            cursor.close()
            connection.close()


def get_all():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        cursor.execute(query)
        items = cursor.fetchall()
        item_dicts = []
        for row in items:
            print("id = ", row[0], )
            print("name = ", row[1])
            print("dining_hall_id  = ", row[2])
            print("calories  = ", row[3])
            print("protein  = ", row[4])
            print("carbs  = ", row[5])
            print("fats  = ", row[6], "\n")
            item_dicts.append(row_to_dict(row))
        return item_dicts
    finally:
        if connection:
            cursor.close()
            connection.close()


def put(item_id: str, item_dict: dict):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        query = """
            UPDATE items
            SET name=%s, dining_hall_id=%s, calories=%s, protein=%s, carbs=%s, fats=%s
            WHERE id=%s
            RETURNING id, name, dining_hall_id, calories, protein, carbs, fats;
        """

        cursor.execute(query, (
            item_dict["name"],
            item_dict["dining_hall_id"],
            item_dict["calories"],
            item_dict["protein"],
            item_dict["carbs"],
            item_dict["fats"],
            item_id
        ))
        item = cursor.fetchone()
        connection.commit()
        if item is None:
            return None
        return row_to_dict(item)

    finally:
        if connection:
            cursor.close()
            connection.close()

def delete(item_id: str):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE id=%s RETURNING id;"
        cursor.execute(query, (item_id,))
        row = cursor.fetchone()
        connection.commit()
        return row is not None

    finally:
        if connection:
            cursor.close()
            connection.close()

def delete_all():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        
        query = """DELETE FROM items"""
        cursor.execute(query)
        connection.commit()
        return cursor.rowcount
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")