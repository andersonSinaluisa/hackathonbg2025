


from core.service.score_buro import ScoreBuroService

from core.service.income import IncomeService
from core.service.payments_history import PaymentHistoryService
from core.service.sn_score import SocialScoreService

class CalculateScoreService:
    
    W_INCOME = 0.3
    W_PAYMENT = 0.3
    W_SOCIAL = 0.15
    W_ONLINE = 0.15
    W_UBICACION = 0.10
    
    
    
    def __init__(self):
        self.score_buro = ScoreBuroService()
        self.income = IncomeService()
        self.payment = PaymentHistoryService()
        self.social = SocialScoreService()
    


    def calculate(self, identification, income_value, username_social):
        score_buro = self.score_buro.calculate(identification)
        income = self.income.calculate(income_value)
        payment = self.payment.calculate(identification)
        social = self.social.calculate(username_social)
        online =  0.54
        ubicacion = 0.78
        
        
        
        score = (
            self.W_INCOME * income +
            self.W_PAYMENT * payment +
            self.W_SOCIAL * social +
            self.W_ONLINE * online +
            self.W_UBICACION * ubicacion
            
        ) * 1000
        
        return {
            'score': score,
            'score_buro': score_buro,
            'income': income,
            'payment': payment,
            'social': social,
            'online': online,
            'ubicacion': ubicacion
        }
        
        