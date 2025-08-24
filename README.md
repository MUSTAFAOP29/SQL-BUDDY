# 📊 SQL Buddy

SQL Buddy is a **Streamlit-based interactive tool** designed to simplify SQL practice and learning.  
With a clean interface and built-in SQL execution environment, it helps learners and professionals practice queries in real-time.


![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## ✨ Features
- 🖥️ Interactive SQL query execution  
- 📂 Support for sample databases  
- 📊 Query results displayed in a neat, tabular format  
- ⚡ Fast and lightweight UI powered by **Streamlit**  
- 📱 Works directly in the browser – no installation required  

---

## 🛠️ Tech Stack
- **Frontend & UI**: Streamlit  
- **Backend**: SQLite (or custom DB as configured)  
- **Language**: Python  

---

## 📂 Project Structure
~~~
SQL-BUDDY/
│── README.md
│── app.py
│── requirements.txt
│── MNC.db
│── assets/
│   ├── screenshot1.png
│   ├── screenshot2.png
│   └── screenshot3.png
│   ├── screenshot4.png

~~~
## 🗄️ Database Schema (MNC.db)

```mermaid
erDiagram
    MNC {
        int mnc_id PK
        string name
        string headquarters
        int founded_year
        string industry
        float revenue_billion
    }

    Regions {
        int region_id PK
        int mnc_id FK
        string region_name
        string head_office
    }

    NorthAmerica_Organizations {
        int org_id PK
        int region_id FK
        string org_name
        string location
        int established_year
        int num_employees
    }

    Europe_Organizations {
        int org_id PK
        int region_id FK
        string org_name
        string location
        int established_year
        int num_employees
    }

    AsiaPacific_Organizations {
        int org_id PK
        int region_id FK
        string org_name
        string location
        int established_year
        int num_employees
    }

    India_Organizations {
        int org_id PK
        int region_id FK
        string org_name
        string location
        int established_year
        int num_employees
    }

    Employees {
        int emp_id PK
        int region_id FK
        int org_id
        string org_table
        string name
        string gender
        string designation
        string department
        float salary
        date join_date
        string hire_type
        int performance_rating
        float bonus
    }

    Sales {
        int sale_id PK
        int region_id FK
        int org_id
        string org_table
        int year
        float revenue_million
        float profit_million
        int customer_count
        float yoy_growth_percent
    }

    %% Relationships
    MNC ||--o{ Regions : has
    Regions ||--o{ NorthAmerica_Organizations : includes
    Regions ||--o{ Europe_Organizations : includes
    Regions ||--o{ AsiaPacific_Organizations : includes
    Regions ||--o{ India_Organizations : includes
    Regions ||--o{ Employees : employs
    Regions ||--o{ Sales : generates
```
## 📦 Installation (Run Locally)

1. **Clone the repo**
   ```
   git clone https://github.com/<your-username>/SQL-BUDDY.git
   cd SQL-BUDDY
   
2. **Create a virtual environment (recommended)**
~~~
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
Run the Streamlit app
~~~

streamlit run app.py

## 🧠 Tech Stack

| Component  | Technology        |
| ---------- | ----------------- |
| Frontend   | Streamlit         |
| Backend AI | Google Gemini API |
| Database   | SQLite            |
| Language   | Python            |

## Screenshots
### 🔹 English Commands
![English Commands](https://github.com/MUSTAFAOP29/SQL-BUDDY/blob/main/Screenshot%20(2369).png)

### 🔹 Tamil Commands
![Tamil Commands](https://github.com/MUSTAFAOP29/SQL-BUDDY/blob/main/Screenshot%20(2370).png) 

### 🔹 Urdu Commands
![Urdu Commands](https://github.com/MUSTAFAOP29/SQL-BUDDY/blob/main/Screenshot%20(2371).png)




## 🚀 Live Demo
👉 [Try SQL Buddy here](https://sql-buddy-08.streamlit.app/)



📜 License
This project is licensed under the MIT License – free to use and modify with attribution.

👨‍💻 Author
Developed with ❤️ by Syed Mustafa
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syedmustafa29)
