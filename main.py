# Desarrollo de aplicaciones básicas de DSP usando IA
# Codigo generado por iA a partir de prompt de profesor Vic.

from arduino.app_utils import *
import time
import math

# Configuraciones de la señal
INCREMENT = 0.1
STEPS_PER_CYCLE = int((2 * math.pi) / INCREMENT)

def loop():
    print(f"--- Iniciando nuevo ciclo de señal ({time.ctime()}) ---")
    
    # Iteramos exactamente los pasos que componen un ciclo
    for i in range(STEPS_PER_CYCLE + 1):
        # Solicitamos el dato al MCU vía Router Bridge
        val = Bridge.call("get_sine_value")
        
        # Formateamos la salida para ver la "curva" en consola (opcional)
        visual_bar = " " * int((val + 1) * 20) + "*"
        print(f"Val: {val:2.4f} | {visual_bar}")
        
        time.sleep(0.05) # Pequeño delay para no saturar el buffer
    
    print("\nCiclo completado. Esperando 15 segundos...")
    time.sleep(15)

# Ejecutamos la App
App.run(user_loop=loop)
