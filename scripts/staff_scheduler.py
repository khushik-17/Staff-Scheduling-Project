import pandas as pd
import requests
import gradio as gr
from optimization import optimize_schedule

# OpenRouter API Key
API_KEY = "your_api_key_here"

def load_data():
    """ Load CSV files for staff scheduling. """
    historical_demand = pd.read_csv("data/historical_demand.csv")
    staff_details = pd.read_csv("data/staff_details.csv")

    min_staff_morning = staff_details["Min Staff Weekday Morning"].tolist()
    min_staff_evening = staff_details["Min Staff Weekday Evening"].tolist()
    min_staff_night = staff_details["Min Staff Weekday Night"].tolist()

    hiring_firing_costs = pd.read_csv("data/hiring_firing_costs.csv")
    return historical_demand, staff_details, hiring_firing_costs

def query_openrouter(prompt):
    """ Send scheduling prompt to DeepSeek AI via OpenRouter API. """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "deepseek-ai",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

def generate_schedule():
    """ Generate staff scheduling with AI recommendations. """
    # Load data
    historical_demand, staff_details, hiring_firing_costs = load_data()

    # Optimize schedule using LP
    optimized_schedule = optimize_schedule(historical_demand, staff_details, hiring_firing_costs)

    # Generate AI prompt
    prompt = f"""
    Generate an optimized staff schedule given:
    - Staff categories: {list(staff_details['Staff Category'])}
    - Hiring costs: {hiring_firing_costs.to_dict()}
    - Historical shift requirements: {historical_demand.to_dict()}
    - Objective: Minimize costs while meeting constraints.
    Optimized LP Results:
    {optimized_schedule}
    Suggest adjustments for better efficiency.
    """

    # Get AI Recommendations
    ai_response = query_openrouter(prompt)
    
    return optimized_schedule, ai_response

# Gradio UI
def gradio_interface():
    optimized_schedule, ai_response = generate_schedule()
    
    return f"""
     **Optimized Shift Schedule:**
    {optimized_schedule}
    
     **AI Recommendations:**
    {ai_response}
    """

# Launch Gradio App
gr.Interface(fn=gradio_interface, inputs=[], outputs="text").launch()
