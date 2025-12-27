// Verbind met de database (naam zoals opgegeven in MONGO_INITDB_DATABASE)
db = db.getSiblingDB("appdb");

// Maak een collectie en voeg documenten toe
db.users.insertMany([
  { name: "Alice", email: "alice@example.com" },
  { name: "Bob", email: "bob@example.com" }
]);

db.products.insertMany([
  { name: "Laptop", price: 1200 },
  { name: "Phone", price: 800 }
]);
