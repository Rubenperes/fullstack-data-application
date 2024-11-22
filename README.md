# Data FullStack Application

Sommaire : 

1. Description Globale du projet
2. Les Outils utilisées
3. Guide d'utilisation
   A. Lancer le projet
   B. Page d'Inscription
   C. Page de Connexion
   D. Page Utilisateur
4. Conseils pour les gestions de build
5. Conclusions et axes d'améliorations


# 1.  Description Globale du projet : 

Ce projet de **génération d'images** a été réalisé dans le cadre du cours **Full Stack Data**, en 5ème année.

Nous avons utilisé, pour chaque parties du code : 

- **Backend** : FastApi, Python et PostGreSQL
- **Frontend** : Svelte (Framework de JavaScript écrit en TypeScript)

# 2.  Les Outils : 

Comme dit précédemment, nous avons utilisé FastApi et Python ainsi que PostGreSQL pour le **Backend**, Svelte pour le **Frontend**.

Il faut aussi utilisé **DockerDesktop** pour pouvoir faire marcher le projet

Pour finir, nous avons également utilisé **GitHub Desktop** pour gérer les push/pull sur les branches du projet plus facilement.

# 3.  Guide d'utilisation : 

**A -  Lancer le projet :**

Tout d'abord, il faut lancer l'application **DockerDesktop** et doit fonctionner correctement avant de pouvoir continuer.

Il faut également s'assurer d'être dans le bon répertoire comme l'image ci-dessous: 

![image](https://github.com/user-attachments/assets/f309371c-d562-4b66-b123-c141677e56aa)

Une fois que l'on est dans le bon répertoire, on peut rentrer la commmande : 

![image](https://github.com/user-attachments/assets/59f98c1b-c1f0-4cc4-b168-64347d03b38e)

Une fois lancé, veuillez attendre que l'on affiche le bon fonctionnement du front. Cela sera indiqué par le lien en local et avec IP: 

![image](https://github.com/user-attachments/assets/cfe429ca-bed4-420b-888e-a248ff9d73e0)

A retenir que l'application fonctionne en local, et donc, n'a pas de donnée pré-enregistrée et, si vous fermez l'application, toute vos données disparaîtrons.

Après que le chargement soit fini, veuillez entrer sur la barre de recherche : 

![image](https://github.com/user-attachments/assets/6cfb6aba-53ae-4a85-a6aa-693b2f78d10f)


**B - Page d'Inscription :** 

Nous avons au départ, la page de connexion :

![image](https://github.com/user-attachments/assets/38d90654-da54-421f-8831-d9e36521a44e)

Evidemment, avant de pouvoir se connecter, il faut s'inscrire, veuillez appuyer sur le bouton indiquée avec la flèche rouge dans l'image au-dessus.

On se retrouve sur cette page d'inscription : 

![image](https://github.com/user-attachments/assets/e7bb1fbb-d852-4655-b6dc-3a9d1e75ef75)

Il faut s'assurer, comme indiqué, de bien entrer le bon mot de passe 2 fois sinon nous avons une erreur :

![image](https://github.com/user-attachments/assets/617e6e54-8233-4656-9936-6da3971a6ce5)

Dans le cas où l'on met le même mot de passe, l'appli nous envoie directement sur la page de connexion pour s'inscrire.

**C - Page de Connexion :**

Voici la page de connexion : 

![image](https://github.com/user-attachments/assets/1c7a49db-4878-4408-8bcb-0e1100d08f49)

Si on utilise le même mot de passe et nom d'utilisateur, on peut accéder à l'application. Cependant si on met un utilisateur qui n'existe pas, cela fait une erreur, ce qui est normal car il n'est pas connu dans la base de données : 

![image](https://github.com/user-attachments/assets/7500f0d5-59b5-44b0-b0d1-a92ae3b5442a)

Connectons nous avec notre utilisateur : 

![image](https://github.com/user-attachments/assets/32773fa3-2059-4701-94d5-c0160450f1c1)

**D - Page Utilisateur :**

On se retrouve enfin sur la page qui nous intéresse. 

Maintenant qu'on est connecté, nous pouvons utilisé le générateur d'images.

Attention : Le nombres d'images dépendant de l'API utilisé, et ayant utilisé une API gratuite (**StarryAI**), il nous reste environ 80 images utilisables.

Voici un exemple de prompt que l'on peut faire : 

![image](https://github.com/user-attachments/assets/6e7fb457-721d-4232-936d-bb68c079cf82)

A noter : Le temps de chargement est d'environ 1 minute voire un peu plus.

**4. Conseils pour les gestions de build:**

Nous avons remarqué que, lorsque l'on build avec la commande : 

![image](https://github.com/user-attachments/assets/59f98c1b-c1f0-4cc4-b168-64347d03b38e)

Et que l'on modifie le code, nous avions une erreur de build récurrente qui apparaît à chaque fois :

![image](https://github.com/user-attachments/assets/e15df2fd-f03b-444f-9755-e18fc7550a5b)

Il faut simplement supprimer ce fichier (qui, après chaque re-build, réapparaît) : 

![image](https://github.com/user-attachments/assets/15d6eeca-b49f-4db7-b357-a69438368846)

**5. Conclusions et axes d'améliorations:**

Ce qui saute aux yeux et qui pourrait être amélioré c'est principalement la créations de la galerie d'images (et donc de l'enregistrement des images prompts pour la session en cours) que nous avons pas pu finir de programmer mise à part les boutons qui sont présents.

On peut en conclure que ce projet nous a permis d'apprendre beaucoup de nouvelles librairies et surtout, d'apprendre à assembler toutes les connaissances que nous avions au préalables dans un seul et même projet.










