import axios from 'axios';
import { useState, useEffect } from 'react';

function ItemList() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    const res = await axios.get('/api/items');
    setItems(res.data);
  };

  const deleteItem = async (id) => {
    await axios.delete(`/api/items/${id}`);
    fetchItems(); // Refresh after delete
  };

  const updateItem = async (id, updatedData) => {
    await axios.put(`/api/items/${id}`, updatedData);
    fetchItems(); // Refresh after update
  };

  return (
    <div>
      <h2>Items</h2>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name}  {item.description}
            <button onClick={() => deleteItem(item.id)}>Delete</button>
            <button onClick={() => updateItem(item.id, { name: 'Updated Name' })}>Update</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ItemList;
