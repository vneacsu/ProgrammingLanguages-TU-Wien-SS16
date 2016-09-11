import logging
import subprocess
from shlex import split

from InterpreterParser import InterpreterParser
from InterpreterVisitor import InterpreterVisitor

RETURN_VALUE = "RETURN_VALUE"


def remove_quotes(str):
    return str[1:-1]


def is_block_delimiter(child):
    return child.getText() == "{" or child.getText() == "}"


class MyVisitor(InterpreterVisitor):
    def __init__(self):
        self.global_scope = {}
        self.stack = [{}] * 100
        self.block_level = 0
        self.functionCall = False

    def visitRefer_prop(self, ctx: InterpreterParser.Refer_propContext):
        expr = self.visit(ctx.expression())
        subObj = ctx.IDENTIFIER(0).getText()
        logging.debug("refer: " + expr)
        if subObj == 'syscall':
            result = str(subprocess.call(expr, shell=True))
            logging.debug("refer: syscall: " + result)
            return result
        elif subObj == 'iosyscall':
            expr1 = expr.split("|")[0]
            expr2 = expr.split("|")[1]

            p1 = subprocess.Popen(split(expr1), stdout=subprocess.PIPE)
            p2 = subprocess.Popen(split(expr2), stdin=p1.stdout, stdout=subprocess.PIPE).communicate()[0]
            result = p2.decode("ascii").replace("\n", "")

            logging.debug("refer: iosyscall: " + result)
            return result

    def visitPar_enclosing(self, ctx: InterpreterParser.Par_enclosingContext):
        value = self.visit(ctx.expression())
        logging.debug("par enclosing: " + value)
        return value

    def visitAssign(self, ctx: InterpreterParser.AssignContext):
        var_ref = ctx.reference()
        var_name = var_ref.IDENTIFIER(0).getText()

        if type(ctx.expression()) is InterpreterParser.Function_blockContext:
            self.stack[self.block_level][var_name] = ctx.expression()
        else:
            value = self.visit(ctx.expression())

            if len(var_ref.IDENTIFIER()) == 1:
                logging.debug("assign: " + var_name + " -> " + str(value))
                self.stack[self.block_level][var_name] = value
            elif len(var_ref.IDENTIFIER()) == 2:
                prop_name = var_ref.IDENTIFIER(1).getText()
                if var_name in self.stack[self.block_level]:
                    self.stack[self.block_level][var_name][prop_name] = value
                else:
                    prop_value = {prop_name: value}
                    self.stack[self.block_level][var_name] = prop_value
            else:
                raise ValueError('Operation unsupported')

    def visitString(self, ctx: InterpreterParser.StringContext):
        value = remove_quotes(ctx.STRING().getText())
        logging.debug("string: " + value)
        return value

    def visitRefer(self, ctx: InterpreterParser.ReferContext):
        reference = ctx.reference()
        refer_var_name = reference.IDENTIFIER(0).getText()

        if reference.STAR() is None:
            value = self.stack[self.block_level][refer_var_name]
        else:
            block_ref_diff = len(reference.STAR().getText())
            value = self.stack[self.block_level - block_ref_diff][refer_var_name]

        if type(value) is InterpreterParser.Function_blockContext:
            self.functionCall = True
            function_block_value = self.visit(value)
            self.functionCall = False
            logging.debug("refer: function: " + refer_var_name + " -> " + function_block_value)
            return function_block_value
        else:
            if len(reference.IDENTIFIER()) == 1:
                logging.debug("refer: variable: " + refer_var_name + " -> " + str(value))
                return value
            elif len(reference.IDENTIFIER()) == 2:
                property_name = reference.IDENTIFIER(1).getText()
                return value[property_name]
            else:
                raise ValueError('Operation unsupported')

    def visitAdd(self, ctx: InterpreterParser.AddContext):
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

    def visitFunction_block(self, ctx: InterpreterParser.Function_blockContext):
        logging.debug("function_block")

        for child in ctx.block().children:
            if is_block_delimiter(child):
                if child.getText() == "{":
                    self.handle_block_begin(self.functionCall)
                elif child.getText() == "}":
                    self.handle_block_end()
                else:
                    raise ValueError('Invalid block delimiter ' + str(child.getText()))

            self.visit(child)
            if RETURN_VALUE in self.global_scope:
                value = self.global_scope[RETURN_VALUE]
                del self.global_scope[RETURN_VALUE]
                self.handle_block_end()
                return value

        contains_only_assignments = self.contains_only_assignments(ctx)
        if not contains_only_assignments:
            raise ValueError('No return value')

    def handle_block_begin(self, function_call):
        self.block_level += 1
        if not function_call:
            self.stack[self.block_level] = {}
        logging.debug("function_block: block_level: " + str(self.block_level))

    def handle_block_end(self):
        self.block_level -= 1
        logging.debug("function_block: block_level: " + str(self.block_level))

    def contains_only_assignments(self, ctx):
        contains_only_assignments = True
        for child in ctx.block().children:
            if not is_block_delimiter(child) and type(child) != InterpreterParser.AssignContext:
                contains_only_assignments = False
        return contains_only_assignments

    def visitReturn(self, ctx: InterpreterParser.ReturnContext):
        value = self.visit(ctx.expression())
        logging.debug("return: " + str(value))
        self.global_scope[RETURN_VALUE] = value
        return value

    def visitExecute_guarded(self, ctx: InterpreterParser.Execute_guardedContext):
        guardCond = self.visit(ctx.guard())
        if guardCond:
            for command in ctx.command():
                self.visit(command)

    def visitGuard(self, ctx: InterpreterParser.GuardContext):
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
