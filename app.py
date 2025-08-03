from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # for session handling

# Dummy user data
dummy_user = {
    "email": "intern@gmail.com",    # <-- use email here
    "password": "1234",
    "name": "Sham Kumar",
    "referral": "sham2025",
    "donations": 17000
}


@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == dummy_user['email'] and password == dummy_user['password']:
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Just a dummy signup
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/leaderboard')
def leaderboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('leaderboard.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/api/user')
def api_user():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({
        "name": dummy_user['name'],
        "referral": dummy_user['referral'],
        "donations": dummy_user['donations']
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


