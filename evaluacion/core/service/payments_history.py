import random
class PaymentHistoryService:
    def find_by_dni(self,identification):
        
        lista = []
        
        for _ in range(0, random.randint(0, 150)):

            data = {
                'invoice_number': random.randint(0, 1000),
                'status': random.choice(['pagado a tiempo', 'pagado atrasado', 'no pagado']),
                'value_paid': random.randint(0, 1000),
                'value_to_pay': random.randint(0, 1000),
                'payment_date': '2021-01-01',
                'due_date': '2021-01-01',
            }
            lista.append(data)
        
        return lista
    def calculate(self,identification):
        
        lista = self.find_by_dni(identification)
        
        total = 0

        total = len(lista)
        total_ontime = 0
        for item in lista:
            if item['status'] == 'pagado a tiempo':
                total_ontime += 1
        if total == 0 or total_ontime == 0:
            return 0
        
        return total_ontime / total
