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


    # Enter a parse tree produced by InterpreterParser#command.
    def enterCommand(self, ctx:InterpreterParser.CommandContext):
        pass

    # Exit a parse tree produced by InterpreterParser#command.
    def exitCommand(self, ctx:InterpreterParser.CommandContext):
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


    # Enter a parse tree produced by InterpreterParser#identifier.
    def enterIdentifier(self, ctx:InterpreterParser.IdentifierContext):
        pass

    # Exit a parse tree produced by InterpreterParser#identifier.
    def exitIdentifier(self, ctx:InterpreterParser.IdentifierContext):
        pass


    # Enter a parse tree produced by InterpreterParser#string.
    def enterString(self, ctx:InterpreterParser.StringContext):
        pass

    # Exit a parse tree produced by InterpreterParser#string.
    def exitString(self, ctx:InterpreterParser.StringContext):
        pass


    # Enter a parse tree produced by InterpreterParser#subobj.
    def enterSubobj(self, ctx:InterpreterParser.SubobjContext):
        pass

    # Exit a parse tree produced by InterpreterParser#subobj.
    def exitSubobj(self, ctx:InterpreterParser.SubobjContext):
        pass


    # Enter a parse tree produced by InterpreterParser#parenthesis.
    def enterParenthesis(self, ctx:InterpreterParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by InterpreterParser#parenthesis.
    def exitParenthesis(self, ctx:InterpreterParser.ParenthesisContext):
        pass


