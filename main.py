from scripts.staff_scheduler import generate_schedule
import gradio as gr

def main():
    """ Main function to execute staff scheduling optimization. """
    print(" Generating Optimized Shift Schedule...")
    
    # Generate schedule & AI recommendations
    optimized_schedule, ai_response = generate_schedule()

    # Display output in console
    print("\n Optimized Staff Schedule:")
    print(optimized_schedule)
    print("\n AI Recommendations:")
    print(ai_response)

    # Launch Gradio UI
    print("\n Launching Gradio Interface...")
    gr.Interface(fn=lambda: (optimized_schedule, ai_response), inputs=[], outputs="text").launch()

if __name__ == "__main__":
    main()
