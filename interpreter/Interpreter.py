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

    lexer = InterpreterLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = InterpreterParser(token_stream)
    tree = parser.block()

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    visitor = MyVisitor()
    visitor.visit(tree)