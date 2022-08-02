# Controle Financeiro

Projeto proposto pela Alura Challend Backend.

## Rotas

**Por padrão as Rotas da api se iniciam como** /api/v1

- /receitas
- /receitas/<id>
- /despesas
- /despesas/<id>

### exemplos:

no caso de localhost e porta 5000:

Adcionar uma receita

- http://localhost.5000/api/v1/receitas

metodo POST com campos obrigatorios (descrição, valor, data), no formato json

```json
{
    "descricao": "Minha descrição de receita",
    "valor": "1000,00",
    "data": "2022-08-02 19:43:10"
}
```

Visualizar todas as receita

- http://localhost.5000/api/v1/receitas

metodo GET, visualização em json

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

Deletar receita

- http://localhost.5000/api/v1/receitas/1

metodo DELETE, visualização em json

```json
{
    "message": "Registro deletado com sucesso para o id: 1"
}
```

Visualizar uma receita

- http://localhost.5000/api/v1/receitas/1

metodo GET, visualização em json

```json
{
    "id": 1,
    "descricao": "Minha descrição de receita",
    "valor": "1000,00",
    "data": "2022-08-02 19:43:10"
}
```

Atualizar uma receita

- http://localhost.5000/api/v1/receitas/1

metodo PUT com campos obrigatorios (descrição, valor, data), no formato json

```json
{
    "descricao": "Minha descrição atualizada de receita",
    "valor": "1000,00",
    "data": "2022-08-02 19:43:10"
}
```

visualização de resulta com json

```json
{
	"message": "Dados atualizado"
}
```