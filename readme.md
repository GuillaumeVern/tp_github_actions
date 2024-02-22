# TP Github Actions
### 1. liaison du compte 

la clé ssh est liée a mon compte github
![cle ssh](image.png)

### 2. test du premier workflow github actions

création du fichier .yml de config des actions dans .github/workflows/
puis commit sur un repo github:
![commit](image-1.png)

on peut voir dans l'onglet "actions" que ça fonctionne
![action proof](image-2.png)

### 3. création des classes SimpleMath et TestSimpleMath en python

```py
import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b
    
    @staticmethod
    def soustraction(a, b):
        return a - b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleMath.addition(17, 12) , 29)

    def test_soustraction(self):
        self.assertEqual(SimpleMath.soustraction(8, 2), (6))
```

### 4. push sur github + création du workflow