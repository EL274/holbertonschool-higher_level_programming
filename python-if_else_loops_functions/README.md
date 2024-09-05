# Projet Python - Structures de contrôle

Ce projet montre l'utilisation des instructions conditionnelles (`if/else`), des boucles et des fonctions en Python. L'objectif est de présenter des exemples simples et efficaces pour illustrer ces concepts fondamentaux.

## Prérequis

- Python 3.x doit être installé sur votre machine.
- Un éditeur de texte (VSCode, PyCharm, Sublime Text, etc.) ou un IDE pour exécuter le code Python.

## Contenu

### 1. Conditions `if/else`

Le bloc `if/else` permet de prendre des décisions dans le programme en fonction des conditions.

Exemple :
```python
x = 10
if x > 5:
    print("x est supérieur à 5")
else:
    print("x est inférieur ou égal à 5")
```

### 2. Boucles

Les boucles permettent de répéter une série d'instructions jusqu'à ce qu'une condition soit remplie.

#### Boucle `for`

La boucle `for` est utilisée pour itérer sur une séquence (liste, tuple, chaîne, etc.).

Exemple :
```python
for i in range(5):
    print(i)
```

#### Boucle `while`

La boucle `while` continue tant qu'une condition reste vraie.

Exemple :
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 3. Fonctions

Les fonctions permettent de regrouper du code réutilisable et de le rendre plus modulaire.

Exemple :
```python
def addition(a, b):
    return a + b

resultat = addition(5, 3)
print(resultat)  # Affiche 8
```

## Exécution du projet

1. Clonez le projet ou copiez les exemples de code.
2. Ouvrez un terminal.
3. Exécutez le script avec la commande :
   ```
   python nom_du_script.py
   ```

## Contributions

Les contributions sont les bienvenues. N'hésitez pas à proposer des améliorations ou des corrections via des pull requests.

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer.

---

Cela offre un aperçu simple et fonctionnel des éléments que tu veux couvrir.
