import axios from "axios";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState('');

 const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
        await axios.post('/api/users/register/', {
            username,
            email,
            password,
            password2
        });

        navigate('/login')
    } catch (error) {
        console.error(`Registration failed. ${error}`);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input
        type="text"
        value={username}
        onChange={(e) => {
          setUsername(e.target.value);
        }}
        placeholder="Username"
        required
      />
      <input
        type="email"
        value={email}
        onChange={(e) => {
          setEmail(e.target.value);
        }}
        placeholder="Email"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => {
          setPassword(e.target.value);
        }}
        placeholder="Password"
        required
      />
      <input
        type="password"
        value={password2}
        onChange={(e) => {
          setPassword2(e.target.value);
        }}
        placeholder="Confirm Password"
        required
      />
      <button type="submit">Register</button>
    </form>
  );
};

export default Register;
