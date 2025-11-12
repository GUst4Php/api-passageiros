from xmlrpc.client import ServerProxy

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

        print(serv_api.printarTab())
        print("")
        categoria = int(input("Digite o numero da atvidade que deseja realizar: "))
        print("")

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
                print(serv_api.printarAssentosVoo(str(input("Digite o ID do voo para o qual deseja fazer a reserva: "))))
                print("")
                resposta = serv_api.adReserva(str(input("Digite o ID da reserva: ")), str(input("Data e Hora de Embarque: ")), str(input("Status da Reserva: ")), str(input("Digite o assento desejado (Exemplo: 12A): ")),str(input("Digite o ID do passageiro")), str(input("Digite o ID do voo: ")))
                print("")
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
                resposta = serv_api.adPassageiro(str(input("Digite o ID do passageiro: ")), str(input("Digite o nome do passageiro: ")), str(input("Digite o email do passageiro: ")), str(input("Digite o telefone do passageiro: ")))
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
            if servicos == 1: #verificar se voo existe
                resposta = serv_api.vooExiste(str(input("Digite o ID do voo que deseja verificar: ")))
                if resposta:
                    print("")
                    print("--O voo existe no sistema.--")
                    print("")
                else:
                    print("")
                    print("--O voo não existe no sistema.--")
                    print("")

            if servicos == 2: #quantidade de vagas no voo
                print("")
                resposta = serv_api.vagasVoo(str(input("Digite o ID do voo que deseja consultar as vagas:  ")))
                print("")
                print(f"--O voo possui {resposta} vagas disponíveis.-- \n")
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
            if servicos == 4: #dados de um voo
                resposta = serv_api.printarVoo(str(input("Digite o ID do voo que deseja consultar: ")))
                if resposta != None:
                    print("")
                    print("--Dados do voo:--")
                    print(resposta)
                    print("")
                else:
                    print("--Voo não encontrado. Verifique o ID e tente novamente.--")

        if categoria == 4:
            serv_api.salvar_db()
            print("")
            print("--Banco de dados salvo com sucesso!--")
            print("")
            continue
            

        if categoria == 5:
            serv_api.salvar_db()
            break


if __name__ == "__main__":
    main()