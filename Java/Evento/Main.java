package com.mycompany.aula20250423.setevento;

public class Aula20250423SetEvento {

    public static void main(String[] args) {
        System.out.println("Evento!");
        Evento ev1 = new Evento("Visita tecnica");
        
        Participante p1 = new Participante("Cassio", "cassio@uvv.br");
        Participante p2 = new Participante("Joao", "joao@uvv.br");
        Participante p3 = new Participante("Pedro", "pedro@uvv.br");
        
        Participante p4 = new Participante("Cassio", "cassio@uvv.br");

        
        ev1.adicionarParticipante(p1);
        ev1.adicionarParticipante(p2);
        ev1.adicionarParticipante(p3);
        
        ev1.imprimir();
        
        //ev1.adicionarParticipante(p4);
        
        ev1.removerParticipante(p1);
        ev1.removerParticipante(p1);
        
    }
}
