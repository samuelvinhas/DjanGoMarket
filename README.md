# DjanGoMarket - Supermarket Management System

## Introduction

DjanGoMarket is a web-based information system developed to help manage supermarket operations. Our system is built using **Django** platform and uses **SQLite** as the database backend with Django's Object-Relational Mapping (ORM) system. 

Our application serves as a hub for managing supermarket operations including:
- Employee and personnel management
- Product inventory and warehouse organization
- Customer purchases and transactions
- Supplier/Distributor relationships
- Store locations and section management

---

## Main Features of our App

### 1. Data Model & Database Management
- Relational database with 11 interconnected models
- **Implemented Models:**
  - `Supermarket` - Store locations with opening/closing times
  - `Section` - Product sections/departments
  - `Employee` - Staff management with roles, hierarchy (supervisor relationships), and salary tracking
  - `Product` - Product catalog with pricing and temperature requirements
  - `Warehouse` - Inventory storage locations
  - `Distributor` - Supplier information
  - `Client` - Customer data with fidelity program tracking
  - `Purchase` - Transaction management with multiple payment methods
  - Additional junction models for M:N relationships with attributes

### 2. Django Admin Interface
- Admin panel for CRUD operations on all models
- Data validation and constraints enforced at model level
- Pre-populated sample data available via `populate_db.py`

### 3. Form System
- TODO: Create Django forms

### 4. User Views & Templates
- TODO: Create views

### 5. User Authentication & Authorization
- TODO: Implement Django authentication system with:
  - Login/registration for different user roles
  - Role-based access control (Admin, Employee)
  - Permission-based view restrictions

---

## Access Information

### Deployed Application
- **Link**: TODO - Deploy to PythonAnywhere
- **URL Structure**: TODO - Add deployment URL here

### User Authentication Information

#### Admin Account
- **Username**: `admin`
- **Email**: `admin@gmail.com`
- **Password**: `adminpass123!`
- **Access**: Django Admin Panel at `/admin/`

#### User Roles
- **Admin**: Full system access, user management
- **Employee**: Can't add/edit/remove, only view data

---

## Configuration for Running Locally

### Prerequisites
- Python 3.8+
- Virtual Environment (venv)
- Git

### Installation Steps

1. **Clone/Navigate to the project:**
```bash
git clone https://github.com/samuelvinhas/DjanGoMarket.git
cd DjanGoMarket
```

2. **Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Apply Database Migrations:**
```bash
chmod +x migrate.sh
./migrate.sh
```

5. **Populate Database with Data (Optional):**
```bash
python3 populate_db.py
```

6. **Run Development Server:**
```bash
python3 manage.py runserver
```
- Access: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/
TODO more

---

## Conclusions

TODO

---