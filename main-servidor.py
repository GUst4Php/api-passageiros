from xmlrpc.server import SimpleXMLRPCServer
import modulo_funcoes as mf

 # ======== Funções da API de reservas ========
def adPassageiro(idpass, nome, email, fone): #Adiciona passageiro
    return mf.adPassageiro(bd, idpass, nome, email, fone)

def adReserva(idres, data, status, assento, idpass, idvoo): #Adiciona reserva
    return mf.adReserva(bd, idres, data, status, assento, idpass, idvoo)

def adVoo(idvoo, numvoo, origem, destino, dtpartida, dtchegada, vagas): #Adiciona voo
    return mf.adVoo(bd, idvoo, numvoo, origem, destino, dtpartida, dtchegada, vagas)

def getPassageiro(idpass): #Retorna passageiro
    return mf.getPassageiro(bd, idpass)

def getVoo(idvoo): #Retorna voo
    return mf.getVoo(bd,idvoo)

def getReserva(idres): #Retorna reserva
    return mf.getReserva(bd, idres)

def vooExiste(idvoo): #Verifica se voo existe
    return mf.vooExiste(bd, idvoo)

def passExiste(idpass): #Verifica se passageiro existe
    return mf.passExiste(bd,idpass)

def vagasVoo(idvoo): #retorna número de vagas disponíveis em um voo
    return mf.vagasVoo(bd, idvoo)

def assentoLivre(idvoo, assento): #verifica se o assento está livre em um determinado voo
    return mf.assentoLivre(bd, idvoo, assento)

def printarTab(): #Função para printar o banco de dados
    return mf.printarTab()

def printarTabPassageiros(): #Função para printar tabela de funcionalidades de passageiros
    return mf.printarTabPassageiros()

def printarPassageiros(): #Função para printar tabela de passageiros
    return mf.printarPassageiros(bd)

 # ======== Fim das funções da API de reservas ========




def main():
    # Arquivos de entrada
    arq_i_pass = "Material para o trabalho avaliação 2/tabpassageiros.txt"
    arq_i_res = "Material para o trabalho avaliação 2/tabreservas.txt"
    arq_i_voos = "Material para o trabalho avaliação 2/tabvoos.txt"

    #configurando o serv
    server = SimpleXMLRPCServer(("localhost", 8000))

    #Definindo as funções que serão disponibilizadas pelo servidor
    server.register_function(adPassageiro, "adPassageiro")
    server.register_function(adReserva, "adReserva")
    server.register_function(adVoo, "adVoo")
    server.register_function(getPassageiro, "getPassageiro")
    server.register_function(getVoo, "getVoo")
    server.register_function(getReserva, "getReserva")
    server.register_function(vooExiste, "vooExiste")
    server.register_function(passExiste, "passExiste")
    server.register_function(vagasVoo, "vagasVoo")
    server.register_function(assentoLivre, "assentoLivre")
    server.register_function(printarTab, "printarTab")
    server.register_function(printarTabPassageiros, "printarTabPassageiros")
    server.register_function(printarPassageiros, "printarPassageiros")

    print("Servidor aguardando requisições...")

    #carregando o banco de dados
    global bd
    bd = mf.open_db(arq_i_pass,arq_i_res,arq_i_voos)

    server.serve_forever() #rodando o servidor

if __name__ == "__main__":
    main()