module UnusedPropInspection where

import Lexer
import Parser


inspectUnused :: Block -> ([Token], [Token])
inspectUnused tree =
    let assgs = findAllAssgs tree
        unusedProps = map (fst) $ filter (\(prop, parent) -> not $ isPropUsed prop parent 0) assgs
    in
        (unusedProps, [])



findAllAssgs :: Block -> [(Token, Block)]
findAllAssgs tree = visitBlock tree
    where
        visitBlock parent@(Block commands) = visitCommands commands parent

        visitCommands (Cmds cmds) parent = visitAll visitCommand cmds parent

        visitAll visitor rules parent = concat $ map (\rule -> visitor rule parent) rules

        visitCommand (GuardCmd guard commands) parent = (visitGuard guard parent) ++ (visitCommands commands parent)
        visitCommand (ExprCmd expr) parent = visitExpression expr parent
        visitCommand (ReturnCmd expr) parent = visitExpression expr parent
        visitCommand (AssgCmd ref expr) parent = (visitReference ref parent) ++ (visitExpression expr parent)

        visitGuard (Guard bools) parent = visitAll visitBoolExpr bools parent

        visitBoolExpr (BoolEq e1 e2) parent = (visitExpression e1 parent) ++ (visitExpression e2 parent)

        visitExpression (AddExpr primary _ exprs) parent = (visitPrimary primary parent) ++ (visitAll visitExpression exprs parent)

        visitPrimary (BlockPrim b) _ = visitBlock b
        visitPrimary (ParensPrim e) parent = visitExpression e parent
        visitPrimary _ _ = []

        visitReference (Ref stars name) parent =
            case null stars of True -> [(name, parent)]
                               _ -> []

isPropUsed :: Token -> Block -> Int -> Bool
isPropUsed prop scope nestingLevel = visitBlock (text prop) scope nestingLevel
    where
        visitBlock name (Block commands) nesting = visitCommands name commands nesting

        visitCommands name (Cmds cmds) nesting = any (\c -> visitCommand name c nesting) cmds

        visitCommand name (GuardCmd guard commands) nesting = (visitGuard name guard nesting) || (visitCommands name commands nesting)
        visitCommand name (ExprCmd expr) nesting = visitExpression name expr nesting
        visitCommand name (ReturnCmd expr) nesting = visitExpression name expr nesting
        visitCommand name (AssgCmd _ expr) nesting = visitExpression name expr nesting

        visitGuard name (Guard bools) nesting = any (\b -> visitBoolExpr name b nesting) bools

        visitBoolExpr name (BoolEq e1 e2) nesting = (visitExpression name e1 nesting) || (visitExpression name e2 nesting)

        visitExpression name (AddExpr primary _ exprs) nesting = (visitPrimary name primary nesting) || (any (\e -> visitExpression name e nesting) exprs)

        visitPrimary name (BlockPrim b) nesting = visitBlock name b (nesting + 1)
        visitPrimary name (RefPrim ref) nesting = visitReference name ref nesting
        visitPrimary name (ParensPrim e) nesting = visitExpression name e nesting
        visitPrimary _ _ _ = False

        visitReference name (Ref stars (Token _ refName _)) nesting = (length stars == nesting) && (name == refName)