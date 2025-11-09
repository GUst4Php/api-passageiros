import modulo_funcoes as mf
def main():
    arq_i_pass = "Material para o trabalho avaliação 2/tabpassageiros.txt"
    arq_i_res = "Material para o trabalho avaliação 2/tabreservas.txt"
    arq_i_voos = "Material para o trabalho avaliação 2/tabvoos.txt"

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