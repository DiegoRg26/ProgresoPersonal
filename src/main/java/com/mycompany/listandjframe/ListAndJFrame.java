package com.mycompany.listandjframe;

import java.util.List;
import java.util.ArrayList;

public class ListAndJFrame {

    public static void main(String[] args) {
        
        /*
        List<Integer> numeros;
        
        numeros = new ArrayList<>();
        
        numeros.add(1);
        numeros.add(2);
        numeros.add(3);
        numeros.add(4);
        */
        /*
        List<String> Usuarios;
        
        Usuarios = new ArrayList<>();
        
        Usuarios.add("Jose");
        Usuarios.add("Maria");
        Usuarios.add("Daniela");
        Usuarios.add("Alejandro");
        
        System.out.println("La cantidad de elementos de la lista es de: " + Usuarios.size() + "\n");
        
        for (int i = 0; i < Usuarios.size(); i++) {
            System.out.println("\nLa identificacion del usuario numero " + (i+1) + " es: " + Usuarios.get(i));
        }
        */
        
        /*
        List<Persona> Lista_Personas = new ArrayList<>();
        
        Persona p1 = new Persona("Julio","Ramirez",21);
        Persona p2 = new Persona("Daniela","Sanchez",20);
        Persona p3 = new Persona("Alejandro","Roman",19);
        Persona p4 = new Persona("Paula","Escudero",18);
        
        Lista_Personas.add(p1);
        Lista_Personas.add(p2);
        Lista_Personas.add(p3);
        Lista_Personas.add(p4);
        
        System.out.println("Se creo una lista con una cantidad de personas de: " + Lista_Personas.size()+"\n"+"Los nombres y apellidos de estas son: "+"\n");
        
        for (int i = 0; i < Lista_Personas.size(); i++) {
            System.out.println("Datos persona "+ (i+1)+"- Nombre y Apellido: "+ Lista_Personas.get(i).getNombre()+" "+ Lista_Personas.get(i).getApedillo()+" Edad: "+Lista_Personas.get(i).getEdad());
            
        }
        */
        Ventana v1 = new Ventana();
        v1.setVisible(true);
        
        
    }
}
