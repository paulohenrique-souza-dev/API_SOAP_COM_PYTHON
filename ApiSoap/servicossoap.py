from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, ComplexModel
from spyne.protocol.soap import Soap11
import requests
from spyne.server.wsgi import WsgiApplication



from models import Produto, Estoque, Vendedor, Cliente, Categoria, Fornecedor, Pedido, ItemPedido
BASE_URL = "https://apirest01.pythonanywhere.com/api"




class ResponseMessage(ComplexModel):
    status = Unicode
    mensagem = Unicode






def get_results(endpoint):
    url = f"{BASE_URL}/{endpoint}/"
    resultados = []
    limite_paginas = 100
    pagina = 0

    while url and pagina < limite_paginas:
        r = requests.get(url, timeout=20)
        r.raise_for_status()

        data = r.json()

        if isinstance(data, dict) and "results" in data:
            resultados.extend(data.get("results", []))
            url = data.get("next")
        elif isinstance(data, list):
            resultados.extend(data)
            url = None
        else:
            resultados.append(data)
            url = None

        pagina += 1

    return resultados


def get_one(endpoint, id_value):
    r = requests.get(f"{BASE_URL}/{endpoint}/{id_value}/", timeout=20)
    r.raise_for_status()
    return r.json()


def create_item(endpoint, payload):
    try:
        r = requests.post(f"{BASE_URL}/{endpoint}/", json=payload, timeout=20)
        if r.status_code in [200, 201]:
            return ResponseMessage(status="SUCESSO", mensagem="Registro criado com sucesso")
        return ResponseMessage(status="ERRO", mensagem=r.text)
    except Exception as exc:
        return ResponseMessage(status="ERRO", mensagem=str(exc))


def update_item(endpoint, id_value, payload):
    try:
        r = requests.put(f"{BASE_URL}/{endpoint}/{id_value}/", json=payload, timeout=20)
        if r.status_code in [200, 202]:
            return ResponseMessage(status="SUCESSO", mensagem="Registro atualizado com sucesso")
        return ResponseMessage(status="ERRO", mensagem=r.text)
    except Exception as exc:
        return ResponseMessage(status="ERRO", mensagem=str(exc))


def delete_item(endpoint, id_value):
    try:
        r = requests.delete(f"{BASE_URL}/{endpoint}/{id_value}/", timeout=20)
        if r.status_code in [200, 204]:
            return ResponseMessage(status="SUCESSO", mensagem="Registro deletado com sucesso")
        return ResponseMessage(status="ERRO", mensagem=r.text)
    except Exception as exc:
        return ResponseMessage(status="ERRO", mensagem=str(exc))




