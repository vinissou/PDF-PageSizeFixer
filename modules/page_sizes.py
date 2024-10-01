from dataclasses import dataclass


@dataclass
class PaperSize:
    x: float
    y: float


p = PaperSize(1.5, 2.5)

print(p)  # Point(x=1.5, y=2.5, z=0.0)
print(p.x)  # Point(x=1.5, y=2.5, z=0.0)
