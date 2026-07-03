## Template 

Normalement j'ai fourni un template qui contient l'arborescence que j'utilisais et que je trouve plutôt pratique pour ne pas avoir des fichiers de compilation partout, et qui permet d'avoir à la fois le cours, le TD, et un mix des deux. Au cas ou l'arborescence ce serait perdue, la voici : 

```
latex/
├── commun
|   ├── images
|   |   └── ampoule.png
|   ├── config.tex
|   ├── prepacours.cls
|   └── raccourcis.sty
├── chapitre1
|   ├── chapitre1.tex
|   ├── cours
|   |   ├── contenu.tex
|   |   └── cours1.tex
|   └── TD 
|       ├── contenu_td.tex
|       └── TD1.tex
|   
└── ...
```

Le fichier `config.tex` contient les métadonnées communes à tous les fichiers, `prepacours.cls` la classe personalisée, et `raccourcis.sty` les raccourcis. L'image `ampoule.png` est utilisée pour les environnements idée. 

Le fichier `chapitre_.tex` contient cela : 
```latex
\documentclass{../commun/prepacours}
\usepackage{../commun/raccourcis}

\input{../commun/config.tex}

\begin{document}
\chapitre{1}{Normes et distances}

\pagedegarde

\input{cours/contenu.tex}

\clearpage
\passerenmodeexos
\input{TD/contenu_td.tex}

\end{document}
```

Le fichier `TD_.tex` (qui utilise une autre classe fonctionnant globalement de la même façon) :
```latex
\documentclass{../../commun/prepacours_TD}
\usepackage{../../commun/raccourcis}

\input{../../commun/config.tex}
\chapitre{1}{TD : Normes et distances}

\begin{document}
\thispagestyle{premierepageschapitre}  % Pour avoir le style spécial en première page

\input{contenu_td.tex}

\end{document}

```

et `cours_.tex` :
```latex
\documentclass{../../commun/prepacours}
\usepackage{../../commun/raccourcis}

\input{../../commun/config.tex}

\begin{document}
\chapitre{1}{Normes et distances}

\pagedegarde

\input{contenu.tex}

\end{document}
```

## Images

Pour les images, celles-ci se trouvent dans le dossier du chapitre l'utilisant. Pour pouvoir compiler l'intégrale, il faut donc copier ces images dans le sous-dossier images du dossier `integrale`.
