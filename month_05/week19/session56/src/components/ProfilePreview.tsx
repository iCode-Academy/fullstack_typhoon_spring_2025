import React from "react";

type ProfileData = {
  firstName: string;
  lastName: string;
  email: string;
};

type ProfilePreviewProps = {
  data: ProfileData;
};

export const ProfilePreview = ({ data }: ProfilePreviewProps) => {
  return (
    <div
      style={{ marginTop: "20px", border: "1px solid #ccc", padding: "10px" }}
    >
      <h3>Live Preview</h3>
      <p>
        <strong>First Name:</strong>
        {data.firstName}
      </p>
      <p>
        <strong>Last Name:</strong>
        {data.lastName}
      </p>
      <p>
        <strong>Email:</strong>
        {data.email}
      </p>
    </div>
  );
};
