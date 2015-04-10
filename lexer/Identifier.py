from config import keywords
def t_ID( t ):
    r"[A-Za-z][a-zA-Z0-9]*"
    if ( t.value in keywords ): t.type = t.value
    return t