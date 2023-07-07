from tower import MainBoard, Tower
from laptop import Laptop
from prototype_manager import PrototypeManager


manager = PrototypeManager()
l1 = Laptop(model='L1', processor='Intel', memory='32GB', 
            hard_drive='2TB SSD', graphics='onboard', screen='1920x1080')
l1.display()
manager |= {'l1': l1}   # update manager by merging t1 with manager variable.
l2 = manager['l1'].clone()
l2.model = 'L2'
l2.processor = 'AMD'
l2.display()

t1 = Tower(model='Tower1', mainboard=MainBoard("HP", "Probook"), 
           processor='Intel', memory='32GB', hard_drive='2TB SSD', 
           graphics='onboard', monitor='1920x1080')
t1.display()
manager |= {'t1': t1}   # update manager by merging t1 with manager variable.

t2 = manager['t1'].clone()
t2.model = 'Tower 2'
t2.mainboard.model = 'Business Server'
t2.display()
t1.display()

print(manager)
