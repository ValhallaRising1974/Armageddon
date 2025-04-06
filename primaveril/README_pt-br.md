# 🌺 Evento Armageddon – Primaveril, a Deusa Corrompida

Este repositório contém os arquivos do evento especial **Armageddon** em *Valhalla Rising – The Parchment*, com foco na entidade Primaveril. Inclui códigos em Python e Java, documentação em três idiomas e as mecânicas exclusivas desse evento.

---

## 📁 Conteúdo

- `primaveril_system.py` – Implementação em Python do evento com sistema de votação, pausa de PvP e ativação de buffs.
- `PrimaverilSystem.java` – Implementação equivalente em Java.
- `lore_pt-br.md`, `lore_en.md`, `lore_fr.md` – Lore completa da Primaveril em três idiomas.

---

## ⚙️ Instruções Técnicas

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

## 🧠 Mecânicas do Evento

- Primaveril aparece aleatoriamente em um dos lagos da selva.
- O jogo envia uma mensagem de áudio para as equipes votarem.
- Caso a maioria aceite o combate:
  - O PvP é pausado.
  - Ambas as equipes se unem para enfrentar Primaveril.
  - Após derrotá-la, os jogadores devem retornar à base para ativar o buff.
  - PvP retorna após a ativação.
- O buff dura **3 minutos** e concede:
  - + Dano Físico
  - + Dano Mágico
  - + Velocidade de Ataque

---

**Criado por Marcelo**  
🗓️ 07 de julho de 2017  
📌 Adicionado ao repositório em 06 de abril de 2025
