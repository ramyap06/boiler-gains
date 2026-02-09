import React from "react";
import Section from "./Section";

export default function Navbar() {
    return (
        <header className="bg-amber-200">
            <nav>
                <ul className="flex items-center gap-20 p-4">
                    <Section path="/">Home</Section>
                    <Section path="#">Halls</Section>
                    <Section path="#">About</Section>
                    <Section path="#">FAQ</Section>
                </ul>
            </nav>
        </header>
    );
}