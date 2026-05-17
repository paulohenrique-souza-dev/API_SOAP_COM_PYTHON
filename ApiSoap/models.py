from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, ComplexModel
from spyne.protocol.soap import Soap11

from spyne import (
    Application, rpc, ServiceBase,
    Integer, Unicode, Iterable, ComplexModel,
    Decimal, Date
)


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
    data_cadastro = Date
    tipo_cliente = Unicode


class Vendedor(ComplexModel):
    id_vendedor = Integer
    nome = Unicode
    regiao = Unicode
    salario = Decimal
    data_admissao = Date


class Produto(ComplexModel):
    id_produto = Integer
    nome_produto = Unicode
    preco = Decimal
    custo = Decimal
    id_categoria = Integer
    id_fornecedor = Integer


class Estoque(ComplexModel):
    id_estoque = Integer
    quantidade = Decimal
    estoque_minimo = Decimal
    data_atualizacao = Date
    id_produto = Integer


class Pedido(ComplexModel):
    id_pedido = Integer
    data_pedido = Date
    status_pedido = Unicode
    id_cliente = Integer
    id_vendedor = Integer


class ItemPedido(ComplexModel):
    id_item = Integer
    quantidade = Decimal
    valor_unitario = Decimal
    id_pedido = Integer
    id_produto = Integer
