import { Link } from 'react-router-dom';

export default function DiningHall({children, path, dist, hMeter}) {
    return (
        <Link to={path}>
            <li className="list-none block bg-gradient-to-br from-gray-900 via-black to-gray-800 rounded-xl p-4 shadow-md hover:scale-105 transition-transform duration-300 border border-yellow-500/30 h-full">
                <h3 className="text-xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-yellow-400 to-orange-500">
                {children}
                </h3>
                <p className="text-gray-300 mt-1 text-sm">Distance: {dist} miles</p>
                <p className="text-gray-400 text-sm">Health-meter: {hMeter}</p>
            </li>
        </Link>
    );
}