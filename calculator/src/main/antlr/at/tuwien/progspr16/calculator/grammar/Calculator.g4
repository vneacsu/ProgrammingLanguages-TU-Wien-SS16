grammar Calculator;

@header {
package at.tuwien.progspr16.calculator.grammar;
}

calculator
    : (operand | operation)*
    ;

operand
    : INT                   #integer
    | '[' calculator ']'    #block
    ;

operation
    : '+' | '-' | '*' | '/' | '%' | '&' | '|'
    | '=' | '<' | '>' | '~' | 'c' | 'd' | 'a'
    | 'i' | 'b' | 'w' | 'x'
    ;

// Lexer tokens

INT
    : [0-9]+
    ;

WS
    : [ \t]+ -> skip
    ;

BAD_CHARACTER
    : .
    ;