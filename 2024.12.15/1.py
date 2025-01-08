import math

class Tetrahedron:
    def __init__(self, edge: float):
        """Устанавливает длину ребра."""
        self.edge = float(edge)
    
    def surface(self) -> float:
        """Вычисляет площадь поверхности тетраэдра."""
        return math.sqrt(3) * (self.edge ** 2)
    
    def volume(self) -> float:
        """Вычисляет объём тетраэдра."""
        return (self.edge ** 3) / (6 * math.sqrt(2))

#>>> t1 = Tetrahedron(5)
#>>> t1.edge
#5.0
#>>> t1.surface()
#43.30127018922193
#>>> t1.volume()
#14.731391274719739
#>>> t1.edge = 6
#>>> t1.surface()
#62.35382907247958
#>>>