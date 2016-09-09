import logging
import subprocess

from InterpreterParser import InterpreterParser
from InterpreterVisitor import InterpreterVisitor


def remove_quotes(str):
    return str[1:-1]


class MyVisitor(InterpreterVisitor):
    def __init__(self):
        self.memory = {}

    def visitRefer_prop(self, ctx:InterpreterParser.Refer_propContext):
        expr = self.visit(ctx.expression())
        subObj = ctx.IDENTIFIER().pop().getText()
        logging.debug("refer: " + expr)
        # print(type(expr))
        if subObj == 'syscall':
            result = str(subprocess.call(expr, shell=True))
            logging.debug("refer: syscall: " + result)
            return result

    def visitPar_enclosing(self, ctx:InterpreterParser.Par_enclosingContext):
        value = self.visit(ctx.expression())
        logging.debug("par enclosing: " + value)
        return value

    def visitAssign(self, ctx:InterpreterParser.AssignContext):
        varName = ctx.reference().IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        logging.debug("assign: " + varName + " -> " + value)
        self.memory[varName] = value
        return value

    def visitString(self, ctx:InterpreterParser.StringContext):
        value = remove_quotes(ctx.STRING().getText())
        logging.debug("string: " + value)
        return value

    def visitRefer(self, ctx:InterpreterParser.ReferContext):
        refer = ctx.reference().IDENTIFIER().getText()
        value = self.memory[refer]
        logging.debug("refer: " + refer + " -> " + value)
        return value

    def visitAdd(self, ctx:InterpreterParser.AddContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left is None:
            logging.debug("add: left: NONE!!")
            logging.debug("add: right: " + str(right))
            return right
        else:
            logging.debug("add: left: " + str(left))
            logging.debug("add: right: " + str(right))
            return left + right

    def visitBlock(self, ctx:InterpreterParser.BlockContext):
        logging.debug("block")
        for child in ctx.children:
            value = self.visit(child)
            if type(child) == InterpreterParser.ReturnContext:
                return value

    def visitReturn(self, ctx:InterpreterParser.ReturnContext):
        value = self.visit(ctx.expression())
        logging.debug("return: " + str(value))
        return value

    def visitExecute_guarded(self, ctx:InterpreterParser.Execute_guardedContext):
        guardCond = self.visit(ctx.guard())
        if guardCond:
            for command in ctx.command():
                self.visit(command)

    def visitGuard(self, ctx:InterpreterParser.GuardContext):
        expr1 = self.visit(ctx.expression(0))
        expr2 = self.visit(ctx.expression(1))
        logging.debug("guard: expr1: " + str(expr1))
        logging.debug("guard: expr2: " + str(expr2))
        logging.debug("guard: op: " + str(ctx.op.text))

        if ctx.op.text == "=":
            logging.debug("guard: result: " + str(expr1 == expr2))
            return expr1 == expr2
        else:
            logging.debug("guard: result: " + str(expr1 != expr2))
            return expr1 != expr2