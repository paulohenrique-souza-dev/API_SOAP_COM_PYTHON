from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import requests
from servicossoap import ServicosApiSoap, get_results, get_one, create_item, update_item, delete_item

from models import Produto, Estoque, Vendedor, Cliente, Categoria, Fornecedor, Pedido, ItemPedido






soap_application = Application(
    [ServicosApiSoap],
    tns="http://sgp.enterprise.soap",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)


class CORSMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        origin = environ.get("HTTP_ORIGIN", "*")
        cors_headers = [
            ("Access-Control-Allow-Origin", origin),
            ("Access-Control-Allow-Methods", "POST, GET, OPTIONS"),
            ("Access-Control-Allow-Headers", "Content-Type, SOAPAction, X-Requested-With"),
            ("Access-Control-Max-Age", "86400"),
        ]

        if environ.get("REQUEST_METHOD") == "OPTIONS":
            start_response("204 No Content", cors_headers)
            return [b""]

        def custom_start_response(status, headers, exc_info=None):
            existing = {h[0].lower() for h in headers}
            for key, value in cors_headers:
                if key.lower() not in existing:
                    headers.append((key, value))
            return start_response(status, headers, exc_info)

        return self.app(environ, custom_start_response)


application = CORSMiddleware(WsgiApplication(soap_application))


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    print("SOAP rodando em http://localhost:8000")
    print("WSDL em http://localhost:8000/?wsdl")
    server = make_server("0.0.0.0", 8000, application)
    server.serve_forever()
