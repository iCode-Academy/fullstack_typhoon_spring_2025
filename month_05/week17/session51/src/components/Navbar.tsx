import React from "react";

const Navbar: React.FC = () => {

    return (
        // Fragment
        <>
            <div className="navbar-menu">
                <div className="navbar-menu-left">
                    <p className="navbar-menu-left-green">Alkusr's</p>
                    <p>Portfolio</p>
                </div>
                <div className="navbar-menu-right">
                    <p>Home</p>
                    <p className="description-right">About</p>
                    <p className="description-right">Design</p>
                    <p className="description-right">Illustration</p>
                    <p id="contact-menu">Contact me!</p>
                </div>
            </div>
        </>
    )
}

export default Navbar;