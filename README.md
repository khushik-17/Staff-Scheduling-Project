# Staff-Scheduling-Project

🚀 AI-Powered Staff Scheduling Optimization  
**An intelligent staff scheduling system using Linear Programming (PuLP) and OpenRouter DeepSeek AI, with a user-friendly Gradio UI.**  

---

## 📖 **Project Overview**
This project optimizes staff scheduling for a **home care facility** by:  
✅ **Minimizing staff costs** while meeting demand  
✅ **Considering hiring, firing, and overtime costs**  
✅ **Balancing shift allocations based on workload**  
✅ **Using AI (DeepSeek via OpenRouter) to refine scheduling**  
✅ **Providing an interactive UI for scheduling insights**  

---

## 📂 **Folder Structure**
Staff_Scheduling_Project/ │── env/ # Virtual Environment │── data/
│ ├── historical_demand.csv # Past 6 months staffing demand │ ├── staff_details.csv # Staff categories & shift constraints │ ├── hiring_firing_costs.csv # Hiring & firing costs per staff type │── scripts/ │ ├── staff_scheduler.py # Main module (Optimization + AI Integration) │ ├── optimization.py # Linear programming model │── notebooks/ │ ├── analysis.ipynb # Jupyter Notebook for staffing trend analysis │── main.py # Project entry-point (runs UI + AI) │── requirements.txt # Dependencies list │── README.md # Project Documentation

yaml
Copy
Edit

---

## 🔧 **Installation & Setup**
### **1️⃣ Create Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate  # Windows
2️⃣ Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Prepare Data (Ensure CSVs Exist in /data/)
Historical Demand: historical_demand.csv

Staff Details: staff_details.csv

Hiring & Firing Costs: hiring_firing_costs.csv

If missing, generate CSVs using:

bash
Copy
Edit
python scripts/staff_details_generator.py
🚀 Running the Project
1️⃣ Run Optimization + AI + UI
bash
Copy
Edit
python main.py
This will: ✅ Optimize staff scheduling
✅ Query OpenRouter DeepSeek AI for schedule refinement
✅ Launch Gradio UI for interactive analysis

2️⃣ Run Data Analysis (Jupyter Notebook)
bash
Copy
Edit
jupyter notebook notebooks/analysis.ipynb
This will: ✅ Visualize staffing demand trends
✅ Analyze cost impact
✅ Provide data-driven recommendations

🧩 How It Works
🔹 Linear Programming (PuLP)
Uses mathematical optimization to minimize cost while meeting demand.

Constraints include:

Shift balance

Weekend staff increase

Hiring & firing costs

Overtime rules

🔹 AI-Powered Recommendations (DeepSeek AI)
Queries OpenRouter API to refine shift schedules dynamically.

Provides real-time staff allocation insights.

🔹 Gradio UI
Shows optimized shift schedule

Displays AI-based schedule adjustments

Interactive for real-time insights

📊 Expected Outputs
🔹 Console Output (main.py)
vbnet
Copy
Edit
🔄 Generating Optimized Shift Schedule...

✅ Optimized Staff Schedule:
- Morning Shift: 12 caregivers, 7 nurses, 6 support staff
- Evening Shift: 14 caregivers, 6 nurses, 5 support staff
- Night Shift: 9 caregivers, 5 nurses, 4 support staff

🤖 AI Recommendations:
- Increase weekend staff by 10% to meet peak demands.
- Shift 50% of night staff to morning/evening to reduce exhaustion.
- Consider hiring 2 more caregivers next month due to winter demand.

🚀 Launching Gradio Interface...
🔹 Gradio UI Output
📌 Optimized Shift Schedule:

diff
Copy
Edit
- Morning Shift: 12 caregivers, 7 nurses, 6 support staff
- Evening Shift: 14 caregivers, 6 nurses, 5 support staff
- Night Shift: 9 caregivers, 5 nurses, 4 support staff
🤖 AI Recommendations:

vbnet
Copy
Edit
- Increase weekend staff by 10% to meet peak demands.
- Shift 50% of night staff to morning/evening to reduce exhaustion.
- Consider hiring 2 more caregivers next month due to winter demand.
📌 CSV Files Explanation
1️⃣ historical_demand.csv (Staffing Demand)
Month	Morning_C	Morning_N	Morning_S	Evening_C	Evening_N	Evening_S	Night_C	Night_N	Night_S
Sep	12	7	6	14	6	5	9	5	4
Oct	11	6	5	13	5	4	8	4	3
Nov	10	6	5	12	5	4	8	4	3
2️⃣ staff_details.csv (Staff Categories)
Staff Category	Hourly Wage (₹)	Regular Hours/Week	Min Staff Morning	Min Staff Evening	Min Staff Night
Caregivers	300	40	10	12	8
Nurses	450	35	6	5	4
Support Staff	250	30	5	4	3
3️⃣ hiring_firing_costs.csv (Hiring & Firing)
Staff Category	Hiring Cost (₹)	Firing Cost (₹)
Caregivers	5000	3500
Nurses	7500	5000
Support Staff	4000	2500
🔥 Next Steps
✅ Deploy This as a Web App
Deploy Gradio UI using Hugging Face Spaces or Streamlit Cloud.

✅ Enhance AI Recommendations
Train custom GPT models for better AI-based staff allocation.

⚠️ Troubleshooting
🔹 Issue: API not working
🔹 Solution: Ensure OpenRouter API key is set correctly in staff_scheduler.py.

🔹 Issue: Gradio UI not launching
🔹 Solution: Check if port 7860 is free, or specify a different port:

bash
Copy
Edit
python main.py --port 5000
👨‍💻 Contributors
Khushi Karelia (Project Owner)
