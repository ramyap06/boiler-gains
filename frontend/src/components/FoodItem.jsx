import React, { useEffect, useState } from 'react';
import api from '../api.js';


export default function FoodItem({ name, calories, carbs, protein, fats}) {
  return (
    <button className="
      w-full
      text-left
      rounded-2xl
      border border-gray-200
      bg-gradient-to-br from-white to-gray-50
      p-6
      shadow-lg
      hover:shadow-xl
      transition-all duration-200
      transform hover:-translate-y-1
      focus:outline-none focus:ring-2 focus:ring-blue-500
    ">
      <h2 className="text-xl font-bold text-gray-900 mb-3">{name}</h2>
      <div className="text-gray-700 space-y-1 text-sm">
        <p>Calories: <span className="font-medium">{calories}g</span></p>
        <p>Carbs: <span className="font-medium">{carbs}g</span></p>
        <p>Protein: <span className="font-medium">{protein}g</span></p>
        <p>Fats: <span className="font-medium">{fats}g</span></p>
      </div>
    </button>
  );
}