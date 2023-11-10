package com.example.calcolatrice;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    double primoNumero;
    String operazioni;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // creazioni pulsanti numeri, operazioni e controllo
        Button num0 = findViewById(R.id.num0);
        Button num1 = findViewById(R.id.num1);
        Button num2 = findViewById(R.id.num2);
        Button num3 = findViewById(R.id.num3);
        Button num4 = findViewById(R.id.num4);
        Button num5 = findViewById(R.id.num5);
        Button num6 = findViewById(R.id.num6);
        Button num7 = findViewById(R.id.num7);
        Button num8 = findViewById(R.id.num8);
        Button num9 = findViewById(R.id.num9);

        Button on = findViewById(R.id.on);
        Button off = findViewById(R.id.off);
        Button ac = findViewById(R.id.ac);
        Button del = findViewById(R.id.del);
        Button point = findViewById(R.id.point);
        Button equal = findViewById(R.id.equal);

        Button piu = findViewById(R.id.piu);
        Button meno = findViewById(R.id.meno);
        Button x = findViewById(R.id.x);
        Button div = findViewById(R.id.div);

        TextView screen = findViewById(R.id.screen);

        // set acceso con la visione di 0
        ac.setOnClickListener(view -> {
            primoNumero = 0;
            screen.setText("0");
        });

        // set spento
        off.setOnClickListener(view -> screen.setVisibility(View.GONE));
        on.setOnClickListener(view -> {
            screen.setVisibility((View.VISIBLE));
            screen.setText("0");
        });

        ArrayList<Button> nums = new ArrayList<>();
        nums.add(num0);
        nums.add(num1);
        nums.add(num2);
        nums.add(num3);
        nums.add(num4);
        nums.add(num5);
        nums.add(num6);
        nums.add(num7);
        nums.add(num8);
        nums.add(num9);

        for (Button b : nums) {
            b.setOnClickListener(view -> {
                if (!screen.getText().toString().equals("0")) {
                    screen.setText(screen.getText().toString() + b.getText().toString());
                } else {
                    screen.setText(b.getText().toString());
                }
            });
        }

        ArrayList<Button> opera = new ArrayList<>();
        opera.add(div);
        opera.add(x);
        opera.add(meno);
        opera.add(piu);
        for (Button b : opera) {
            b.setOnClickListener(view -> {
                primoNumero = Double.parseDouble(screen.getText().toString());
                operazioni = b.getText().toString();
                screen.setText("0");
            });
        }

        // impostazione cancellazione ultimo numero
        del.setOnClickListener(view -> {
            String num = screen.getText().toString();
            if (num.length() > 1) {
                screen.setText(num.substring(0, num.length() -1));
            } else if (num.length() == 1 && !num.equals("0")) {
                screen.setText("0");
            }
        });

        // impostazione del punto
        point.setOnClickListener(view -> {
            if (!screen.getText().toString().contains(".")) {
                screen.setText(screen.getText().toString() + ".");
            }
        });

        // calcolo e stampa operazione
        equal.setOnClickListener(view -> {
            double secondoNum = Double.parseDouble(screen.getText().toString());
            double ris;
            switch (operazioni) {
                case "/":
                    ris = primoNumero / secondoNum;
                    break;
                case "X":
                    ris = primoNumero * secondoNum;
                    break;
                case "+":
                    ris = primoNumero + secondoNum;
                    break;
                case "-":
                    ris = primoNumero - secondoNum;
                    break;
                default:
                    ris = primoNumero + secondoNum;
            }
            screen.setText(String.valueOf(ris));
            primoNumero = ris;
        });




    }
}