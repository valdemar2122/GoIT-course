class HDD:
    def __init__(self, type_hdd: str, size: str) -> None:
        self.type_hdd = type_hdd
        self.size = size

    def __str__(self) -> str:
        return f"Type - {self.type_hdd}, size - {self.size}"

class Laptop():
    def __init__(self, model: str, preinstalled_OS: str = None) -> None:
        self.model = model
        self.hdd = HDD("hdd", "1Tb")
        self.installed_soft = [preinstalled_OS] if preinstalled_OS else []
        
    
    def change_hdd(self, hdd:HDD):
        self.hdd = hdd
    
    def install_os(self, OS: str) -> str:
        if not self.installed_soft:
            self.installed_soft.append(OS)
            return f"Install {OS}"
        return "OS installed, uninstall before"

    def __str__(self) -> str:
        installed_os = ", " + self.installed_soft[0] if len (self.installed_soft) > 0 else ""
        return "{}, {}{} ". format(self.model,
                                    self.hdd,
                                    installed_os 
                                    )


lp = Laptop("Apple")
lp1 = Laptop("Dell")

new_hdd = HDD("SSD", "256GB")
lp.change_hdd(new_hdd)
print (lp)
print(lp1)