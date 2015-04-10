    C  : Command

    CL : CommandList

    D  : Declaration

    DL : DeclarationList

    E  : Expression

    EL : ExpressionList

    I  : Identifier

    IL : IdentifierList

    L  : LefthandSide

    N  : Numeral

    P  : Program

    T  : TypeTemplate

---

    C  ::=  L = E  |  if E : CL1 else CL2 end  |  print E  |  L ( EL )

    CL ::=  C  |  C ; CL  |  empty

    D  ::=  int I = E  |  obj I = E  |  def I ( IL ) : CL end  |  class I : T

    DL ::=  D;*

    E  ::=  N  |  ( E1 OP E2 )  |  L  |  new T  |  nil

    EL ::=  E  |  E , EL  | empty

    I  ::=  string of letters

    IL ::=  I  |  I , IL  |  empty

    L  ::=  I  |  L . I

    N  ::=  string of digits

    OP ::=  +  |  -

    P  ::=  DL  CL

    T  ::=  { DL }  |  L

---

    CLIST ::=  [ CTREE* ]

    CTREE ::=  [ "=", LTREE, ETREE ]  |  [ "if", ETREE, CLIST, CLIST ]  |  [ "print", LTREE ]  |  [ "call", LTREE, ELIST ]

    DLIST ::=  [ DTREE* ]

    DTREE ::=  [ "int", ID, ETREE ]  |  [ "obj", ID, ETREE ]  |  [ "def", ID, ILIST, CLIST ]  |  [ "class", ID, TTREE ]

    ELIST ::=   [ ETREE* ]

    ETREE ::=  NUM  |  [ "+", ETREE, ETREE ] |  [ "deref", LTREE ]  |  [ "new", TTREE ]  |  "nil"

    ID    ::=  string of letters

    ILIST ::=  [ ID+ ]

    LTREE ::=  ID  |  [ "dot", LTREE, ID ]

    NUM   ::=  string of digits

    PTREE ::=  [ DLIST, CLIST ]

    TTREE ::=  [ "struct", DLIST ]  |  [ "call", LTREE ]