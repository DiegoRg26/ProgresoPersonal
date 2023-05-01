package com.mycompany.listandjframe;

public class Persona {
    private String Nombre;
    private String Apedillo;
    private int edad;
    private int nhijos;

    public Persona(String Nombre, String Apellido, int edad, int nhijos) {
        if (Nombre == "" & Apellido == "" & edad <= 0){
            this.Nombre = "Nn";
            this.Apedillo = "Nn";
            this.edad = 1;
            this.nhijos = nhijos;
        }else{
            if (Nombre == "" & Apellido == ""){
                this.Nombre = "Nn";
                this.Apedillo = "Nn";
                this.edad = edad;
                this.nhijos = nhijos;
            }else{
                if (Nombre == "" & edad <= 0){
                    this.Nombre = "Nn";
                    this.Apedillo = Apellido;
                    this.edad = 1;
                    this.nhijos = nhijos;
                }else{
                    if (Apellido == "" & edad <= 0){
                        this.Nombre = Nombre;
                        this.Apedillo = "Nn";
                        this.edad = 1;
                        this.nhijos = nhijos;
                    }else{
                        if (Nombre == ""){
                            this.Nombre = "Nn";
                            this.Apedillo = Apellido;
                            this.edad = edad;
                            this.nhijos = nhijos;                        
                        }else{
                            if (Apellido == ""){
                                this.Nombre = Nombre;
                                this.Apedillo = "Nn";
                                this.edad = edad;
                                this.nhijos = nhijos;                            
                            }else{
                                if(edad <= 0){
                                    this.Nombre = Nombre;
                                    this.Apedillo = Apellido;
                                    this.edad = 1;
                                    this.nhijos = nhijos;
                                }else{
                                    this.Nombre = Nombre;
                                    this.Apedillo = Apellido;
                                    this.edad = edad;
                                    this.nhijos = nhijos;  
                                }
                            }
                        }
                    }
                }
            }
        }
    }        
    public Persona(String Nombre, String Apellido, int edad) {
        if (Nombre == "" & Apellido== "" & edad <= 0){
            this.Nombre = "Nn";
            this.Apedillo = "Nn";
            this.edad = 1;
        }else{
            if(Nombre == "" & Apellido == ""){
                this.Nombre = "Nn";
                this.Apedillo = "Nn";
                this.edad = edad;
            }else{
                if (Nombre == "" & edad <= 0){
                    this.Nombre = "Nn";
                    this.Apedillo = Apellido;
                    this.edad = 1;                
                }else{
                    if(Apellido == "" & edad <= 0){
                        this.Nombre = Nombre;
                        this.Apedillo = "Nn";
                        this.edad = 1;
                    }else{
                        if (Nombre == ""){
                            this.Nombre = "Nn";
                            this.Apedillo = Apellido;
                            this.edad = edad;
                        }else{
                            if (Apellido == ""){
                                this.Nombre = Nombre;
                                this.Apedillo = "Nn";
                                this.edad = edad;
                            }else{
                                if (edad <= 0){
                                    this.Nombre = Nombre;
                                    this.Apedillo = Apellido;
                                    this.edad = 1;
                                }else{
                                    this.Nombre = Nombre;
                                    this.Apedillo = Apellido;
                                    this.edad = edad;
                                }
                            }
                        }   
                    }
                }
            }
        }        
    }        
    public Persona(String Nombre, int edad, int nhijos) {
        if (Nombre == "" & edad == 0){
            this.Nombre = "Nn";
            this.Apedillo = "Nn";
            this.edad = 1;
            this.nhijos = nhijos;
        }else{
            if(Nombre == ""){
                this.Nombre = "Nn";
                this.Apedillo = "Nn";
                this.edad = edad;
                this.nhijos = nhijos;  
            }else{
                if(edad <= 0){
                    this.Nombre = Nombre;
                    this.Apedillo = "Nn";
                    this.edad = 1;
                    this.nhijos = nhijos;
                }else{
                    this.Nombre = Nombre;
                    this.Apedillo = "Nn";
                    this.edad = edad;
                    this.nhijos = nhijos;
                }
            }
        }
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public String getApedillo() {
        return Apedillo;
    }

    public void setApedillo(String Apedillo) {
        this.Apedillo = Apedillo;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public int getNhijos() {
        return nhijos;
    }

    public void setNhijos(int nhijos) {
        this.nhijos = nhijos;
    }
    public Persona() {}
    
    @Override
    public String toString() {
        return "nombre:"+ " " + Nombre + " / " +"Apellido:" + " " + Apedillo +" / "+ "edad:" +" "+ edad + " / " + "Cantidad de hijos:"+ " " + nhijos;
    }   
}