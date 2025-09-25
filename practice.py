from __future__ import annotations


class Vector3:

    # TODO: Implement the constructor
    """
    - Initialize a Vector3 object with three parameters (x, y, z).
    - Make sure that all the member variables are private (using double underscore) to avoid accidental modification.
    - Member variables must be float so that calculations are consistent.
    """

    # TODO: Implement +, -, * operator overloading
    """
    Overload the following operators to make Vector3 objects behave like numbers:
    - operator +: vector addition (v1 + v2)
    - operator -: vector subtraction (v1 - v2)
    - operator *: cross product (v1 * v2)
    """

    # TODO: Implement getter and setter methods for variables x, y, and z, respectively.

    # Do not modify the code inside this function.
    def to_tuple(self):
        return (self.__x, self.__y, self.__z)

    # Do not modify the code inside this function.
    def __repr__(self) -> str:
        return f"Vector3(x={self.__x:.6g}, y={self.__y:.6g}, z={self.__z:.6g})"


# Do not modify the code inside the sum_components function.
def sum_components(v: Vector3) -> float:
    x, y, z = v.to_tuple()
    return x + y + z


# Do not modify the code inside the vectors_from_student_id function.
def vectors_from_student_id(sid: str):
    digits = [int(c) for c in sid if c.isdigit()]
    if not digits:
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(digits) < 10:
        digits += digits
    digits = digits[:10]

    year = int(sid[:4]) if len(sid) >= 4 and sid[:4].isdigit() else sum(digits)
    dept = int(sid[4:7]) if len(sid) >= 7 and sid[4:7].isdigit() else (sum(digits) % 1000)

    # Vector A
    ax = ((digits[0] + 2 * digits[3] + dept) % 9) + 1
    ay = ((digits[1] + 2 * digits[4] + year) % 9) + 1
    az = ((digits[2] + 2 * digits[5] + year + dept) % 9) + 1
    sx = -1 if (digits[6] % 2) else 1
    sy = -1 if (digits[7] % 2) else 1
    sz = -1 if (digits[8] % 2) else 1
    A = Vector3(sx * ax, sy * ay, sz * az)

    # Vector B
    bx = ((digits[3] + 3 * digits[6] + 2 * dept) % 9) + 1
    by = ((digits[4] + 3 * digits[7] + year) % 9) + 1
    bz = ((digits[5] + 3 * digits[8] + dept) % 9) + 1
    tx = -1 if (digits[1] % 2) else 1
    ty = -1 if (digits[2] % 2) else 1
    tz = -1 if (digits[3] % 2) else 1
    B = Vector3(tx * bx, ty * by, tz * bz)

    if (A * B).to_tuple() == (0.0, 0.0, 0.0):
        B = Vector3(B.x, B.y, B.z + 1)

    # Vector C
    cx = ((digits[0] + 4 * digits[9] + dept) % 9) + 1
    cy = ((digits[1] + 4 * digits[8] + year) % 9) + 1
    cz = ((digits[2] + 4 * digits[7] + dept + year) % 9) + 1
    ux = -1 if (digits[9] % 2) else 1
    uy = -1 if (digits[0] % 2) else 1
    uz = -1 if (digits[4] % 2) else 1
    C = Vector3(ux * cx, uy * cy, uz * cz)

    return A, B, C


# Do not modify the code inside the checksum_value function.
def checksum_value(sid: str) -> str:
    A, B, C = vectors_from_student_id(sid)
    AB = A * B
    S = sum_components(A) + sum_components(B) + sum_components(C) + sum_components(AB)
    return f"{abs(int(S)) % 100:02d}"


if __name__ == "__main__":
    # Put your own student ID and copy the printed checksum value into your Pull Request description.
    sid = "2025311532"
    print(checksum_value(sid))

    # Example usage
    # v1 = Vector3(1, 2, 3)
    # v2 = Vector3(4, 5, 6)

    # print(v1 + v2)  # Expected: Vector3(x=5, y=7, z=9)
    # print(v1 - v2)  # Expected: Vector3(x=-3, y=-3, z=-3)
    # print(v1 * v2)  # Expected: Vector3(x=-3, y=6, z=-3)
    # print(v2 * v1)  # Expected: Vector3(x=3, y=-6, z=3)
   
class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    # Getter
    def get_x(self): return self.__x
    def get_y(self): return self.__y
    def get_z(self): return self.__z

    # Setter
    def set_x(self, value): self.__x = value
    def set_y(self, value): self.__y = value
    def set_z(self, value): self.__z = value

    def __repr__(self):
        return f"Vector3({self.__x}, {self.__y}, {self.__z})"
    class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def get_x(self): return self.__x
    def get_y(self): return self.__y
    def get_z(self): return self.__z

    def set_x(self, value): self.__x = value
    def set_y(self, value): self.__y = value
    def set_z(self, value): self.__z = value

    def __repr__(self):
        return f"Vector3({self.__x}, {self.__y}, {self.__z})"

    # 加法
    def __add__(self, other):
        return Vector3(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    # 减法
    def __sub__(self, other):
        return Vector3(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    # 叉乘
    def __mul__(self, other):
        x = self.__y * other.__z - self.__z * other.__y
        y = self.__z * other.__x - self.__x * other.__z
        z = self.__x * other.__y - self.__y * other.__x
        return Vector3(x, y, z)
    
from typing import List, Tuple
import math


class Shape:
    # 抽象方法：只定义接口，不提供实现
    def measure(self) -> float:
        """
        计算图形的面积。
        子类必须重写此方法。
        """
        raise NotImplementedError("Subclasses must implement measure().")


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def measure(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def measure(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float]):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def measure(self) -> float:
        # 计算三边长
        def dist(a, b):
            return math.hypot(a[0] - b[0], a[1] - b[1])

        a = dist(self.p1, self.p2)
        b = dist(self.p2, self.p3)
        c = dist(self.p3, self.p1)

        # 海伦公式
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])

 
    