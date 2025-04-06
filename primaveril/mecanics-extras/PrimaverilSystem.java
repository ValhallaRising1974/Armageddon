// PrimaverilSystem.java
// Evento Armaggeddon - Sistema com pausa de PvP, votação e ativação de buff
// Criado por Marcelo | Valhalla Rising – The Parchment

class Player {
    String name;
    boolean hasBuff = false;  // Indica se o jogador já ativou o buff
    boolean atBase = false;   // Indica se o jogador retornou à base

    public Player(String name) {
        this.name = name;
    }

    public void returnToBase() {
        this.atBase = true;
        activateBuff();
    }

    public void activateBuff() {
        // Ativa o buff quando o jogador retorna à base
        if (atBase) {
            hasBuff = true;
            System.out.println(name + " has activated the buff!");
        }
    }
}

class PvPManager {
    boolean pvpActive = true;  // Estado atual do PvP

    public void pausePvp() {
        pvpActive = false;
        System.out.println("PvP is now paused.");
    }

    public void resumePvp() {
        pvpActive = true;
        System.out.println("PvP has resumed.");
    }

    public void sendAudioMessage() {
        // Simula o envio de mensagem de áudio para votação
        System.out.println("[AUDIO] Une géante Armaggeddon est apparue. Voulez-vous l'affronter ? Votez maintenant !");
    }
}

public class GameSimulation {
    public static void main(String[] args) {
        PvPManager pvp = new PvPManager();
        Player[] players = { new Player("Herald 1"), new Player("Herald 2") };

        int voteTeam1 = 3;
        int voteTeam2 = 2;

        pvp.sendAudioMessage();
        if (voteTeam1 >= 3 || voteTeam2 >= 3) {
            // Caso a maioria aceite o combate
            pvp.pausePvp();
            System.out.println("Buff will be available after returning to base.");
            for (Player p : players) {
                p.returnToBase();
            }
            pvp.resumePvp();
        } else {
            System.out.println("Teams declined the encounter. PvP continues normally.");
        }
    }
}
