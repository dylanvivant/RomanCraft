# Documentation technique de RomanCraft

Ce document fournit des informations détaillées sur l'architecture, la structure du code et les choix techniques de RomanCraft.

## Architecture

RomanCraft suit une architecture Modèle-Vue-Contrôleur (MVC) :

- **Modèles** : Représentent les données et la logique métier (Roman, Chapitre, Personnage, Idée)
- **Vues** : Gèrent l'interface utilisateur (MainWindow, ChapitreView, PersonnageView, IdeeView)
- **Contrôleurs** : Lient les modèles et les vues (RomanController, ChapitreController, PersonnageController, IdeeController)

## Structure du projet

```
RomanCraft/
├── src/
│   └── main/
│       ├── controllers/
│       ├── models/
│       ├── views/
│       └── app.py
├── resources/
│   ├── icons/
│   └── styles/
├── docs/
└── tests/
```

## Dépendances principales

- PyQt6 : Framework d'interface graphique
- json : Pour la sérialisation et la désérialisation des données

## Fonctionnalités clés

1. **Gestion des romans** : Création, ouverture, sauvegarde
2. **Gestion des chapitres** : Ajout, modification, suppression
3. **Gestion des personnages** : Ajout, modification, suppression
4. **Gestion des idées** : Ajout, modification, suppression

## Flux de données

1. L'utilisateur interagit avec l'interface (Vues)
2. Les Vues notifient les Contrôleurs des actions de l'utilisateur
3. Les Contrôleurs mettent à jour les Modèles
4. Les Modèles notifient les Contrôleurs des changements
5. Les Contrôleurs mettent à jour les Vues

## Style et design

Le design de RomanCraft suit une approche minimaliste et moderne, utilisant une palette de couleurs sombres pour une expérience visuelle agréable. Les styles sont définis dans le fichier `resources/styles/style.qss`.

## Tests

Les tests unitaires et d'intégration sont situés dans le dossier `tests/`. Utilisez pytest pour exécuter les tests :

```
pytest tests/
```

## Contribution

Pour contribuer au projet, veuillez suivre ces étapes :

1. Forker le dépôt
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commiter vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pousser vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

Pour plus d'informations, consultez le fichier CONTRIBUTING.md à la racine du projet.
