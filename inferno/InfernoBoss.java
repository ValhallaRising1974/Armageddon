// INFERNO – A PLATAFORMA DA PERDIÇÃO
// Simulação de buff temporário após derrota
// Autor: Marcelo

import java.util.ArrayList;
import java.util.HashMap;

class Jogador {
    String nome;
    ArrayList<HashMap<String, String>> buffs = new ArrayList<>();

    public Jogador(String nome) {
        this.nome = nome;
    }
}

public class Inferno {
    int buffDuration = 300; // 5 minutos
    boolean buffActive = false;

    public String derrotadoPor(Jogador j) {
        HashMap<String, String> buff = new HashMap<>();
        buff.put("nome", "Fúria de Inferno");
        buff.put("dano_igneo", "+20%");
        buff.put("penetracao_magica", "+15%");
        buff.put("tempo_restante", buffDuration + "s");

        j.buffs.add(buff);
        buffActive = true;

        return j.nome + " recebeu o buff de Inferno por 5 minutos.";
    }

    public static void main(String[] args) {
        Jogador j = new Jogador("Herald2");
        Inferno boss = new Inferno();
        System.out.println(boss.derrotadoPor(j));
        System.out.println("Buffs ativos: " + j.buffs);
    }
}
