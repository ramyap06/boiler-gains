import React from 'react';
import { Link } from 'react-router-dom';

export default function Section({children, path}) {
    return (
        <Link to={path}>
            <li className="text-black font-sanserif text-xl hover:text-amber-300">
                {children}
            </li>
        </Link>
    );
}