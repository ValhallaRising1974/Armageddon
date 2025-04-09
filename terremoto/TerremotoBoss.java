// TERREMOTO – A MONTANHA QUE GRITA
// Simulação de buff de defesa após derrota
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

public class Terremoto {
    int buffDuration = 360; // 6 minutos

    public String derrotadoPor(Jogador j) {
        HashMap<String, String> buff = new HashMap<>();
        buff.put("nome", "Proteção de Terremoto");
        buff.put("vida_total", "+15%");
        buff.put("armadura", "+25%");
        buff.put("tempo_restante", buffDuration + "s");

        j.buffs.add(buff);
        return j.nome + " recebeu o buff de Terremoto por 6 minutos.";
    }

    public static void main(String[] args) {
        Jogador j = new Jogador("Herald3");
        Terremoto boss = new Terremoto();
        System.out.println(boss.derrotadoPor(j));
        System.out.println("Buffs ativos: " + j.buffs);
    }
}
