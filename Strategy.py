import cmath


class DiscriminantStrategy:
  def calculate_discriminant(self, a, b, c):
    pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
  def calculate_discriminant(self, a, b, c):
    return b * b - 4 * a * c


class RealDiscriminantStrategy(DiscriminantStrategy):
  def calculate_discriminant(self, a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
      return float('nan')
    return d


class QuadraticEquationSolver:
  def __init__(self, strategy):
    self.strategy = strategy

  def solve(self, a, b, c):
    d = self.strategy.calculate_discriminant(a, b, c)
    sqrt_d = cmath.sqrt(d)
    plus = (-b + sqrt_d) / (2 * a)
    minus = (-b - sqrt_d) / (2 * a)
    return (plus, minus)


if __name__ == '__main__':
  solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
  print(solver.solve(1, 10, 16))

  solver_real = QuadraticEquationSolver(RealDiscriminantStrategy())
  print(solver_real.solve(1, 4, 5))

  solver_ord_neg = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
  print(solver_ord_neg.solve(1, 4, 5))
