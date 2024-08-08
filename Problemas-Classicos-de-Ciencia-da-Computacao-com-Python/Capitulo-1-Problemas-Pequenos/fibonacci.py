# Sequência de Fibonacci

# Implementação básica de recursividade
# 
# Desvantagens
#   - complexidade O(2^n)
#   - Desempenho ruim para valores grandes. 
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
 

# Usando a formula de Binet.
# 
# Vantagens
#   - Complexidade O(1)
#   - Melhor desempenho que a implementação básica de recursividade
#   - Complexidade constante
#   - Eficiência: Não requer armazenamento intermediário de resultados
# 
# Desvantagens:
#   - Em cálculos com números grandes, a precisão pode ser comprometida devido a
# limitações com ponto fluente
def fibinet(n: int) -> int:
    phi = (1 + 5**0.5) / 2
    psi = (1 - 5**0.5) / 2
    return int(round((phi**n - psi**n) / 5**0.5))


# lru_cache é um decorador disponível no módulo functools, usado para otimizar o
# desempenho de funçoes através de um mecanismo de cache. Ele implementa o 
# conceito de "Least Recently Used" (LRU), menos usado recentemente.
#
# cache LRU deve ser usado somente quando precisar reutilizar valores calculados
# anteriomente. Quando a mesma função for chamada novamente com os mesmos 
# argumentos, o resultado possa ser obtido diretamente do cache em vez de 
# recalcular.
#
# Vantagens
#   - complexidade O(n)
#   - uso de cache evita o recalculo
#
# Desvantagens
#   - Uso de memória cache, pode ser problemática em ambientes com restrição de
#       memoria.
from functools import lru_cache
@lru_cache(maxsize=None)
def fib_LRUCache(n: int) -> int:
    if n < 2:
        return n
    return fib_LRUCache(n-2) + fib_LRUCache(n-1)


# Forma iterativa
#
# Vantagens
#   - complexidade O(n-1)
def fibInterativo(n: int) -> int:
    if n == 0: return n
    last:int = 0
    next:int = 1
    
    for _ in range(1, n):
        last, next = next, last + next
    return next


# Com Gerador
#
# Eficiência de Memória. O gerador produz os valores sob demanda.
#
# Vantagens
#   - complexidade O(n-1)
def fib_generator(n:int):
    yield 0
    if n > 0: yield 1
    last:int = 0
    next:int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

if __name__ == '__main__':
    for i in fib_generator(50):
        print(i)

    # gen = fib_generator(5)
    # print(next(gen))  # 0
    # print(next(gen))  # 1
    # print(next(gen))  # 1
    # print(next(gen))  # 2
    # print(next(gen))  # 3
    # print(next(gen))  # 3

