grammar Interpreter;

block : '{' command* '}' ;

command : '[' guard ':' (command)* ']'
        | (('*')* IDENTIFIER '=')? expression ';'
        | '^' expression ';'
        ;

guard : expression ( '=' | '#' ) expression (',' guard )? ;

expression  : STRING                            # string
            | block                             # blk
            | ('*')* IDENTIFIER                 # identifier
            | '(' expression ')'                # parenthesis
            | expression ('.' IDENTIFIER)+      # subobj
            | expression '+' expression         # add
            ;

IDENTIFIER : [a-z]+ ;

STRING : '"' (~'"')* '"';

ADD : '+' ;

WS : [ \t\r\n]+ -> skip ;           // skip spaces, tabs, newlines, \r (Windows)
COMMENTS : '%' .*? '\n' -> skip ;   // skip comments