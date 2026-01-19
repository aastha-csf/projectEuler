import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.helpers import sumOfTheMultiplesOf

n = 1000

multiple_3 = 3
k_3 = (n-1) // multiple_3

multiple_5 = 5
k_5 = (n-1) // multiple_5

multiple_15 = 15
k_15 = (n-1) // multiple_15

print(sumOfTheMultiplesOf(multiple_3, k_3) + sumOfTheMultiplesOf(multiple_5, k_5) - sumOfTheMultiplesOf(multiple_15, k_15))