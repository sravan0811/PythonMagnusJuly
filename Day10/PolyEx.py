class Car_2022:
    def roof(self):
        print("Sun Roof")
    def wheels(self):
        print("Normal ALloy Wheels")
    def music(self):
        print('7" Music Touch Player')
class Car_2023(Car_2022):
    def roof(self):
        print("Panaromic Sun Roof")
        super().roof()
    def music(self):
        print('11" Music Touch Player')
    def mobileConnect(self):
        print("Hyundai Blue Mobile Connect which can manage the car from mobile.")

obj1 = Car_2023()
obj1.roof()
obj1.wheels()
obj1.music()
obj1.mobileConnect()