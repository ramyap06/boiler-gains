import React from "react";

export default function Header() {
    return (
        <div className="flex flex-col items-center justify-center min-h-[60vh] text-white text-center">
            <h1 class="text-6xl font-extrabold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-yellow-400 to-orange-500 drop-shadow-lg">
            BoilerGains
            </h1>
            <h3 class="mt-4 text-xl font-light text-gray-300 italic">
            Your best friend for grueling dining hall food...
            </h3>
        </div>
    );
}