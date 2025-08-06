import React, { useState } from "react";


const SubmissionForm = () => {
    /**
     * username гэдэг state үүсгэж түүнийгээ handleSubmit гэдэг функц
     * дотор утгыг нь өөрчилж дуудаж alert дээр Submitting username: Khangaikhuu
     * гэх мэтээр хэвлэж харуулдаг болгоорой.
     * Form-ийг submit хийхэд хуудас дахин ачаалахгүй болгоорой.
     */
    const [username, setUsername] = useState<string>('');

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        alert(`Submitting username: ${username}`);
    }
    return (
        <>
            <h3>OnSubmit Example</h3>
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">UserName: </label>
                <input type="text" id="username" value={username}
                onChange={(e) => {
                    setUsername(e.target.value);
                }}
                />
                <button type="submit">Submit</button>
            </form>
        </>
    )
} 
export default SubmissionForm;