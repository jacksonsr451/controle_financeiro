from flask_restful import reqparse


class DespesasRequest:
    def __init__(self):
        self.request = reqparse.RequestParser()
        self.request.add_argument('categoria', type=str, required=False)
        self.request.add_argument(
            'descricao',
            type=str,
            help='Descricao é um campor obrigatório e do tipo str.',
            required=True,
        )
        self.request.add_argument(
            'valor',
            type=str,
            help='Valor é um campor obrigatório e do tipo str.',
            required=True,
        )
        self.request.add_argument(
            'data', help='Data é um campor obrigatório.', required=True
        )

    @staticmethod
    def get():
        return DespesasRequest().request.parse_args()
