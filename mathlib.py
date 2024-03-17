lllllllllllllll, llllllllllllllI, lllllllllllllIl = Exception, str, min

import math

def lllIIIlllIlllIlIIl(lllllIlIIIlIIIllll, lIlIIlIIIlIlIIIlIl):
    IIlIlIlIIIllllIIIl = math.sqrt(lllllIlIIIlIIIllll[2] ** 2 + lllllIlIIIlIIIllll[3] ** 2)
    IllIIllIIIIIllIIll = 2 * IIlIlIlIIIllllIIIl * math.tan(int(lIlIIlIIIlIlIIIlIl )/ 2)
    IllIIllIIIIIllIIll = lllllllllllllIl(IllIIllIIIIIllIIll, IIlIlIlIIIllllIIIl)
    llllIlIIlIllllIllI = lllllIlIIIlIIIllll[0] + (lllllIlIIIlIIIllll[2] - IllIIllIIIIIllIIll) // 2
    lIIlllIIIlIIIlllll = lllllIlIIIlIIIllll[1] + (lllllIlIIIlIIIllll[3] - IllIIllIIIIIllIIll) // 2
    IlllIIIllIlllllIII = (llllIlIIlIllllIllI, lIIlllIIIlIIIlllll, IllIIllIIIIIllIIll, IllIIllIIIIIllIIll)
    return IlllIIIllIlllllIII
import random
import base64
from datetime import datetime, timedelta

def lIIIIIllIllIlllIll(IIlIlllIIllIlllIII):
    try:
        (lllIIIlllIlIIIlIlI, IlIIIIIlllIlIIlIII) = IIlIlllIIllIlllIII.split(':')
        llIlIIIlllllIIllIl = base64.b64decode(lllIIIlllIlIIIlIlI.encode()).decode()
        IIIlIIllllIIllIllI = datetime.strptime(base64.b64decode(IlIIIIIlllIlIIlIII.encode()).decode(), '%Y-%m-%d')
        IIIllIIllIIlllIllI = datetime.utcnow()
        IlIIlIIIlIIIIIllII = IIIllIIllIIlllIllI - timedelta(days=365)
        IIIllllllIlllIlllI = True if IlIIlIIIlIIIIIllII <= IIIlIIllllIIllIllI <= IIIllIIllIIlllIllI else False
        return {'random_string': llIlIIIlllllIIllIl, 'generated_date': IIIlIIllllIIllIllI, 'is_valid': IIIllllllIlllIlllI}
    except lllllllllllllll as IlIlllIlIlIIlllIII:
        return {'error': llllllllllllllI(IlIlllIlIlIIlllIII)}