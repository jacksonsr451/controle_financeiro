from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.models.despesas_model import DespesasModel
from app.models.receitas_model import ReceitasModel



class Resumo(Resource):
    @jwt_required()
    def get(self, ano, mes):
        total_receitas = self.get_total_receitas(ano, mes)
        total_despesas = self.get_total_despesas(ano, mes)
        saldo_final = total_receitas - total_despesas
        total_gasto_por_categoria = self.get_total_gasto_por_categoria(ano, mes); 
        return jsonify({
            "total receitas": "{:.2f}".format(total_receitas).replace(".", ","),
            "total despesas": "{:.2f}".format(total_despesas).replace(".", ","),
            "saldo final": "{:.2f}".format(saldo_final).replace(".", ","),
            "total gasto por categoria": total_gasto_por_categoria
        })
        
    
    def get_total_despesas(self, ano, mes):
        despesas = DespesasModel.filter_by_ano_and_mes(ano=ano, mes=mes)
        value: float = 0
        for row in despesas:
            value += float(row.valor.replace(",", "."))
        return value
        
    
    def get_total_receitas(self, ano, mes):
        receitas = ReceitasModel.filter_by_ano_and_mes(ano=ano, mes=mes)
        value: float = 0
        for row in receitas:
            value += float(row.valor.replace(",", "."))
        return value
    
    
    def get_total_gasto_por_categoria(self, ano, mes):
        despesas = DespesasModel.filter_by_ano_and_mes(ano=ano, mes=mes)
        dict_categorias = self.get_dict_categorias()
        for row in despesas:
            dict_categorias[row.categoria.value] += float(row.valor.replace(",", "."))
        return self.pass_by_string_values_categoria(dict_categorias)
    
    
    @staticmethod
    def pass_by_string_values_categoria(dict_categoria):
        dict_categoria["Alimentação"] = "{:.2f}".format(dict_categoria["Alimentação"]).replace(".", ",")
        dict_categoria["Saúde"] = "{:.2f}".format(dict_categoria["Saúde"]).replace(".", ",")
        dict_categoria["Moradia"] = "{:.2f}".format(dict_categoria["Moradia"]).replace(".", ",")
        dict_categoria["Transporte"] = "{:.2f}".format(dict_categoria["Transporte"]).replace(".", ",")
        dict_categoria["Educação"] = "{:.2f}".format(dict_categoria["Educação"]).replace(".", ",")
        dict_categoria["Lazer"] = "{:.2f}".format(dict_categoria["Lazer"]).replace(".", ",")
        dict_categoria["Imprevistos"] = "{:.2f}".format(dict_categoria["Imprevistos"]).replace(".", ",")
        dict_categoria["Outras"] = "{:.2f}".format(dict_categoria["Outras"]).replace(".", ",")
        return dict_categoria
    
    
    @staticmethod
    def get_dict_categorias() -> dict:
        return {
            "Alimentação": 0.00,
            "Saúde": 0.00,
            "Moradia": 0.00,
            "Transporte": 0.00,
            "Educação": 0.00,
            "Lazer": 0.00,
            "Imprevistos": 0.00,
            "Outras": 0.00
        }
    