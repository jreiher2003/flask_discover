from flask import Flask, render_template, redirect, request, url_for, session, flash

app = Flask(__name__)

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			flash('Invalid credentials. Please try again.', 'danger')
		else:
			session['logged_in'] = True
			flash('Your logged in!', 'success')
			return redirect(url_for('home'))
	return render_template('login.html')

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You just logged out!', 'danger')
    return redirect(url_for('welcome'))



if __name__ == '__main__':
	app.secret_key = 'jeffrey'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)