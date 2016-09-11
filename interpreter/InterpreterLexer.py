# Generated from Interpreter.g4 by ANTLR 4.5.3
from io import StringIO

from antlr4 import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\25")
        buf.write("j\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\6\17E\n\17\r\17\16\17F\3\20\6\20J\n\20")
        buf.write("\r\20\16\20K\3\21\3\21\7\21P\n\21\f\21\16\21S\13\21\3")
        buf.write("\21\3\21\3\22\3\22\3\23\6\23Z\n\23\r\23\16\23[\3\23\3")
        buf.write("\23\3\24\3\24\7\24b\n\24\f\24\16\24e\13\24\3\24\3\24\3")
        buf.write("\24\3\24\3c\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write("\3\2\5\4\2C\\c|\3\2$$\5\2\13\f\17\17\"\"n\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\3)\3\2\2\2\5+\3\2\2\2\7-\3\2\2\2\t/\3\2\2\2\13")
        buf.write("\61\3\2\2\2\r\63\3\2\2\2\17\65\3\2\2\2\21\67\3\2\2\2\23")
        buf.write("9\3\2\2\2\25;\3\2\2\2\27=\3\2\2\2\31?\3\2\2\2\33A\3\2")
        buf.write("\2\2\35D\3\2\2\2\37I\3\2\2\2!M\3\2\2\2#V\3\2\2\2%Y\3\2")
        buf.write("\2\2\'_\3\2\2\2)*\7}\2\2*\4\3\2\2\2+,\7\177\2\2,\6\3\2")
        buf.write("\2\2-.\7]\2\2.\b\3\2\2\2/\60\7<\2\2\60\n\3\2\2\2\61\62")
        buf.write("\7_\2\2\62\f\3\2\2\2\63\64\7?\2\2\64\16\3\2\2\2\65\66")
        buf.write("\7=\2\2\66\20\3\2\2\2\678\7`\2\28\22\3\2\2\29:\7%\2\2")
        buf.write(":\24\3\2\2\2;<\7.\2\2<\26\3\2\2\2=>\7*\2\2>\30\3\2\2\2")
        buf.write("?@\7+\2\2@\32\3\2\2\2AB\7\60\2\2B\34\3\2\2\2CE\t\2\2\2")
        buf.write("DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\36\3\2\2\2H")
        buf.write("J\7,\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2L \3\2")
        buf.write("\2\2MQ\7$\2\2NP\n\3\2\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2")
        buf.write("QR\3\2\2\2RT\3\2\2\2SQ\3\2\2\2TU\7$\2\2U\"\3\2\2\2VW\7")
        buf.write("-\2\2W$\3\2\2\2XZ\t\4\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2")
        buf.write("\2[\\\3\2\2\2\\]\3\2\2\2]^\b\23\2\2^&\3\2\2\2_c\7\'\2")
        buf.write("\2`b\13\2\2\2a`\3\2\2\2be\3\2\2\2cd\3\2\2\2ca\3\2\2\2")
        buf.write("df\3\2\2\2ec\3\2\2\2fg\7\f\2\2gh\3\2\2\2hi\b\24\2\2i(")
        buf.write("\3\2\2\2\b\2FKQ[c\3\b\2\2")
        return buf.getvalue()


class InterpreterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    IDENTIFIER = 14
    STAR = 15
    STRING = 16
    ADD = 17
    WS = 18
    COMMENTS = 19

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'['", "':'", "']'", "'='", "';'", "'^'", "'#'", 
            "','", "'('", "')'", "'.'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "STAR", "STRING", "ADD", "WS", "COMMENTS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "IDENTIFIER", 
                  "STAR", "STRING", "ADD", "WS", "COMMENTS" ]

    grammarFileName = "Interpreter.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


