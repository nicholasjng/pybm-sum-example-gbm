import pybm
import google_benchmark as gbm

from main import my_sum


@gbm.register
def custom_sum(state):
    while state:
        my_sum(10000)


if __name__ == "__main__":
    pybm.run(module_context=globals())
