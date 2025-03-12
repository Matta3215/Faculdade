package com.mycompany.aula20250312classeteste;

public class Teste {
    public static int quantidade= 0;
    
    public int a;
    public int b;
    private int c;

    public Teste(){
        this.a = 0;
        this.b = 0;
        this.c = 0;
        quantidade++;
    }
    public Teste(int a, int b, int c){
        this.a = a;
        this.b = b;
        this.c = c;
        quantidade++;
    }
    
    public int getC() {
        return c;
    }

    public void setC(int c) {
        this.c = c;
    }

  
    public void ImprimeA(){
        System.out.println(this.a);
    }
    public void ImprimeB(){
        System.out.println(this.b);
    }
    public void ImprimeC(){
        System.out.println(this.c);
    }
    
    public static void Imprimir(){
        System.out.println(quantidade);
    }
}
