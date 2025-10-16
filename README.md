# template-depot-git
## Template de Projet Développement logiciel et dépôt Git — BTS CIEL

[![Utiliser ce template](https://img.shields.io/badge/GitHub-Use%20this%20template-brightgreen?logo=github)](https://github.com/boudjelaba/template-depot-git/generate)

## Description
Ce template sert d'exemple pour les étudiants souhaitant créer un dépôt GitHub pour leurs projets en développement logiciel. Il montre une structure de base avec des fichiers essentiels (HTML, CSS, JS, Python) et des bonnes pratiques pour organiser un dépôt.

## Prérequis
Avant de commencer, assurez-vous d’avoir les éléments suivants installés :
- [Git](https://git-scm.com/) pour gérer le contrôle de version (pour travailler en local et pousser les modifications vers Github).
- [Python](https://www.python.org/downloads/) pour exécuter des scripts Python (si nécessaire).

---

### Informations sur le dépôt

[![GitHub Stars](https://img.shields.io/github/stars/IgorAntun/node-chat.svg)](https://github.com/boudjelaba/template-depot-git) 
![GitHub forks](https://img.shields.io/github/forks/boudjelaba/template-depot-git)
![GitHub watchers](https://img.shields.io/github/watchers/boudjelaba/template-depot-git)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Créé le](https://img.shields.io/github/created-at/boudjelaba/template-depot-git?label=Créé%20le)
![Dernier commit](https://img.shields.io/github/last-commit/boudjelaba/template-depot-git?label=Dernier%20commit)
[![Status](https://img.shields.io/badge/Status-En%20développement-yellow)]()

![Taille du repo](https://img.shields.io/github/repo-size/boudjelaba/template-depot-git?label=Taille%20du%20repo)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/boudjelaba/template-depot-git)
![GitHub language count](https://img.shields.io/github/languages/count/boudjelaba/template-depot-git)
![GitHub repo file or directory count](https://img.shields.io/github/directory-file-count/boudjelaba/template-depot-git)
[![GitHub Issues](https://img.shields.io/github/issues/IgorAntun/node-chat.svg)](https://github.com/boudjelaba/template-depot-git/issues) [![Current Version](https://img.shields.io/badge/version-1.0.7-green.svg)](https://github.com/boudjelaba/template-depot-git/node-chat)
[![All Contributors](https://img.shields.io/badge/all_contributors-73-orange.svg?style=flat-square)]([./CONTRIBUTORS.md](https://github.com/boudjelaba/template-depot-git))

---

### Informations sur le projet

[![github](https://img.shields.io/badge/GitHub-black?logo=github&logoColor=white)]()
[![GIT](https://img.shields.io/badge/GIT-E44C30?logo=git&logoColor=white)]()
[![Markdown](https://img.shields.io/badge/Markdown-191970?logo=markdown&logoColor=white)](https://www.markdownguide.org/)
[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)]()
[![mac os](https://img.shields.io/badge/mac%20os-000000?logo=apple&logoColor=white)]()
[![windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)]()

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?logo=javascript)
[![HTML & CSS](https://img.shields.io/badge/HTML%20%26%20CSS-yellow?logo=html5&logoColor=white)](https://developer.mozilla.org/fr/docs/Web)

---

## Table des matières

<!-- TOC START -->
- [Template de Projet Développement logiciel et dépôt Git — BTS CIEL](#template-de-projet-développement-logiciel-et-dépôt-git--bts-ciel)
  - [Description](#description)
  - [Prérequis](#prérequis)
    - [Informations sur le dépôt](#informations-sur-le-dépôt)
    - [Informations sur le projet](#informations-sur-le-projet)
  - [Table des matières](#table-des-matières)
  - [Objectifs](#objectifs)
  - [Structure du template GitHub](#structure-du-template-github)
  - [Comment utiliser ce template](#comment-utiliser-ce-template)
  - [À faire](#à-faire)
  - [Commandes utiles](#commandes-utiles)
  - [Bonnes pratiques](#bonnes-pratiques)
  - [Contribution](#contribution)
    - [Création du dépôt GitHub](#création-du-dépôt-github)
  - [Bonnes pratiques](#bonnes-pratiques-1)
  - [Feuille de route](#feuille-de-route)
  - [Automatisation du sommaire](#automatisation-du-sommaire)
    - [Utilisation](#utilisation)
  - [Licence](#licence)
  - [Auteurs](#auteurs)
<!-- TOC END -->

---

## Objectifs

- la gestion de projet collaboratif,
- Prendre en main Git et GitHub,
- l’organisation d’un dépôt Git/GitHub propre,
- comprendre l'importance du versionnement
- la structuration d’un code source réutilisable,
- la documentation et le suivi de projet.

---

## Structure du template GitHub

```plaintext
📁 template-depot-git/
├── README.md        # Fichier de description du projet
├── .gitignore       # Fichiers à ignorer dans Git
├── CONTRIBUTING.md  # Guide de contribution
├── LICENSE          # Licence du projet
├── assets/          # Contient les fichiers statiques et les scripts (images, CSS, JS, etc.)
│   ├── logo.png
│   ├── css/
│   │  └── style.css
│   └── js/
│      └── script.js
├── scripts/         # Scripts et outils divers
│   └── generate_toc.py
└── index.html       # Page d'accueil du projet
```

## Comment utiliser ce template

1. Cliquez sur **"Use this template"** en haut à droite de la page GitHub.
2. Créez un nouveau dépôt à partir de ce template.
3. Clonez votre nouveau dépôt sur votre machine :
   ```bash
   git clone <url-de-votre-nouveau-depot>
   ```
4. Créez une branche de développement :
   ```bash
   git checkout -b dev
   ```
5. Ajoutez ou modifiez des fichiers :
   * **index.html** : Modifiez le code HTML pour refléter votre projet.
   * **style.css** : Adaptez le style CSS à vos besoins.
   * **script.js** : Ajoutez votre logique JavaScript.
6. Enregistrez vos modifications :
   ```bash
   git add .
   git commit -m "Ajout de mes modifications"
   git push origin dev
   ```
7. Créez une Pull Request sur GitHub pour proposer vos changements.
8. Exécutez les scripts :
   Vous pouvez exécuter `generate_toc.py` de cette manière pour générer une table des matières automatiquement :
   ```bash
   python scripts/generate_toc.py
   ```

**Si vous n'avez pas de compte Github**

Pour utiliser ce template, commencez par cloner le dépôt Git sur votre machine locale :

```bash
git clone https://github.com/boudjelaba/template-depot-git.git
```



## À faire

- [ ] Forkez ce dépôt
- [ ] Créez une branche `dev`
- [ ] Ajoutez un nouveau fichier HTML ou modifiez celui existant
- [ ] Poussez vos changements
- [ ] Créez une Pull Request

## Commandes utiles

```bash
git clone <url>
git checkout -b nom-de-branche
git add .
git commit -m "mon message"
git push origin nom-de-branche
```

## Bonnes pratiques

- Travaillez toujours sur une branche dédiée (ex : `dev`, `feature/ma-fonctionnalite`)
- Décrivez clairement vos commits et Pull Requests
- Relisez le code avant de fusionner
  
---
Ce template est conçu pour faciliter la collaboration et l’apprentissage autour de Git et GitHub.

---

## Contribution

Si vous souhaitez contribuer à ce projet, veuillez lire le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour connaître les bonnes pratiques et les étapes à suivre.


### Création du dépôt GitHub

Initialiser le dépôt et le publier sur GitHub :

```bash
git init
git add .
git commit -m "Initial commit"
gh repo create mon_projet --public --source=. --remote=origin
git push -u origin main
```

---

## Bonnes pratiques

- **Ne jamais versionner les mots de passe ou secrets** : utilisez des fichiers d’exemple (`db.sample.php`).
- **Nettoyez régulièrement les fichiers temporaires**.
- **Protégez les dossiers sensibles avec `.htaccess`**.
- **Utilisez le script de déploiement pour éviter d’exposer des fichiers inutiles ou sensibles en production**.

---

## Feuille de route

- [x] Créer un nouveau dépôt Git
- [x] Créer une issue
- [ ] Support Multi-plateforme
    - [ ] MacOS
    - [ ] Linux
- [ ] Autre
---

<details><summary><b>Dates à retenir</b></summary>

1. Début du projet : Date 1
2. Fiches recettes : Date 2
3. Rapport et présentation : Date 3

</details>

<br>

---

## Automatisation du sommaire

### Utilisation

1. Enregistrer le fichier sous `generate_toc.py` dans le même dossier que le `readme.md`. (voir fichier joint)
2. Lancer-le avec :

```bash
python generate_toc.py
```

3. S'assurer d’avoir dans le `readme.md` une section avec les balises :

```bash
<!-- TOC START -->
<!-- TOC END -->
```

---

## Licence

Ce projet est sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## Auteurs

- <r>&copy;</r> K.B.
- <o>&reg;</o> Carnus
- <g>Date :</g> 01/09/2025