class ServicosApiSoap(ServiceBase):
    @rpc(_returns=Iterable(Fornecedor))
    def GetFornecedores(ctx):
        for item in get_results("fornecedores"):
            yield Fornecedor(id_fornecedor=item.get("id_fornecedor"), nome_fornecedor=item.get("nome_fornecedor"), cidade=item.get("cidade"), estado=item.get("estado"))

    @rpc(Integer, _returns=Fornecedor)
    def GetFornecedorById(ctx, id_fornecedor):
        item = get_one("fornecedores", id_fornecedor)
        return Fornecedor(id_fornecedor=item.get("id_fornecedor"), nome_fornecedor=item.get("nome_fornecedor"), cidade=item.get("cidade"), estado=item.get("estado"))

    @rpc(Unicode, Unicode, Unicode, _returns=ResponseMessage)
    def CreateFornecedor(ctx, nome_fornecedor, cidade, estado):
        return create_item("fornecedores", {"nome_fornecedor": nome_fornecedor, "cidade": cidade, "estado": estado})

    @rpc(Integer, Unicode, Unicode, Unicode, _returns=ResponseMessage)
    def UpdateFornecedor(ctx, id_fornecedor, nome_fornecedor, cidade, estado):
        return update_item("fornecedores", id_fornecedor, {"nome_fornecedor": nome_fornecedor, "cidade": cidade, "estado": estado})

    @rpc(Integer, _returns=ResponseMessage)
    def DeleteFornecedor(ctx, id_fornecedor):
        return delete_item("fornecedores", id_fornecedor)

    @rpc(_returns=Iterable(Categoria))
    def GetCategorias(ctx):
        for item in get_results("categorias"):
            yield Categoria(id_categoria=item.get("id_categoria"), nome_categoria=item.get("nome_categoria"))

    @rpc(Integer, _returns=Categoria)
    def GetCategoriaById(ctx, id_categoria):
        item = get_one("categorias", id_categoria)
        return Categoria(id_categoria=item.get("id_categoria"), nome_categoria=item.get("nome_categoria"))

    @rpc(Unicode, _returns=ResponseMessage)
    def CreateCategoria(ctx, nome_categoria):
        return create_item("categorias", {"nome_categoria": nome_categoria})

    @rpc(Integer, Unicode, _returns=ResponseMessage)
    def UpdateCategoria(ctx, id_categoria, nome_categoria):
        return update_item("categorias", id_categoria, {"nome_categoria": nome_categoria})

    @rpc(Integer, _returns=ResponseMessage)
    def DeleteCategoria(ctx, id_categoria):
        return delete_item("categorias", id_categoria)

    @rpc(_returns=Iterable(Cliente))
    def GetClientes(ctx):
        for item in get_results("cliente"):
            yield Cliente(id_cliente=item.get("id_cliente"), nome=item.get("nome"), cidade=item.get("cidade"), data_cadastro=item.get("data_cadastro"), tipo_cliente=item.get("tipo_cliente"))

    @rpc(Integer, _returns=Cliente)
    def GetClienteById(ctx, id_cliente):
        item = get_one("cliente", id_cliente)
        return Cliente(id_cliente=item.get("id_cliente"), nome=item.get("nome"), cidade=item.get("cidade"), data_cadastro=item.get("data_cadastro"), tipo_cliente=item.get("tipo_cliente"))

    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=ResponseMessage)
    def CreateCliente(ctx, nome, cidade, data_cadastro, tipo_cliente):
        return create_item("cliente", {"nome": nome, "cidade": cidade, "data_cadastro": data_cadastro, "tipo_cliente": tipo_cliente})

    @rpc(Integer, Unicode, Unicode, Unicode, Unicode, _returns=ResponseMessage)
    def UpdateCliente(ctx, id_cliente, nome, cidade, data_cadastro, tipo_cliente):
        return update_item("cliente", id_cliente, {"nome": nome, "cidade": cidade, "data_cadastro": data_cadastro, "tipo_cliente": tipo_cliente})

    @rpc(Integer, _returns=ResponseMessage)
    def DeleteCliente(ctx, id_cliente):
        return delete_item("cliente", id_cliente)

    @rpc(_returns=Iterable(Vendedor))
    def GetVendedores(ctx):
        for item in get_results("vendedores"):
            yield Vendedor(id_vendedor=item.get("id_vendedor"), nome=item.get("nome"), regiao=item.get("regiao"), salario=item.get("salario"), data_admissao=item.get("data_admissao"))

    @rpc(Integer, _returns=Vendedor)
    def GetVendedorById(ctx, id_vendedor):
        item = get_one("vendedores", id_vendedor)
        return Vendedor(id_vendedor=item.get("id_vendedor"), nome=item.get("nome"), regiao=item.get("regiao"), salario=item.get("salario"), data_admissao=item.get("data_admissao"))

    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=ResponseMessage)
    def CreateVendedor(ctx, nome, regiao, salario, data_admissao):
        return create_item("vendedores", {"nome": nome, "regiao": regiao, "salario": salario, "data_admissao": data_admissao})

    @rpc(Integer, Unicode, Unicode, Unicode, Unicode, _returns=ResponseMessage)
    def UpdateVendedor(ctx, id_vendedor, nome, regiao, salario, data_admissao):
        return update_item("vendedores", id_vendedor, {"nome": nome, "regiao": regiao, "salario": salario, "data_admissao": data_admissao})

    @rpc(Integer, _returns=ResponseMessage)
    def DeleteVendedor(ctx, id_vendedor):
        return delete_item("vendedores", id_vendedor)

    @rpc(_returns=Iterable(Produto))
    def GetProdutos(ctx):
        for item in get_results("produto"):
            yield Produto(id_produto=item.get("id_produto"), nome_produto=item.get("nome_produto"), preco=item.get("preco"), custo=item.get("custo"), id_categoria=item.get("id_categoria"), id_fornecedor=item.get("id_fornecedor"))

    @rpc(Integer, _returns=Produto)
    def GetProdutoById(ctx, id_produto):
        item = get_one("produto", id_produto)
        return Produto(id_produto=item.get("id_produto"), nome_produto=item.get("nome_produto"), preco=item.get("preco"), custo=item.get("custo"), id_categoria=item.get("id_categoria"), id_fornecedor=item.get("id_fornecedor"))

    @rpc(Unicode, Unicode, Unicode, Integer, Integer, _returns=ResponseMessage)
    def CreateProduto(ctx, nome_produto, preco, custo, id_categoria, id_fornecedor):
        return create_item("produto", {"nome_produto": nome_produto, "preco": preco, "custo": custo, "id_categoria": id_categoria, "id_fornecedor": id_fornecedor})

    @rpc(Integer, Unicode, Unicode, Unicode, Integer, Integer, _returns=ResponseMessage)
    def UpdateProduto(ctx, id_produto, nome_produto, preco, custo, id_categoria, id_fornecedor):
        return update_item("produto", id_produto, {"nome_produto": nome_produto, "preco": preco, "custo": custo, "id_categoria": id_categoria, "id_fornecedor": id_fornecedor})

    @rpc(Integer, _returns=ResponseMessage)
    def DeleteProduto(ctx, id_produto):
        return delete_item("produto", id_produto)

    @rpc(_returns=Iterable(Estoque))
    def GetEstoque(ctx):
        for item in get_results("estoque"):
            yield Estoque(id_estoque=item.get("id_estoque"), quantidade=item.get("quantidade"), estoque_minimo=item.get("estoque_minimo"), data_atualizacao=item.get("data_atualizacao"), id_produto=item.get("id_produto"))

    @rpc(Integer, _returns=Estoque)
    def GetEstoqueById(ctx, id_estoque):
        item = get_one("estoque", id_estoque)
        return Estoque(id_estoque=item.get("id_estoque"), quantidade=item.get("quantidade"), estoque_minimo=item.get("estoque_minimo"), data_atualizacao=item.get("data_atualizacao"), id_produto=item.get("id_produto"))

    @rpc(Unicode, Unicode, Unicode, Integer, _returns=ResponseMessage)
    def CreateEstoque(ctx, quantidade, estoque_minimo, data_atualizacao, id_produto):
        return create_item("estoque", {"quantidade": quantidade, "estoque_minimo": estoque_minimo, "data_atualizacao": data_atualizacao, "id_produto": id_produto})

    @rpc(Integer, Unicode, Unicode, Unicode, Integer, _returns=ResponseMessage)
    def UpdateEstoque(ctx, id_estoque, quantidade, estoque_minimo, data_atualizacao, id_produto):
        return update_item("estoque", id_estoque, {"quantidade": quantidade, "estoque_minimo": estoque_minimo, "data_atualizacao": data_atualizacao, "id_produto": id_produto})

    @rpc(Integer, _returns=ResponseMessage)
    def DeleteEstoque(ctx, id_estoque):
        return delete_item("estoque", id_estoque)

    @rpc(_returns=Iterable(Pedido))
    def GetPedidos(ctx):
        for item in get_results("pedidos"):
            yield Pedido(id_pedido=item.get("id_pedido"), data_pedido=item.get("data_pedido"), status_pedido=item.get("status_pedido"), id_cliente=item.get("id_cliente"), id_vendedor=item.get("id_vendedor"))

    @rpc(Integer, _returns=Pedido)
    def GetPedidoById(ctx, id_pedido):
        item = get_one("pedidos", id_pedido)
        return Pedido(id_pedido=item.get("id_pedido"), data_pedido=item.get("data_pedido"), status_pedido=item.get("status_pedido"), id_cliente=item.get("id_cliente"), id_vendedor=item.get("id_vendedor"))

    @rpc(Unicode, Unicode, Integer, Integer, _returns=ResponseMessage)
    def CreatePedido(ctx, data_pedido, status_pedido, id_cliente, id_vendedor):
        return create_item("pedidos", {"data_pedido": data_pedido, "status_pedido": status_pedido, "id_cliente": id_cliente, "id_vendedor": id_vendedor})

    @rpc(Integer, Unicode, Unicode, Integer, Integer, _returns=ResponseMessage)
    def UpdatePedido(ctx, id_pedido, data_pedido, status_pedido, id_cliente, id_vendedor):
        return update_item("pedidos", id_pedido, {"data_pedido": data_pedido, "status_pedido": status_pedido, "id_cliente": id_cliente, "id_vendedor": id_vendedor})

    @rpc(Integer, _returns=ResponseMessage)
    def DeletePedido(ctx, id_pedido):
        return delete_item("pedidos", id_pedido)

    @rpc(_returns=Iterable(ItemPedido))
    def GetItensPedido(ctx):
        for item in get_results("itens-pedido"):
            yield ItemPedido(id_item=item.get("id_item"), quantidade=item.get("quantidade"), valor_unitario=item.get("valor_unitario"), id_pedido=item.get("id_pedido"), id_produto=item.get("id_produto"))

    @rpc(Integer, _returns=ItemPedido)
    def GetItemPedidoById(ctx, id_item):
        item = get_one("itens-pedido", id_item)
        return ItemPedido(id_item=item.get("id_item"), quantidade=item.get("quantidade"), valor_unitario=item.get("valor_unitario"), id_pedido=item.get("id_pedido"), id_produto=item.get("id_produto"))

    @rpc(Unicode, Unicode, Integer, Integer, _returns=ResponseMessage)
    def CreateItemPedido(ctx, quantidade, valor_unitario, id_pedido, id_produto):
        return create_item("itens-pedido", {"quantidade": quantidade, "valor_unitario": valor_unitario, "id_pedido": id_pedido, "id_produto": id_produto})

    @rpc(Integer, Unicode, Unicode, Integer, Integer, _returns=ResponseMessage)
    def UpdateItemPedido(ctx, id_item, quantidade, valor_unitario, id_pedido, id_produto):
        return update_item("itens-pedido", id_item, {"quantidade": quantidade, "valor_unitario": valor_unitario, "id_pedido": id_pedido, "id_produto": id_produto})

    @rpc(Integer, _returns=ResponseMessage)
    def DeleteItemPedido(ctx, id_item):
        return delete_item("itens-pedido", id_item)