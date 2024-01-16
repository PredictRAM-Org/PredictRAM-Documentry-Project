# Import necessary libraries
import streamlit as st
import sqlite3

# Function to create the database table
def create_table():
    conn = sqlite3.connect('project_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert a new project into the database
def insert_project(name, description, status):
    conn = sqlite3.connect('project_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO projects (name, description, status)
        VALUES (?, ?, ?)
    ''', (name, description, status))
    conn.commit()
    conn.close()

# Function to retrieve all projects from the database
def get_all_projects():
    conn = sqlite3.connect('project_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects')
    projects = cursor.fetchall()
    conn.close()
    return projects

# Streamlit app
def main():
    st.title("Cloud Project Management Software")

    # Create the database table if not exists
    create_table()

    # Add a new project
    st.header("Add New Project")
    project_name = st.text_input("Project Name:")
    project_description = st.text_area("Project Description:")
    project_status = st.selectbox("Project Status", ["Not Started", "In Progress", "Completed"])

    if st.button("Add Project"):
        insert_project(project_name, project_description, project_status)
        st.success("Project added successfully!")

    # Display all projects
    st.header("All Projects")
    projects = get_all_projects()

    if not projects:
        st.info("No projects available.")
    else:
        for project in projects:
            st.write(f"**Project Name:** {project[1]}")
            st.write(f"**Description:** {project[2]}")
            st.write(f"**Status:** {project[3]}")
            st.write("---")

if __name__ == "__main__":
    main()
