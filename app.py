import gradio as gr
import time

# Bubble Sort Generator — generates list states step-by-step with early exit
def bubble_sort_steps(arr):
    arr = arr[:]
    n = len(arr)
    steps = []

    # perform bubble sort & track actions
    for i in range(n):
        swapped = False  # track if any swap happens in this pass
        for j in range(0, n - i - 1):
            steps.append((arr[:], j, j + 1, "compare"))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                steps.append((arr[:], j, j + 1, "swap"))
        if not swapped:  # early exit if no swaps in this pass
            break

    steps.append((arr[:], -1, -1, "done"))
    return steps

# Render "bars" that represent the size of each number as HTML, centered horizontally
def render_bars(arr, highlight1, highlight2, action):
    html = '<div style="display:flex; justify-content:center; gap:5px; align-items:flex-end;">'
    max_val = max(arr) if arr else 1
    for i, val in enumerate(arr):
        color = "#3498db"  # normal colour
        if i == highlight1 or i == highlight2:
            color = "#e74c3c" if action == "swap" else "#f1c40f" # colours change to demonstrate swapping
        height = int((val / max_val) * 100)
        html += f'<div style="width:30px; height:{height}px; background-color:{color}; display:flex; align-items:flex-end; justify-content:center; color:white; font-weight:bold;">{val}</div>' # the height of each bar is the number it represents
    html += '</div>'
    return html

# Gradio generator function for animation
def visualize_bubble_sort(numbers):
    # simple exception handling
    try:
        nums = [int(x) for x in numbers.split(",")] # seperates out each int
    except:
        yield "Error: Enter whole numbers separated by commas"
        return

    steps = bubble_sort_steps(nums) # retrives the "steps" in sorting the numbers
    for state, h1, h2, action in steps:
        frame = render_bars(state, h1, h2, action)
        yield frame
        time.sleep(0.3) # time in between "frames"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("<center><h1>Bubble Sort Visualizer 🫧</h1></center>")
    gr.Markdown("Enter numbers separated by commas and watch the sorting animation.")
    input_numbers = gr.Textbox(label="Numbers", placeholder="e.g., 5,3,2,4,1")
    output_html = gr.HTML()
    run_button = gr.Button("Run Bubble Sort")
    run_button.click(visualize_bubble_sort, inputs=input_numbers, outputs=output_html)

demo.launch(theme='shivi/calm_seafoam')
