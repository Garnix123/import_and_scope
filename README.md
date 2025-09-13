# 🐍 Python JSON Handling Exercise  

## 📌 Overview  
This project demonstrates how to **work with JSON files in Python**.  
The exercise consists of two scripts:  
- `jsongenerator.py` → creates JSON data.  
- `employee.py` → reads and processes JSON data.  
- `employee.json` → sample dataset with employee details.  

It covers the following concepts:
- Importing built-in Python libraries (`json`).
- Writing JSON data to a file.
- Reading JSON data from a file.
- Parsing and accessing dictionary values in Python.

---

## 📂 Files in This Repository  

### 1. `jsongenerator.py`  
- Generates JSON data for employees.  
- Demonstrates how to **serialize Python objects into JSON** using `json.dump()`.  
- Creates or updates `employee.json`.  

### 2. `employee.json`  
Sample dataset used in this exercise:  

```json
{
  "first_name": "Mario",
  "age": 55,
  "title": "owner"
}
```

### 3. `employee.py`
- Reads employee.json.
- Demonstrates how to deserialize JSON into Python objects using json.load().
- Accesses and prints the values (first_name, age, title).
