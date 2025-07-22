"""
🎲 PROJETO 2: JOGO DA ADIVINHAÇÃO

Jogo onde o computador pensa em um número e você tenta adivinhar!
"""

import random

def escolher_dificuldade():
    print("\n🎯 ESCOLHA A DIFICULDADE:")
    print("1. 😊 Fácil (1-10)")
    print("2. 😐 Médio (1-50)")  
    print("3. 😈 Difícil (1-100)")
    
    while True:
        opcao = input("Sua escolha (1-3): ")
        
        if opcao == "1":
            return 10, "Fácil"
        elif opcao == "2":
            return 50, "Médio"
        elif opcao == "3":
            return 100, "Difícil"
        else:
            print("❌ Opção inválida!")

def obter_palpite(maximo):
    while True:
        try:
            palpite = int(input(f"Seu palpite (1-{maximo}): "))
            if 1 <= palpite <= maximo:
                return palpite
            else:
                print(f"❌ Digite um número entre 1 e {maximo}!")
        except ValueError:
            print("❌ Digite um número válido!")

def dar_dica(palpite, numero_secreto, diferenca):
    if diferenca <= 2:
        print("🔥 MUITO QUENTE!")
    elif diferenca <= 5:
        print("🌡️  Quente!")
    elif diferenca <= 10:
        print("❄️  Frio!")
    else:
        print("🧊 MUITO FRIO!")
    
    if palpite < numero_secreto:
        print("📈 Tente um número MAIOR!")
    else:
        print("📉 Tente um número MENOR!")

def calcular_pontuacao(tentativas, maximo):
    if tentativas <= 3:
        return 100
    elif tentativas <= 5:
        return 80
    elif tentativas <= 8:
        return 60
    else:
        return 40

# Jogo principal
def jogar():
    print("🎲" * 20)
    print("   JOGO DA ADIVINHAÇÃO")
    print("🎲" * 20)
    print("🤖 Vou pensar em um número...")
    print("🎯 Sua missão: adivinhar qual é!")
    
    maximo, dificuldade = escolher_dificuldade()
    numero_secreto = random.randint(1, maximo)
    tentativas = 0
    max_tentativas = 10
    
    print(f"\n🎮 Modo: {dificuldade}")
    print(f"🎯 Pensei em um número entre 1 e {maximo}")
    print(f"⏱️  Você tem {max_tentativas} tentativas!")
    print("🔥 Dicas: QUENTE = perto, FRIO = longe")
    
    while tentativas < max_tentativas:
        tentativas += 1
        print(f"\n--- TENTATIVA {tentativas}/{max_tentativas} ---")
        
        palpite = obter_palpite(maximo)
        
        if palpite == numero_secreto:
            pontuacao = calcular_pontuacao(tentativas, maximo)
            print("\n🎉" * 15)
            print("   PARABÉNS! VOCÊ ACERTOU!")
            print(f"🎯 Número secreto: {numero_secreto}")
            print(f"⚡ Tentativas: {tentativas}")
            print(f"⭐ Pontuação: {pontuacao} pontos")
            print("🎉" * 15)
            return True
        
        else:
            diferenca = abs(palpite - numero_secreto)
            dar_dica(palpite, numero_secreto, diferenca)
            print(f"❌ Errou! Restam {max_tentativas - tentativas} tentativas")
    
    # Game Over
    print("\n💀" * 15)
    print("   GAME OVER!")
    print(f"🎯 O número era: {numero_secreto}")
    print("🔄 Tente novamente!")
    print("💀" * 15)
    return False

# Sistema de ranking
def salvar_pontuacao(nome, pontuacao):
    try:
        with open("ranking.txt", "a") as arquivo:
            arquivo.write(f"{nome}: {pontuacao} pontos\n")
    except:
        pass  # Se não conseguir salvar, continua

# Loop principal
print("🎮 BEM-VINDO AO JOGO DA ADIVINHAÇÃO!")
nome_jogador = input("👤 Qual seu nome? ")

while True:
    if jogar():
        print(f"\n🏆 Parabéns, {nome_jogador}!")
    
    jogar_novamente = input("\n🔄 Jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        break

print(f"\n👋 Obrigado por jogar, {nome_jogador}!")
print("🎮 Volte sempre!")

# 🎯 IDEIAS PARA MELHORAR:
# 1. Adicione ranking de melhores jogadores
# 2. Crie modo multiplayer
# 3. Adicione sons ou emojis animados
# 4. Salve estatísticas do jogador
