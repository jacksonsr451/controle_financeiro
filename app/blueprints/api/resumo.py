from flask import jsonify, request
from flask_restful import Resource, reqparse



class Resumo(Resource):
    def get(self, ano, mes):
        total_receitas = self.get_total_receitas(ano, mes)
        total_despesas = self.get_total_despesas(ano, mes)
        saldo_final = total_receitas - total_despesas
        total_gasto_por_categoria = self.get_total_gasto_por_categoria(ano, mes); 
        return jsonify({
            "total receitas": total_receitas,
            "total despesas": total_despesas,
            "saldo final": saldo_final,
            "total gasto por categoria": total_gasto_por_categoria
        })
        
    
    def get_total_despesas(self, ano, mes):
        pass
    
    
    def get_total_receitas(self, ano, mes):
        pass
    
    
    def get_total_gasto_por_categoria(self, ano, mes):
        pass
    