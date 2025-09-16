import { useContext, createContext } from "react";

// Context Type
export interface AppContextType {
    username: string;
    theme: 'light' | 'dark';
}

// Provider 

export const AppContext = createContext<AppContextType | undefined>(undefined);

// Custom hook буюу context ашиглах
export const useAppContext = () => {
    const context = useContext(AppContext);
    if (context === undefined) {
        throw new Error('useAppContext must be used within an AppProvider');
    }
    return context;
}