def run():

     persona = 1
     ano_nac = 0
     persona_ano = []
     persona_cumple = []
    
     ano_actual = int(input('Ingrese el año actual: '))
     for i in range (0,3):
            ano_nac = int(input("Ingrese el año de nacimiento de la persona " + str(persona) + ":"))
            persona =persona +1
            persona_ano.append(ano_nac)
            cumple = ano_actual - ano_nac
            persona_cumple.append(cumple)

     print ("cumples de las tres personas: ", persona_cumple) 
if __name__ == "__main__":
    run()