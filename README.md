# Controle Financeiro

Projeto proposto pela Alura Challend Backend.

# Rotas

**Por padrão as Rotas da api se iniciam como** /api/v1

- ```/receitas```
- ```/receitas/<id>```
- ```/despesas```
- ```/despesas/<id>```

### exemplos:

no caso de localhost e porta 5000:

Adcionar uma receita

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
    "message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"
}
```

Visualizar todas as receita

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
    "message": "Não há registros em receitas"
}
```

Deletar receita

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
    "message": "Registro não existe para este id: 1"
}
```

Visualizar uma receita

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

## Atualizar uma receita

- ```http://localhost.5000/api/v1/receitas/1```

metodo PUT com campos obrigatorios (descrição, valor, data), no formato json

```json
{
    "descricao": "Minha descrição atualizada de receita",
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
	"message": "Não há registro para receita de id: 1"
}
```

caso ERRO

```json
{
	"message": "Erro ao alualizar receita de id: 1"
}
```

## Adcionar uma despesas

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

Visualizar todas as despesas

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

Deletar despesa

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

Visualizar uma despesa

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

Atualizar uma despesa

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
