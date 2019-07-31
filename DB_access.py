import psycopg2
import datetime
from decimal import Decimal


class AcessaBD():
    global conn
    global cur

    def __init__(self):
        self.conn = psycopg2.connect(dbname='ddp2de2t1mnh7g', user='rxtzanglblvbnm', 
            password='8e2c520c6abb3a8d10d307ade361e4564eafd85e1abe4bfde35ba2e194630d3b', 
            host='ec2-50-19-222-129.compute-1.amazonaws.com')
        self.cur = self.conn.cursor()

    def inserir_texto(self, texto, topic, tag_user, tag_predicted):
        print('texto: {}\n\n topico: {} \n\n usuario: {} \n\n modelo: {}'.format(texto, topic, tag_user, tag_predicted))

        self.cur.execute("insert into textos (texto, topic, tag_user, tag_predicted) values (%s, %s, %s, %s)",
                         (texto, topic, tag_user, tag_predicted))
        self.conn.commit()

    def get_textos(self):
        self.cur.execute("select * from textos;")
        return self.cur.fetchall()
        # return type(v)
    #
    # def devolveBuscasRecentesCliente(self, idCliente, N):
    #     self.cur.execute("select busca from buscas where idCliente = " + str(idCliente)
    #                      + " order by dt desc limit " + str(N) + ";")
    #     return self.cur.fetchall()
    #
    # def devolveBuscasRecentesSemLogin(self, N):
    #     self.cur.execute("select busca from buscas order by dt desc limit " + str(N) + ";")
    #     return self.cur.fetchall()
    #
    # # Pesquisa por categoria
    # def inserirProduto(self, idProduto, categoria, arrayTAG, preco):
    #     self.cur.execute("insert into produto (idProduto, categoria, arrayTAG, preco) " +
    #                      "values (%s, %s, %s, %s)", (idProduto, categoria, arrayTAG, preco))
    #     self.conn.commit()
    #
    # def atualizeProdutoPreco(self, idProduto, preco):
    #     self.cur.execute("update produto set preco = " + str(preco) + " where idProduto =" + str(idProduto) + ";")
    #     self.conn.commit()
    #
    # def atualizeProdutoTags(self, idProduto, arrayTAG):
    #     self.cur.execute(
    #         "update produto set arrayTAG = \'" + str(arrayTAG) + "\' where idProduto =" + str(idProduto) + ";")
    #     self.conn.commit()
    #
    # def atualizeProdutoCategoria(self, idProduto, categoria):
    #     self.cur.execute(
    #         "update produto set categoria = \'" + categoria + "\' where idProduto =" + str(idProduto) + ";")
    #     self.conn.commit()
    #
    # def devolveProdutos(self):
    #     self.cur.execute("select idProduto, arrayTAG, categoria from produto order by vizualizado desc;")
    #     return self.cur.fetchall()
    #
    # def devolveProdutosPorCategoria(self, categoria):
    #     self.cur.execute(
    #         "select idProduto, arrayTAG from produto where categoria = \'" + categoria + "\' order by vizualizado desc;")
    #     return self.cur.fetchall()
    #
    # def devolveProdutoComIntervaloDePreco(self, min_preco, max_preco):
    #     self.cur.execute("select idProduto, arrayTAG, preco from produto where preco between "
    #                      + str(min_preco) + " and " + str(max_preco) + " order by vizualizado desc;")
    #     return self.cur.fetchall()
    #
    # def devolveProdutoComIntervaloDePrecoECategoria(self, min_preco, max_preco, categoria):
    #     self.cur.execute("select idProduto, arrayTAG from produto where categoria = \'" + categoria + "\' and "
    #                      + "preco between " + str(min_preco) + " and " + str(max_preco) + " order by vizualizado desc;")
    #     return self.cur.fetchall()


# bd = AcessaBD()
# texto = 'Depois de já haver retornado ao Brasil, foi preso durante escala na Ucrânia a caminho de suposta oportunidade de emprego em 2016 e condenado a treze anos de prisão por terrorismo e formação de organização paramilitar ilegal no ano seguinte. Ainda em 2017, foi provisoriamente liberto em Tribunal de Apelação, havendo controvérsias em relação aos reais motivos, e refugiou-se no Mosteiro da Santa Intercessão, em Holosiivski. Em 4 de maio de 2018, após ter seu paradeiro divulgado pela mídia, foi capturado pelos grupos Batalhão Azov e S14, que questionavam sua soltura, e levado às autoridades, que continuamente decretaram sua detenção provisória até ser condenado em 2 de maio do ano seguinte a 13 anos de prisão'
# print(bd)
# bd.inserir_texto(texto, 'dhgh')
# bd.inserirProduto(6, 'blusa', [1.00000002,-2.25896354,3,5,9,1,2,3,5,5,2,2,3,5,9,1,2,3,5,5,2,2,3,5,
# 9,1,2,3,5,5,2,2,3,5,9,1,2,3,5,5,2,2,3,5,9,1,2,3,5,5],20.20)
# rows = bd.devolveBuscasRecentesCliente(2, 2
# bd.atualizeProdutoTags(6, [0.55556, 1.00004484])
# rows = bd.devolveProdutoComIntervaloDePreco(30, 100)
# rows = bd.devolveProdutosPorCategoria('saia')
# for row in rows:
#     print(row)
# print(rows)