# Staff-Scheduling-Project

🚀 **AI-Powered Staff Scheduling Optimization**  
**An intelligent staff scheduling system using Linear Programming (PuLP) and OpenRouter DeepSeek AI, with a user-friendly Gradio UI.**  

---

## 📖 **Project Overview**
This project optimizes staff scheduling for a **home care facility** by:
- ✅ **Minimizing staff costs** while meeting demand  
- ✅ **Considering hiring, firing, and overtime costs**  
- ✅ **Balancing shift allocations based on workload**  
- ✅ **Using AI (DeepSeek via OpenRouter) to refine scheduling**  
- ✅ **Providing an interactive UI for scheduling insights**  

---

## 🔧 **Installation & Setup**

### **1️⃣ Create Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate  # Windows
```

### **2️⃣ Install Required Libraries**
```bash
pip install -r requirements.txt
```

### **3️⃣ Prepare Data (Ensure CSVs Exist in `/data/`)**
- **Historical Demand:** `historical_demand.csv`
- **Staff Details:** `staff_details.csv`
- **Hiring & Firing Costs:** `hiring_firing_costs.csv`

If missing, generate CSVs using:
```bash
python scripts/staff_details_generator.py
```

---

## 🚀 **Running the Project**

### **1️⃣ Run Optimization + AI + UI**
```bash
python main.py
```
This will:
- ✅ Optimize staff scheduling
- ✅ Query OpenRouter DeepSeek AI for schedule refinement
- ✅ Launch Gradio UI for interactive analysis

### **2️⃣ Run Data Analysis (Jupyter Notebook)**
```bash
jupyter notebook notebooks/analysis.ipynb
```
This will:
- ✅ Visualize staffing demand trends
- ✅ Analyze cost impact
- ✅ Provide data-driven recommendations

---

## 🧩 **How It Works**

### 🔹 **Linear Programming (PuLP)**
Uses mathematical optimization to minimize costs while meeting demand.
#### **Constraints include:**
- Shift balance
- Weekend staff increase
- Hiring & firing costs
- Overtime rules

### 🔹 **AI-Powered Recommendations (DeepSeek AI)**
- Queries OpenRouter API to refine shift schedules dynamically.
- Provides real-time staff allocation insights.

### 🔹 **Gradio UI**
- Shows optimized shift schedule
- Displays AI-based schedule adjustments
- Interactive for real-time insights

---

## ⚠️ **Troubleshooting**

### 🔹 **Issue: API not working**
**Solution:** Ensure OpenRouter API key is set correctly in `staff_scheduler.py`.

### 🔹 **Issue: Gradio UI not launching**
**Solution:** Check if port `7860` is free, or specify a different port:
```bash
python main.py --port 5000
```

---

## 👨‍💻 **Contributors**
- **Khushi Karelia** (Project Owner)

