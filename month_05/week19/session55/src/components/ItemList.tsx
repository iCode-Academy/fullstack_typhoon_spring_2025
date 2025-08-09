import React, { useState } from "react";

interface Item {
  id: number;
  text: string;
}

const ItemList: React.FC = () => {
  const [items, setItems] = useState<Item[]>([
    { id: 1, text: "First Item" },
    { id: 2, text: "Second Item" },
    { id: 3, text: "Third Item" },
  ]);

  const handleAddItem = () => {
    const newItem: Item = {
        id: Date.now(),
        text: `New Item ${items.length + 1}`
    }

    setItems([...items, newItem]);
  }
  const handleRemoveItem = (idToRemove: number) => {
    const updatedItems = items.filter((item) => item.id != idToRemove);
    setItems(updatedItems);
  }
  // react virtual dom VS JS DOM
  return (
    <div>
      <h2>Item List</h2>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            {item.text} 
            <button onClick={() => handleRemoveItem(item.id)}>Remove</button>
         </li>
        ))}
      </ul>
      <button onClick={handleAddItem}>Add Item</button>
    </div>
  );
};
export default ItemList;
