# 🌺 Armageddon Event – Primaveril, the Corrupted Goddess

This repository contains the special **Armageddon** event files from *Valhalla Rising – The Parchment*, featuring the entity Primaveril. It includes Python and Java code, lore in three languages, and unique mechanics for this encounter.

---

## 📁 Contents

- `primaveril_system.py` – Python implementation with voting, PvP pause, and buff activation systems.
- `PrimaverilSystem.java` – Equivalent implementation in Java.
- `lore_pt-br.md`, `lore_en.md`, `lore_fr.md` – Full lore of Primaveril in three languages.

---

## ⚙️ Technical Instructions

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

## 🧠 Event Mechanics

- Primaveril spawns randomly at one of the jungle lakes.
- The game plays an audio message requesting a vote.
- If the majority agrees to fight:
  - PvP is paused.
  - Both teams join to fight Primaveril.
  - After victory, players must return to base to activate the buff.
  - PvP resumes afterward.
- Buff lasts **3 minutes** and grants:
  - + Physical Damage
  - + Magic Damage
  - + Attack Speed

---

**Created by Marcelo**  
🗓️ July 7, 2017  
📌 Added to repository on April 6, 2025
