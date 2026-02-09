import { useParams } from "react-router-dom";
import Navbar from '../components/Navbar';
import FoodItem from "../components/FoodItem";

export default function DiningHallPage() {
    const { hallName } = useParams();
    return (
        <div className="min-h-screen bg-black text-white">
            <Navbar />

            {/* Title */}
            <div className="p-6 text-center">
                <h1 className="text-3xl font-bold capitalize mb-2">
                    {hallName} Dining Hall
                </h1>
            </div>

            {/* Food items */}
            <div className="flex justify-center mt-6">
                <div className="w-3/4 grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-2">
                    <FoodItem name="Sandwich" calories={530} carbs={30} fats={10} protein={25} />
                    <FoodItem name="Fries" calories={530} carbs={30} fats={10} protein={25} />
                    <FoodItem name="Yogurt" calories={530} carbs={30} fats={10} protein={25} />
                    <FoodItem name="Banana" calories={530} carbs={30} fats={10} protein={25} />
                </div>
            </div>
        </div>
    );
}