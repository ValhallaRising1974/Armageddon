"""
INFERNO – A PLATAFORMA DA PERDIÇÃO
Simulação de buff temporário de dano ígneo e penetração mágica
Autor: Marcelo
"""

import time

class Inferno:
    def __init__(self):
        self.buff_duration = 300  # 5 minutos em segundos
        self.buff_active = False

    def derrotado_por(self, jogador):
        jogador["buffs"].append({
            "nome": "Fúria de Inferno",
            "dano_igneo": "+20%",
            "penetracao_magica": "+15%",
            "tempo_restante": self.buff_duration
        })
        self.buff_active = True
        return f"{jogador['nome']} recebeu o buff de Inferno por 5 minutos."

# Simulação de jogador
if __name__ == "__main__":
    jogador = {"nome": "Herald2", "buffs": []}
    boss = Inferno()
    print(boss.derrotado_por(jogador))
    print("Buffs ativos:", jogador["buffs"])
