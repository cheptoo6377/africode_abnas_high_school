Creating a **meal plan using Flask** typically means building a web app where users can generate, view, and maybe even save meal plans. Below is a **basic example** of a Flask web app that:

* Shows a daily meal plan.
* Lets you regenerate it with different meals.

You can expand it later with a database, authentication, or meal preferences.

---

### 📁 Project Structure

```
meal_planner/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css  (optional)
```

---

### 🐍 `app.py`

```python
from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

# Sample meal data
meals = {
    'breakfast': ['Oatmeal with fruits', 'Scrambled eggs & toast', 'Smoothie bowl', 'Greek yogurt with granola'],
    'lunch': ['Grilled chicken salad', 'Turkey sandwich', 'Veggie wrap', 'Pasta primavera'],
    'dinner': ['Baked salmon & veggies', 'Stir-fry tofu and rice', 'Chicken curry & naan', 'Beef tacos'],
    'snacks': ['Almonds', 'Fruit salad', 'Protein bar', 'Hummus and carrots']
}

def generate_meal_plan():
    return {
        'breakfast': random.choice(meals['breakfast']),
        'lunch': random.choice(meals['lunch']),
        'dinner': random.choice(meals['dinner']),
        'snacks': random.choice(meals['snacks'])
    }

@app.route('/')
def index():
    plan = generate_meal_plan()
    return render_template('index.html', meal_plan=plan)

@app.route('/refresh')
def refresh():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 🧾 `templates/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Daily Meal Plan</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        h1 { color: #4CAF50; }
        .meal { margin: 10px 0; }
        button { padding: 10px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Today's Meal Plan</h1>
    <div class="meal"><strong>Breakfast:</strong> {{ meal_plan.breakfast }}</div>
    <div class="meal"><strong>Lunch:</strong> {{ meal_plan.lunch }}</div>
    <div class="meal"><strong>Dinner:</strong> {{ meal_plan.dinner }}</div>
    <div class="meal"><strong>Snacks:</strong> {{ meal_plan.snacks }}</div>

    <form action="{{ url_for('refresh') }}">
        <button type="submit">Generate New Plan</button>
    </form>
</body>
</html>
```

---

### ▶️ How to Run

1. Save the above files in a folder.
2. Run the app:

   ```bash
   python app.py
   ```
3. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

### ✅ Next Steps

* Add user login and saved meal plans using Flask-Login and a database (SQLite).
* Let users set preferences (vegetarian, keto, etc.).
* Add a calendar view for weekly planning.

Would you like me to expand it into a weekly meal planner with a database?
