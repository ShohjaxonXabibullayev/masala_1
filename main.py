def count_positives_sum_negatives(arr):
    if not arr:
        return []

    count = sum(1 for i in arr if i > 0)
    total = sum(i for i in arr if i < 0)
    return [count, total]

print(count_positives_sum_negatives([1, -2, 3, -4, 5]))  # [3, -6]
print(count_positives_sum_negatives([]))  # []
