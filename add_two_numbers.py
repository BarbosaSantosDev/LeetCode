"""
Você recebe duas listas vinculadas não vazias, representando dois números inteiros não negativos. 
Os dígitos são armazenados em ordem inversa e cada um de seus nós contém um único dígito. 
Adicione os dois números e retorne a soma como uma lista vinculada.

Você pode assumir que os dois números não contêm zero líder, exceto o próprio número 0.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Restrições:

O número de nós em cada lista vinculada está no intervalo [1, 100].
0 <= node.val <= 9
É garantido que a lista representa um número que não possui zeros líderes.

"""



# como organizar numeros invertidos.
from typing import List

class Solution:
    def addTwoNumbers(self, l1: list, l2: list) -> List:
        invert_l1 = list(reversed(l1))
        print(invert_l1)
        invert_l2 = list(reversed(l2))
        string_l1 = "".join(map(str, invert_l1))
        string_l2 = "".join(map(str, invert_l2))
        convert_int_l1 = int(string_l1)
        convert_int_l2 = int(string_l2)
        soma = [convert_int_l1 + convert_int_l2]
        invert_sum = list(reversed(soma))
        return invert_sum

if __name__ == "__main__":
    solutio = Solution()
    t = solutio.addTwoNumbers([2,4,3], [5,6,4])  
    print(t)