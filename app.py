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
def load_gemini(question, prompt, preferred_model="gemini-2.5-flash"):
    try:
        model = genai.GenerativeModel(preferred_model)
        response = model.generate_content([prompt[0], question])
        return response.text.strip()
    except Exception as exc:
        # If the model isn't available, print helpful info and raise a clearer error
        # (You can optionally call list_models() here to show available models.)
        msg = str(exc)
        # Provide immediate hint for the user
        raise RuntimeError(
            f"Model '{preferred_model}' unavailable for this API/version. "
            "Run a model-list helper to see available models. Original error: "
            + msg
        ) from exc

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
            # Try to render with Streamlit's dataframe (which requires pandas).
            # If there's a binary incompatibility (numpy/pandas), catch it and
            # render a simple Markdown table as a safe fallback.
            try:
                st.dataframe(data, use_container_width=True, hide_index=True)
            except Exception as e:
                st.warning(
                    "Couldn't render dataframe using pandas (binary incompatibility). Showing fallback table instead."
                )

                # Helper: render rows (list of tuples) and column names as a Markdown table
                def _render_markdown_table(rows, cols):
                    if cols:
                        header = "| " + " | ".join(cols) + " |"
                        sep = "| " + " | ".join(["---"] * len(cols)) + " |"
                        body_lines = []
                        for row in rows:
                            # convert each item to string and escape pipe characters
                            safe_items = [str(item).replace("|", "\\|") for item in row]
                            body_lines.append("| " + " | ".join(safe_items) + " |")
                        md = "\n".join([header, sep] + body_lines)
                        st.markdown(md)
                    else:
                        # No column names available: render rows as a bullet list
                        for r in rows:
                            st.write(r)

                _render_markdown_table(data, columns)
        else:
            st.info("No results found for this query.")

# model_list.py
from google.ai import generativelanguage_v1beta as genai_client
import os

# make sure GOOGLE_API_KEY is exported in env before running
client = genai_client.services.generative_service.client.GenerativeServiceClient()
models = client.list_models()
for m in models:
    print(m.name)
