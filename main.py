from dataclasses import dataclass

@dataclass
class Config :
    batch_size : int
    lr: float = 0.001
    epochs: int = 10
    

c1 = Config(43)
print(c1)
