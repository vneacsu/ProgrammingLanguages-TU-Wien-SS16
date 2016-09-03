grammar Interpreter;

block : '{' command* '}' ;

command : '[' guard ':' (command)* ']'
        | (('*')* IDENTIFIER '=')? expression ';'
        | '^' expression ';'
        ;

guard : expression ( '=' | '#' ) expression (',' guard )? ;

expression : ( STRING | block | ('*')* IDENTIFIER | '(' expression ')' ) ('.' IDENTIFIER)* ('+' expression)? ;

IDENTIFIER : [a-z]+ ;

STRING: '"' (~'"')* '"';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)