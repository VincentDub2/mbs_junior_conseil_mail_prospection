# 🚀 MBS Junior Conseil Mail Automation

Ce projet fournit un script Python pour automatiser l'envoi d'e-mails personnalisés. Le script lit une liste d'adresses e-mail stockées dans un fichier CSV et utilise un modèle d'e-mail pour générer le contenu, en adaptant la salutation selon le sexe du destinataire et en intégrant leur nom dans le message.

## 🌟 Fonctionnalités

- 📬 Envoi automatique d'e-mails personnalisés.
- 📋 Lecture des destinataires depuis un fichier CSV.
- 📝 Personnalisation de l'e-mail selon le nom et le sexe du destinataire.
- 📜 Utilisation d'un modèle pour le contenu du message.

## 📌 Prérequis

- 🐍 Python 3.
- 🧰 Bibliothèques Python : `smtplib`, `email`, `csv`, `os`, `dotenv`.
- 📤 Un serveur SMTP (Gmail, Outlook, etc.).

## ⚙️ Configuration

1. **Installer Python 3** : Vérifiez que Python 3 est installé sur votre système.

2. **Installer les Dépendances** : Utilisez `pip` pour installer les dépendances nécessaires.

   ```bash
   pip install python-dotenv
   ```

3. **Créer un fichier `.env`** : Dans le répertoire racine du projet, créez un fichier `.env` avec les variables suivantes :
    ```
    SMTP_SERVER=adresse_du_serveur_smtp
    SMTP_PORT=port_du_serveur
    SMTP_USER=votre_adresse_email
    SMTP_PASSWORD=votre_mot_de_passe
    ENVOYEUR=votre_nom_et_prenom
    header_email=le_nom_affiche_dans_le_client_email
    ```
    Un fichier `.example.env` est fourni comme exemple.

4. **Préparer le Fichier CSV** : Structurez `emails.csv` avec les colonnes `Nom`, `Sexe` et `Email`.

5. **Rédiger le Modèle d'E-mail** : Créez un fichier `email_content.txt` avec l'objet et le corps de l'e-mail, utilisant `{salutation}`, `{envoyeur}` et `{nom}` comme placeholders.

## 🚀 Utilisation

Pour lancer le script :

```bash
python chemin/vers/le/script.py
```

Le script lira les adresses e-mail du CSV, préparera les e-mails avec le modèle fourni, et les enverra à chaque destinataire.

## 🔄 Conversion Excel/Numbers en CSV

Pour utiliser des données d'Excel ou Numbers :
- Ouvrez le fichier avec Excel/Numbers.
- Choisissez `Fichier > Enregistrer sous...`.
- Sélectionnez le format `CSV`.
- Enregistrez le fichier.

Assurez-vous que le fichier CSV final respecte la structure requise.

## 👤 Auteurs

- Vincent Dubuc
- Quentin Privat

## ©️ Licence

Ce projet est sous licence libre.

## 📝 Remarques

- Assurez-vous d'avoir l'autorisation pour envoyer des e-mails aux destinataires.
- Testez le script avec un petit nombre d'adresses avant une utilisation à grande échelle.

