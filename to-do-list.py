import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.pack(pady=20)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, bg="#e0e0e0", fg="#333333", selectbackground="#333333", selectforeground="#ffffff")
        self.task_listbox.pack(side=tk.LEFT, padx=20)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, width=12, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=10)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task, width=12, bg="#2196F3", fg="white")
        self.update_button.grid(row=0, column=1, padx=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, width=12, bg="#F44336", fg="white")
        self.delete_button.grid(row=0, column=2, padx=10)

        self.complete_button = tk.Button(self.button_frame, text="Complete Task", command=self.complete_task, width=12, bg="#FFC107", fg="white")
        self.complete_button.grid(row=0, column=3, padx=10)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            new_task = simpledialog.askstring("Update Task", "Enter the new task:", initialvalue=self.tasks[task_index]["task"])
            if new_task:
                self.tasks[task_index]["task"] = new_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks.pop(task_index)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index]["completed"] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Complete Task", "Please select a task to mark as completed.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["completed"] else "Not Done"
            self.task_listbox.insert(tk.END, f"{task['task']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
