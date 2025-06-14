# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.

## 🚀 Features

- ➕ Add, update, and delete expenses  
- 📅 View expense history and filter by date  
- 📊 Visualize spending through charts and summaries  

---

## 🆕 Budget Management Tab

- 🎯 Set a monthly budget  
- 🚨 Get real-time alerts if your expenses exceed your set budget  

---

## 📈 Monthly Analytics Tab

- 📅 View monthly expense breakdown  
- 📊 Analyze total spending by month using bar charts  
- 📋 Tabular summary sorted by latest month  

    
## 🗂 Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## ⚙️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
