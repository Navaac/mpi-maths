# Compilation avec script

## Windows
### Scripts
Le script qui est à utiliser est le fichier `compilation_complet.ps1`, qui permet de compiler à la fois le fichier `chapitre_.tex`, le fichier `cours_.tex` et le fichier `TD_.tex`. 
Lorsque le script est exécuté sans arguments, il compile automatiquement le dernier chapitre.
Sinon, on peut utiliser le paramètre `-chapitres`, auquel on passe la liste des chapitres à compiler. Donc `-chapitres "2, 6"` compilera les chapitres 2 et 6.
On peut également faire `-chapitres "integrale"` ce qui lancera la compilation des fichiers intégrale. Attention, cela prendra plusieurs minutes !

Il est également possible de compiler l'ensemble des chapitres et l'intégrale en utilisant cet argument : `-chapitres "all"`.

Pour les personnes qui ne seraient intéressées que par le fichier `chapitre_.tex`, vous pouvez utiliser le script `compilation_chapitre.ps1` qui compile uniquement ce fichier.

### Chemins

Pour que ces scripts fonctionnent, il faut leur spécifier le chemin absolu vers le dossier contenant les dossier `chapitre_`. Ce paramètre se trouve sur les toutes premières lignes des fichiers. 

De plus, les pdfs générés sont ensuite copiés vers un dossier destination, qu iest à spécifié au même endroit que là où se trouvent les fichiers source. Chacun des pdfs générés seront mis dans un dossier `chapitre_`, avec pour numéro celui du chapitre associé.

### Problèmes d'exécution

Par défaut, windows bloque l'exécution de scripts powershell. Il faut donc l'activer avec cette commande : `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` et vous pouvez ensuite les réactiver si vous le souhaités avec cette commande : `Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser`

## Multi plateformes

Pas encore écrits.