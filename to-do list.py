'''
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists
'''
import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("300x400")
        self.root.configure(bg="#282a36")  # Dracula theme background color

        self.title_label = tk.Label(root, text="To-Do List", bg="#282a36", fg="#f8f8f2", font=("Helvetica", 16, "bold"))  # Dracula theme text color
        self.title_label.pack(pady=10)

        self.entry = tk.Entry(root, width=30, font=("Helvetica", 12))
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add task", command=self.add_task, bg="#50fa7b", fg="#282a36", font=("Helvetica", 10, "bold"), width=20)  # Dracula theme green color
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(root, text="Edit task", command=self.edit_task, bg="#ff79c6", fg="#282a36", font=("Helvetica", 10, "bold"), width=20)  # Dracula theme pink color
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete task", command=self.delete_task, bg="#ff5555", fg="#f8f8f2", font=("Helvetica", 10, "bold"), width=20)  # Dracula theme red color
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as complete", command=self.complete_task, bg="#f1fa8c", fg="#282a36", font=("Helvetica", 10, "bold"), width=20)  # Dracula theme yellow color
        self.complete_button.pack(pady=5)

        self.listbox_frame = tk.Frame(root)
        self.listbox_frame.pack(pady=10)

        self.listbox = tk.Listbox(self.listbox_frame, width=50, height=10, bg="#44475a", fg="#f8f8f2", font=("Helvetica", 10))  # Dracula theme selection color
        self.listbox.pack(side="left", fill="y")

        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
        else:
            messagebox.showinfo("Warning", "Please enter a task.")
        self.entry.delete(0, "end")
    
    def edit_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            task_to_edit = self.tasks[task_index]
            if task_to_edit.startswith("[Completed] "):
                task_to_edit = task_to_edit.replace("[Completed] ", "", 1)
            self.entry.delete(0, "end")
            self.entry.insert(0, task_to_edit)
            self.add_button.config(text="Update task", command=lambda: self.update_task(task_index))
        except:
            messagebox.showinfo("Warning", "Please select a task to edit.")
    
    def update_task(self, task_index):
        new_task = self.entry.get()
        if new_task != "":
            self.tasks[task_index] = new_task
            self.update_listbox()
            self.add_button.config(text="Add task", command=self.add_task)
            self.entry.delete(0, "end")
        else:
            messagebox.showinfo("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            del self.tasks[task_index]
            self.update_listbox()
        except:
            messagebox.showinfo("Warning", "Please select a task to delete.")

    def complete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            if not self.tasks[task_index].startswith("[Completed] "):
                self.tasks[task_index] = "[Completed] " + self.tasks[task_index]
                self.update_listbox()
            else:
                messagebox.showinfo("Warning", "This task is already marked as complete.")
        except:
            messagebox.showinfo("Warning", "Please select a task to mark as complete.")

    def update_listbox(self):
        self.listbox.delete(0, "end")
        for task in self.tasks:
            self.listbox.insert("end", task)

def main():
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()