// Java – Armageddon System with Buff Activation and PvP Pause

class Player {
    String name;
    boolean hasBuff = false;
    boolean atBase = false;

    public Player(String name) {
        this.name = name;
    }

    public void returnToBase() {
        this.atBase = true;
        activateBuff();
    }

    public void activateBuff() {
        if (atBase) {
            hasBuff = true;
            System.out.println(name + " has activated the buff!");
        }
    }
}

class PvPManager {
    boolean pvpActive = true;

    public void pausePvp() {
        pvpActive = false;
        System.out.println("PvP is now paused.");
    }

    public void resumePvp() {
        pvpActive = true;
        System.out.println("PvP has resumed.");
    }

    public void sendAudioMessage() {
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
