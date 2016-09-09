grammar Interpreter;

block : '{' command* '}' ;

command : '[' guard ':' (command)* ']'              # execute_guarded
        | reference '=' expression ';'              # assign
        | expression ';'                            # execute
        | '^' expression ';'                        # return
        ;

guard : expression op=('='|'#') expression (',' guard )? ;

expression  : STRING                            # string
            | block                             # blk
            | reference                         # refer
            | '(' expression ')'                # par_enclosing
            | expression ('.' IDENTIFIER)+      # refer_prop
            | expression '+' expression         # add
            ;

reference: ('*')* IDENTIFIER;

IDENTIFIER : [a-zA-Z]+ ;

STRING : '"' (~'"')* '"';

ADD : '+' ;

WS : [ \t\r\n]+ -> skip ;           // skip spaces, tabs, newlines, \r (Windows)
COMMENTS : '%' .*? '\n' -> skip ;   // skip comments