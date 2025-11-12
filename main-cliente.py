from xmlrpc.client import ServerProxy
import os #Utlilizado para limpar a tela

def main():

    serv_api = ServerProxy("http://localhost:8080/", allow_none=True)

    print("BEM VINDOS AO SISTEMA DE RESERVAS DE VOOS DA GUSTA AIRLINES")
    print("")

    print("Atividades disponíveis:")
    print("")
    
    instrucao = str(input("Deseja iniciar o sistema de reservas? (s/n): \n")).lower()

    if instrucao == 's':
        print("Iniciando o sistema de reservas... \n")
        print("")
    else:
        print("Encerrando o sistema de reservas. Até mais!")
        return None

    categoria = 10
    

    while categoria != 0:

        print("")
        print(serv_api.printarTab())
        print("")
        categoria = int(input("Digite o numero da atvidade que deseja realizar: "))
        print("")
        os.system('clear')

        if categoria == 1: #atividades relacionadas a reservas
            print("--Atividades relacionadas a reservas: --")
            print("")
            print(serv_api.printarTabReservas())
            print("")
            servicos = int(input("Digite o número do serviço que deseja realizar: "))
            print("")

            if servicos == 1:
                resposta = serv_api.printarReserva(str(input("Digite o ID da reserva que deseja consultar: ")))
                if resposta != None:
                    print("")
                    print(resposta)
                    print("")
                else:
                    print("")
                    print("--Reserva não existente--")
                    print("")
            if servicos == 2:
                print("")
                voo = str(input("Digite o ID do voo que deseja fazer a reserva:"))
                if serv_api.vooExiste(voo) == False:
                    print("")
                    print("--Voo não encontrado. Verifique o ID e tente novamente.--")
                    continue
                print("")
                print(serv_api.printarAssentosVoo(voo))
                print("")
                reserva = str(input("Digite o ID da reserva: "))
                dta = str(input("Data e Hora de Embarque: "))
                status = str(input("Status da Reserva: "))
                assento = str(input("Digite o assento desejado (Exemplo: 12A): ").upper())
                id_passageiro = str(input("Digite o ID do passageiro: "))
                print("")
                resposta = serv_api.adReserva(reserva, dta, status, assento, id_passageiro, voo)
                if resposta == 0:
                    print("--Reserva adicionada com sucesso!--")
                    print("")
                elif resposta == 1:
                    print("--Erro ao adicionar reserva: Passageiro não encontrado.--")
                    print("")
                elif resposta == 2:
                    print("--Erro ao adicionar reserva: Voo não encontrado.--")
                    print("")
                elif resposta == 3:
                    print("--Erro ao adicionar reserva: Voo não possui vagas.--")
                    print("")
                elif resposta == 4:
                    print("--Erro ao adicionar reserva: Assento já está ocupado.--")
                    print("")
                elif resposta == 5:
                    print("--Erro ao adicionar reserva: Duplicidade de reserva com o ID.--")
                    print("")

                print("")

            if servicos == 3: #listar todas as reservas
                print("")
                print(serv_api.printarReservas())
                print("")

            if servicos == 4:
                print("--Encerrando atividades relacionadas a reservas.--")
                continue
        if categoria == 2: #atividades relacionadas a passageiros
            print("--Atividades relacionadas a passageiros: --")
            print("")
            print(serv_api.printarTabPassageiros())
            print("")
            servicos = int(input("Digite o número do serviço que deseja realizar: "))
            print("")

            if servicos == 1:   #consultar passageiro
                resposta = serv_api.printarPassageiro(str(input("Digite o ID do passageiro que deseja consultar: ")))
                if resposta != None:
                    print("")
                    print(resposta)
                    print("")
                else:
                    print("")
                    print("--Passageiro não encontrado. Verifique o ID e tente novamente.--")
                    print("")

            if servicos == 2: #adicionar passageiro
                print("")
                id = str(input("Digite o ID do passageiro: "))
                if serv_api.passExiste(id) == True:
                    print("--Erro ao adicionar passageiro: Passageiro com ID já existente.--")
                    print("")
                    continue
                nome = str(input("Digite o nome do passageiro: "))
                email = str(input("Digite o email do passageiro: "))
                fone = str(input("Digite o telefone do passageiro: "))

                resposta = serv_api.adPassageiro(id, nome, email, fone)
                print("")
                if resposta:
                    print("--Passageiro adicionado com sucesso!--")
                    print("")
                else:
                    print("--Erro ao adicionar passageiro. Verifique os dados e tente novamente.--")

            if servicos == 3: #printar tabela de passageiros
                print("")
                print(serv_api.printarPassageiros())
                print("")

            if servicos == 4: #sair
                print("--Encerrando atividades relacionadas a passageiros.--")
                continue

        if categoria == 3:
            print("")
            print("--Atividades relacionadas a Voo: --")
            print("")
            print(serv_api.printarTabVoo())
            print("")
            servicos = int(input("Digite o número do serviço que deseja realizar: "))

            if servicos == 1: #Dados do voo
                print("")
                resposta = serv_api.printarVoo(str(input("Digite o ID do voo que deseja consultar os dados:  ")))
                if resposta != None:
                    print("")
                    print("--Dados do voo:--")  
                    print(resposta)
                    print("")
                else:
                    print("")
                    print("--Voo não encontrado. Verifique o ID e tente novamente.--")
                    print("")
            if servicos == 2: #Vagas disponíveis
                resposta = serv_api.vagasVoo(str(input("Digite o ID do voo que deseja consultar as vagas disponíveis: ")))
                if resposta != None:
                    print("")
                    print(f"--Número de vagas disponíveis no voo: {resposta}--")
                    print("")
                else:
                    print("")
                    print("--Voo não encontrado. Verifique o ID e tente novamente.--")
                    print("")
            
            if servicos == 3: #adicionar voo
                resposta = serv_api.adVoo(str(input("Digite o ID do voo: ")),str(input("Digite o Número de voo: ")), str(input("Digite a origem do voo: ")), str(input("Digite o destino do voo: ")), str(input("Data de partida do Voo: ")),str(input("Data de chegada do Voo: ")), str(input("Digite a quantidade de vagas voo: ")))
                if resposta:
                    print("")
                    print("--Voo adicionado com sucesso!--")
                    print("")
                else:
                    print("")
                    print("--Erro ao adicionar voo. Verifique os dados e tente novamente.--")
                    print("")
            if servicos == 3: #dados de um voo
                resposta = serv_api.printarVoo(str(input("Digite o ID do voo que deseja consultar: ")))
                if resposta != None:
                    print("")
                    print("--Dados do voo:--")
                    print(resposta)
                    print("")
                else:
                    print("--Voo não encontrado. Verifique o ID e tente novamente.--")

            if servicos == 4: #listar todos os voos
                print("")
                print(serv_api.printarVoos())
                print("")
            if servicos == 5: #voltar ao menu principal
                print("")
                print("--Encerrando atividades relacionadas a voos.--")
                print("")
                continue

        if categoria == 4:
            serv_api.salvar_db()
            print("")
            print("--Banco de dados salvo com sucesso!--")
            print("")
            break
            

if __name__ == "__main__":
    main()