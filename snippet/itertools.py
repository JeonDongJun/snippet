# itertools 이용한 permutation과 computation 구하기
import itertools

chars = ['A', 'B', 'C']

p = itertools.permutations(chars, 2)  # 순열
c = itertools.combinations(chars, 2)  # 조합