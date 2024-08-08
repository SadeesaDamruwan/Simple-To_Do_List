import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")

tasks = []

# Frame to hold the listbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Listbox to display tasks
listbox = tk.Listbox(frame, width=50, height=10, selectmode=tk.SINGLE)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Entry widget to add a task
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({'description': task, 'done': False})
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "[Done] " if task['done'] else ""
        listbox.insert(tk.END, f"{status}{task['description']}")

# Function to mark a task as done
def mark_task_done():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks[index]['done'] = True
        update_listbox()
    else:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to delete a task
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks.pop(index)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "You must select a task.")

# Buttons for adding, marking as done, and deleting tasks
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=10)

done_button = tk.Button(button_frame, text="Mark Task as Done", command=mark_task_done)
done_button.grid(row=0, column=1, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=10)

# Start the GUI event loop
root.mainloop()
