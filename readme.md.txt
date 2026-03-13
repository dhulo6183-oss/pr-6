# 📝 Personal Journal Manager

A simple **Python CLI (Command Line Interface) application** that allows users to write and manage personal journal entries directly from the terminal.

This project helps users:
- Record daily thoughts 📖
- View previous entries 🗂️
- Search for specific entries 🔎
- Delete all entries when needed 🧹

The journal entries are stored in a text file with timestamps.

---

# ✨ Features

✅ Add a new journal entry with date & time  
✅ View all saved journal entries  
✅ Search entries using keywords or dates  
✅ Delete all entries with confirmation  
✅ Simple menu-driven interface  

---

# 🛠️ Technologies Used

- 🐍 Python
- 📂 File Handling
- ⏰ Datetime Module
- 💻 Command Line Interface (CLI)

---

# 📂 Project Structure

```
Personal-Journal-Manager
│
├── journal.txt          # Stores all journal entries
├── main.py              # Python program
├── Screenshots
│   ├── s1.png
│   ├── s2.png
│   ├── s3.png
│   ├── s4.png
│   └── s5.png
└── README.md
```

---

# 🚀 How to Run the Project

1️⃣ Make sure Python is installed on your system  

2️⃣ Clone the repository or download the project

3️⃣ Open terminal in the project folder

4️⃣ Run the program

```bash
python main.py
```

---

# 📸 Screenshots

## 🖊️ Adding Journal Entries
![Add Entry](Screenshots/s1.png)

---

## 📖 Viewing All Entries
![View Entries](Screenshots/s2.png)

---

## 🔍 Searching Entries
![Search Entries](Screenshots/s3.png)

---

## 🧹 Deleting All Entries
![Delete Entries](Screenshots/s4.png)

---

## 👋 Exiting the Program
![Exit Program](Screenshots/s5.png)

---

# ⚙️ Program Menu

When you run the program you will see:

```
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

You can simply type the number of the option you want.

---

# 📌 How Entries Are Stored

Each entry is saved with a **timestamp** in `journal.txt`.

Example:

```
[2026-02-17 13:24:55]
Today was a productive day.

[2026-02-17 13:25:09]
I learned Python.
```

---

# 📚 Program Logic

The program uses **Python file handling** to store and retrieve journal entries.

Main functions included in the project:

- `add_entry()` → Adds a new entry
- `view_entries()` → Displays all entries
- `search_entry()` → Searches entries by keyword
- `delete_entries()` → Deletes all entries
- Menu system using a `while` loop

The implementation can be seen in the source code. :contentReference[oaicite:0]{index=0}

---

# 🎯 Future Improvements

- GUI version using Tkinter
- Edit existing journal entries
- Delete a specific entry
- Export entries to PDF
- Password protection for privacy

---

# 👨‍💻 Author

**DHRUV**
