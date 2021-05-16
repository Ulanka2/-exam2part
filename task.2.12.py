class Monitoring:
    money = 0
    maker = 58
    def __init__(self, name, lastname, id):
        self.name = name
        self.lastname = lastname
        self.id = id
    
    def info(self):
        print(f"Имя –{self.name, self.lastname}\nПерсональный номер - {self.id}")
    
    def salary(self,fix_salary, hour):
        self.hour = hour
        self.fix_salary = fix_salary
        print(f'Одного менеджера -\nЗП – {self.fix_salary}\nКоличество проработанных часов за последнюю неделю -{self.hour}')
        Monitoring.money += self.fix_salary
    
    def salary1(self, salare, sales, hourr, comis=50):
        self.salare = salare
        self.sales = sales
        self.hourr = hourr
        self.salare = self.salare + (comis * self.sales)
        print(f'Одного продавца -\nФиксированная зп – {self.salare} \nКол-во произведенных продаж – {self.sales}\nКоличество проработанных часов за последнюю неделю -{self.hourr}') 
        Monitoring.money += self.salare
    
    def salary2(self, hour_work, hour=100):
        self.hour_work = hour_work
        hour_work = self.hour_work * hour
        print(f'Количество проработанных часов за последнюю неделю:{self.hour_work}\nПочасовой оклад {hour_work}')
        Monitoring.money += hour_work
        Monitoring.maker -= self.hour_work
    
    def howMany():
        '''Выводит summu trata company.'''
        print(f'Company potratila { Monitoring.money} somov.')
        print(f'Cамый продуктивный Алтынай Ширинбаева{Monitoring.maker} часов работы.')
        print(f'Cамый непродуктивный  Барсбек Канаткулов - 18 часов работы.')
    howMany = staticmethod(howMany)

class Manager(Monitoring):

    def __init__(self, name, lastname, id):
        super().__init__(name, lastname, id)

class Secretar(Monitoring):

    def __init__(self, name, lastname, id):
        super().__init__(name, lastname, id)

    def salary(self,fix_salary, hour):
        self.hour = hour
        self.fix_salary = fix_salary
        print(f'Одного секретаря -\nЗП – {self.fix_salary}\nКоличество проработанных часов за последнюю неделю -{self.hour}')
        Monitoring.money += self.fix_salary

class Seller(Monitoring):

    def __init__(self, name, lastname, id):
        super().__init__(name, lastname, id)

class Worker(Monitoring):

    def __init__(self, name, lastname, id):
        super().__init__(name, lastname, id)



print("----------------------------------------")
manager = Manager("Барсбек", "Канаткулов", 1)
manager.info()
manager.salary(45000, 18)
print("----------------------------------------")
secretar = Secretar('Алымкул', 'Тилекбаев', 2)
secretar.info()
secretar.salary(45000, 38)
print("----------------------------------------")
seler = Seller('Айпери', 'Шалымбекова', 3)
seler.info()
seler.salary1(20000, 20, 38)
print("----------------------------------------")
print('Двух работников цеха -')
worker = Worker('Бакыт', 'Рустамов', 4)
worker.info()
worker.salary2(25)
print("----------------------------------------")
worker = Worker('Алтынай', 'Ширинбаева', 5)
worker.info()
worker.salary2(40)
print('---------------------------------------------')
print('Одного секретаря на замену')
worker = Worker('Жанар', 'Рыскулов', 6)
worker.info()
worker.salary2(33)
print('----------------------------------------------')
Monitoring.howMany()
