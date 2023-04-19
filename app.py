from flask import Flask, render_template, request
from flask_mailman import Mail, EmailMessage
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['MAIL_SERVER'] = 'your.smtp.server'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your.email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

csrf = CSRFProtect(app)
mailman = Mail(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/send_email_with_template', methods=['POST'])
def send_email_with_template():
    recipient = request.form['recipient']
    name = request.form['name']
    msg = EmailMessage(
        subject='Welcome to Flask-Mailman Tutorial',
        body=render_template('email_template.html', name=name),
        from_email='test.medium@gmail.com',
        to=[recipient]
    )
    msg.content_subtype = "html"
    msg.send()
    return 'Email sent using template!'