class Laptop:
    def __init__(self, model: str) -> None:
        self.model = model
    
    def __str__(self) -> str:
        return f"Laptop - {self.model}"
    
if __name__ == "__main__":
    lp = Laptop("Apple")

    print(lp)

