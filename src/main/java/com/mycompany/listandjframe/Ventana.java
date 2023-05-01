package com.mycompany.listandjframe;

import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Ventana extends JFrame{

    public Ventana() {
        this.setSize(500,500);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setTitle("Ejercicios de List y JFrame");
        //this.setLocation(100,200);
        //this.setBounds(100, 200, 500, 500);
        this.setLocationRelativeTo(null);
        iniciarcomponenetes();
    }
    private void iniciarcomponenetes(){
        JPanel panel = new JPanel();
        this.getContentPane().add(panel);
    
    }
}
