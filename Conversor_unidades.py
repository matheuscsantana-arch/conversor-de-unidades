# Bibliotecas
import os

# Contantes

# Gravidade da terra padrão
G = 9.80665

# Fatores de conversão para unidades de COMPRIMENTO
FATOR_MILIMETROS_PARA_METROS = 1/1000
FATOR_CENTIMETROS_PARA_METROS = 1/100
FATOR_QUILOMETROS_PARA_METROS = 1000
FATOR_POLEGADAS_PARA_METROS = 25.4*FATOR_MILIMETROS_PARA_METROS
FATOR_PES_PARA_METROS = 12*FATOR_POLEGADAS_PARA_METROS

# Fatores de conversão para unidades de MASSA
FATOR_GRAMAS_PARA_QUILOGRAMAS = 1/1000
FATOR_LIBRAS_PARA_QUILOGRAMAS = 0.45359237

# Fatores de conversão para unidades de FORÇA
FATOR_KGF_PARA_NEWTONS = 1*G
FATOR_LBF_PARA_NEWTONS = FATOR_LIBRAS_PARA_QUILOGRAMAS*G

# Fatores de conversão para unidades de TEMPO
FATOR_MINUTOS_PARA_SEGUNDOS = 60
FATOR_HORA_PARA_SEGUNDOS = 60*FATOR_MINUTOS_PARA_SEGUNDOS
FATOR_MILISEGUNDOS_PARA_SEGUNDOS = 1/1000

# Fatores de conversão para unidades de VELOCIDADE
FATOR_KM_POR_HORA_PARA_METROS_POR_SEGUNDO = FATOR_QUILOMETROS_PARA_METROS/FATOR_HORA_PARA_SEGUNDOS
FATOR_MILHAS_POR_HORA_PARA_METROS_POR_SEGUNDO = 1.609344*FATOR_KM_POR_HORA_PARA_METROS_POR_SEGUNDO

# Fatores de conversão para unidades de ENERGIA
FATOR_CALORIAS_PARA_JOULES = 4.184
FATOR_BTU_PARA_JOULES = 1055.05585

# Fatores de conversão para unidade de POTÊNCIA
FATOR_CV_PARA_WATTS = 735.49875
FATOR_HP_PARA_WATTS = 745.699872
FATOR_BTU_POR_HORA_PARA_WATTS = FATOR_BTU_PARA_JOULES/FATOR_HORA_PARA_SEGUNDOS

# Funções

def converter_para_metros(opcao,unidade):

    unidade_convertida = float(unidade)
    match opcao:
        case "mm":
            resultado = unidade_convertida*FATOR_MILIMETROS_PARA_METROS
            return resultado
        
        case "cm":
            resultado = unidade_convertida*FATOR_CENTIMETROS_PARA_METROS
            return resultado
        
        case "km":
            resultado = unidade_convertida*FATOR_QUILOMETROS_PARA_METROS
            return resultado
        
        case "in":
            resultado = unidade_convertida*FATOR_POLEGADAS_PARA_METROS
            return resultado
        
        case "ft":
            resultado = unidade_convertida*FATOR_PES_PARA_METROS
            return resultado
        
        case _:
            print("Unidade inválida")
            return "Unidade inválida"
        
def converter_para_newtons(opcao,unidade):
    
    unidade_convertida = float(unidade)
    match opcao:
        case "kgf":
            resultado = unidade_convertida*FATOR_KGF_PARA_NEWTONS
            return resultado
        
        case "lbf":
            resultado = unidade_convertida*FATOR_LBF_PARA_NEWTONS
            return resultado
                
        case _:
            print("Unidade inválida")
            return "Unidade inválida"

def converter_para_quilogramas(opcao,unidade):
    
    unidade_convertida = float(unidade)
    match opcao:
        case "g":
            resultado = unidade_convertida*FATOR_GRAMAS_PARA_QUILOGRAMAS
            return resultado
        
        case "lb":
            resultado = unidade_convertida*FATOR_LIBRAS_PARA_QUILOGRAMAS
            return resultado
                
        case _:
            print("Unidade inválida")
            return "Unidade inválida"

