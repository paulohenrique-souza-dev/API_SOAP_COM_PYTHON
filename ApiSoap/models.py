from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, ComplexModel
from spyne.protocol.soap import Soap11




class Fornecedor(ComplexModel):
    id_fornecedor = Integer
    nome_fornecedor = Unicode
    cidade = Unicode
    estado = Unicode


class Categoria(ComplexModel):
    id_categoria = Integer
    nome_categoria = Unicode


class Cliente(ComplexModel):
    id_cliente = Integer
    nome = Unicode
    cidade = Unicode
    data_cadastro = Unicode
    tipo_cliente = Unicode


class Vendedor(ComplexModel):
    id_vendedor = Integer
    nome = Unicode
    regiao = Unicode
    salario = Unicode
    data_admissao = Unicode


class Produto(ComplexModel):
    id_produto = Integer
    nome_produto = Unicode
    preco = Unicode
    custo = Unicode
    id_categoria = Integer
    id_fornecedor = Integer


class Estoque(ComplexModel):
    id_estoque = Integer
    quantidade = Unicode
    estoque_minimo = Unicode
    data_atualizacao = Unicode
    id_produto = Integer


class Pedido(ComplexModel):
    id_pedido = Integer
    data_pedido = Unicode
    status_pedido = Unicode
    id_cliente = Integer
    id_vendedor = Integer


class ItemPedido(ComplexModel):
    id_item = Integer
    quantidade = Unicode
    valor_unitario = Unicode
    id_pedido = Integer
    id_produto = Integer