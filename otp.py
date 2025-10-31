"""import random
print(f"{random.randint(1,100):04d}")"""
"""import secrets
print(f"{secrets.randbelow(100):04d}")"""
import secrets
from datetime import datetime,timedelta
def getotp(expires_sec=300):
    code=f"{secrets.randbelow(100):04d}"
    expiry=datetime.now()+timedelta(seconds=expires_sec)
    return code,expiry
def verify(input_code,actual_code,expiry):
    if datetime.now() > expiry:
        return "expired"
    if input_code==actual_code:
        return "verified"
    else:
        return"incorrect otp"
otp,expiry=getotp()
print(otp)
ok=verify("0042",otp,expiry)
print(ok)