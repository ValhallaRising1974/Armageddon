// ElsbethySystem.java
// Evento Armageddon – Elsbethy, a Bruxa Esquelética Gigante
// Criado por Marcelo dos Santos Prado

class Elsbethy {
    int hp = 8000;
    int dps = 1500;
    boolean channeling = false;

    void castCurse() {
        // PT: Canaliza maldição (vulnerável)
        // EN: Channels curse (vulnerable)
        // FR: Canalise la malédiction (vulnérable)
        channeling = true;
        System.out.println("Elsbethy is channeling a curse!");
    }

    void summonBoneStorm() {
        // PT: Invoca redemoinhos flamejantes
        // EN: Summons flaming bone storms
        // FR: Invoque des tempêtes d’os
        System.out.println("Elsbethy summons a burning bone storm!");
    }

    void takeDamage(int dmg) {
        if (channeling) {
            hp -= dmg;
            System.out.println("Elsbethy takes " + dmg + " damage! Current HP: " + hp);
        } else {
            System.out.println("Elsbethy is immune! Not in channeling phase.");
        }
    }

    boolean isDefeated() {
        return hp <= 0;
    }
}

class Team {
    boolean speedBuff = false;

    void receiveBuff() {
        // PT: Ganha buff de velocidade
        // EN: Gains speed buff
        // FR: Reçoit un bonus de vitesse
        speedBuff = true;
        System.out.println("Team has received the movement speed buff!");
    }
}

public class ElsbethySystem {
    public static void main(String[] args) {
        Elsbethy elsbethy = new Elsbethy();
        Team team = new Team();

        elsbethy.summonBoneStorm();
        elsbethy.takeDamage(1000); // Imune
        elsbethy.castCurse();
        elsbethy.takeDamage(3000);
        elsbethy.takeDamage(5000);

        if (elsbethy.isDefeated()) {
            team.receiveBuff();
        }
    }
}
