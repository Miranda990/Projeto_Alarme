from datetime import datetime
import time


hora_alarme = input("Qual o horário do alarme?\n")

hora_atual = datetime.now().strftime("%H:%M")


while True:
    
        print("Hora Atual", hora_atual)
    
        if hora_atual == hora_alarme:
            print("HORA DE ACORDAR MEU PATRÃO")
            print('\a')
            print('\a')
            print('\a')
            break
        
        time.sleep(1)
