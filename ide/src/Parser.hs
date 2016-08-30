module Parser where

import Data.List

import Lexer

data Block = Block Commands
    deriving (Show, Eq)

data Commands = EmptyCmds
              | Cmd Command
              | Cmds Command Commands
    deriving (Show, Eq)

data Command = ExprCmd Expression
    deriving (Show, Eq)

data Expression = Ref Token
    deriving (Show, Eq)

parse :: [Token] -> (Maybe Block, [Token])
parse toks =
    let (next', toks') = consume toks
    in
        case tokType next' of
            EOF -> (Nothing, [next'])

            LCURLY ->
                let (cmds'', toks'', errs'') = commands toks'
                    (next'', rest'') = consume toks''
                in
                    case tokType next'' of
                        RCURLY -> (Just $ Block cmds'', errs'' ++ trailingErrs rest'')

                        _ -> (Just $ Block cmds'', errs'' ++ filter acceptsToken toks'')

            _ -> 
                let (b'', errs'') = parse toks'
                in
                    (b'', next':errs'')

--parse tokens = parse' tokens []
--    where
--        parse' toks errs = 
--            let (next, toks') = consume toks
--            in
--                if tokType next == LCURLY then
--                    parse'' toks' errs 
--                else if tokType next /= EOF
--                    let (b, errs') = parse' toks' []
--                    in
--                        (b, next:errs')
--                else
--                    (EmptyBlock, errs)
--
--        parse'' toks errs =
--            case tokType $ lookAhead toks of
--                RCURLY -> 
--                    let (_, rest) = consume toks
--                        trailingErrs = filter acceptsToken rest
--                    in
--                        (EmptyBlock, errs ++ trailingErrs)
--
--                _ ->
--                    let ((cmds, errs'), rest) = commands toks errs
--                        trailingErrs = filter acceptsToken rest
--                    in
--                        (Block cmds, errs' + trailingErrs)

commands :: [Token] -> (Commands, [Token], [Token])
commands toks = (EmptyCmds, toks, [])

--command :: [Token] -> [Token] -> (Maybe Command, [Token], [Token])
--command toks errs = (Nothing, toks, errs)
--
--expression :: [Token] -> [Token] -> (Maybe Command, [Token], [Token])
--expression toks errs = (Nothing, toks, errs)

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

trailingErrs :: [Token] -> [Token]
trailingErrs = filter (\t -> acceptsToken t && tokType t /= EOF)