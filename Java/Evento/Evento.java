package com.mycompany.aula20250423.setevento;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Evento {
    private String nome;
    Set<Participante> participantes;
    
    public Evento(String nome){
        this.nome = nome;
        this.participantes = new HashSet<>();
    }
    
    public void adicionarParticipante(Participante p){

        boolean retorno = participantes.add(p); 
        if(retorno == true){
            System.out.println("Participante adicionado!");
        }else{
            System.out.println("Part. já cadastrado");
        }   
    }
    
    public void removerParticipante(Participante p){
        boolean retorno = participantes.remove(p); 
        if(retorno == true){
            System.out.println("Participante removido!");
        }else{
            System.out.println("Part. não encontrado");
        }      
    }
    
    public void imprimir(){
        if(participantes.isEmpty()){
            System.out.println("Evento vazio.");
        }else{
            System.out.println("Evento: "+this.nome);
            for(Participante temp: participantes){
                System.out.println(temp);
            }
        }
    }
    
    
    
}
