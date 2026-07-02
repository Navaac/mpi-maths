# Création de cartes anki

Le principe de ce script est de créer des cartes anki directement à partir des sources LaTeX, en extrayant les propositions, définitions, théorèmes, ...
Le script va générer un fichier .txt, qui pourra ensuite être importé directement dans anki.

## Type de notes

Pour que tout fonctionne correctement, j'utilise un type de notes personnalisé, appelé `maths`. Pour importer ce type de notes, ce que vous devez obligatoirement faire avant toute autre chose la première fois, ajoutez ce greffon à votre anki : `1513387587`, que vous pouvez trouver [ici](https://ankiweb.net/shared/info/1513387587).
Une fois le greffon installé et anki redémarré, allez dans `outils` puis `import note type` et importer le fichier `maths_note_type` qui est dans ce dossier.

## Scripts d'extraction

Pour que le script fonctionne, vous devez conserver la même architecture locale des dossiers que celle du repo.
Vous avez alors deux scripts que vous pouvez exécuter. Soit vous appelez `importation_auto.py` auquel cas vous passez en argument directement depuis la ligne de commande ce qu'il doit faire, soit vous utilisez `importation.py`, et là il faut aller rentrer les pramaètres à la fin du fichier, dans la fonction main.

Le backend des deux scripts est identique. 

## Script avec option sur ligne de commande

Lorsque vous appelez le script, il y a donc plusieurs options possibles. La première est `-chapitre` pour spécifier le chapitre à traiter, qui peut être raccourcie en `-c`.

Il y a ensuite `-o` pour `-offset`, qui spécifie au script les combien premières cartes ne doivent pas être traitées. Donc si le script est appelé avec `-o 10`, les dix premières propositions, définitions, ... (le compteur de dix étant global aux propositions, définition, ...) ne seront pas prises en compte.

Il y a également un paramètre pour activer le mode test `-t` ou `-test`, et qui va lui utiliser le fichier text.tex plutôt qu'un chapitre, et exécuter le script en mode test.


## Fonctionnement du script

Le script fonctionne en plusieurs passes à cause des raccourcies personalisés utilisés, ainsi que des environnements équation dans les fichiers LaTeX. En effet, le script va, dans un premier temps, faire appel à `expand_shortcut_xomplet.py` dont le role sera de créer un fichier LaTeX sans aucun raccourcis, et dans lequel les environnements maths ont été modifiés pour être compatibles avec Anki. Le fichier LaTeX généré peut ne pas compiler, c'est normal.
Il y a toutefois un point de vigilance : le script de suppression des raccourcis n'est pas aussi puissant que LaTeX (il faudrait utiliser des grammaires ou d'autres outils de ce type), et donc lorsqu'un raccourci est utilisé dans un environnement définition, ..., si ses paramètres ne sont pas donnés entre accolades, alors le raccourci ne sera pas modifié et sera donc laissé tel quel dans la carte anki associée.
Je ne sais plus également si le script est récursif, c'est à dire si il remplace les raccourcis utilisés dans des raccourcis, à vérifier.

Une fois ce fichier LaTeX sans raccourcis créé, le script principal reprend la main et va alors extraire les propriétés par section et subsection, afin d'obtenir la même arborescence que celle du cours.

Le titre des propriétés est celui qui est spécifié dans le latex :
```latex
\begin{proposition}{Titre de la proposition}{}
    Contenu de la proposition
\end{proposition}
```

Les doublons sont génrés par le script, donc si deux propositions ont le même titre, le script en modifie un des deux. Cela fonctionne pour `n` propositions ayant le même titre.

De plus le script utilise un système de mémoire. En effet, après chaque exécution il enregistre quelles cartes ont été extraites dans ce chapitre, et la prochaine fois qu'il est appelé sur ce chapitre, il reprend l'extraction où il l'avait arrêtée. Cette fonctionnalité était surtout utile lorsque le cours était en développement. Donc si vous voulez réimporter un chapitre de zéro, pensez bien à supprimer le fichier de sauvegarde.

## Logs

Des fichiers de logs sont créés à chaque exécution du script dans le dossier du paquet associé, pour tracer les nouvelles cartes, ainsi que les cartes créées ou supprimées. 

## Type des cartes

Le type de notes utilisé a un champ `type` dans lequel le script met automatiquement des chaines du genre `Proposition 5.4` comme dans les polys.