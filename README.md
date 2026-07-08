# 💊 MedStore Wholesale Management System

A modular Python console application developed for the **Fundamentals of Computing (CS4051NI/CC4059NI)** coursework. The system manages medicine inventory, processes sales and restocking transactions, generates invoices, and maintains inventory records using text files.

---

# Table of Contents

- Overview
- Features
- System Requirements
- Installation
- Quick Start
- Project Structure
- Usage
- Modules Overview
- Design & Architecture
- Testing
- Build & Runtime Requirements
- Contribution Guidelines
- License
- Changelog
- Known Issues
- Future Improvements
- Screenshots
- Contact

---

# Overview

The MedStore Wholesale Management System is designed to simplify inventory management for a medicine wholesaler. The application allows administrators to manage medicine stock, sell medicines, restock inventory, search medicines, and automatically generate transaction invoices while keeping inventory synchronized with the storage file.

The application follows a modular programming approach, making it easy to maintain, understand, and extend.

---

# Features

## Inventory Management

- Load medicines from a text file
- Save updated inventory automatically
- Display all medicines
- Search medicines by name or brand

## Sales Management

- Sell medicines by tablet or strip
- Automatic stock validation
- Bulk strip discount (5%)
- Customer invoice generation
- Inventory update after every sale

## Restock Management

- Restock existing medicines
- Add completely new medicines
- Supplier invoice generation
- Automatic inventory update

## User Experience

- Input validation
- Error handling
- Menu-driven interface
- Modular code organization

---

# System Requirements

- Python 3.10 or later
- Windows, macOS, or Linux
- Terminal / Command Prompt
- No third-party libraries required

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/medstore-wholesale-system.git
```

Navigate to the project folder:

```bash
cd medstore-wholesale-system
```

No additional packages are required.

---

# Quick Start

Run the application:

```bash
python main.py
```

or

```bash
python3 main.py
```

Example workflow:

```text
1. View Medicines

2. Sell Medicines

3. Restock Medicines

4. Search Medicine

0. Exit
```

---

# Project Structure

```
MedStore-Wholesale-System/

│
├── main.py
├── inventory.py
├── display.py
├── sales.py
├── restock.py
├── search.py
├── utils.py
│
├── medicines.txt
│
├── sale_YYYYMMDD_xxxx.txt
├── restock_YYYYMMDD_xxxx.txt
│
└── README.md
```

---

# Usage

## View Medicines

Displays all available medicines currently in stock.

---

## Sell Medicines

- Select medicine
- Choose Tablet or Strip
- Enter quantity
- Discount applied automatically for strip purchases
- Invoice generated
- Inventory updated

---

## Restock Medicines

- Restock existing medicine

OR

- Add a completely new medicine

Supplier invoice is generated automatically.

---

## Search Medicines

Search by:

- Medicine Name
- Brand Name

Matching medicines are displayed immediately.

---

# Modules Overview

## main.py

Program entry point.

Responsibilities:

- Displays menu
- Loads inventory
- Calls appropriate modules
- Saves inventory on exit

---

## inventory.py

Handles

- Loading inventory
- Saving inventory
- Reading medicines.txt

---

## display.py

Responsible for

- Displaying medicine list
- Selecting medicines

---

## sales.py

Responsible for

- Sales processing
- Discount calculation
- Invoice generation
- Stock update

---

## restock.py

Responsible for

- Restocking medicines
- Adding new medicines
- Supplier invoices

---

## search.py

Responsible for

- Searching medicines
- Displaying results

---

## utils.py

Provides utility functions

- Input validation
- Filename generation
- Date & Time
- Pause screen

---

# Module Interaction

```
          main.py
             │
 ┌───────────┼─────────────┐
 │           │             │
 ▼           ▼             ▼
sales.py restock.py search.py
 │           │
 ▼           ▼
inventory.py
 │
 ▼
medicines.txt
```

---

# Design & Architecture

The project follows a **modular programming architecture**.

### Design Principles

- Separation of Concerns
- Single Responsibility Principle
- Reusable utility functions
- File-based persistence
- Input validation
- Error handling

### Data Structure

Inventory is stored as

```python
[
    {
        "name": "...",
        "brand": "...",
        "quantity": 100,
        "rate_tablet": 2.5,
        "rate_strip": 25,
        "tablets_per_strip": 10
    }
]
```

---

# Example Code

Loading inventory

```python
inventory = load_inventory()
```

Saving inventory

```python
save_inventory(inventory)
```

Searching

```python
search(medicines)
```

---

# Testing

The project was manually tested using multiple scenarios.

## Test Cases

✔ Load inventory

✔ Display inventory

✔ Search medicine

✔ Sell medicine

✔ Strip discount calculation

✔ Restock medicine

✔ Add new medicine

✔ Inventory updates

✔ Invoice generation

✔ Invalid numeric input

✔ Missing inventory file

---

## Unit Testing

No automated testing framework (unittest/pytest) is included.

Future versions may integrate:

- unittest
- pytest
- coverage.py

---

# Build & Runtime Requirements

Python Version

```
Python 3.10+
```

Build

No compilation required.

Run

```bash
python main.py
```

Dependencies

None

---

# Contribution Guidelines

Contributions are welcome.

1. Fork repository

2. Create branch

```bash
git checkout -b feature-name
```

3. Commit

```bash
git commit -m "Implemented new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open Pull Request

### Code Style

- Follow PEP 8
- Use meaningful variable names
- Write descriptive comments
- Keep functions modular

---

# License

This project was developed for educational purposes as coursework for the Fundamentals of Computing module.

You may use or modify this project for learning purposes.

---

# Changelog

## Version 1.0

Initial release

- Inventory management
- Medicine search
- Sales module
- Restock module
- Invoice generation
- File persistence

---

# Known Issues

- Text file database is not suitable for large inventories
- Console interface only
- No authentication
- No graphical interface
- No database integration

---

# Future Improvements

- SQLite/MySQL database
- Graphical User Interface (Tkinter/PyQt)
- Barcode scanner support
- User authentication
- Sales reports
- Inventory analytics
- CSV/PDF export
- Email invoices

---

# Screenshots

Create a folder named

```
screenshots/
```

Example

```
screenshots/

main-menu.png

inventory.png

sale.png

restock.png

invoice.png
```

Markdown

```markdown
## Main Menu

![Main Menu](screenshots/main-menu.png)

## Inventory

![Inventory](screenshots/inventory.png)

## Sale Invoice

![Sale](screenshots/sale.png)
```

---

# Contact

**Author**

Om Dangol

**Module**

CS4051NI – Fundamentals of Computing

**Repository**

https://github.com/yourusername/medstore-wholesale-system

**Issue Tracker**

https://github.com/yourusername/medstore-wholesale-system/issues

**Documentation**

See the coursework report included with the submission.

---

## Acknowledgements

Developed as an individual coursework project for the **Fundamentals of Computing** module at Islington College, affiliated with London Metropolitan University.

---
