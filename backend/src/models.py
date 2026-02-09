from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

# make datamodel (tables)

class DiningHallInfo(Base):
    __tablename__ = "dining_hall_info"

    dining_hall_id = Column(Integer, index=True, primary_key=True)
    name = Column(String(100), index=True)
    location = Column(String(100), index=True)

class NutritionalGoals(Base):
    __tablename__ = "nutritional_goals"

    nutritional_goal_id = Column(Integer, index=True, primary_key=True)
    name = Column(String(100), index=True)

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, index=True, primary_key=True)
    name = Column(String(100), index=True)
    weight_lbs = Column(Integer, index=True)
    height_in = Column(Integer, index=True)
    meal_plan = Column(Integer, index=True)
    curr_loc = Column(String(100), index=True)
    nutritional_goal_id = Column(Integer, index=True)

class Items(Base):
    __tablename__ = "items"

    item_id = Column(Integer, index=True, primary_key=True)
    name = Column(String(100), index=True)
    calories = Column(Integer, index=True)
    protein = Column(Integer, index=True)
    carbs = Column(Integer, index=True)
    fats = Column(Integer, index=True)
    dining_hall_id = Column(Integer, index=True)

class MealLog(Base):
    __tablename__ = "meal_log"

    meal_log_id = Column(Integer, index=True, primary_key=True)
    date_time = Column(String, index=True)
    user_id = Column(Integer, index=True)
    dining_hall_id = Column(Integer, index=True)
    item_id = Column(Integer, index=True)
    nutritional_goal_id = Column(Integer, index=True)