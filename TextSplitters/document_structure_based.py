from langchain_text_splitters import RecursiveCharacterTextSplitter, Language



text = """# --- task_manager.py ---
import datetime

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return f"Task({self.title}, Priority={self.priority})"

class TaskManager:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

    def add_task(self, title, priority="Medium"):
        new_task = Task(title, priority)
        self.tasks.append(new_task)
        print(f"Added: {title}")

    def show_tasks(self):
        print(f"\n{self.owner}'s Task List:")
        for task in self.tasks:
            print(f"- {task.title} [{task.priority}]")

    def clear_all(self):
        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() == 'y':
            self.tasks = []
            print("List cleared.")

def main():
    # Initializing the app
    manager = TaskManager("Rahul")
    
    # Adding some sample data
    manager.add_task("Fix LangChain bug", "High")
    manager.add_task("Buy groceries", "Low")
    manager.add_task("Finish 100 lines of code", "Medium")
    
    manager.show_tasks()

if __name__ == "__main__":
    main()
    """

spliter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 100,
    chunk_overlap = 10
)

chunk = spliter.split_text(text)

print(chunk[2])