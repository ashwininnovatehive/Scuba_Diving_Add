from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# --- ROUTES FOR DETAIL PAGES ---
@app.route('/discover-scuba-details')
def discover_scuba_details():
    return render_template('discover-scuba-details.html')

@app.route('/average-deep-dive-details')
def average_deep_dive_details():
    return render_template('average-deep-dive.html')

@app.route('/shallow-scuba-dive-details')
def shallow_scuba_dive_details():
    return render_template('shallow-scuba-dive.html')
    
@app.route('/watersports-package-details')
def watersports_package_details():
    return render_template('watersports-package.html')

# Route to handle the booking form submission
@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    email = request.form.get('email')
    activity = request.form.get('activity')
    date = request.form.get('date')
    people = request.form.get('people')
    with open('bookings.txt', 'a') as f:
        f.write(f"Name: {name}, Email: {email}, Activity: {activity}, Date: {date}, People: {people}\n")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
    