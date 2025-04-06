# primaveril_system.py
# Evento Armaggeddon - Sistema com pausa de PvP, votação e ativação de buff
# Criado por Marcelo | Valhalla Rising – The Parchment

class Player:
    def __init__(self, name):
        self.name = name
        self.has_buff = False  # Indica se o jogador já ativou o buff
        self.at_base = False   # Indica se o jogador retornou à base

    def return_to_base(self):
        self.at_base = True
        self.activate_buff()

    def activate_buff(self):
        # Ativa o buff quando o jogador retorna à base
        if self.at_base:
            self.has_buff = True
            print(f"{self.name} has activated the buff!")

class PvPManager:
    def __init__(self):
        self.pvp_active = True  # Estado atual do PvP

    def pause_pvp(self):
        # Pausa o combate PvP durante o evento
        self.pvp_active = False
        print("PvP is now paused.")

    def resume_pvp(self):
        # Retoma o combate PvP após o evento
        self.pvp_active = True
        print("PvP has resumed.")

    def send_audio_message(self):
        # Simula o envio de mensagem de áudio para votação
        print("[AUDIO] A Gigante Armaggeddon surgiu. Vocês desejam enfrentá-la? Votem agora!")

class GameSimulation:
    def __init__(self):
        self.pvp_manager = PvPManager()
        self.players = [Player("Herald 1"), Player("Herald 2")]

    def armageddon_event(self, vote_team1, vote_team2):
        self.pvp_manager.send_audio_message()
        if vote_team1 >= 3 or vote_team2 >= 3:
            # Caso a maioria aceite o combate
            self.pvp_manager.pause_pvp()
            print("Buff will be available after returning to base.")
            for player in self.players:
                player.return_to_base()
            self.pvp_manager.resume_pvp()
        else:
            print("Teams declined the encounter. PvP continues normally.")

# Execução de simulação
sim = GameSimulation()
sim.armageddon_event(3, 2)
