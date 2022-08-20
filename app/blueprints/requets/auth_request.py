from flask_restful import reqparse


class AuthRequest:
    def __init__(self):
        self.request = reqparse.RequestParser()
        self.request.add_argument(
            'email',
            type=str,
            help='E-mail é um campor obrigatório e do tipo str.',
            required=True,
        )
        self.request.add_argument(
            'password',
            type=str,
            help='Password é um campor obrigatório e do tipo str.',
            required=False,
        )

    @staticmethod
    def get():
        return AuthRequest().request.parse_args()
