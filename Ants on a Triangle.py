def probability_no_collision():
    total_outcomes = 2**3
    favorable_outcomes = 1

    probability = favorable_outcomes / total_outcomes

    return round(probability, 2)

result = probability_no_collision()
print(result)