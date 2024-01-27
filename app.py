from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    paid_by = db.Column(db.String(50), nullable=False)
    participants = db.Column(db.String(255), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form.get('description')
        amount = float(request.form.get('amount', 0.0))
        paid_by = request.form.get('paid_by')
        participants = request.form.get('participants')

        expense = Expense(description=description, amount=amount, paid_by=paid_by, participants=participants)
        db.session.add(expense)
        db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