def converter_para_segundos(opcao,unidade):
    
    unidade_convertida = float(unidade)
    match opcao:
        case "h":
            resultado = unidade_convertida*FATOR_HORA_PARA_SEGUNDOS
            return resultado
        
        case "min":
            resultado = unidade_convertida*FATOR_MINUTOS_PARA_SEGUNDOS
            return resultado
        
        case "ms":
            resultado = unidade_convertida*FATOR_MILISEGUNDOS_PARA_SEGUNDOS
            return resultado
                
        case _:
            print("Unidade inválida")
            return "Unidade inválida"

def converter_para_metros_por_segundo(opcao,unidade):
    
    unidade_convertida = float(unidade)
    match opcao:
        case "km/h":
            resultado = unidade_convertida*FATOR_KM_POR_HORA_PARA_METROS_POR_SEGUNDO
            return resultado
        
        case "mph":
            resultado = unidade_convertida*FATOR_MILHAS_POR_HORA_PARA_METROS_POR_SEGUNDO
            return resultado
                        
        case _:
            print("Unidade inválida")
            return "Unidade inválida"

def converter_para_joules(opcao,unidade):
    
    unidade_convertida = float(unidade)
    match opcao:
        case "BTU":
            resultado = unidade_convertida*FATOR_BTU_PARA_JOULES
            return resultado
        
        case "cal":
            resultado = unidade_convertida*FATOR_CALORIAS_PARA_JOULES
            return resultado
                        
        case _:
            print("Unidade inválida")
            return "Unidade inválida"

def converter_para_watts(opcao,unidade):
    
    unidade_convertida = float(unidade)
    match opcao:
        case "BTU/h":
            resultado = unidade_convertida*FATOR_BTU_POR_HORA_PARA_WATTS
            return resultado
        
        case "cv":
            resultado = unidade_convertida*FATOR_CV_PARA_WATTS
            return resultado
        
        case "hp":
            resultado = unidade_convertida*FATOR_HP_PARA_WATTS
            return resultado
                        
        case _:
            print("Unidade inválida")
            return "Unidade inválida"


# Início do programa

# Variável de controle do menu
sair = False

