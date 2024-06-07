from logging import getLogger

log = getLogger(__name__)

from time import sleep
def get_prime():
    for num in range(2, int(1e6) + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            log.error(num)
            sleep(0.5)


if __name__ == "__main__":
    get_prime()
