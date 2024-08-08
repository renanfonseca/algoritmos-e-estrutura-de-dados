# Capítulo 1 <br> Problemas Pequenos

## Sequência de Fibonacci

A sequência de Fibonacci é um padrão numérico em que o primeiro e o segundo 
termo são iguais a 1 e cada termo a partir do terceiro é a soma dos dois termos 
anteriores.

<br>

$$
F_{n} = F_{n-1} + F_{n-2}  ,\  n \ge 3
$$

<br>

Existe uma fórmula, chamada fórmula de Binet, que pode ser utilizada para 
encontrar qualquer termo da sequência de Fibonacci. Essa fórmula é dada pela 
seguinte expressão, com $ n\ge 1$:

<br>

$$
F_n=\frac{1}{\sqrt{5}}\bigg(\frac{1+\sqrt{5}}{2} \bigg)^n 
- \frac{1}{\sqrt{5}}\bigg(\frac{1-\sqrt{5}}{2} \bigg)^n
$$

<br>

Para uma explicação mais detalhada, você pode assistir a este vídeo do professor 
Possani: [Sequência de Fibonacci](https://www.youtube.com/watch?v=ngN3QD3l3D4)


→ [Código](fibonacci.py)
