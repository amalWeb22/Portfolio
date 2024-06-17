from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration de l'email (exemple avec Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'amal.abghouni@etu.uae.ac.ma'  # Remplacez par votre adresse email Gmail
app.config['MAIL_PASSWORD'] = 'TEstttt'  # Remplacez par votre mot de passe Gmail

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            msg = Message('Nouveau message depuis le formulaire de contact',
                          sender=email,  # Utilise l'adresse email saisie comme expéditeur
                          recipients=['amal.abghouni@etu.uae.ac.ma'])  # Remplacez par l'adresse email destinataire
            msg.body = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"
            mail.send(msg)

            return "Message envoyé avec succès!"
        else:
            return "Méthode non autorisée pour cette route."
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
