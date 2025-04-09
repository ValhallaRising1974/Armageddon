"""
TERREMOTO – A MONTANHA QUE GRITA
Simulação de buff defensivo após derrota
Autor: Marcelo
"""

import time

class Terremoto:
    def __init__(self):
        self.buff_duration = 360  # 6 minutos
        self.buff_active = False

    def derrotado_por(self, jogador):
        jogador["buffs"].append({
            "nome": "Proteção de Terremoto",
            "vida_total": "+15%",
            "armadura": "+25%",
            "tempo_restante": self.buff_duration
        })
        self.buff_active = True
        return f"{jogador['nome']} recebeu o buff de Terremoto por 6 minutos."

# Simulação de uso
if __name__ == "__main__":
    jogador = {"nome": "Herald3", "buffs": []}
    boss = Terremoto()
    print(boss.derrotado_por(jogador))
    print("Buffs ativos:", jogador["buffs"])
