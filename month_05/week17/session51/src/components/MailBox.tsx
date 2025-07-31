import React from "react";

interface MailBoxProps {
  unreadMessages: string[];
}

const MailBox: React.FC<MailBoxProps> = ({ unreadMessages }) => {
  return (
    <div>
      <h1>Hello!</h1>
      {unreadMessages.length > 0 && (
        <h2>You have {unreadMessages.length} unread Messages</h2>
      )}
    </div>
  );
};

export { MailBox };
