import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    if dp[amount] == float('inf'):
        return {}
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

# Порівняння ефективності
amount = 113

start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

start_time = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start_time

# Висновки про ефективність
comparison_text = f"""
Порівняння алгоритмів для задачі розбиття суми на монети:

1. Жадібний алгоритм (Greedy):
   - Результат: {greedy_result}
   - Час виконання: {greedy_time:.6f} секунд
   - Переваги: швидкий, простий у реалізації.
   - Недоліки: не завжди знаходить оптимальне рішення.

2. Динамічне програмування (DP):
   - Результат: {dp_result}
   - Час виконання: {dp_time:.6f} секунд
   - Переваги: гарантує мінімальну кількість монет.
   - Недоліки: складніший у реалізації, займає більше пам’яті.

Висновок: Жадібний алгоритм швидший і простіший, але не завжди знаходить найменшу кількість монет. Динамічний алгоритм дає оптимальний результат, але працює довше.
"""

# Створення README файлу
with open("readme.md", "w", encoding="utf-8") as file:
    file.write(comparison_text)
