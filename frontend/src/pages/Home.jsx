import Navbar from '../components/Navbar';
import Header from '../components/Header';
import DiningList from '../components/DiningList';

export default function Home() {
    return (
        <div>
            <Navbar />
            <div className="bg-gradient-to-br from-gray-900 via-black to-gray-800 p-10">
            <Header />
            <DiningList />
            </div>
        </div>
    );
}