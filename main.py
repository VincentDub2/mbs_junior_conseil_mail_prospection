import csv
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv
import os

# Charger les variables d'environnement du fichier .env
load_dotenv()


# Accéder aux variables d'environnement
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
smtp_user = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASSWORD')
envoyeur=os.getenv('ENVOYEUR')

# Assurez-vous que vos variables ne sont pas None
if not all([smtp_server, smtp_port, smtp_user, smtp_password]):
    print("Les informations d'authentification SMTP ne sont pas définies correctement.")
    exit(1)


# Chemin vers votre fichier texte
file_path = 'email_content.txt'


# Lire le modèle d'e-mail à partir du fichier texte
def lire_modele_email(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        subject = file.readline().strip().replace('Objet: ', '')
        file.readline()  # Ignorer la ligne de séparation
        body_template = file.read().strip()
    return subject, body_template

# Récupérer le sujet et le modèle du corps de l'e-mail
email_subject, email_body_template = lire_modele_email('email_content.txt')

# Afficher l'objet et le corps pour vérification
print(f"Objet: {email_subject}")
print(f"Corps: {email_body_template}")


# Créer une connexion SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_user, smtp_password)

# Lire les adresses e-mail depuis le fichier CSV
with open('emails.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    
    # Passer l'en-tête si nécessaire
    next(reader, None)  # Enlève l'en-tête si votre fichier en a un
    
    for row in reader:
        if len(row) > 1:
            
            nom, sexe, email = row[0], row[1], row[2]
            
            print(f"L'email récupéré est : {email}")
            
            salutation = 'Madame' if sexe == 'F' else 'Monsieur'
            
             # Remplacer les placeholders dans le modèle de l'e-mail
            email_body = email_body_template.replace('{salutation}', salutation).replace('{nom}', nom).replace('{envoyeur}',envoyeur)
            

            # Créer un objet MIMEText
            msg = MIMEText(email_body)
            msg['Subject'] = email_subject
            msg['From'] = smtp_user
            msg['To'] = email
            # Envoyer l'e-mail
            try:
                server.sendmail(smtp_user, email, msg.as_string())
                print(f"Mail envoyé à {email}")
            except Exception as e:
                print(f"Erreur lors de l'envoi à {email}: {e}")
        else:
            print("Ligne vide, on passe à la suivante.")

# Fermer la connexion SMTP
server.quit()
