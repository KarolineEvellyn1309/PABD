#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome_empresa, endereço, telefone):
    db.cur.execute("""
                   INSERT into empresa (nome_empresa, endereço, telefone)
                   VALUES ('%s','%s','%s')
                   """ % (nome_empresa, endereço, telefone))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM empresa
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows


#função para excluir 
def deletar (id):
    db.cur.execute("""
            DELETE FROM empresa WHERE id_funcionario = '%s'
""" % (id))
db.con.commit()
