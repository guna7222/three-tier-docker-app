import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState('');
  const [editingId, setEditingId] = useState(null);
  const [editName, setEditName] = useState('');

  const API_URL = '/api/items'; // Adjust if needed

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    const res = await axios.get(API_URL);
    setItems(res.data);
  };

  const addItem = async () => {
    if (!name.trim()) return alert('Enter item name');
    await axios.post(API_URL, { name });
    setName('');
    fetchItems();
  };

  const deleteItem = async (id) => {
    await axios.delete(`${API_URL}/${id}`);
    fetchItems();
  };

  const startEdit = (id, currentName) => {
    setEditingId(id);
    setEditName(currentName);
  };

  const updateItem = async () => {
    if (!editName.trim()) return alert('Enter new name');
    await axios.put(`${API_URL}/${editingId}`, { name: editName });
    setEditingId(null);
    setEditName('');
    fetchItems();
  };

  return (
    <div style={{ padding: '20px', maxWidth: '500px', margin: 'auto' }}>
      <h2>CRUD App (Name Only)</h2>

      <input
        type="text"
        placeholder="Item Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{ width: '100%', marginBottom: '10px' }}
      />
      <button onClick={addItem}>Add Item</button>

      <hr />

      {items.map((item) => (
        <div key={item.id} style={{ marginBottom: '10px' }}>
          {editingId === item.id ? (
            <>
              <input
                type="text"
                value={editName}
                onChange={(e) => setEditName(e.target.value)}
              />
              <button onClick={updateItem}>Save</button>
              <button onClick={() => setEditingId(null)}>Cancel</button>
            </>
          ) : (
            <>
              {item.name}
              <button onClick={() => startEdit(item.id, item.name)} style={{ marginLeft: '10px' }}>Edit</button>
              <button onClick={() => deleteItem(item.id)} style={{ marginLeft: '5px' }}>Delete</button>
            </>
          )}
        </div>
      ))}
    </div>
  );
}

export default App;
