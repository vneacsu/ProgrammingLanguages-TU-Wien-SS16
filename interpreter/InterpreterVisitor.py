# Generated from Interpreter.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .InterpreterParser import InterpreterParser
else:
    from InterpreterParser import InterpreterParser

# This class defines a complete generic visitor for a parse tree produced by InterpreterParser.

class InterpreterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by InterpreterParser#block.
    def visitBlock(self, ctx:InterpreterParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#command.
    def visitCommand(self, ctx:InterpreterParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#guard.
    def visitGuard(self, ctx:InterpreterParser.GuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#blk.
    def visitBlk(self, ctx:InterpreterParser.BlkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#add.
    def visitAdd(self, ctx:InterpreterParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#identifier.
    def visitIdentifier(self, ctx:InterpreterParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#string.
    def visitString(self, ctx:InterpreterParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#subobj.
    def visitSubobj(self, ctx:InterpreterParser.SubobjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#parenthesis.
    def visitParenthesis(self, ctx:InterpreterParser.ParenthesisContext):
        return self.visitChildren(ctx)



del InterpreterParser