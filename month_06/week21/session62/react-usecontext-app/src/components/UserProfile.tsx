import React from "react";
interface UserProfileProps {
    username: string;
    theme: 'light' | 'dark';
}


const UserProfile: React.FC<UserProfileProps> = ({username, theme}) => {
    const style = {
        color: theme === 'dark' ? '#FFF' : '#000',
        backgroundColor: theme === 'dark' ? '#333' : '#F0F0F0',
        padding: '1rem',
        borderRadius: '8px'
    }
    return (
        <div style={style}>
            <h2>User Info</h2>
            <p>Name: {username}</p>
            <p>Active Theme: {theme} </p>
        </div>
    )
}

export default UserProfile;