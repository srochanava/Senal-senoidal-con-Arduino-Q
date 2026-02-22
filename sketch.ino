// Codigo generado por IA para la generacion de senal sinusoidal en Arduino UNO Q
// a partir de prompt de Prof. Vic. 
// Curso Desarrollo de aplicaciones básicas de DSP usando IA

// Arduino UNO Q cuenta con MPU y con MCU
// realiza la conexion entre MPU (python) y MCU (arduino) mediante RouterBridge

#include "Arduino_RouterBridge.h"
#include <math.h>

float angle = 0.0;
const float increment = 0.1; // Ajusta para cambiar la resolución de la onda

void setup() {
    Bridge.begin();
    // Proveemos la función para que Python pueda obtener el valor actual
    Bridge.provide("get_sine_value", get_sine_value);
}

void loop() {
    // El loop se mantiene vacío porque el Bridge maneja las peticiones
}

float get_sine_value() {
    float val = sin(angle);
    angle += increment;
    
    // Reiniciar el ángulo al completar un ciclo (2 * PI)
    if (angle >= 2 * M_PI) {
        angle = 0;
    }
    return val;
}
