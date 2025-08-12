import React, { useState } from "react";
import { InputField } from "./InputField";
import { ProfilePreview } from "./ProfilePreview";

interface FormState {
  firstName: string;
  lastName: string;
  email: string;
}

const ProfileEditor: React.FC = () => {
  const [formData, setFormData] = useState<FormState>({
    firstName: "",
    lastName: "",
    email: "",
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  return (
    <>
      <h2>Profile Editor</h2>
      <InputField
        label="First Name"
        name="firstName"
        value={formData.firstName}
        onChange={handleInputChange}
      />
      <InputField
        label="LastName Name"
        name="lastName"
        value={formData.lastName}
        onChange={handleInputChange}
      />
      <InputField
        label="Email"
        name="email"
        value={formData.email}
        onChange={handleInputChange}
      />
      {/* Preview Component */}
      <ProfilePreview data={formData} />
    </>
  );
};

export default ProfileEditor;
