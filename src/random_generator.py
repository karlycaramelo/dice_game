import secrets
import hmac
import hashlib
# in this case, the RandomGenerator class is used to generate random numbers and HMAC values
class RandomGenerator:
    @staticmethod
    def generate_number(upper_bound):
        return secrets.randbelow(upper_bound) # The random number is generated using the secrets module, which is a secure random number generator.

    @staticmethod
    def generate_hmac(number):
        key = secrets.token_hex(32)
        hmac_value = hmac.new(key.encode(), str(number).encode(), hashlib.sha3_256).hexdigest() # The HMAC value is calculated using the SHA-3-256 hash function.
        return hmac_value.upper(), key
