# 🛍 WE Care Shop Management System

## 📖 Overview
This project is a **Python-based inventory management system** developed as part of the *CS4051NI Fundamentals of Computing* coursework.  
It is designed for **WE Care**, a skincare shop, to handle daily operations such as **buying, selling, restocking products**, and generating invoices automatically.

The system:
- Reads and updates product information from a text file
- Generates invoices for each transaction
- Calculates free items for bulk purchases
- Provides a simple **menu-driven command-line interface**

---

## 🎯 Objectives
- Apply Python basics to solve a **real-world problem**
- Implement **file handling** for reading/writing inventory data
- Understand **billing systems** in business models
- Use **modular programming** by separating tasks into different `.py` files
- Enhance logical thinking and problem-solving skills

---

## ✨ Key Features
### 🛒 Buying Products
- Check stock before purchase
- Offer free items for buying ≥ 3 of the same product
- Update inventory after purchase
- Generate and save a **Buy Invoice** (`.txt` file)

### 💰 Selling/Restocking Products
- Sell existing or newly added products
- Update quantities or add new product entries
- Generate and save a **Sell Invoice** (`.txt` file)

### 📂 Product Management
- Display all available products with:
  - Name
  - Manufacturer
  - Quantity
  - Price
  - Country of origin

### 🛠 Error Handling
- Reject invalid product IDs
- Prevent negative or zero quantities
- Handle incorrect menu selections with try-except

---

## 🗂 Project Structure
```
📂 project-folder
 ├── BuyInvoice_testfile2_ktm          # Sample Buy Invoice file
 ├── SellInvoice_sellertest            # Sample Sell Invoice file
 ├── Product_list                      # Product data (text file)
 ├── main.py                           # Entry point, user menu & navigation
 ├── operation.py                      # Buy/Sell/Restock logic
 ├── read.py                           # Reads & displays product data
 ├── write.py                          # File handling & invoice generation
```

---

## ⚙️ How It Works
1. **Run `main.py`**
2. Choose from menu:
   - `1` → Buy Product
   - `2` → Sell/Restock Product
   - `3` → Display Product List
   - `4` → Exit
3. The program:
   - Reads data via `read.py`
   - Processes logic via `operation.py`
   - Updates inventory and creates invoices via `write.py`

---

## 🧪 Testing & Results
| Test | Description | Result |
|------|-------------|--------|
| 1 | Handling invalid menu input | ✅ Successful |
| 2 | Negative values in Buy function | ✅ Successful |
| 3 | Negative values in Sell function | ✅ Successful |
| 4 | Invoice generation after purchase | ✅ Successful |
| 5 | Invoice generation after restocking | ✅ Successful |
| 6 | Product list updates after transactions | ✅ Successful |

---

## 📊 Example Workflow
### Buying a Product
1. Choose option **1** (Buy Product)
2. Enter **Product ID** and **Quantity**
3. System checks stock availability
4. Free product calculation if eligible
5. Generates **Buy Invoice** and updates `Product_list.txt`

### Selling/Restocking
1. Choose option **2** (Sell/Restock Product)
2. Choose:
   - Sell existing product (update quantity)
   - Sell new product (add entry)
3. Generates **Sell Invoice** and updates `Product_list.txt`

---

## 📚 Technologies & Tools Used
- **Python 3.x** — Core programming language
- **IDLE** — Development environment
- **Notepad** — Data storage for `.txt` files
- **Draw.io** — Flowchart design
- **Microsoft Word** — Report documentation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed

### Installation
```bash
# Clone this repository
git clone https://github.com/<your-username>/<repo-name>.git

# Navigate into the folder
cd <repo-name>
```

### Run the Program
```bash
python main.py
```

---

## 📌 Author
**Prasim Basnet**  
London Met ID: *24046815*  
📅 Year: 2024/25

---

## 📝 License
This project was created for **academic purposes** as part of the *CS4051NI Fundamentals of Computing* coursework.  
It is free to use and modify for **educational purposes only**.
