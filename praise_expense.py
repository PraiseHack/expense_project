from uuid import uuid4
from datetime import datetime, timezone


class Expense:
    def __init__(self, title, amount, updated_at) -> None:
        self.id = uuid4()
        self.title = title
        self.amount = amount
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update(self, new_title=None, new_amount=None):
        if new_title:
            self.title = new_title
        if new_amount:
            self.amount = new_amount
        self.updated_at = datetime.now()
        print(f"title {self.title} updated successfully")    
        print(f"amount {self.amount} updated successfully")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }   

    def __repr__(self) -> str:
        return f"{self.title}_{self.amount}"




class ExpenseDataBase:
    def __init__(self) -> None:
        self.expensesdb = []


    def add_expense(self, expense):
        self.expensesdb.append(expense)
        
        print(f"{expense} added successfully")
        return expense.id

    def remove_expense(self, expense_id):
        self.expensesdb = [expense for expense in self.expensesdb if expense.id != expense_id]
        print(f"expense with ID {expense_id} has been removed")
        

    def get_expense_by_id(self, expense_id):
         for expense in self.expensesdb:
            if expense.id == expense_id:
                return expense
            print(f"expense with ID {expense_id} gotten successfully")
         return None 

    def get_expense_by_title(self, expense_title):
        return [expense for expense in self.expensesdb if expense.title == expense_title]


    def to_dict(self):
        return {"expenses": [expense.to_dict() for expense in self.expensesdb]}   




                 
if __name__ == "__main__":
    expense1 = Expense(1, "Cereals", 500)
    expense2 = Expense(2, "Perfumes", 1500)
    expense3 = Expense(3, "Red_wine", 12000)
    expense4 = Expense(4, "Jeans", 15000)
    expense5 = Expense(5, "Bra", 2000)

    db_of_expenses = [expense1, expense2, expense3, expense4, expense5]

    for expense in db_of_expenses:
        print(f"expense: {expense} type: {type(expense)}")

db = ExpenseDataBase()
db.add_expense(expense1)
db.add_expense(expense2)
db.add_expense(expense3)
db.add_expense(expense4)
db.add_expense(expense5)

# Updating an expense
expense1.update(new_amount=550)
expense2.update(new_amount=5000, new_title="Shoe")
expense3.update(new_amount=12500)
expense4.update(new_amount=17000)
expense.update(new_amount=2500, new_title="Flip_flop")

# Retrieving an expense by ID 
expense_by_id = db.get_expense_by_id('c0b092b0-4e6a-40bc-9399-236ca5f59100')
if expense_by_id:
    print(expense_by_id.to_dict())

# # Retrieving expenses by title
expense_by_title = db.get_expense_by_title("Flip_flop")
for expense in expense_by_title:
    print(expense.to_dict())

# Removing an expense
db.remove_expense('6ff7860d-bd36-4ffd-a673-d8f4e994e65d')

# Converting database to dictionary and print it
print(db.to_dict())



