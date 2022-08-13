from taskmanager import db

class Category(db.Model):
    id = db.Column(db.integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks= db.relationship("Task", backref="category", cascade="all, delete", lazy=True)


    def __repr__(self):
        return self.category_name




class Task(db.Model):
    id = db.Column(db.integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.text, nullable=False)
    is_urgent = db.Column(db.boolean, default=False, nullable=False)
    due_date = db.column(db.date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"#{self.id} - Task: {self.task_name} | Urgent: {self.is_urgent}"