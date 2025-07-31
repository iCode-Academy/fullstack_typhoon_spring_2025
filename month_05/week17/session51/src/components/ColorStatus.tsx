import React from "react";

interface ColorStatusProps {
  isBlue: boolean;
  width: number;
}

const ColorStatus: React.FC<ColorStatusProps> = ({ isBlue, width }) => {
  //   object destructure
  return (
    <div>
      {isBlue ? <h1>It is Blue</h1> : <h1>It is Red</h1>}
      {width}
    </div>
  );
};

export { ColorStatus };
