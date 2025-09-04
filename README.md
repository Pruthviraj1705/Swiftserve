
# SwiftServe - Restaurant Management System (Python)

SwiftServe is a beginner-friendly, command-line-based **restaurant and hotel management system**.  
It allows restaurants to manage menus, take customer orders, and generate detailed bills with **automatic tax and packing charge calculations**.

This project is perfect for:
- Small restaurant businesses
- Students learning Python
- Developers looking to integrate billing systems

---

## 🚀 Features
- View a full restaurant menu with prices.
- Take **multiple orders per customer** in a single session.
- Supports **Dine-In** and **Parcel (Takeaway)** orders.
- Automatically applies:
  - GST at 5%
  - Packing charges for parcel orders
- Generates **detailed printed bills**.
- Saves all bills to a **receipts folder** with timestamped filenames.
- Includes a **default menu** and allows customization via `menu.json`.
- Beginner-friendly code with clean structure and comments.

---

## 📂 Folder Structure
```
SwiftServe/
│
├── source_code/
│   ├── main.py
│   ├── data/
│   │   └── menu.json
│   └── receipts/
│
├── docs/
│   ├── Documentation.pdf
│   └── QuickStart.txt
│
├── demo/
│   └── screenshots/
│
├── LICENSE.txt
├── README.md
└── requirements.txt
```

---

## ⚙️ Requirements
- **Python 3.10+**
- No external libraries required.  
All dependencies are built into Python.

---

## 📝 Installation
1. **Download the ZIP file** and extract it.
2. Open a terminal or command prompt in the `source_code` folder.
3. Run the program:
   ```bash
   python main.py
   ```

---

## 💻 Usage
1. Enter the **customer name**.
2. Choose order type:
   - `1` → Dine-In
   - `2` → Parcel
3. Select items from the menu and specify quantities.
4. The system calculates **total cost, GST, and packing charges** automatically.
5. Final bill is **saved in the receipts folder**.

---

## 📜 License
This project is licensed under the **MIT License**.  
You are free to modify and sell this code, provided you include the original copyright notice.

---

## 📞 Support
For questions or support, please reach out:
- **Email:** pruthvirajj1217@gmail.com
- **GitHub:** [https://github.com/Pruthviraj1705](https://github.com/Pruthviraj1705)
