# Simple variable usage
X = 10
Y = 8
from magic_math import X_PLUS_Y_DIVIDED_BY_TWO  # 10 + (8 / 2) = 14.0
print(f"{X_PLUS_Y_DIVIDED_BY_TWO = }")

# Mix variables and literals
RATE = 1.5
from magic_math import RATE_TIMES_FORTY_TWO  # 1.5 * 42 = 63.0
print(f"{RATE_TIMES_FORTY_TWO = }")

# Multiple variables
BASE = 100
TAXRATE = 0.2
SHIPPING = 10
from magic_math import BASE_PLUS_BASE_TIMES_TAXRATE_PLUS_SHIPPING  # 100 + (100 * 0.2) + 10 = 130.0
print(f"{BASE_PLUS_BASE_TIMES_TAXRATE_PLUS_SHIPPING = }")

# Literals
from magic_math import TEN_TIMES_FIVE_DIVIDED_BY_TWO  # (10 * 5) / 2 = 25.0
print(f"{TEN_TIMES_FIVE_DIVIDED_BY_TWO = }")

from magic_math import FIVE_TIMES_FIVE  # 5 * 5 = 25.0
print(f"{FIVE_TIMES_FIVE = }")

from magic_math import TWO_HUNDRED_MINUS_TEN  # 200 - 10 = 190.0
print(f"{TWO_HUNDRED_MINUS_TEN = }")

from magic_math import SIX_HUNDRED_AND_SIXTY_SIX_DIVIDED_BY_TWO_TIMES_EIGHT  # (666 / 2) * 8 = 2664.0
print(f"{SIX_HUNDRED_AND_SIXTY_SIX_DIVIDED_BY_TWO_TIMES_EIGHT = }")

# Reassign variables
X = 10
Y = 20

from magic_math import OPEN_X_PLUS_Y_CLOSE_TIMES_TWO  # (10 + 20) * 2 = 60
from magic_math import X_PLUS_OPEN_Y_TIMES_TWO_CLOSE  # 10 + (20 * 2) = 50
from magic_math import OPEN_TWO_HUNDRED_PLUS_X_CLOSE_DIVIDED_BY_TWO  # (200 + 10) / 2 = 105

print(f"{OPEN_X_PLUS_Y_CLOSE_TIMES_TWO = }")
print(f"{X_PLUS_OPEN_Y_TIMES_TWO_CLOSE = }")
print(f"{OPEN_TWO_HUNDRED_PLUS_X_CLOSE_DIVIDED_BY_TWO = }")

# Floating point support
ABC = 123.456
from magic_math import ABC_DIVIDED_BY_ONE_HUNDRED_POINT_ONE
print(f"{ABC_DIVIDED_BY_ONE_HUNDRED_POINT_ONE = }")

from magic_math import THREE_POINT_THREE_TIMES_TWO  # 3.3 * 2 = 6.6
print(f"{THREE_POINT_THREE_TIMES_TWO = }")

from magic_math import FIVE_DOT_FIVE_DIVIDED_BY_ONE_POINT_ONE  # 5.5 / 1.1 = 5.0
print(f"{FIVE_DOT_FIVE_DIVIDED_BY_ONE_POINT_ONE = }")

# Parentheses support
from magic_math import OPEN_TEN_MINUS_OPEN_SEVEN_DIVIDED_BY_TWO_CLOSE_CLOSE  # (10 - (7 / 2)) = 6.5
print(f"{OPEN_TEN_MINUS_OPEN_SEVEN_DIVIDED_BY_TWO_CLOSE_CLOSE = }")