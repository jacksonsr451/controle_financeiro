# Controle Financeiro

Projeto proposto pela Alura Challend Backend.

# Utilizando

- Dokerfile: docker
- docker-compose
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- flask-marshmallow
- marshmallow-sqlalchemy
- marshmallow-enum
- Flask-JWT-Extended
- gunicorn

Projeto bem bacana para se trabalhar, utilizando conseitos de login com jwt. Efetuei o vinculo de usuário a cada um dos modelos através do login, pegando o e-mail e assim tendo o id de usuário para cadastrar cada despesa ou receita.


# Login

``` http://localhost:5500/api/v1/auth/login ```

```json
{
    "email": "email@email.com",
    "password": "123456"
}
```

caso de sucesso deve se retornar um novo token

```json
{
    "token": "eyJ0eXAiOiJAL1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MDc4ODg3NSlkanRpIjoiNzgzNTAyMzYtYzRhYS00NDRmLWE1OGEtOGQwMDliNjFmNzgwIiwidHlaTSI6ImFjY2VzcyIsInN1YiI6eyJlbWFpbCI6ImphY2tzb25zcjQ1MUBnbWFpbC5ja20ifSwibmJmIjoxNjYwNzg4ODc1LCJleHAiOjE2NjA3OTYwNzV9.SgX6-LH4G5lEwGMltxUxi6Zjd80Vn84VPIO10lkq_Ro"
}
```

caso de erro

```json
{
    "error": "Erro ao tentar login!"
}
```

a cada rota da api deve ser entregue o TOKEN meno para cadastro de usuário.

``` Authorization: Bearer meu-token ```

```py 
    @classmethod
    def add_user_id(cls, user_id):
        cls.user_id = user_id
        return cls
```

Assim ao controlador chamar o model é passado a ele o usuário que esta utilizando para efetuar o cadastro de uma receita ou despesa.

```py
from flask_jwt_extended import get_jwt_identity

def meu_controller(self):
    user = UserModel.get_user_by_email(email=get_jwt_identity()["email"])

    DespesasModel.add_user_id(user_id=user.id).add(request=req_request)

    ReceitasModel.add_user_id(user_id=user.id).add(request=req_request)
```

# Rotas

**Por padrão as Rotas da api se iniciam como** /api/v1

- ```/api/v1/receitas```
- ```/api/v1/receitas?descricao=??```
- ```/api/v1/receitas/<id>```
- ```/api/v1/receitas/<ano>/<mes>```
- ```/api/v1/despesas```
- ```/api/v1/despesas?descricao=??```
- ```/api/v1/despesas/<id>```
- ```/api/v1/despesas/<ano>/<mes>```
- ```/api/v1/resumo/<ano>/<mes>```
- ```/api/v1/usuarios```
- ```/api/v1/usuarios/<id>```
- ```/api/v1/auth/login```

### exemplos:

no caso de localhost é porta 5000:

### Adcionar uma receita

- ```http://localhost.5000/api/v1/receitas```

metodo POST com campos obrigatorios (descrição, valor, data), no formato json

```json
{
    "descricao": "Minha descrição de receita",
    "valor": "1000,00",
    "data": "2022-08-02 19:43:10"
}
```

caso de SUCESSO

```json
{
	"message": "Dados inseridos com sucesso"
}
```

caso ERRO

```json
{
    "error": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"
}
```

### Visualizar todas as receita

- ```http://localhost.5000/api/v1/receitas```

metodo GET, visualização em json

caso tenha REGISTROS

```json
[
    {
        "id": 1,
        "descricao": "Minha descrição de receita",
        "valor": "1000,00",
        "data": "2022-08-02 19:43:10"
    },
    {
        "id": 2,
        "descricao": "Minha descrição 2 de receita",
        "valor": "1000,00",
        "data": "2022-08-02 19:43:10"
    }
]
```

caso não tenha REGISTOS

```json
{
    "error": "Não há registros em receitas"
}
```

### Deletar receita

- ```http://localhost.5000/api/v1/receitas/1```

metodo DELETE, visualização em json

caso SUCESSO

```json
{
    "message": "Registro deletado com sucesso para o id: 1"
}
```

caso ERRO

```json
{
    "error": "Registro não existe para este id: 1"
}
```

### Visualizar uma receita

- ```http://localhost.5000/api/v1/receitas/1```

metodo GET, visualização em json

```json
{
    "id": 1,
    "descricao": "Minha descrição de receita",
    "valor": "1000,00",
    "data": "2022-08-02 19:43:10"
}
```

### Atualizar uma receita

- ```http://localhost.5000/api/v1/receitas/1```

metodo PUT com campos obrigatorios (descrição, valor, data), no formato json

```json
{
    "descricao": "Minha descrição atualizada de receita",
    "valor": "1000,00",
    "data": "2022-08-02 19:43:10"
}
```

visualização de resultado com json

caso SUCESSO

```json
{
	"message": "Dados atualizado"
}
```

caso não encontre REGISTO

```json
{
	"error": "Não há registro para receita de id: 1"
}
```

caso ERRO

```json
{
	"message": "Erro ao alualizar receita de id: 1"
}
```

### Adcionar uma despesas

- ```http://localhost.5000/api/v1/despesas```

metodo POST com campos obrigatorios (descrição, valor, data), no formato json

```json
{
    "descricao": "Minha descrição de receita",
    "valor": "1000,00",
    "data": "2022-08-02 19:43:10"
}
```

visualizando resultado em json

caso de SUCESSO

```json
{
	"message": "Dados inseridos com sucesso"
}
```

caso ERRO

```json
{
    "message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"
}
```

### Visualizar todas as despesas

- ```http://localhost.5000/api/v1/despesas```

metodo GET, visualização em json

caso tenha REGISTROS

```json
[
    {
        "id": 1,
        "descricao": "Minha descrição de despesa",
        "valor": "1000,00",
        "data": "2022-08-02 19:43:10"
    },
    {
        "id": 2,
        "descricao": "Minha descrição 2 de despesa",
        "valor": "1000,00",
        "data": "2022-08-02 19:43:10"
    }
]
```

caso não tenha REGISTOS

```json
{
    "message": "Não há registros em receitas"
}
```

### Deletar despesa

- ```http://localhost.5000/api/v1/despesas/1```

metodo DELETE, visualização em json

caso SUCESSO

```json
{
    "message": "Registro deletado com sucesso para o id: 1"
}
```

caso ERRO

```json
{
    "message": "Registro não existe para este id: 1"
}
```

### Visualizar uma despesa

- ```http://localhost.5000/api/v1/despesas/1```

metodo GET, visualização em json

```json
{
    "id": 1,
    "descricao": "Minha descrição de despesa",
    "valor": "1000,00",
    "data": "2022-08-02 19:43:10"
}
```

### Atualizar uma despesa

- ```http://localhost.5000/api/v1/despesas/1```

metodo PUT com campos obrigatorios (descrição, valor, data), no formato json

```json
{
    "descricao": "Minha descrição atualizada de despesa",
    "valor": "1000,00",
    "data": "2022-08-02 19:43:10"
}
```

visualização de resulta com json

caso SUCESSO

```json
{
	"message": "Dados atualizado"
}
```

caso não encontre REGISTO

```json
{
	"message": "Não há registro para despesa de id: 1"
}
```

caso ERRO

```json
{
	"message": "Erro ao alualizar despesa de id: 1"
}
```
