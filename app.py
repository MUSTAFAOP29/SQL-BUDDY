from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
import sqlite3

# ✅ Load environment variables
load_dotenv()

# Get the API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ No GOOGLE_API_KEY found. Please add it to your .env file")
else:
    genai.configure(api_key=api_key)

# function to load gemini
def load_gemini(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt[0], question])
    return response.text.strip()  # ✅ ensure no extra quotes/newlines

# function to retrieve data from the database
def read_sql(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        col_names = [description[0] for description in cur.description] if cur.description else []
        conn.commit()
        conn.close()
        return rows, col_names
    except Exception as e:
        return f"❌ SQL Error: {e}", []

# defining the prompt
prompt = ["""You are a multilingual SQL expert who can understand natural language queries in English, Hindi, Tamil, Telugu, and Urdu and convert them into efficient SQL queries for a database of a multinational corporation (MNC).

The following is the database schema for the MNC:

MNC
 └── Regions
       ├── Indian_organizations
       │     ├── Employees
       │     └── Sales
       ├── Europe_organizations
       │     ├── Employees
       │     └── Sales
       ├── NorthAmerica_organizations
       │     ├── Employees
       │     └── Sales
       └── AsiaPacific_organizations
             ├── Employees
             └── Sales

The schema contains the following tables:

The database contains the following tables:

- MNC(mnc_id, name, headquarters, founded_year, industry, revenue_billion)
- Regions(region_id, mnc_id, region_name, head_office)
- NorthAmerica_Organizations(org_id, region_id, org_name, location, established_year, num_employees)
- Europe_Organizations(org_id, region_id, org_name, location, established_year, num_employees)
- AsiaPacific_Organizations(org_id, region_id, org_name, location, established_year, num_employees)
- India_Organizations(org_id, region_id, org_name, location, established_year, num_employees)
- Employees(emp_id, region_id, org_id, org_table, name, gender, designation, department, salary, join_date, hire_type, performance_rating, bonus)
- Sales(sale_id, region_id, org_id, org_table, year, revenue_million, profit_million, customer_count, yoy_growth_percent)

⚠️ Important: Each region has its own table for organizations. 
When writing SQL, always query the correct region-specific table (e.g., `NorthAmerica_Organizations` instead of `Organizations`).
Here are some example queries:
Generate only valid SQL queries as output.
Important: Do not include ```sql or ``` in your output.
...
(Examples same as before)
"""]

# Streamlit UI
st.title("🌍 Multilingual SQL Query Generator for MNC Database")
user_input = st.text_area("Enter your query in English, Hindi, Tamil, Telugu or Urdu")
submit = st.button("Generate SQL Query")

if submit:
    response = load_gemini(user_input, prompt)

    st.subheader("🔹 Generated SQL Query:")
    st.code(response, language="sql")

    data, columns = read_sql(response, 'MNC.db')

    if isinstance(data, str):  # error case
        st.error(data)
    else:
        st.subheader("📊 Query Results:")
        if data:
            st.dataframe(data, use_container_width=True, hide_index=True)
        else:
            st.info("No results found for this query.")
