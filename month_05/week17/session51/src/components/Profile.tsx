import React from "react";
type Props = {
  width: number;
  height: number;
  url: string,
  alternative: string
};
const Profile: React.FC<Props> = (props) => {
  return (
    <img
      src={props.url}
      alt={props.alternative}
      width={props.width}
      height={props.height}
    />
  );
};

export default Profile;
