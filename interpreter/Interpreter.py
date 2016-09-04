import logging
import sys

from antlr4 import *
from antlr4.InputStream import InputStream

from InterpreterLexer import InterpreterLexer
from InterpreterParser import InterpreterParser
from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    logging.basicConfig(level=logging.DEBUG)

    lexer = InterpreterLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = InterpreterParser(token_stream)
    tree = parser.block()

    visitor = MyVisitor()
    visitor.visit(tree)