while not sair:
    
    print("------------------------MENU------------------------")
    print("1 - Converter unidades de comprimento para metros")
    print("2 - Converter unidades de massa para gramas")
    print("3 - Converter unidades de tempo para segundos")
    print("4 - Converter unidades de velocidade para m/s")
    print("5 - Converter unidades de força para Newtons")
    print("6 - Converter unidades de energia para Joules")
    print("7 - Converter unidades de potência para Watts")
    print("8 - Sair")

    # Opção do menu principal escolhida pelo usuário
    opcao_menu_principal = input("Escolha uma opção: ")

    match opcao_menu_principal:

        case "1":
            # Comando para limpar o terminal (cls - windows("nt"), clear - linux/OS("posix")
            os.system("cls" if os.name == "nt" else "clear")
            print(24*"-" + "MENU" + 24*"-")
            print("Milímetros - mm")
            print("Centímetros - cm")
            print("Quilômetros - km")
            print("Polegadas - in")
            print("Pés - ft")

            # Unidade escolhida pelo usuário para ser convertida
            opcao_sub_menu = input("Escolha a sigla da unidade que você quer converter: ")
            print(52*"-")

            # Trocando vírgula por ponto
            unidade = input("Digite o valor da unidade: ").replace(",",".")

            # Trecho para garantir que o input pode ser convertido para float
            try:
                resultado = converter_para_metros(opcao_sub_menu,unidade)
                if(resultado != "Unidade inválida"):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f'{unidade} {opcao_sub_menu} = {resultado:.5f} m')
            
            except ValueError:
                print("Valor inválido!")

        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            print(24*"-" + "MENU" + 24*"-")
            print("Gramas - g")
            print("Libras - lb")
            opcao_sub_menu = input("Escolha a sigla da unidade que você quer converter: ")
            print(52*"-")
            unidade = input("Digite o valor da unidade: ").replace(",",".")

            try:
                resultado = converter_para_quilogramas(opcao_sub_menu,unidade)
                if(resultado != "Unidade inválida"):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f'{unidade} {opcao_sub_menu} = {resultado:.5f} kg')
            
            except ValueError:
                print("Valor inválido!")

        case "3":
            os.system("cls" if os.name == "nt" else "clear")
            print(24*"-" + "MENU" + 24*"-")
            print("Horas - h")
            print("Minutos - min")
            print("Milissegundos - ms")
            opcao_sub_menu = input("Escolha a sigla da unidade que você quer converter: ")
            print(52*"-")
            unidade = input("Digite o valor da unidade: ").replace(",",".")

            try:
                resultado = converter_para_segundos(opcao_sub_menu,unidade)
                if(resultado != "Unidade inválida"):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f'{unidade} {opcao_sub_menu} = {resultado:.5f} s')
            
            except ValueError:
                print("Valor inválido!")

        case "4":
            os.system("cls" if os.name == "nt" else "clear")
            print(24*"-" + "MENU" + 24*"-")
            print("Quilômetros por hora - km/h")
            print("Milhas por hora - mph")
            opcao_sub_menu = input("Escolha a sigla da unidade que você quer converter: ")
            print(52*"-")
            unidade = input("Digite o valor da unidade: ").replace(",",".")

            try:
                resultado = converter_para_metros_por_segundo(opcao_sub_menu,unidade)
                if(resultado != "Unidade inválida"):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f'{unidade} {opcao_sub_menu} = {resultado:.5f} m/s')
            
            except ValueError:
                print("Valor inválido!")

        case "5":
            os.system("cls" if os.name == "nt" else "clear")
            print(24*"-" + "MENU" + 24*"-")
            print("Quilograma-força - kgf")
            print("Libra-força - lbf")
            opcao_sub_menu = input("Escolha a sigla da unidade que você quer converter: ")
            print(52*"-")
            unidade = input("Digite o valor da unidade: ").replace(",",".")

            try:
                resultado = converter_para_newtons(opcao_sub_menu,unidade)
                if(resultado != "Unidade inválida"):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f'{unidade} {opcao_sub_menu} = {resultado:.5f} N')
            
            except ValueError:
                print("Valor inválido!")

        case "6":
            os.system("cls" if os.name == "nt" else "clear")
            print(24*"-" + "MENU" + 24*"-")
            print("British Thermal Unit - BTU")
            print("Calorias - cal")
            opcao_sub_menu = input("Escolha a sigla da unidade que você quer converter: ")
            print(52*"-")
            unidade = input("Digite o valor da unidade: ").replace(",",".")

            try:
                resultado = converter_para_joules(opcao_sub_menu,unidade)
                if(resultado != "Unidade inválida"):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f'{unidade} {opcao_sub_menu} = {resultado:.5f} J')
            
            except ValueError:
                print("Valor inválido!")

        case "7":
            os.system("cls" if os.name == "nt" else "clear")
            print(24*"-" + "MENU" + 24*"-")
            print("British Thermal Unit por hora - BTU/h")
            print("Cavalo-vapor - cv")
            print("Horsepower - hp")
            opcao_sub_menu = input("Escolha a sigla da unidade que você quer converter: ")
            print(52*"-")
            unidade = input("Digite o valor da unidade: ").replace(",",".")

            try:
                resultado = converter_para_watts(opcao_sub_menu,unidade)
                if(resultado != "Unidade inválida"):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f'{unidade} {opcao_sub_menu} = {resultado:.5f} W')
            
            except ValueError:
                print("Valor inválido!")

        case "8":
            print("PROGRAMA ENCERRADO!")
            sair = True

        case _:
            print("Opção inválida!")