import React, { useState } from "react";

const ControlledInput: React.FC = () => {
    // TODO
    /**
     * Энэхүү компонент нь хэрвээ input дээр бичвэл тухайн 
     * бичсэн утгуудыг Current Value: гэдэг хэсэгт харуулна
     * үүнд шинээр value гэдэг нэртэй useState hook ашиглана уу.
     * Шинээр handleInputChange гэдэг функц үүсгээд түүнийг
     * value-гийн утгыг нь өөрчилдөг болгоорой.
     */
 const [value, setValue] = useState<string>('');
 const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setValue(event.target.value);
 }

  return (
    <>
      <h3>On Change Example</h3>
      <input
        type="text"
        placeholder="Type Something ..."
        value={value}
        onChange={handleInputChange}
      />
      <p>Current Value: {value}</p>
    </>
  );
};
export default ControlledInput;
