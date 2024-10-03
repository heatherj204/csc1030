def is_heteromecic(n, num=1):
    if n == num:
        return False
    if num * (num + 1) == n:
        return True
    return is_heteromecic(n, num + 1)


print(is_heteromecic(110))