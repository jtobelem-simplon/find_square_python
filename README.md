# find-square-python


## Pour trouver les carrés dans les cartes du dossier `cartes`
```
chmod +x find_square.py
```

```
./find_square.py cartes/*
```

## Tests et CI/CD
- Le fichier test.py contient des tests pour les méthodes is_valid et is_free de find_square.py.
- Les classes du projet qui héritent de unittest.TestCase sont executées à chaque push ou pull request sur le repository.

[![Run Python Tests](https://github.com/jtobelem-simplon/find_square_python/actions/workflows/test.yml/badge.svg)](https://github.com/jtobelem-simplon/find_square_python/actions/workflows/test.yml)

