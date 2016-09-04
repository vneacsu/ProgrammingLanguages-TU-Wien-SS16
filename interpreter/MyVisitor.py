from InterpreterVisitor import InterpreterVisitor
from InterpreterParser import InterpreterParser

import subprocess
import logging

def remove_quotes(str):
    return str[1:-1]


class MyVisitor(InterpreterVisitor):
    def __init__(self):
        self.memory = {}

    def visitRefer_prop(self, ctx:InterpreterParser.Refer_propContext):
        expr = self.visit(ctx.expression())
        subObj = ctx.IDENTIFIER().pop().getText()
        logging.debug("refer property: " + expr)
        # print(type(expr))
        if subObj == 'syscall':
            return subprocess.call(expr, shell=True)

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
            logging.debug("left: NONE!!")
            logging.debug("right: " + str(right))
            return right
        else:
            logging.debug("left: " + left)
            logging.debug("right: " + right)
            return left + right