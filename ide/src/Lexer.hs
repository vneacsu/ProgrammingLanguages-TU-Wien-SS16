{-# LANGUAGE FlexibleContexts #-}
module Lexer
  ( TokenType(..)
  , Token(..)
  , tokenize
  ) where

import Text.ParserCombinators.Parsec hiding (token, tokens, alphaNum)

data TokenType = ID | STAR | LCURLY | RCURLY | SEMICOL | CARET 
               | NL | WS | ERR | EOF
  deriving (Show, Eq)

data Token = Token { tokType :: TokenType 
                   , text :: String
                   , pos :: SourcePos
                   } deriving (Show, Eq)


tokenize :: String -> [Token]
tokenize txt = let Right res = parse tokens "" txt in res

tokens :: Parser [Token]
tokens = do
  toks <- many token
  position <- getPosition
  return $ toks ++ [Token EOF " " position]

token :: Parser Token
token = choice
  [ accept STAR $ string "*"
  , accept LCURLY $ string "{"
  , accept RCURLY $ string "}"
  , accept SEMICOL $ string ";"
  , accept CARET $ string "^"
  , accept NL $ string "\n"
  , accept WS $ many1 $ oneOf " \t"
  , accept ID $ do t <- oneOf alpha ; ts <- many $ oneOf alphaNum ; return (t:ts :: String)
  , accept ERR $ do t <- anyToken ; return [t]
  ]
  where
    alpha = ['A'..'Z'] ++ ['a'..'z'] ++ "_"
    alphaNum = alpha ++ ['0'..'9']

accept :: TokenType -> Parser String -> Parser Token
accept tt p = do
  position <- getPosition
  txt <- p
  return $ Token tt txt position