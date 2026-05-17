#  API SOAP COM PYTHON

API SOAP corporativa desenvolvida em Python utilizando Spyne.

O projeto atua como uma camada de integração responsável por consumir uma API REST e disponibilizar os dados através de serviços SOAP/XML.

---

#  Objetivo

O objetivo deste projeto é demonstrar a integração entre arquiteturas modernas REST e sistemas legados/baseados em SOAP, simulando cenários reais utilizados em ambientes corporativos.

A API SOAP realiza:

* Consumo de uma API REST
* Conversão REST → SOAP
* Serialização XML
* Paginação automática
* CRUDs empresariais
* Integração entre protocolos

---

#  Arquitetura

```txt id="yut6wg"
Cliente SOAP
      ↓
API SOAP (Spyne)
      ↓
API REST Django
      ↓
Banco de Dados
```

---

# ⚙️ Tecnologias Utilizadas

* Python
* Spyne
* Zeep
* Flask
* Requests
* Django REST Framework
* XML SOAP
* REST API

---

# Funcionalidades
---
## Clientes

* GetClientes
* GetClienteById
* CreateCliente
* UpdateCliente
* DeleteCliente

---

## Produtos

* GetProdutos
* GetProdutoById
* CreateProduto
* UpdateProduto
* DeleteProduto

---

## Pedidos

* GetPedidos
* GetPedidoById
* CreatePedido
* UpdatePedido
* DeletePedido

---

## Estoque

* GetEstoque
* GetEstoqueById
* CreateEstoque
* UpdateEstoque
* DeleteEstoque

---

## Categorias

* GetCategorias
* GetCategoriaById
* CreateCategoria
* UpdateCategoria
* DeleteCategoria

---

## Fornecedores

* GetFornecedores
* GetFornecedorById
* CreateFornecedor
* UpdateFornecedor
* DeleteFornecedor

---

## Vendedores

* GetVendedores
* GetVendedorById
* CreateVendedor
* UpdateVendedor
* DeleteVendedor

---

## Itens do Pedido

* GetItensPedido
* GetItemPedidoById
* CreateItemPedido
* UpdateItemPedido
* DeleteItemPedido

---

# 🌐 Integração REST → SOAP

A API SOAP consome internamente uma API REST paginada desenvolvida em Django REST Framework.


O projeto realiza:

* Paginação automática
* Conversão JSON → XML SOAP
* Tratamento de respostas
* Integração entre protocolos
* Padronização de payloads

---

# 📂 Estrutura do Projeto

```txt id="5rqf28"
API_SOAP_COM_PYTHON/
│
├── app.py
├── services/
├── models/
├── config.py
├── requirements.txt
├── soap_client.py
└── README.md
```

---

# 🚀 Como Executar

## 1️⃣ Clone o projeto com :

```bash id="xhjtmz"
git clone https://github.com/paulohenrique-souza-dev/API_SOAP_COM_PYTHON.git
```

---

## 2️⃣ Entre na pasta

```bash id="y9hlfd"
cd ApiSoap
```

---

## 3️⃣ Crie ambiente virtual

```bash id="0m8r6y"
python -m venv venv
```


---

## 4️⃣ Ative o ambiente virtual

```bash id="pljlwm"
venv\Scripts\activate
```

## 5️⃣ Instale as dependências

```bash id="4mhvxf"
pip install -r requirements.txt
```

---

## 6️⃣ Execute o projeto

```bash id="i4k1k8"
python app.py
```

---

#  WSDL em :

```txt id="9f9d5s"
http://localhost:8000/?wsdl
```


---

# 💡 Conceitos Aplicados

* SOAP/XML
* REST APIs
* Middleware
* Integração de sistemas
* Serialização XML
* APIs corporativas
* Arquitetura distribuída
* Serviços empresariais
* Paginação REST
* Conversão de protocolos

---

# Mais um projeto, até a próxima!


