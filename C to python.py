import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("C to Python Converter")

# Create a label to prompt the user to enter C code
label = tk.Label(text="Enter C code:")
label.pack()

# Create a text area for the user to enter the C code
text = tk.Text()
text.pack()

# Create a function to convert the C code to Python
def convert_code():
  # Get the C code from the text area
  c_code = text.get("1.0", "end")

  # Convert the C code to Python
  python_code = c_code.replace("if", "if")
  python_code = python_code.replace("else", "else")
  python_code = python_code.replace("for", "for")
  python_code = python_code.replace("while", "while")
  python_code = python_code.replace("do", "do")
  python_code = python_code.replace("break", "break")
  python_code = python_code.replace("continue", "continue")
  python_code = python_code.replace("switch", "elif")
  python_code = python_code.replace("case", "elif")
  python_code = python_code.replace("default", "else")

  # Convert the printf statement to the print function
  python_code = python_code.replace("printf", "print")

  # Display the converted Python code
  result_text.delete("1.0", "end")
  result_text.insert("1.0", python_code)

# Create a button to initiate the conversion
convert_button = tk.Button(text="Convert", command=convert_code)
convert_button.pack()

# Create a label to display the result
result_label = tk.Label(text="Converted Python code:")
result_label.pack()

# Create a text area to display the result
result_text = tk.Text()
result_text.pack()

# Run the main loop
window.mainloop()
