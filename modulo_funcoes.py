import json

"""Esta função tem como objetivo ler 3 arquivos referentes a passageiro, 
reservas e voos, ela retorna uma lista de dicionarios, que serão utilizados pela função 
salva_bd em formato json"""

"""
EX: {passageiros : [{"id": "1", "nome": "fulano", "email": "fulano@gmail.com" ...} , {}], reservas : [id, voo, assento, talz]...}
"""

def open_db(tabnamePass, tabnameRes, tabnameVoos)->dict :
    line = str()
    passageiro = list()
    lista_pass = {"passageiros": [], "reservas": [], "voos": []}

    with open (tabnamePass, 'rt', encoding='utf-8') as wo: #abrindo o arquivo de passageiros e pegando os passageiros
        line = wo.readline()

        while line != "":
            passageiro = line.strip().split(",")
            lista_pass["passageiros"].append({
                'id' : passageiro[0],
                'nome' : passageiro[1],  
                'email' : passageiro[2], 
                'tel' : passageiro[3]
            })
            line = wo.readline()

    with open (tabnameRes, 'rt', encoding='utf-8') as wo: #abrindo o arquivo de reservas e pegando as reservas
        line = wo.readline()

        while line != "":
            reservas = line.strip().split(",")
            lista_pass["reservas"].append({
                'id' : reservas[0],    
                'data' : reservas[1],  
                'status' : reservas[2], 
                'assento' : reservas[3],
                'idpass' : reservas[4],
                'idvoo' : reservas[5]
            })
            line = wo.readline()
    
    with open (tabnameVoos, 'rt', encoding='utf-8') as wo: #abrindo o arquivo de voos e pegando os voos
        line = wo.readline()

        while line != "":
            voos = line.strip().split(",")
            lista_pass["voos"].append({
                'id' : voos[0],    
                'numvoo' : voos[1],  
                'origem' : voos[2], 
                'destino' : voos[3],
                'datapda' : voos[4],
                'datache' : voos[5],
                'vagas' : int(voos[6])
            })
            line = wo.readline()

    return lista_pass



"""
Verifica se o voo com o ID do parametro existe, retorna bool como resposta:
True para existe
False para não existe
"""
def vooExiste(bd, idvoo)->bool:

    for voo in bd["voos"]:
        if voo["id"] == idvoo:
            return True

    return False


"""
Esta função verifica se há  vagas no Voo, e retorna a quantidade e vagas disponíveis,
e caso o voo não exista, retorna -1
"""
def vagasVoo(bd, idvoo):
    cont_assentos = int(0)

    for reserva in bd["reservas"]: 
        if (reserva["idvoo"] == idvoo) and (reserva["status"] == "Confirmada"): #conta as vagas ocupadas daquele voo
            cont_assentos += 1

    for voo in bd["voos"]:
        if voo["id"] == idvoo:
            if voo["vagas"] >= cont_assentos: #verifica se há vagas livres
                return voo["vagas"] - cont_assentos #retorna a quantidade de vagas livres, mesmo que seja 0

    return -1 #Voo não existe
                




"""
Verifica se o passageiro com o ID do parametro existe, retorna bool como resposta:
True para existe
False para não existe
"""
def passExiste(bd, idpass)->bool:

    for passageiro in bd["passageiros"]:
        if passageiro["id"] == idpass:
            return True

    return False

def resExiste(bd, idres):

    for reserva in bd["reservas"]:
        if reserva["id"] == idres:
            return True

    return False


"""
Esta função retorna o bd (obtido da função open_bd), e reescreve os arquivos em formato json
EX: arq passageiros -> {
                            passageiros : [{passageiro1 ...}, {passageiro2 ...}, {passageiro3 ...}]}
                        }
"""

def salva_bd(bd, tabnamePass, tabnameRes, tabnameVoos):

    with open(tabnamePass, 'wt', encoding='utf-8') as wo:
        json.dump({"passageiros" : bd["passageiros"]},wo,indent=4,ensure_ascii=False)

    with open(tabnameRes, 'wt', encoding='utf-8') as wo:
        json.dump({"reservas": bd["reservas"]},wo,indent=4,ensure_ascii=False)

    with open(tabnameVoos, 'wt', encoding='utf-8') as wo:
        json.dump({"voos" : bd["voos"]},wo,indent=4,ensure_ascii=False)
        
    return True



"""
Registra um novo passageiro no banco de dados json, também faz a verificação se o passageiro
Já existe dentro daquele bd no arq json
"""
def adPassageiro(bd, idpass, nome, email, fone):
    for passageiro in bd["passageiros"]: #filtro para não sobrescrever id sobre id
        if passageiro["id"] == idpass:
            return bd
        
    passageiro = {"id" : idpass,
                    "nome" : nome,
                    "email" : email,
                    "tel" : fone}
    bd["passageiros"].append(passageiro)

    return bd


"""
Recebe os parametros necessários para criar o cadastro, e cria o cadastro, com as condições
de: 1. Id do passageiro existe, 2. voo existir e tiver vaga, 3. O assento não esteja ocupado
Ele retorna o próprio Bd se estiver tudo certo

caso contrário retorna:
1 - passageiro não existe
2 - voo não existe
3 - existe mas sem vaga
4 - existe, tem vaga, mas assento está ocupado
5 - ja exista reserva com este id
"""

