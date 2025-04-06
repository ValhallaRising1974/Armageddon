# 🌺 Événement Armaggeddon – Primaveril, la Déesse Corrompue

Ce dépôt contient les fichiers de l’événement spécial **Armaggeddon** de *Valhalla Rising – The Parchment*, mettant en vedette l'entité Primaveril. Il comprend du code en Python et Java, une documentation multilingue et des mécaniques uniques.

---

## 📁 Contenu

- `primaveril_system.py` – Implémentation Python avec système de vote, pause du PvP et activation des buffs.
- `PrimaverilSystem.java` – Implémentation équivalente en Java.
- `lore_pt-br.md`, `lore_en.md`, `lore_fr.md` – Histoire complète de Primaveril dans trois langues.

---

## ⚙️ Instructions Techniques

### Python

```bash
python3 primaveril_system.py
```

### Java

```bash
javac PrimaverilSystem.java
java GameSimulation
```

---

## 🧠 Mécaniques de l’Événement

- Primaveril apparaît aléatoirement dans l’un des lacs de la jungle.
- Un message audio est envoyé pour voter.
- Si la majorité accepte :
  - Le PvP est suspendu.
  - Les deux équipes combattent ensemble Primaveril.
  - Après la victoire, les joueurs doivent retourner à la base pour activer le buff.
  - Le PvP reprend ensuite.
- Le buff dure **3 minutes** et accorde :
  - + Dégâts Physiques
  - + Dégâts Magiques
  - + Vitesse d’Attaque

---

**Créé par Marcelo**  
🗓️ 7 juillet 2017  
📌 Ajouté au dépôt le 6 avril 2025
