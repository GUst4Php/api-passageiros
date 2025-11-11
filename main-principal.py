from xmlrpc.server import SimpleXMLRPCServer
import modulo_funcoes as mf

 # ======== Funções da API de reservas ========
def adPassageiro(idpass, nome, email, fone):
    return mf.adPassageiro(bd, idpass, nome, email, fone)

def adReserva(idres, data, status, assento, idpass, idvoo):
    return mf.adReserva(bd, idres, data, status, assento, idpass, idvoo)

def adVoo(idvoo, numvoo, origem, destino, dtpartida, dtchegada, vagas):
    return mf.adVoo(bd, idvoo, numvoo, origem, destino, dtpartida, dtchegada, vagas)

def getPassageiro(idpass):
    return mf.getPassageiro(bd, idpass)

def getVoo(idvoo):
    return mf.getVoo(bd,idvoo)

def getReserva(idres):
    return mf.getReserva(bd, idres)

def vooExiste(idvoo):
    return mf.vooExiste(bd, idvoo)

def passExiste(idpass):
    return mf.passExiste(bd,idpass)

def vagasVoo(idvoo):
    return mf.vagasVoo(bd, idvoo)

    


    #Reverificar o assento livre, pois ele deve retornas se apenas aquela vaga está vazia ou nn








def main():
    arq_i_pass = "Material para o trabalho avaliação 2/tabpassageiros.txt"
    arq_i_res = "Material para o trabalho avaliação 2/tabreservas.txt"
    arq_i_voos = "Material para o trabalho avaliação 2/tabvoos.txt"

    global bd
    bd = mf.open_db(arq_i_pass,arq_i_res,arq_i_voos)

    print(bd)


    
    """
    idres = str(input())
    data = str(input())
    status = str(input())
    assento = str(input())
    idpass = str(input())
    idvoo = str(input())
    
    bd = mf.adReserva(bd, idres, data, status, assento, idpass, idvoo)
    """
    for reservas in bd["reservas"]:
        print(reservas["assento"])


if __name__ == "__main__":
    main()