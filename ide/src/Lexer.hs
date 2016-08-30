module Lexer where

import Data.Char


data TokenType = ID | STAR | LCURLY | RCURLY | SEMICOL | CARET 
               | NL | WS | ERR | EOF
  deriving (Show, Eq)

data Token = Token { tokType :: TokenType 
                   , text :: String
                   , start :: Int
                   } deriving (Show, Eq)


tokenize :: String -> [Token]
tokenize txt = tokenize' txt 0

tokenize' :: String -> Int -> [Token]
tokenize' [] s = [(Token EOF " " s)]
tokenize' t@(c:cs) s
  | elem c " \t" = whitespace t s
  | c == '\n' = (Token NL [c] s) : tokenize' cs (s + 1)
  | isAlpha c = identifier t s
  | c == '*' = (Token STAR [c] s) : tokenize' cs (s + 1)
  | c == '{' = (Token LCURLY [c] s) : tokenize' cs (s + 1)
  | c == '}' = (Token RCURLY [c] s) : tokenize' cs (s + 1)
  | c == ';' = (Token SEMICOL [c] s) : tokenize' cs (s + 1)
  | c == '^' = (Token CARET [c] s) : tokenize' cs (s + 1)
  | otherwise = (Token ERR [c] s) : tokenize' cs (s + 1)


whitespace :: String -> Int -> [Token]
whitespace txt s =
  let (result, rest) = consumeWhile isWs txt 
  in
    (Token WS result s) : tokenize' rest (s + (length result))
  where
    isWs c = elem c " \t"

consumeWhile :: (Char -> Bool) -> String -> (String, String)
consumeWhile p txt =
  let match = takeWhile p txt
      rest = dropWhile p txt
  in
    (match, rest)

identifier :: String -> Int -> [Token]
identifier txt s =
  let (prefix, rest) = consumeWhile isAlpha txt
      (postfix, rest') = consumeWhile isAlphaNum rest
      name = prefix ++ postfix
      newOffset = s + (length name)
  in
    (Token ID name s) : tokenize' rest' newOffset