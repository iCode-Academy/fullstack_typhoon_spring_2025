import React from "react";
import Header from "./Header";

interface LayoutProps {
    username: string;
    theme: 'light' | 'dark';
    children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({username, theme, children}) => {
    return (
        <div>
            <h1>Layout Part</h1>
            <Header username={username} theme={theme} />
            <main>
                {children}
            </main>
        </div>
    )
}

export default Layout;