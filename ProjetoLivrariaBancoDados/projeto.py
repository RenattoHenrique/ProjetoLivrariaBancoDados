import mysql.connector
import os

import Formatação_cores
import AnimacaoInicial
import AnimacaoFinal

conexao = mysql.connector.connect(host = "localhost", password = "", user = "root", database = "livraria", port = "3307")
cursor = conexao.cursor()

#Rai

def CadastrarLivro():
    os.system("cls")
    print("Insira os dados do novo livro:")
    titulo = input("Título do Livro: ")
    if titulo.lower() == "sair":
        Menu()
    genero = input("Gênero: ")
    if genero.lower() == "sair":
        Menu()
    sinopse = input("Sinopse: ")
    if sinopse.lower() == "sair":
        Menu()
    autor = input("Autor: ")
    if autor.lower() == "sair":
        Menu()
    publicacao = input("Data de publicação (AAAA/MM/DD): ")
    if publicacao.lower() == "sair":
        Menu()
    valorCompra = input("Valor de Compra: ")
    if valorCompra.lower() == "sair":
        Menu()
    valorRevenda = input("Valor de revenda: ")
    if titulo.lower() == "sair":
        Menu()
    if not titulo or not genero or not sinopse or not autor or not publicacao or not valorCompra or not valorRevenda or len(publicacao) != 10:
        print("\033[31mDados inválidos. Verifique os dados e tente novamente.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()
    try:
        cursor.execute(f"INSERT INTO livro (titulo, genero, sinopse, autor, publicacao, valor_compra, valor_revenda) VALUES ('{titulo}', '{genero}', '{sinopse}', '{autor}', '{publicacao}', '{valorCompra}', '{valorRevenda}')")
        conexao.commit()
        cursor.execute("SELECT id FROM livro")
        add_estoque = cursor.fetchall()
        for linha in add_estoque:
            id = linha[0]
        cursor.execute(f"INSERT INTO estoque (id_livro, quantidade) VALUES ('{id}', '{0}')")
        conexao.commit()
        print("\033[32mCadastro registrado com sucesso.\033[m")
    except:
        print("\033[31mNão foi possível registrar o cadastro. Verifique os dados e tente novamente.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()

def ListarLivros():
    os.system("cls")
    cursor.execute("SELECT * FROM livro")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print("\033[31mNão há registros.\033[m")
        input()
        Menu()
    print("═"*50)
    print("Livros Cadastrados")
    print("═"*50)
    for linha in resultado:
        print(f"ID: {linha[0]}")
        print(f"Título: {linha[1]}")
        print(f"Gênero: {linha[2]}")
        print(f"Autor: {linha[3]}")
        print(f"Publicação: {linha[4]}")
        print(f"Sinopse: {linha[5]}\n")
        print("-"*50)
    print("\033[32mListagem Concluída com sucesso.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()

def ListarEstoque():
    os.system("cls")
    cursor.execute("select l.id, l.titulo, l.valor_compra, l.valor_revenda, e.quantidade from livro as l join estoque as e on l.id = e.id_livro")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print("\033[31mNão há livros registrados para listar um estoque.\033[m")
        input()
        Menu()
    print("═"*50)
    print("ESTOQUE")
    print("═"*50)
    for linha in resultado:
        print(f"livro ID: {linha[0]}")
        print(f"Título: {linha[1]}")
        print(f"Preço de compra: {linha[2]}R$")
        print(f"Valor de revenda: {linha[3]}R$")
        print(f"Quantidade disponível: {linha[4]}\n")
        print("-"*50)
    print("\033[32mListagem concluída com sucesso.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()


#Renato

def ComprarLivros():
    os.system("cls")
    id_livro = input("Insira o ID do livro a ser comprado: ")
    if not id_livro:
        ComprarLivros()
    if id_livro.lower() == "sair":
        Menu()
    cursor.execute(f"SELECT * FROM livro WHERE id = {id_livro}")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print(f"\033[31mNão há livro registrado com o id {id_livro}\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()
    for linha in resultado:
        titulo = linha[1]
        valor_compra = linha[6]
    print(f"Insira quantas cópias do livro {titulo} serão compradas.")
    try:
        quantidade = int(input())
    except ValueError:
        print("\033[31mDado inválido.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()
    data_compra = input("Registre a data da compra. (AAAA/MM/DD): ") 
    if len(data_compra) != 10:
        print("\033[31m data precisa ter 10 caracteres.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu() 
    custo = valor_compra * quantidade
    try:
        cursor.execute("SELECT * from estoque")
        resultado3 = cursor.fetchall()
        for linha in resultado3:
            quantidadeEstoque = linha[1]
            atualizarQuantidade = quantidadeEstoque + quantidade
        cursor.execute(f"INSERT INTO compra (id_livro, quantidade, data_compra, custo) VALUES ('{id_livro}','{quantidade}','{data_compra}','{custo}')")
        conexao.commit()
        cursor.execute(f"UPDATE estoque SET quantidade = {atualizarQuantidade} WHERE id_livro = {id_livro}")
        conexao.commit()
        print("\033[32mCompra registrada com sucesso.\033[m") 
        input("\nDigite ENTER para retornar ao Menu...")
    except:
        print("\033[31mNão foi possível registrar a compra. verifique os dados e tente novamente.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
    Menu()

def ListarCompras():
    os.system("cls")
    cursor.execute("SELECT c.id, l.id, l.titulo, c.quantidade, c.data_compra, c.custo FROM compra as c JOIN livro as l ON c.id_livro = l.id")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print("\033[31mNão há registro.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()
    print("═"*50)
    print("REGISTRO DE COMPRAS")
    print("═"*50)
    for linha in resultado:
        id = linha[0]
        id_livro = linha[1]
        titulo = linha[2]
        quantidade = linha[3]
        data_compra = linha[4]
        custo = linha[5]
        print(f"ID da compra: {id}")
        print(f"ID do livro: {id_livro}")
        print(f"Livro: {titulo}")
        print(f"Quantidade comprada: {quantidade}")
        print(f"Data da compra: {data_compra}")
        print(f"Custo total: {custo}R$\n")
        print("-"*50)
    print("\033[32mListagem concluída com sucesso.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()

def VenderLivros():
    os.system("cls")
    cursor.execute("SELECT * FROM livro")
    disponibilidade = cursor.fetchall()
    if len(disponibilidade) == 0:
        print("\033[31mNão há livros cadastrados para a venda.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()
    id_livro = input("Insira o ID do livro a ser vendido: ")
    if id_livro.lower() == "sair":
        Menu()
    if not id_livro:
        VenderLivros()
    cursor.execute(f"SELECT * FROM livro WHERE id = {id_livro}")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print(f"\033[31mNão há livro registrado com o id {id_livro}\033[m")
        VenderLivros()
    for linha in resultado:
        id = linha[0]
        titulo = linha[1]
        valor_compra = linha[6]
        valor_venda = linha[7]
    cursor.execute(f"SELECT quantidade FROM estoque WHERE id_livro = {id}")
    estoqueBolado = cursor.fetchall()
    for linha in estoqueBolado:
        quantidadeEstocada = linha[0]
    if quantidadeEstocada == 0:
        print(f"\033[31mNão há cópias do livro {titulo} disponíveis a serem vendidas.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()
    id_cliente = input(f"Insira o ID do cliente que irá comprar o livro {titulo}: ")
    if id_cliente.lower() == "sair":
        Menu()
    cursor.execute(f"SELECT * FROM cliente WHERE id = {id_cliente}")
    resultado2 = cursor.fetchall()
    for linha in resultado2:
        nome = linha[1]
    if len(resultado2) == 0:
        print(f"\033[31mNão há cliente registrado com o id {id_livro}\033[m")
        input()
        VenderLivros()
    print(f"Insira quantas cópias do livro {titulo} o senhor(a) {nome} irá comprar:")
    try:
        quantidade = int(input())
    except ValueError:
        print("\033[31mDado inválido.\033[m")
        input()
        VenderLivros()
    if quantidade > quantidadeEstocada:
        quantidade = quantidadeEstocada
    data_venda = input("Registre a data da venda. (AAAA/MM/DD): ") 
    if len(data_venda) != 10:
        print("\033[31m data precisa ter 10 caracteres.\033[m")
        input()
        VenderLivros() 
    lucro = (valor_venda - valor_compra) * quantidade 
    novaQuantidade = quantidadeEstocada - quantidade
    try:
        cursor.execute(f"INSERT INTO venda (data_venda, quantidade, id_cliente, id_livro, lucro) VALUES ('{data_venda}','{quantidade}','{id_cliente}','{id_livro}','{lucro}')")
        conexao.commit()
        cursor.execute(f"UPDATE estoque SET quantidade = {novaQuantidade} WHERE id_livro = {id_livro}")
        conexao.commit()
        print("\033[32mVenda registrada com sucesso.\033[m") 
        input()
    except:
        print("\033[32mNão foi possível registrar a venda. verifique os dados e tente novamente.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
    Menu()

def ListarVendas():
    os.system("cls")
    cursor.execute("SELECT v.id, l.id, c.id, l.titulo, c.nome, v.quantidade, v.lucro FROM venda AS v JOIN livro AS l ON v.id_livro = l.id JOIN cliente AS c ON v.id_cliente = c.id ")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print("\033[31mNão há registro.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()
    print("═"*50)
    print("LISTA DE VENDAS")
    print("═"*50)
    for linha in resultado:
        v_id = linha[0]
        l_id = linha[1]
        c_id = linha[2]
        l_titulo = linha[3]
        c_nome = linha[4]
        v_quantidade = linha[5]
        v_lucro = linha[6]
        print(f"ID da venda: {v_id}")
        print(f"ID do livro: {l_id}")
        print(f"ID do cliente: {c_id}")
        print(f"Livro: {l_titulo}")
        print(f"Ciente: {c_nome}")
        print(f"Cópias vendidas: {v_quantidade}")
        print(f"Lucro: {v_lucro}R$\n")
        print("-"*50)
    print("\033[32mListagem concluída com sucesso.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()


#João

def RemoverLivro():
    os.system("cls")
    print("Insira o ID do livro a ser removido:")
    id = input()
    if not id:
        RemoverLivro()
    if id.lower() == "sair":
        Menu()
    cursor.execute(f"SELECT id, titulo, autor FROM livro WHERE id = {id}")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print(f"\033[31mERRO. Nenhum registro encontrado com o id {id}\033[m")
        input()
        return RemoverLivro()
    print("\033[32mRegistro encontrado !\033[m")
    print("-"*100)
    print(f"{'ID':5}{'Título':30}{'Autor'}")
    print("-"*100)
    for linha in resultado:
        id = linha[0]
        titulo = linha[1]
        autor = linha[2]
        print(f"{id:<5}{titulo:20}{autor:21}")
        print("-"*100)
    print("Deseja realmente \033[31mexcluir\033[m esse registro ? S / N:")
    opcao = input()
    if opcao.lower() == "s":
        try:
            cursor.execute(f"DELETE FROM livro WHERE id = {id}")
            conexao.commit()
            print("\033[32mRegistro deletado com sucesso.\033[m")
            input("\nDigite ENTER para retornar ao Menu...")
            Menu()
        except:
            print("\031[32mNão foi possível deletar o cadastro por um erro sinistro.\031[m")
            input("\nDigite ENTER para retornar ao Menu...")
            Menu()
    else:
        Menu()

def AtualizarLivro():
    os.system("cls")
    print("Insira o ID do livro a ser atualizado:")
    id = input()
    if not id:
        AtualizarLivro()
    if id.lower() == "sair":
        Menu()
    if id.lower() == "sair":
        Menu()
    cursor.execute(f"SELECT * FROM livro WHERE id = {id}")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print(f"\033[mERRO. Nenhum registro encontrado com o id {id}\033[m")
        input()
        return AtualizarLivro()
    print("="*50)
    print("\033[32mRegistro encontrado !\033[m")
    print("="*50)
    for linha in resultado:
        print(f"ID: {linha[0]}")
        print(f"Título: {linha[1]}")
        print(f"Gênero: {linha[2]}")
        print(f"Autor: {linha[3]}")
        print(f"Publicação: {linha[4]}")
        print(f"Sinopse: {linha[5]}")
        print(f"Preço de compra: {linha[6]:.2f}R$")
        print(f"Preço de Venda: {linha[7]:.2f}R$")
        print("-"*50)
    novoTitulo = input("Novo título: ")
    novoGenero = input("Novo Gênero: ")
    novoAutor = input("Novo autor: ")
    novaPublicacao = input("Nova data de publicação (AAAA/MM/DD): ")
    novaSinopse = input("Nova sinopse: ")
    try:
        novoValorCompra = float(input("Novo preço de compra: "))
        novoValorVenda = float(input("Novo preço de revenda: "))
    except ValueError:
        print(f"\033[31mNenhum número inserido.\033[m")
        input()
        return AtualizarLivro()
    if not novoTitulo or not novoGenero or not novoAutor or not novaPublicacao or not novaSinopse or not novoValorCompra or not novoValorVenda or len(novaPublicacao) != 10 or novoValorCompra < 0 or novoValorVenda < 0:
        os.system("cls")
        print("\033[31mDados inválidos. Verifique os dados e tente novamente.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()
    print("\033[33mCONFIRMAÇÃO:\033[m Deseja realmente Atualizar o registro atual ? S/N")
    confirmacao = input()
    if confirmacao.lower() == "s":
        try:
            cursor.execute(f"UPDATE livro SET titulo = '{novoTitulo}', genero = '{novoGenero}', autor = '{novoAutor}', publicacao = '{novaPublicacao}', sinopse = '{novaSinopse}', valor_Compra = '{novoValorCompra}', valor_revenda = '{novoValorVenda}' WHERE (id = {id})")
            conexao.commit()
            print("\033[32mRegistro Atualizado com sucesso.\033[m")
        except:
            print("\033[31mNão foi possível atualizar o registro devido a um erro sinistro.\033[m")
    else:
        os.system("cls")
        print("\033[32mAtualização cancelada.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()

def CadastrarCliente():
    os.system("cls")
    print("Insira os dados do novo cliente:")
    nome = input("Nome: ")
    if nome.lower() == "sair":
        Menu()
    telefone = input("Telefone (11 dígitos): ")
    if telefone.lower() == "sair":
        Menu()
    email = input("E-mail: ")
    if email.lower() == "sair":
        Menu()
    if not nome or not telefone or not email or len(telefone) != 11:
        print("\033[31mDados inválidos. Verifique os dados e tente novamente.\033[m")
        input()
        return CadastrarCliente()
    try:
        cursor.execute(f"INSERT INTO cliente (nome, telefone, email) VALUES ('{nome}', '{telefone}', '{email}')")
        conexao.commit()
        print("\033[32mCadastro registrado com sucesso.\033[m")
    except:
        print("\033[31mNão foi possível registrar o cadastro. Verifique os dados e tente novamente.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()

def ListarClientes():
    os.system("cls")
    cursor.execute("SELECT * FROM cliente")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print("\033[31mNão há registros.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()
    print("="*50)
    print("Clientes cadastrados")
    print("="*50)
    for linha in resultado:
        print(f"ID: {linha[0]}")
        print(f"Nome: {linha[1]}")
        print(f"Telefone: {linha[2]}")
        print(f"E_mail: {linha[3]}\n")
        print("-"*50)
    print("\033[32mListagem Concluída com sucesso.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()


#Ademilson

def AtualizarCliente():
    os.system("cls")
    print("Insira o ID do cliente a ser atualizado:")
    id = input()
    if not id:
        AtualizarCliente()
    if id.lower == "sair":
        Menu()
    cursor.execute(f"SELECT * FROM cliente WHERE id = {id}")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print(f"\033[31mERRO. Nenhum registro encontrado com o id {id}\033[m")
        input()
        AtualizarCliente()
    print("\033[32mRegistro encontrado !\033[m")
    print("-"*100)
    print(f"{'ID':5}{'Nome':20}{'Telefone':21}{'E_mail'}")
    print("-"*100)
    for linha in resultado:
        id = linha[0]
        nome = linha[1]
        telefone = linha[2]
        email = linha[3]
        print(f"{id:<5}{nome:20}{telefone:21}{email}")
        print("-"*100)
    newNome = input("Novo nome: ")
    newTelefone = input("Novo Telefone (11 dígitos): ")
    newEmail = input("Novo E-mail: ")
    if not newNome or not newTelefone or not newEmail or len(newTelefone) != 11:
        print("\033[31mDados inválidos. O registro não foi atualizado.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()
    print("\033[33mCONFIRMAÇÃO:\033[m Deseja realmente Atualizar o registro atual ? S/N")
    confirmacao = input()
    if confirmacao.lower() == "s":
        try:
            cursor.execute(f"UPDATE cliente SET nome = '{newNome}', telefone = '{newTelefone}', email = '{newEmail}' WHERE (id = {id})")
            conexao.commit()
            print("\033[32mRegistro Atualizado com sucesso.\033[m")
        except:
            print("\033[31mNão foi possível atualizar o registro devido a um erro sinistro.\033[m")
    else:
        os.system("cls")
        print("\033[32mAtualização cancelada.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()

def AdicionarAvaliacoes():
    os.system("cls")
    id_cliente = input("ID do cliente que irá avaliar: ")
    if not id_cliente:
        AdicionarAvaliacoes()
    if id_cliente.lower() == "sair":
        Menu()
    cursor.execute(f"select nome from cliente where id = {id_cliente}")
    resultado_cliente = cursor.fetchall()
    if len(resultado_cliente) == 0:
        print(f"Não há cliente cadastrado com o id {id_cliente}")
        input()
        return AdicionarAvaliacoes()
    for linha in resultado_cliente:
        nome = linha[0]
    id_livro = input("ID do livro que será avaliado: ")
    if id_livro.lower() == "sair":
        Menu()
    cursor.execute(f"select titulo from livro where id = {id_livro}")
    resultado_livro = cursor.fetchall()
    if len(resultado_livro) == 0:
        print(f"Não há livro registrado com o ID {id_livro}")
        input()
        return AdicionarAvaliacoes()
    for linha in resultado_livro:
        titulo = linha[0]
    os.system("cls")
    print(f"Qual a nota que o cliente {nome} dará ao livro {titulo} de 1 a 10 ?")
    try:
        nota = int(input())
    except ValueError:
        print("\033[31mA nota precisa ser um número entre 1 e 10.\033[m")
        input()
        return AdicionarAvaliacoes()
    if not nota or nota > 10 or nota < 1:
        print("\033[31mA nota precisa ser um número entre 1 e 10.\033[m")
        input()
        return AdicionarAvaliacoes()
    os.system("cls")
    print(f"Insira o comentário da avaliação:")
    comentario = input()
    try:
        cursor.execute(f"insert into avaliacao (comentario, nota, id_livro, id_cliente) values ('{comentario}', '{nota}', '{id_livro}', '{id_cliente}')")
        conexao.commit()
        print("\033[32mComentário adicionado com sucesso.\033[m")
    except:
        print("\033[31mNão foi possível adicionar o comentário em questão.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()
    
def VerificarAvaliacoes():
    os.system("cls")
    cursor.execute("select a.id, c.nome, l.titulo, a.nota, a.comentario from avaliacao as a JOIN livro as l on l.id = a.id_livro JOIN cliente as c on c.id = a.id_cliente")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print("\033[31mNão há registro.\033[m")
        input()
        Menu()
    print("="*50)
    print("AVALIAÇÕES")
    print("="*50)
    for linha in resultado:
        print(f"ID: {linha[0]}")
        print(f"Cliente: {linha[1]}")
        print(f"Livro: {linha[2]}")
        print(f"Nota: {linha[3]}")
        print(f"Comentário: {linha[4]}\n")
        print("-"*50)
    print("\033[32mConsulta concluída com sucesso.\033[m")
    input("\nDigite ENTER para retornar ao Menu...")
    Menu()
    

#Renan

def RemoverCliente():
    os.system("cls")
    print("Insira o ID do cliente a ser removido:")
    id = input()
    if not id:
        RemoverCliente()
    if id.lower() == "sair":
        Menu()
    cursor.execute(f"SELECT * FROM cliente WHERE id = {id}")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print(f"\033[31mERRO. Nenhum registro encontrado com o id {id}\033[m")
        input()
        return RemoverCliente()
    print("\033[32mRegistro encontrado !\033[m")
    print("-"*100)
    print(f"{'ID':5}{'Nome':20}{'Telefone':21}{'E_mail'}")
    print("-"*100)
    for linha in resultado:
        id = linha[0]
        nome = linha[1]
        telefone = linha[2]
        email = linha[3]
        print(f"{id:<5}{nome:20}{telefone:21}{email}")
        print("-"*100)
    print("Deseja realmente \033[31mexcluir\033[m esse registro ? S / N:")
    opcao = input()
    if opcao.lower() == "s":
        try:
            cursor.execute(f"DELETE FROM cliente WHERE id = {id}")
            conexao.commit()
            print("\033[32mRegistro deletado com sucesso.\033[m")
            input()
            Menu()
        except:
            print("\031[32mNão foi possível deletar o cadastro por um erro sinistro.\031[m")
            input("\nDigite ENTER para retornar ao Menu...")
            Menu()
    else:
        Menu()
    
def deletarAvaliacao():
    os.system("cls")
    id = input("Insira o ID da avaiação a ser deletada: ")
    if not id:
        deletarAvaliacao()
    if id.lower() == "sair":
        Menu()
    cursor.execute(f"SELECT * FROM avaliacao WHERE id = {id}")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print(f"\033[31mNão há avaliação registrada com o ID {id}\033[m")
        input()
        deletarAvaliacao()
    for linha in resultado:
        print("-"*50)
        print(f"ID: {linha[0]}")
        print(f"Cliente: {linha[1]}")
        print(f"Livro: {linha[2]}")
        print(f"Nota: {linha[3]}")
        print(f"Comentário: {linha[4]}\n")
        print("-"*50)
    deletar = input("\033[33mCONFIRMAÇÃO\033[mVocê realmente deseja apagar esse registro ? (S/N): ")
    if deletar.lower() == "s":
        try:
            cursor.execute(f"DELETE FROM avaliacao WHERE id = {id}")
            conexao.commit()
            print("\033[32mRegistro deletado com sucesso.\033[m")
            input()
        except:
            print("\033[31mNão foi possível deletar o registro.\033[m")
            input("\nDigite ENTER para retornar ao Menu...")
        Menu()

def EncerrarConexao():
    os.system("cls")
    try:
        cursor.close()
        conexao.close()
        print("\033[32mConexão Encerrada com segurança.\033[m")
        os._exit(0)
    except:
        print("\033[31mNão foi possível encerrar a conexão. Tente novamente.\033[m")
        input("\nDigite ENTER para retornar ao Menu...")
        Menu()

def Menu():  
    os.system("cls")
    while True:  
        print(" " * 28 + f"{Formatação_cores.GREEN}SISTEMA DE GERENCIAMENTO{Formatação_cores.RESET}\n")  
        print('╔'+'═' * 35  +'╗'+" "* 4 + '╔'+'═' * 35  +'╗')
        print('║'+" 1. CADASTRAR LIVROS          " + " " * 5 +'║'+" "* 4 + '║ ' + "10. CADASTRAR CLIENTES            ║")  
        print('║'+" 2. LISTAR LIVROS CADASTRADOS " + " " * 5 +'║'+" "* 4 + '║ ' + "11. LISTAR CLIENTES CADASTRADOS   ║")  
        print('║'+" 3. LISTAR ESTOQUE DE LIVROS  " + " " * 5 +'║'+" "* 4 + '║ ' + "12. ADICIONAR AVALIAÇÕES USUÁRIOS ║")  
        print('║'+" 4. COMPRAR LIVROS            " + " " * 5 +'║'+" "* 4 + '║ ' + "13. VERIFICAR AVALIAÇÕES          ║")  
        print('║'+" 5. LISTAR COMPRAS DE LIVROS  " + " " * 5 +'║'+" "* 4 + '║ ' + "14. ATUALIZAR CLIENTES            ║")  
        print('║'+" 6. VENDER LIVROS             " + " " * 5 +'║'+" "* 4 + '║ ' + "15. REMOVER CLIENTES              ║")  
        print('║'+" 7. LISTAR VENDAS DE LIVROS   " + " " * 5 +'║'+" "* 4 + '║ ' + "16. REMOVER AVALIAÇÕES            ║")  
        print('║'+" 8. REMOVER LIVROS            " + " " * 5 +'║'+" "* 4 + '║ ' + "17. ENCERRAR CONEXÃO MYSQL        ║")  
        print('║'+" 9. ATUALIZAR LIVROS          " + " " * 5 +'║'+" "* 4 + '║ ' + " " * 34 + "║")  
        print('╚'+'═' * 35  +'╝'+" "* 4 + '╚'+'═' * 35  +'╝\n') 
        print(f"{Formatação_cores.GREEN}INSIRA UM NÚMERO: {Formatação_cores.RESET}", end="")  
        option = input()  
        if option == "1":  
            CadastrarLivro()  
        elif option == "2":  
            ListarLivros()  
        elif option == "3":  
            ListarEstoque()  
        elif option == "4":  
            ComprarLivros()  
        elif option == "5":  
            ListarCompras()  
        elif option == "6":  
            VenderLivros()  
        elif option == "7":  
            ListarVendas()  
        elif option == "8":  
            RemoverLivro()  
        elif option == "9":  
            AtualizarLivro()  
        elif option == "10":  
            CadastrarCliente()  
        elif option == "11":  
            ListarClientes()  
        elif option == "12":  
            AdicionarAvaliacoes()  
        elif option == "13":  
            VerificarAvaliacoes()  
        elif option == "14":  
            AtualizarCliente()  
        elif option == "15":  
            RemoverCliente()  
        elif option == "16":  
            deletarAvaliacao()  
        elif option == "17":  
            print("Deseja realmente encerrar a conexão? S/N")  
            opcao = input()  
            if opcao.lower() == "s":  
                os.system("cls")
                AnimacaoFinal.run_asciimatics_demo()  
            else:  
                continue  
        else:  
            continue  

Menu()