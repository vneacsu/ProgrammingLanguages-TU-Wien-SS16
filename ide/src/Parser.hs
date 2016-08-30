module Parser where

import Data.List

import Lexer

data Block = Block Token
    deriving (Show, Eq)

--data Commands = Cmd Command
--              | Cmds Command Commands
--    deriving (Show, Eq)
--
--data Command = ExprCmd Token

--data Expression = Ref { stars :: [Token]
--                      , name :: Token
--                      } deriving (Show, Eq)

parse :: [Token] -> (Maybe Block, [Token])
parse tokens = parse' tokens []
    where
        parse' toks errs = 
            let (next, toks') = consume toks
            in
                if tokType next == LCURLY then
                    (Just $ Block next, errs ++ (filter acceptsToken toks'))
                else if tokType next == EOF then
                    (Nothing, errs)
                else
                    let (b, errs') = parse' toks' []
                    in
                        (b, next:errs')


--data ParseTree = AddExpr Token ParseTree ParseTree
--               | MulExpr Token ParseTree ParseTree
--               | Id Token
--               deriving Show
--
--parse :: String -> ParseTree
--parse text = 
--    let (tree, _) = expression $ tokenize text
--    in
--        tree
--
--expression :: [Token] -> (ParseTree, [Token])
--expression toks =
--    let (termTree, toks') = term toks
--    in
--        case lookAhead toks' of
--            (OP op) | elem op "+-" ->
--                let (exprTree, toks'') = expression (accept toks')
--                in
--                    (AddExpr op termTree exprTree, toks'') 
--            _ -> (termTree, toks')
--
--term :: [Token] -> (ParseTree, [Token])
--term toks = (Id "abc", [])
----    let (factTree, toks') = factor toks
----    in
----        case lookAhead toks' of
----            (OP op) | elem op "*/" ->
----                let (termTree, toks'') = term (accept toks')
----                in
----                    (MulExpr op factTree termTree, toks'')
----            _ -> (factTree, toks')
----
----factor :: [Token] -> (ParseTree, [Token])
----factor toks =
----    case lookAhead toks of
----        ID s -> (Id s, accept toks)
----        WS c -> (Ws c, accept toks)
----        _ -> error $ "Invalid token at: " ++ show toks
----

lookAhead :: [Token] -> Token
lookAhead l = 
    let e = find acceptsToken l
    in
        case e of
            Nothing -> error "invalid lookAhead call"
            Just e' -> e'

consume :: [Token] -> (Token, [Token])
consume l = 
    let next = dropWhile (not . acceptsToken) l
    in
        (head next, tail next)

acceptsToken :: Token -> Bool
acceptsToken tok =
    case tok of
        Token WS _ _ -> False
        Token NL _ _ -> False
        _ -> True