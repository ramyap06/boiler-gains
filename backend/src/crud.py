import psycopg2
import uuid
from schemas import ItemsBase

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

def row_to_obj(row):
    item = ItemsBase(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6]
    )
    return item

def post(item: ItemsBase):
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        query = """
            INSERT INTO items (id, name, dining_hall_id, calories, protein, carbs, fats)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id, name, dining_hall_id, calories, protein, carbs, fats;
        """
        item.item_id = int(uuid.uuid4())

        cursor.execute(query, (
            item.item_id,
            item.name,
            item.dining_hall_id,
            item.calories,
            item.protein,
            item.carbs,
            item.fats
        ))
        fetched_item = cursor.fetchone()
        connection.commit()
        if fetched_item is None:
            return None
        return item

    finally:
        if connection:
            cursor.close()
            connection.close()


def get(item_id: int):
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
            item_dicts.append(row_to_obj(row))
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