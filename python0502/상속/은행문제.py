class Bank:
    def 대출이자를받다(self):
        return 0

class Bad_bank(Bank):
    def 대출이자를받다(self):
        return 0.1

class Normal_bank(Bank):
    def 대출이자를받다(self):
        return 0.05

class Good_bank(Bank):
    def 대출이자를받다(self):
        return 0.02


bad = Bad_bank()
normal = Normal_bank()
good = Good_bank()

print('bad bank이자율', bad.대출이자를받다())
print('normal bank이자율', normal.대출이자를받다())
print('good bank이자율', good.대출이자를받다())



