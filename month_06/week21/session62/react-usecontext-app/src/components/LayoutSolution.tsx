import React from "react";
import HeaderSolution from "./HeaderSolution";

interface LayoutProps {
    children: React.ReactNode;
}

const LayoutSolution: React.FC<LayoutProps> = ({children}) => {
    return (
        <div>
            <h1>Layout Part</h1>
            <HeaderSolution />
            <main>
                {children}
            </main>
        </div>
    )
}

export default LayoutSolution;