# Algorithm Name: Bubble Sort
I chose Bubble Sort because it creates a simple and visually intuitive animation where larger values “bubble” toward the end of the list. This upward movement makes the algorithm aesthetically pleasing and easy for beginners to understand. Bubble Sort also has a repetitive, step-by-step structure that translates well into a visual demonstration. Since the algorithm compares and swaps adjacent values, each change is small, clear, and easy to track in a GUI. Overall, its simplicity and visual clarity make it ideal for an educational sorting app.

## Problem Breakdown & Computational Thinking
### Decomposition
- Break the problem into reading user input, performing the bubble sort, and displaying each step visually
- Separate the sorting process into repeated passes through the list and comparisons of adjacent items
- Divide the interface into components: input box, visualization area, and status messages

### Pattern Recognition
- The algorithm repeatedly compares pairs of neighboring values and swaps them whenever they are out of order (i.e. the second value is smaller)
- Each pass pushes the largest remaining value to the end, creating a clear, repeated “bubbling” pattern
- The number of comparisons decreases on each pass as the sorted portion grows

### Abstraction
- Show only the key actions: comparisons, swaps, and the updated list after each operation
- Hide low-level implementation details (loop counters, index variables, internal Python mechanics)
- Present the list visually in a simple, readable format rather than exposing raw code

### Algorithm Design
- **Input** → user enters a list of numbers
- **Processing** → bubble sort algorithm runs step-by-step
- **Output** → visual updates show each comparison and swap.
- The GUI controls when sorting starts using a button and displays the evolving list states during the algorithm
- My goal is to produce a sort of "animation" displaying each swap occuring in the sorting. This will be a nice way to visually show the "bubbling" effect of bubble sort.

## Demo video/gif/screenshot of test


## Steps to Run
1. Enter whole numbers seperated by commas (e.g. 3,4,2,1,8,4)
2. Click "Run Bubble Sort"
3. Watch the bubble sort visualization!
## Hugging Face Link
https://huggingface.co/spaces/aerb7/CISC121_Project

## Author & Acknowledgment
Author: Amanda Bayne

Acknowledgements: Used the Hugging Face doccumentation (https://huggingface.co/docs) to help deploy my app. Additionally, I used the Gradio quickstart guide (https://www.gradio.app/guides/quickstart) to implement Gradio UI.