def adReserva(bd, idres, data, status, assento, idpass, idvoo):
    cont_vagas = 0
    ocupado = False
    passageiro_existe = False
    voo_encontrado = None

    # Verifica se o passageiro existe
    if passExiste(bd, idpass):
        passageiro_existe == True
    else:
        return 1  #passageiro não existe

    # Verifica se o voo existe
    for voo in bd["voos"]:
        if voo["id"] == idvoo:
            voo_encontrado = voo
    if voo_encontrado == None:
        return 2  #voo não existe

    # Verifica duplicidade e conta vagas ocupadas
    for reserva in bd["reservas"]:
        if reserva["id"] == idres:
            return 5 #reserva já existe com esse id, nenhuma alteração
        if reserva["status"] == "Confirmada" and reserva["idvoo"] == idvoo:
            cont_vagas += 1
            if reserva["assento"] == assento:
                ocupado = True

    # Verifica se o voo tem vagas
    if cont_vagas >= int(voo_encontrado["vagas"]):
        return 3  #voo cheio

    # Verifica se o assento está ocupado
    if ocupado:
        return 4  #assento já ocupado

    #esta livre para cadastrar
    reserva = {
        "id": idres,
        "data": data,
        "status": status,
        "assento": assento,
        "idpass": idpass,
        "idvoo": idvoo
    }
    bd["reservas"].append(reserva)

    return 0  #Alterado com sucesso



"""
Adiciona um novo voo, se já não existir um voo com o respectivo ID
"""
def adVoo(bd, idvoo, numvoo, origem, destino, dtpartida, dtchegada, vagas):

    for voo in bd["voos"]: 
        if voo["numvoo"] == numvoo: #verifica se já existe um voo com aquele número
            return bd

    if (vooExiste(bd, idvoo) == False): #se o voo não existir e o número do voo for único
        voo = {
            "id": idvoo,
            "numvoo": numvoo,
            "origem": origem,
            "destino": destino,
            "datapda": dtpartida,
            "datache": dtchegada,
            "vagas": vagas
        }
        bd["voos"].append(voo) #registra o novo voo
        return bd

    return bd



"""
Esta função tem como objetivo retornar o passageiro do banco de dados, cujo o id corresponda
"""
def getPassageiro(bd, id):

    if passExiste(bd, id): #se passageiro existir
        for passageiro in bd["passageiros"]: 
            if passageiro["id"] == id: #pegando o passageiro correspondente ao do ID
                return passageiro
    return None



"""
Esta função tem como objetivo retornar o passageiro do banco de dados, cujo o id corresponda
""" 

def getVoo(bd, id):

    if vooExiste(bd, id):
        for voo in bd["voos"]:
            if voo["id"] == id:
                return voo
    return None


"""
Esta função tem como objetivo retornar a reserva do banco de dados, cujo o id corresponda
"""
def getReserva(bd, idres):

    if resExiste(bd, idres):
        for reserva in bd["reservas"]:
            if reserva["id"] ==  idres:
                return reserva
    return None

"""
Esta função verifica se o assento está livre em um determinado voo
Retorna:
True - Assento livre
False - Assento ocupado
"""


def assentoLivre(bd, idvoo, assento):
    if vooExiste(bd, idvoo):
        for reserva in bd["reservas"]:
            if (reserva["idvoo"] == idvoo) and (reserva["assento"] == assento) and (reserva["status"] == "Confirmada"):
                return False #assento ocupado
            
        return True #assento livre
    
    return False  #Voo não existe



"""
Todas as funçoes a baixo são referentes a printar as funcionalidades do banco de dados e realização das atividades
"""

def printarTab(): #Função para printar as funcionalidades do banco de dados
    tabela = {1 : "Reservas", 2 : "Passageiros", 3 : "Voos", 4 : "salvar banco de dados", 5 : "sair"}

    txt = "Escolha as atividades que deseja executar:\n"

    for key in tabela:  
        txt += "|-" + "-" *43 + "-|\n"
        txt += "| {:^10} - {:^30} |\n".format(key, tabela[key])
        txt += "|-"  + "-" *43 + "-|\n"

    return txt


def printarTabPassageiros():
    tabela = {1 : "Verificar se o passageiro existe", 2 : "consultar dados dos passageiros", 3 : "Adicionar passageiro", 4 : "Listar todos os passageiros", 5 : "Voltar ao menu principal"}

    txt = "Escolha as atividades que deseja executar:\n"
    
    for key in tabela:  
        txt += "|-" + "-" *43 + "-|\n"
        txt += "| {:^10} - {:^30} |\n".format(key, tabela[key])
        txt += "|-"  + "-" *43 + "-|\n"
    
    return txt

def printarPassageiros(bd):
    txt = "Lista de passageiros cadastrados:\n"
    txt += "|-" + "-" *60 + "-|\n"
    txt += "| {:^10} | {:^20} | {:^20} | {:^10} |\n".format("ID", "Nome", "Email", "Telefone")
    txt += "|-" + "-" *60 + "-|\n"

    for passageiro in bd["passageiros"]:
        txt += "| {:^10} | {:^20} | {:^20} | {:^10} |\n".format(passageiro["id"], passageiro["nome"], passageiro["email"], passageiro["tel"])
        txt += "|-" + "-" *60 + "-|\n"

    return txt


def printarTabVoo():
    
    tabela = {1: "Verificar se Voo Existe", 2: "Quantidades de vagas no Voo", 3: "Adicionar Voo", 4: "Dados de um Voo"}

    for key in tabela:
        txt += "|-" + "-" *43 + "-|\n"
        txt += "| {:^10} - {:^30} |\n".format(key, tabela[key])
        txt += "|-"  + "-" *43 + "-|\n"

    return txt



    






