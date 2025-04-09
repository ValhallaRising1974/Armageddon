"""
GREEDY – A COBIÇA ENCARNADA
Simulação de mecânica de buff e penalidade
Autor: Marcelo
"""

import random

class Greedy:
    def __init__(self):
        self.buff_gold = True
        self.buff_value = random.randint(300, 500)  # ouro concedido
        self.tentacle_hit = False

    def atacar(self):
        ataques = ["Moedas Douradas", "Pedras Preciosas", "Tentáculos Sombrios"]
        return random.choice(ataques)

    def aplicar_tentaculo(self, jogador):
        jogador["ouro_bonus"] = 0
        self.tentacle_hit = True
        return f"{jogador['nome']} perdeu o buff de ouro!"

    def derrotada(self, jogador):
        if not self.tentacle_hit:
            jogador["ouro_bonus"] += self.buff_value
            return f"{jogador['nome']} recebeu {self.buff_value} de ouro bônus!"
        else:
            return f"{jogador['nome']} não recebeu bônus devido ao tentáculo!"

# Exemplo de uso
if __name__ == "__main__":
    jogador = {"nome": "Herald1", "ouro_bonus": 0}
    boss = Greedy()
    print("Ataque de Greedy:", boss.atacar())
    print(boss.aplicar_tentaculo(jogador))
    print(boss.derrotada(jogador))
