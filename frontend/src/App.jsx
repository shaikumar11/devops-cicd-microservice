import { useEffect, useState } from "react";

export default function App() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState("");
  const load = () => fetch("/api/items").then(r => r.json()).then(setItems);
  useEffect(() => { load(); }, []);
  const add = async () => {
    await fetch("/api/items", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ name }) });
    setName(""); load();
  };
  return (
    <div style={{ padding: 24 }}>
      <h1>DevOps Demo</h1>
      <input value={name} onChange={e => setName(e.target.value)} />
      <button onClick={add}>Add</button>
      <ul>{items.map((i, n) => <li key={n}>{i}</li>)}</ul>
    </div>
  );
}