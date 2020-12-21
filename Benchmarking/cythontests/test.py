import benchmarks

import timeit

cy = timeit.timeit('''benchmarks.test()''',setup='import benchmarks',number=1)

print(cy)
