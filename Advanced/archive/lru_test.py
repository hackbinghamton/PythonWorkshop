import functools
import time

@functools.lru_cache(maxsize=128)
def fibonacci_lru(num):
	if num < 2:
		return num

	else:
		return fibonacci_lru(num - 1) + fibonacci_lru(num - 2)

def fibonacci(num):
	if num < 2:
		return num

	else:
		return fibonacci(num - 1) + fibonacci(num - 2)


no_lru_start_time = time.time()
result = fibonacci(36)
print("Without LRU, took", time.time() - no_lru_start_time)

lru_start_time = time.time()
result = fibonacci_lru(36)
print("With LRU, took", time.time() - lru_start_time)
