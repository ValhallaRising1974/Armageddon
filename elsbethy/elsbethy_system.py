# elsbethy_system.py
# Evento Armageddon – Elsbethy, a Bruxa Esquelética Gigante
# Criado por Marcelo dos Santos Prado

class Elsbethy:
    def __init__(self):
        self.hp = 8000
        self.dps = 1500
        self.channeling = False

    def cast_curse(self):
        # PT: Elsbethy começa a canalizar sua maldição (único momento vulnerável)
        # EN: Elsbethy begins channeling her curse (only vulnerable phase)
        # FR: Elsbethy commence à canaliser sa malédiction (phase de vulnérabilité)
        self.channeling = True
        print("Elsbethy is channeling a curse!")

    def summon_bone_storm(self):
        # PT: Redemoinhos de ossos flamejantes causam dano e lentidão
        # EN: Bone storms cause damage and slow enemies
        # FR: Les tempêtes d’os causent des dégâts et ralentissent les ennemis
        print("Elsbethy summons a burning bone storm!")

    def take_damage(self, dmg):
        if self.channeling:
            self.hp -= dmg
            print(f"Elsbethy takes {dmg} damage! Current HP: {self.hp}")
        else:
            print("Elsbethy is immune! Not in channeling phase.")

    def is_defeated(self):
        return self.hp <= 0

class Team:
    def __init__(self):
        self.movement_speed_buff = False

    def receive_buff(self):
        # PT: Equipe recebe aumento de velocidade por 3 minutos
        # EN: Team receives movement speed buff for 3 minutes
        # FR: L'équipe reçoit un bonus de vitesse pendant 3 minutes
        self.movement_speed_buff = True
        print("Team has received the movement speed buff!")

# Simulação
elsbethy = Elsbethy()
team = Team()

elsbethy.summon_bone_storm()
elsbethy.take_damage(1000)  # Imune
elsbethy.cast_curse()
elsbethy.take_damage(3000)
elsbethy.take_damage(5000)

if elsbethy.is_defeated():
    team.receive_buff()
