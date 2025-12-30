from give_bmi import give_bmi, apply_limit


height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# test nan, inf, -inf, zero, negative, bool, str, different lengths
print(give_bmi([float('nan')], [70]))  # Test NaN
print(give_bmi([float('inf')], [70]))  # Test positive infinity
print(give_bmi([0], [70]))              # Test zero height
print(give_bmi(['a'], [70]))          # Test string height
print(give_bmi(["string"], [70]))       # Test string height
print(give_bmi([True], [70]))       # Test boolean height
print(give_bmi([-1.0], [70]))          # Test negative height
print(give_bmi([1.75], [0]))            # Test zero weight
print(give_bmi([1.75], [-5]))           # Test negative weight
print(give_bmi([1.75], [70, 80]))       # Test different lengths
