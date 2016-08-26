module Lexer where

import Data.Char

data Token = OP Char
           | ID String
           | WS Char
           | NL
           | ERR Char
           | EOF
           deriving (Show, Eq)

tokenize :: String -> [Token]
tokenize [] = [EOF]
tokenize (c:cs)
    | elem c "+-*/" = OP c : tokenize cs
    | isAlpha c = identifier c cs
    | c == '\n' = NL : tokenize cs
    | isSpace c = WS c : tokenize cs
    | otherwise = ERR c : tokenize cs

identifier :: Char -> String -> [Token]
identifier c cs = 
    let (str, cs') = alnums "" cs 
    in
        ID (c:str) : tokenize cs'

alnums :: String -> String -> (String, String)
alnums acc [] = (acc, [])
alnums acc s@(c:cs)
    | isAlphaNum c =
        let (acc', cs') = alnums "" cs
        in
            (c:acc', cs')
    | otherwise = (acc, s)
