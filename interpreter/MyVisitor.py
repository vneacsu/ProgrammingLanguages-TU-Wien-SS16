from InterpreterVisitor import InterpreterVisitor
from InterpreterParser import InterpreterParser

import subprocess

class MyVisitor(InterpreterVisitor):
    def __init__(self):
        self.memory = {}

    def visitSubobj(self, ctx:InterpreterParser.SubobjContext):
        expr = ctx.expression().expression().getText()[1:-1]
        subObj = ctx.IDENTIFIER().pop().getText()
        print(expr)
        print(type(expr))
        if subObj == 'syscall':
            subprocess.call(expr, shell=True)

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx):
        return ctx.INT().getText()

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitMulDiv(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == InterpreterParser.MUL:
            return left * right
        return left / right

    def visitAddSub(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == InterpreterParser.ADD:
            return left + right
        return left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())