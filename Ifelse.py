class Laptops:
    Price = ""
    Processor =""
    RAM = ""

Dell = Laptops()
HP = Laptops()
Apple = Laptops()

Dell.name = "Dell"
HP.name = "HP"
Apple.name = "Apple"

Dell.Price = "40000/-"
Dell.Processor = "NVIDIA"
Dell.RAM = "512GB"

HP.Price = "65000/-"
HP.Processor = "Intel core"
HP.RAM = "1TB"

Apple.Price = "150000/-"
Apple.Processor = "M4 chip"
Apple.RAM = "2TB"


print(Dell.name)
print("Price: ", Dell.Price)
print("Processor: ", Dell.Processor)
print("RAM: ", Dell.RAM)

print(HP.name)
print("Price: ", HP.Price)
print("Processor: ", HP.Processor)
print("RAM: ", HP.RAM)

print(Apple.name)
print("Price: ", Apple.Price)
print("Processor: ", Apple.Processor)
print("RAM: ", Apple.RAM)
