def stdin():
    string, substr = "", raw_input( "" )
    while ( substr == "" ) or ( substr[0] != "!" ):
        string += ( " " + substr + "\n" )
        substr = raw_input( "" )
    return string