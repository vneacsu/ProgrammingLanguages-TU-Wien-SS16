# Generated from Interpreter.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .InterpreterParser import InterpreterParser
else:
    from InterpreterParser import InterpreterParser

# This class defines a complete listener for a parse tree produced by InterpreterParser.
class InterpreterListener(ParseTreeListener):

    # Enter a parse tree produced by InterpreterParser#block.
    def enterBlock(self, ctx:InterpreterParser.BlockContext):
        pass

    # Exit a parse tree produced by InterpreterParser#block.
    def exitBlock(self, ctx:InterpreterParser.BlockContext):
        pass


    # Enter a parse tree produced by InterpreterParser#execute_guarded.
    def enterExecute_guarded(self, ctx:InterpreterParser.Execute_guardedContext):
        pass

    # Exit a parse tree produced by InterpreterParser#execute_guarded.
    def exitExecute_guarded(self, ctx:InterpreterParser.Execute_guardedContext):
        pass


    # Enter a parse tree produced by InterpreterParser#assign.
    def enterAssign(self, ctx:InterpreterParser.AssignContext):
        pass

    # Exit a parse tree produced by InterpreterParser#assign.
    def exitAssign(self, ctx:InterpreterParser.AssignContext):
        pass


    # Enter a parse tree produced by InterpreterParser#execute.
    def enterExecute(self, ctx:InterpreterParser.ExecuteContext):
        pass

    # Exit a parse tree produced by InterpreterParser#execute.
    def exitExecute(self, ctx:InterpreterParser.ExecuteContext):
        pass


    # Enter a parse tree produced by InterpreterParser#return.
    def enterReturn(self, ctx:InterpreterParser.ReturnContext):
        pass

    # Exit a parse tree produced by InterpreterParser#return.
    def exitReturn(self, ctx:InterpreterParser.ReturnContext):
        pass


    # Enter a parse tree produced by InterpreterParser#guard.
    def enterGuard(self, ctx:InterpreterParser.GuardContext):
        pass

    # Exit a parse tree produced by InterpreterParser#guard.
    def exitGuard(self, ctx:InterpreterParser.GuardContext):
        pass


    # Enter a parse tree produced by InterpreterParser#blk.
    def enterBlk(self, ctx:InterpreterParser.BlkContext):
        pass

    # Exit a parse tree produced by InterpreterParser#blk.
    def exitBlk(self, ctx:InterpreterParser.BlkContext):
        pass


    # Enter a parse tree produced by InterpreterParser#add.
    def enterAdd(self, ctx:InterpreterParser.AddContext):
        pass

    # Exit a parse tree produced by InterpreterParser#add.
    def exitAdd(self, ctx:InterpreterParser.AddContext):
        pass


    # Enter a parse tree produced by InterpreterParser#string.
    def enterString(self, ctx:InterpreterParser.StringContext):
        pass

    # Exit a parse tree produced by InterpreterParser#string.
    def exitString(self, ctx:InterpreterParser.StringContext):
        pass


    # Enter a parse tree produced by InterpreterParser#refer.
    def enterRefer(self, ctx:InterpreterParser.ReferContext):
        pass

    # Exit a parse tree produced by InterpreterParser#refer.
    def exitRefer(self, ctx:InterpreterParser.ReferContext):
        pass


    # Enter a parse tree produced by InterpreterParser#refer_prop.
    def enterRefer_prop(self, ctx:InterpreterParser.Refer_propContext):
        pass

    # Exit a parse tree produced by InterpreterParser#refer_prop.
    def exitRefer_prop(self, ctx:InterpreterParser.Refer_propContext):
        pass


    # Enter a parse tree produced by InterpreterParser#par_enclosing.
    def enterPar_enclosing(self, ctx:InterpreterParser.Par_enclosingContext):
        pass

    # Exit a parse tree produced by InterpreterParser#par_enclosing.
    def exitPar_enclosing(self, ctx:InterpreterParser.Par_enclosingContext):
        pass


    # Enter a parse tree produced by InterpreterParser#reference.
    def enterReference(self, ctx:InterpreterParser.ReferenceContext):
        pass

    # Exit a parse tree produced by InterpreterParser#reference.
    def exitReference(self, ctx:InterpreterParser.ReferenceContext):
        pass


