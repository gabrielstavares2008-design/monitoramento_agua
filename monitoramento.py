from colorama import Fore, Style, init

# Inicializa o colorama com autoreset ativado
# (restaura o estilo padrão do terminal automaticamente após cada print)
init(autoreset=True)

# Lista com as informações dos níveis do reservatório
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
]

def obter_mensagem_formatada(nivel_info):
    """
    Retorna a mensagem formatada com a cor correspondente ao nível informado.
    """
    cor = nivel_info["cor"]
    nivel = nivel_info["nivel"]
    situacao = nivel_info["situacao"]
    
    return f"{cor}[Nível {nivel}] Situação do Reservatório: {situacao}"

def simular_monitoramento():
    """
    Simula a exibição dos níveis do reservatório no terminal.
    """
    print("=== SISTEMA DE MONITORAMENTO DE NÍVEL DE ÁGUA ===\n")
    
    for item in niveis_reservatorio:
        mensagem = obter_mensagem_formatada(item)
        print(mensagem)
        
    print("\n================================================")

if __name__ == "__main__":
    simular_monitoramento()
