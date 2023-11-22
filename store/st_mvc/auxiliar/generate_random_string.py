from django.utils.crypto import get_random_string

def get_RandomString(size: int) -> str:
    return get_random_string(size,'0123456789qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM')
