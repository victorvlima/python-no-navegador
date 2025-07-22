"""
📝 PROJETO 3: ORGANIZADOR DE TAREFAS

Gerencie suas tarefas diárias como um profissional!
"""

import datetime

# Lista global de tarefas
tarefas = []

def mostrar_menu():
    print("\n" + "📝" * 20)
    print("   ORGANIZADOR DE TAREFAS")
    print("📝" * 20)
    print("1. ➕ Adicionar tarefa")
    print("2. 📋 Ver todas as tarefas")
    print("3. ✅ Marcar como concluída")
    print("4. ❌ Remover tarefa")
    print("5. 🔍 Buscar tarefa")
    print("6. 📊 Estatísticas")
    print("7. 💾 Salvar em arquivo")
    print("8. 📂 Carregar do arquivo")
    print("0. �� Sair")
    print("📝" * 20)

def adicionar_tarefa():
    print("\n➕ NOVA TAREFA")
    descricao = input("Descrição: ").strip()
    
    if not descricao:
        print("❌ Descrição não pode estar vazia!")
        return
    
    print("\n🎯 PRIORIDADE:")
    print("1. 🔴 Alta")
    print("2. 🟡 Média") 
    print("3. 🟢 Baixa")
    
    while True:
        opcao = input("Escolha (1-3): ")
        if opcao == "1":
            prioridade = "🔴 Alta"
            break
        elif opcao == "2":
            prioridade = "🟡 Média"
            break
        elif opcao == "3":
            prioridade = "🟢 Baixa"
            break
        else:
            print("❌ Opção inválida!")
    
    tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "prioridade": prioridade,
        "concluida": False,
        "data_criacao": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    
    tarefas.append(tarefa)
    print(f"✅ Tarefa '{descricao}' adicionada com sucesso!")

def ver_tarefas():
    if not tarefas:
        print("\n📭 Nenhuma tarefa encontrada!")
        return
    
    print(f"\n📋 SUAS TAREFAS ({len(tarefas)} total)")
    print("-" * 60)
    
    for tarefa in tarefas:
        status = "✅" if tarefa["concluida"] else "⏳"
        print(f"{tarefa['id']}. {status} {tarefa['descricao']}")
        print(f"   {tarefa['prioridade']} | {tarefa['data_criacao']}")
        print("-" * 60)

def marcar_concluida():
    if not tarefas:
        print("\n📭 Nenhuma tarefa para marcar!")
        return
    
    ver_tarefas()
    
    try:
        id_tarefa = int(input("\nID da tarefa para marcar: "))
        
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                if tarefa["concluida"]:
                    print("⚠️  Tarefa já está concluída!")
                else:
                    tarefa["concluida"] = True
                    print(f"✅ Tarefa '{tarefa['descricao']}' marcada como concluída!")
                return
        
        print("❌ Tarefa não encontrada!")
    
    except ValueError:
        print("❌ Digite um número válido!")

def remover_tarefa():
    if not tarefas:
        print("\n📭 Nenhuma tarefa para remover!")
        return
    
    ver_tarefas()
    
    try:
        id_tarefa = int(input("\nID da tarefa para remover: "))
        
        for i, tarefa in enumerate(tarefas):
            if tarefa["id"] == id_tarefa:
                confirmacao = input(f"❓ Remover '{tarefa['descricao']}'? (s/n): ")
                if confirmacao.lower() == 's':
                    tarefas.pop(i)
                    print("🗑️  Tarefa removida com sucesso!")
                else:
                    print("❌ Operação cancelada!")
                return
        
        print("❌ Tarefa não encontrada!")
    
    except ValueError:
        print("❌ Digite um número válido!")

def buscar_tarefa():
    if not tarefas:
        print("\n📭 Nenhuma tarefa para buscar!")
        return
    
    termo = input("\n🔍 Digite o termo de busca: ").lower()
    encontradas = []
    
    for tarefa in tarefas:
        if termo in tarefa["descricao"].lower():
            encontradas.append(tarefa)
    
    if encontradas:
        print(f"\n🔍 ENCONTRADAS ({len(encontradas)} resultados)")
        print("-" * 60)
        for tarefa in encontradas:
            status = "✅" if tarefa["concluida"] else "⏳"
            print(f"{tarefa['id']}. {status} {tarefa['descricao']}")
            print(f"   {tarefa['prioridade']} | {tarefa['data_criacao']}")
            print("-" * 60)
    else:
        print("❌ Nenhuma tarefa encontrada!")

def mostrar_estatisticas():
    if not tarefas:
        print("\n📭 Nenhuma tarefa para analisar!")
        return
    
    total = len(tarefas)
    concluidas = len([t for t in tarefas if t["concluida"]])
    pendentes = total - concluidas
    
    alta = len([t for t in tarefas if "🔴" in t["prioridade"]])
    media = len([t for t in tarefas if "🟡" in t["prioridade"]])
    baixa = len([t for t in tarefas if "🟢" in t["prioridade"]])
    
    progresso = (concluidas / total) * 100 if total > 0 else 0
    
    print(f"\n📊 ESTATÍSTICAS")
    print("=" * 30)
    print(f"📋 Total de tarefas: {total}")
    print(f"✅ Concluídas: {concluidas}")
    print(f"⏳ Pendentes: {pendentes}")
    print(f"📈 Progresso: {progresso:.1f}%")
    print("\n🎯 POR PRIORIDADE:")
    print(f"🔴 Alta: {alta}")
    print(f"🟡 Média: {media}")
    print(f"🟢 Baixa: {baixa}")
    print("=" * 30)

def salvar_arquivo():
    try:
        with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
            for tarefa in tarefas:
                linha = f"{tarefa['id']};{tarefa['descricao']};{tarefa['prioridade']};{tarefa['concluida']};{tarefa['data_criacao']}\n"
                arquivo.write(linha)
        print("💾 Tarefas salvas com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")

def carregar_arquivo():
    try:
        global tarefas
        tarefas = []
        
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 5:
                    tarefa = {
                        "id": int(dados[0]),
                        "descricao": dados[1],
                        "prioridade": dados[2],
                        "concluida": dados[3] == "True",
                        "data_criacao": dados[4]
                    }
                    tarefas.append(tarefa)
        
        print(f"📂 {len(tarefas)} tarefas carregadas com sucesso!")
    
    except FileNotFoundError:
        print("❌ Arquivo não encontrado!")
    except Exception as e:
        print(f"❌ Erro ao carregar: {e}")

# Programa principal
print("📝 BEM-VINDO AO ORGANIZADOR DE TAREFAS!")
print("🎯 Organize sua vida de forma simples e eficiente!")

while True:
    mostrar_menu()
    opcao = input("Sua escolha: ")
    
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        ver_tarefas()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        buscar_tarefa()
    elif opcao == "6":
        mostrar_estatisticas()
    elif opcao == "7":
        salvar_arquivo()
    elif opcao == "8":
        carregar_arquivo()
    elif opcao == "0":
        print("\n👋 Obrigado por usar o Organizador!")
        print("🎯 Continue sendo produtivo!")
        break
    else:
        print("❌ Opção inválida!")
    
    input("\n⏸️  Pressione Enter para continuar...")

# 🎯 IDEIAS PARA EXPANDIR:
# 1. Adicione datas de vencimento
# 2. Crie categorias para as tarefas
# 3. Adicione lembretes
# 4. Exporte para Excel ou PDF
# 5. Adicione interface gráfica
