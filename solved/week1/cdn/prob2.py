###################
# 다음 프로그램의 출력 결과는 무엇인가?

def swap(a, b):
    tmp = a
    a = b; b = tmp
    print('{}, {}, '.format(a, b), end='')

a = 2;b = 3
swap(a, b)
print('{}, {}'.format(a, b))

# 1. 2,3,3,3
# 2. 2,3,3,2
# 3. 2,3,2,3
# 4. 3,2,3,2
# 5. 3,2,2,3


# Python에서는 변수의 type에 따라 immutable과 mutable한 것으로 나뉨
# 대표적인 immutable한 타입은 tuple, string, int, bool 등을 포함한 primitive type들이 있고,
# mutable한 타입은 list, dict 등이 있음
# immutable 특성을 갖는 변수가 함수의 인자로 넘어가게 되면, 변할 수 없는 특성 때문에 그 변수가 그대로 넘어가는 것이 아닌,
# **변수가 갖고 있던 값을 복사** 하여 값을 넘겨주게 됨

# 파이썬의 immutable type과 mutable type에 대해 정리하고 싶었음.