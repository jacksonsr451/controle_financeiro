from flask_restful import reqparse


class UsersRequest:
    def __init__(self):
        self.request = reqparse.RequestParser()
        self.request.add_argument(
            'username',
            type=str,
            help='Username é um campor obrigatório e do tipo str.',
            required=True,
        )
        self.request.add_argument(
            'email',
            type=str,
            help='E-mail é um campor obrigatório e do tipo str.',
            required=True,
        )
        self.request.add_argument('password', required=False)

    @staticmethod
    def get():
        return UsersRequest().request.parse_args()
