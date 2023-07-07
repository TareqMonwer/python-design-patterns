from tower import MainBoard
from tower import Tower
from laptop import Laptop


# l1 = Laptop(model='L1', processor='Intel', memory='32GB', 
#             hard_drive='2TB SSD', graphics='onboard', screen='1920x1080')
# l1.display()

# l2 = l1.clone()
# l2.model = 'L2'
# l2.processor = 'AMD'
# l2.display()

t1 = Tower(model='Tower1', mainboard=MainBoard("HP", "Probook"), 
           processor='Intel', memory='32GB', hard_drive='2TB SSD', 
           graphics='onboard', monitor='1920x1080')
t1.display()

t2 = t1.clone()
t2.model = 'Tower 2'
t2.mainboard.model = 'Business Server'
t2.display()
# problem solved with copy.deepcopy()
t1.display()   # t1 reference to the mainboard is changed not changed anymore.