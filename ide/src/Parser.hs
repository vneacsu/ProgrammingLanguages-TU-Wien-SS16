{-# LANGUAGE FlexibleContexts #-}
module Parser where

import Data.List

import Lexer
--import Text.ParserCombinators.Parsec
--import Text.Parsec.Pos
--import Text.Parsec.Prim

data Block = Block Commands
    deriving (Show, Eq)

data Commands = EmptyCmds
              | Cmds Command Commands
    deriving (Show, Eq)

data Command = ReturnCmd (Maybe Expression)
    deriving (Show, Eq)

data Expression = Ref Token
    deriving (Show, Eq)


parse :: [Token] -> (Maybe Block, [Token])
parse tokens =
    let (mb, rest, errs) = block tokens
    in
        case mb of
            Just _ -> (mb, errs ++ trailingErrs errs)

            Nothing ->
                case null rest of
                    True -> (Nothing, errs)

                    False ->
                        let (mb', errs') = parse rest 
                        in
                            (mb', errs ++ errs')


block :: [Token] -> (Maybe Block, [Token], [Token])
block tokens =
    let next = lookAhead tokens
        rest = consume tokens
    in
        case tokType next of
            LCURLY ->
                let (cmds, toks, errs) = commands $ rest
                    next' = lookAhead toks
                    rest' = consume toks
                in
                    case tokType next' of
                        RCURLY -> (Just $ Block cmds, rest', errs)

                        _ -> (Just $ Block cmds, rest', errs ++ [next'])

            _ -> (Nothing, rest, [next])


commands :: [Token] -> (Commands, [Token], [Token])
commands tokens =
    let (cmd, rest, errs) = command tokens 
    in
        case cmd of
            Nothing -> (EmptyCmds, rest, errs)

            Just cmd' ->
                let (cmds', rest', errs') = commands rest 
                in
                    (Cmds cmd' cmds', rest', errs ++ errs')


command :: [Token] -> (Maybe Command, [Token], [Token])
command tokens = (Nothing, tokens, [])
--    | isReturnCmd tokens = returnCmd tokens
--    | _ = let (next, rest) = (lookAhead tokens, consume tokens) in (Nothing, rest, [next])
--    where
--        isReturnCmd tokens = (tokType $ lookAhead tokens) == CARET
--
--        returnCmd tokens =
--            let (mexpr, rest, errs) = expression $ consume tokens
--            in
--                case null rest of
--                    True -> (ReturnCmd mexpr, rest, errs)
--
--                    False ->
--                        let (next', rest') = (lookAhead rest, consume rest)
--                        in
--                            case tokType next' of 
--                                SEMICOL -> (ReturnCmd mexpr, rest', errs)
--
--                                _ -> (ReturnCmd mexpr, rest', errs ++ [next'])




expression :: [Token] -> (Maybe Expression, [Token], [Token])
expression tokens = (Nothing, tokens, [])

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

consume :: [Token] -> [Token]
consume l = tail $ dropWhile (not . acceptsToken) l

acceptsToken :: Token -> Bool
acceptsToken tok =
    case tok of
        Token WS _ _ -> False
        Token NL _ _ -> False
        _ -> True

trailingErrs :: [Token] -> [Token]
trailingErrs = filter (\t -> acceptsToken t && tokType t /= EOF)


--isToken :: (Stream s m Token) => TokenType -> ParsecT s u m Token
--isToken tt = tokenSatisfies (\t -> tokType t == tt)
--
--isNotToken :: (Stream s m Token) => TokenType -> ParsecT s u m Token
--isNotToken tt = tokenSatisfies (\t -> tokType t /= tt)
--
--tokenSatisfies f = tokenPrim (\t -> text t) 
--                             (\pos t _ -> updatePosString pos $ text t) 
--                             (\t -> if f t then Just t else Nothing)
--
--isAnyToken = tokenSatisfies (\_ -> True)
--
--block = do
--    prefs <- many (isNotToken LCURLY)
--    isToken LCURLY
--    trailing <- many isAnyToken
--    return $ prefs ++ trailing
--
--parseCSV :: String -> Either ParseError [Token]
--parseCSV input = parse block "(unknown)" $ tokenize input
--
--semi :: Stream s m Char => ParsecT s u m String
--semi = string ";"