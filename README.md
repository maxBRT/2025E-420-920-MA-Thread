# Projet Threading - Pratique avec Tkinter


Ce dépôt met en pratique le threading dans le cadre du cours 420-920-MA au
Collège de Maisonneuve (Été 2025).


**Modalité :** En équipe de 4

**Durée :** 2 heures

## Consignes

Le code fourni dans ce dépôt ne fonctionne pas correctement de façon
multi-thread. En fait, l'interface graphique (Tkinter) se fige pendant
l'exécution de la tâche longue. Cela est dû au fait que la tâche longue est
exécutée dans le même thread que l'interface graphique, ce qui empêche cette
dernière de se mettre à jour.

Votre tâche consiste donc à :

1. Faire une duplication (Fork) du dépôt dans votre compte GitHub.
2. Corriger le code pour qu'il fonctionne correctement de façon multi-thread. Vous pouvez
   ajouter des classes ou modifier les classes existantes.
3. À la fin des deux heures, faire une pull request vers le dépôt original. Ce
   code ne sera pas évalué, mais il permettra au professeur de fournir une
   rétroaction.

Cet exercice est complexe. N'hésitez pas à réfléchir en équipe et à
demander de l'aide au professeur ou à votre IA préférée.

## Comment exécuter le code fourni

Vous pouvez exécuter le code fourni en utilisant uv avec la commande suivante :

```bash
uv run main
```