import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
        save_tasks()
    else:
        messagebox.showwarning("Select Task", "No task selected.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        task_done = f"{task} ✔"
        tasks[index] = task_done
        listbox.delete(index)
        listbox.insert(index, task_done)
        save_tasks()
    else:
        messagebox.showwarning("Select Task", "No task selected.")

root = tk.Tk()
root.title("To-Do List App")

tasks = load_tasks()

entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.grid(row=0, column=1)

listbox = tk.Listbox(root, width=50, height=10)
listbox.grid(row=1, column=0, columnspan=2, padx=10)

for task in tasks:
    listbox.insert(tk.END, task)

delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.grid(row=2, column=0, pady=5)

done_btn = tk.Button(root, text="Mark as Done", width=15, command=mark_done)
done_btn.grid(row=2, column=1, pady=5)

root.mainloop()
