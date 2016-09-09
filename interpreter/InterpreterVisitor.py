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


    # Visit a parse tree produced by InterpreterParser#execute_guarded.
    def visitExecute_guarded(self, ctx:InterpreterParser.Execute_guardedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#assign.
    def visitAssign(self, ctx:InterpreterParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#execute.
    def visitExecute(self, ctx:InterpreterParser.ExecuteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#return.
    def visitReturn(self, ctx:InterpreterParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#guard.
    def visitGuard(self, ctx:InterpreterParser.GuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#add.
    def visitAdd(self, ctx:InterpreterParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#string.
    def visitString(self, ctx:InterpreterParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#function_block.
    def visitFunction_block(self, ctx:InterpreterParser.Function_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#refer.
    def visitRefer(self, ctx:InterpreterParser.ReferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#refer_prop.
    def visitRefer_prop(self, ctx:InterpreterParser.Refer_propContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#par_enclosing.
    def visitPar_enclosing(self, ctx:InterpreterParser.Par_enclosingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#reference.
    def visitReference(self, ctx:InterpreterParser.ReferenceContext):
        return self.visitChildren(ctx)



del InterpreterParser