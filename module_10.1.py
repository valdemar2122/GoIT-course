from random import choice

from module_10 import Laptop, HDD

OS_LIST = ("windows", "macOS")

def buy_laptop(model: str) -> Laptop:
    return Laptop(model)

laptops: list[Laptop] = []

def main() -> None:
    while True:
        user_input = input("Write Laptop Model or 'enter' to quit: " )
        if not user_input:
            break
        laptops.append(buy_laptop(user_input))
    install_os = input("Install OS y/n : ")
    if install_os == 'y':
        for laptop in laptops:
            print(laptop.install_os(choice(OS_LIST)))
    print(*laptops)

    print (choice(laptops).install_os(choice(OS_LIST)))

new_hdd = input ("Enter HDD params: ")




if __name__ == "__main__":
    main()

