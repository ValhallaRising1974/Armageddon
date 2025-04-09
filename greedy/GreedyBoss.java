// GREEDY – A COBIÇA ENCARNADA
// Simulação de buff de ouro e penalidade por tentáculos
// Autor: Marcelo

import java.util.Random;

class Jogador {
    String nome;
    int ouroBonus;

    public Jogador(String nome) {
        this.nome = nome;
        this.ouroBonus = 0;
    }
}

public class Greedy {
    boolean buffGold = true;
    int buffValue;
    boolean tentacleHit = false;

    public Greedy() {
        this.buffValue = new Random().nextInt(201) + 300; // 300 a 500
    }

    public String atacar() {
        String[] ataques = {"Moedas Douradas", "Pedras Preciosas", "Tentáculos Sombrios"};
        return ataques[new Random().nextInt(ataques.length)];
    }

    public String aplicarTentaculo(Jogador j) {
        j.ouroBonus = 0;
        tentacleHit = true;
        return j.nome + " perdeu o buff de ouro!";
    }

    public String derrotada(Jogador j) {
        if (!tentacleHit) {
            j.ouroBonus += buffValue;
            return j.nome + " recebeu " + buffValue + " de ouro bônus!";
        } else {
            return j.nome + " não recebeu bônus devido ao tentáculo!";
        }
    }

    public static void main(String[] args) {
        Jogador j = new Jogador("Herald1");
        Greedy boss = new Greedy();

        System.out.println("Ataque de Greedy: " + boss.atacar());
        System.out.println(boss.aplicarTentaculo(j));
        System.out.println(boss.derrotada(j));
    }
}
