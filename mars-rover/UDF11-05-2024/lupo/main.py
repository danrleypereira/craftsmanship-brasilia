class Mars:

  cardialDirectionChanges = {
    "n": {
      'r': 'e',
      'l': 'w',
      },
    "s": {
      'r': 'w',
      'l': 'e',
      },
    "e": {
      'r': 's',
      'l': 'n',
      },
    "w": {
      'r': 'n',
      'l': 's',
      }
    }

  @staticmethod
  def checkIfInputHasOnlyMovement(input: str) -> bool:
    input = input.lower();
    if "r" in input or "l" in input:
      return False
    return True

  @staticmethod
  def checkIfInputHasOnlyDirection(input: str) -> bool:
    input = input.lower();
    if "m" in input:
      return False
    return True

  @staticmethod
  def countMovements(input: str) -> int:
    input = input.lower();
    return input.count("m")

  def checkIfCaracterIsMovement(self, caracter: str) -> bool:
    caracter = caracter.lower();
    for c in caracter:
      if c == "m":
        return True
      return False

  def whichCardialDirection(self, cardialDirection: str, caracter:str ) -> str:
    return self.cardialDirectionChanges.get(cardialDirection.lower()).get(caracter.lower()).upper()

  def countMovementsBeforeDirectionChanges(self, input: str) -> list:
    input = input.lower();
    movements = []
    counter = 0
    for i in range(len(input)):
      if input[i] == "r" or input[i] == "l":
        movements.append(counter)
        counter = 0
      else:
        counter += 1
    return movements

# ("N", [0, 0], "rmmm", [0, 3]) | 0 = X - 1 = Y
  def calculateNewPosition(self, cardialDirection: str, initialPosition: list, input: str) -> str:
    input = input.lower();
    newPosition = initialPosition
    for i in range(len(input)):
      if input[i] == "r" or input[i] == "l":
        cardialDirection = Mars().whichCardialDirection(cardialDirection, input[i])
      else:
        if cardialDirection == "N":
          newPosition[1] += 1
        elif cardialDirection == "S":
          newPosition[1] -= 1
        elif cardialDirection == "E":
          newPosition[0] += 1
        elif cardialDirection == "W":
          newPosition[0] -= 1
    return f"{newPosition[0]}:{newPosition[1]}:{cardialDirection}"

# 1 - cardialDirection = E -> newPosition = [0, 0]
# 2 - cardialDirection = E -> newPosition = [1, 0]
# 3 - cardialDirection = E -> newPosition = [2, 0]
# 4 - cardialDirection = E -> newPosition = [3, 0]
