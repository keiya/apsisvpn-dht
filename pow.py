import hashlib
import string
import itertools
class ProofOfWork:
    @staticmethod
    def solve(target):
        for s in ProofOfWork.bruteforce(string.printable,8):
            hashval = hashlib.sha224(s).hexdigest()
            if hashval.startswith(target):
                return s

    @staticmethod
    def bruteforce(charset, maxlength):
        return (''.join(candidate)
            for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
            for i in range(1, maxlength + 1)))
