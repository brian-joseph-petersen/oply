Oply
---------------------
Tiny object-oriented programming language

    obj time = new {
        int seconds = 0;
        def tick():
            seconds = ( seconds + 1 );
            end;
    };
    time.tick();
    time.tick();
    time.tick();
    print time.seconds;
    !

---

    class time: {
        int minutes = 0;
        int seconds = 0;
        def tick():
            if ( seconds - 59 ):
                seconds = ( seconds + 1 );
            else
                seconds = 0;
                minutes = ( minutes + 1 );
                end;
            end;
    };
    obj clock = new time;
    clock.tick();
    clock.tick();
    clock.tick();
    print clock.seconds;
    print clock.minutes;
    !

Learn More
----------
[PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/index.html)

[Prototyping Interpreters using Python Lex-Yacc](http://www.drdobbs.com/web-development/prototyping-interpreters-using-python-le/184405580)