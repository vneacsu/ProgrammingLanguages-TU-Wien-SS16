# Generated from Interpreter.g4 by ANTLR 4.5.3
# encoding: utf-8
from io import StringIO

from antlr4 import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\25")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\7\2")
        buf.write("\17\n\2\f\2\16\2\22\13\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\32")
        buf.write("\n\3\f\3\16\3\35\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3-\n\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4\64\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5>\n\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\6\5F\n\5\r\5\16\5G\7\5J\n\5\f\5")
        buf.write("\16\5M\13\5\3\6\7\6P\n\6\f\6\16\6S\13\6\3\6\3\6\3\6\2")
        buf.write("\3\b\7\2\4\6\b\n\2\3\4\2\b\b\13\13^\2\f\3\2\2\2\4,\3\2")
        buf.write("\2\2\6.\3\2\2\2\b=\3\2\2\2\nQ\3\2\2\2\f\20\7\3\2\2\r\17")
        buf.write("\5\4\3\2\16\r\3\2\2\2\17\22\3\2\2\2\20\16\3\2\2\2\20\21")
        buf.write("\3\2\2\2\21\23\3\2\2\2\22\20\3\2\2\2\23\24\7\4\2\2\24")
        buf.write("\3\3\2\2\2\25\26\7\5\2\2\26\27\5\6\4\2\27\33\7\6\2\2\30")
        buf.write("\32\5\4\3\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2")
        buf.write("\33\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2\2\36\37\7\7\2")
        buf.write("\2\37-\3\2\2\2 !\5\n\6\2!\"\7\b\2\2\"#\5\b\5\2#$\7\t\2")
        buf.write("\2$-\3\2\2\2%&\5\b\5\2&\'\7\t\2\2\'-\3\2\2\2()\7\n\2\2")
        buf.write(")*\5\b\5\2*+\7\t\2\2+-\3\2\2\2,\25\3\2\2\2, \3\2\2\2,")
        buf.write("%\3\2\2\2,(\3\2\2\2-\5\3\2\2\2./\5\b\5\2/\60\t\2\2\2\60")
        buf.write("\63\5\b\5\2\61\62\7\f\2\2\62\64\5\6\4\2\63\61\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\7\3\2\2\2\65\66\b\5\1\2\66>\7\22\2\2")
        buf.write("\67>\5\2\2\28>\5\n\6\29:\7\r\2\2:;\5\b\5\2;<\7\16\2\2")
        buf.write("<>\3\2\2\2=\65\3\2\2\2=\67\3\2\2\2=8\3\2\2\2=9\3\2\2\2")
        buf.write(">K\3\2\2\2?@\f\3\2\2@A\7\23\2\2AJ\5\b\5\4BE\f\4\2\2CD")
        buf.write("\7\17\2\2DF\7\21\2\2EC\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3")
        buf.write("\2\2\2HJ\3\2\2\2I?\3\2\2\2IB\3\2\2\2JM\3\2\2\2KI\3\2\2")
        buf.write("\2KL\3\2\2\2L\t\3\2\2\2MK\3\2\2\2NP\7\20\2\2ON\3\2\2\2")
        buf.write("PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2RT\3\2\2\2SQ\3\2\2\2TU\7")
        buf.write("\21\2\2U\13\3\2\2\2\13\20\33,\63=GIKQ")
        return buf.getvalue()


class InterpreterParser ( Parser ):

    grammarFileName = "Interpreter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'['", "':'", "']'", "'='", 
                     "';'", "'^'", "'#'", "','", "'('", "')'", "'.'", "'*'", 
                     "<INVALID>", "<INVALID>", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "STRING", "ADD", "WS", "COMMENTS" ]

    RULE_block = 0
    RULE_command = 1
    RULE_guard = 2
    RULE_expression = 3
    RULE_reference = 4

    ruleNames =  [ "block", "command", "guard", "expression", "reference" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    IDENTIFIER=15
    STRING=16
    ADD=17
    WS=18
    COMMENTS=19

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterpreterParser.CommandContext)
            else:
                return self.getTypedRuleContext(InterpreterParser.CommandContext,i)


        def getRuleIndex(self):
            return InterpreterParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = InterpreterParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(InterpreterParser.T__0)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << InterpreterParser.T__0) | (1 << InterpreterParser.T__2) | (1 << InterpreterParser.T__7) | (1 << InterpreterParser.T__10) | (1 << InterpreterParser.T__13) | (1 << InterpreterParser.IDENTIFIER) | (1 << InterpreterParser.STRING))) != 0):
                self.state = 11
                self.command()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self.match(InterpreterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return InterpreterParser.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Execute_guardedContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def guard(self):
            return self.getTypedRuleContext(InterpreterParser.GuardContext,0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterpreterParser.CommandContext)
            else:
                return self.getTypedRuleContext(InterpreterParser.CommandContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecute_guarded" ):
                listener.enterExecute_guarded(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecute_guarded" ):
                listener.exitExecute_guarded(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecute_guarded" ):
                return visitor.visitExecute_guarded(self)
            else:
                return visitor.visitChildren(self)


    class ExecuteContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(InterpreterParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecute" ):
                listener.enterExecute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecute" ):
                listener.exitExecute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecute" ):
                return visitor.visitExecute(self)
            else:
                return visitor.visitChildren(self)


    class ReturnContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(InterpreterParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reference(self):
            return self.getTypedRuleContext(InterpreterParser.ReferenceContext,0)

        def expression(self):
            return self.getTypedRuleContext(InterpreterParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def command(self):

        localctx = InterpreterParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 42
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = InterpreterParser.Execute_guardedContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(InterpreterParser.T__2)
                self.state = 20
                self.guard()
                self.state = 21
                self.match(InterpreterParser.T__3)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << InterpreterParser.T__0) | (1 << InterpreterParser.T__2) | (1 << InterpreterParser.T__7) | (1 << InterpreterParser.T__10) | (1 << InterpreterParser.T__13) | (1 << InterpreterParser.IDENTIFIER) | (1 << InterpreterParser.STRING))) != 0):
                    self.state = 22
                    self.command()
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 28
                self.match(InterpreterParser.T__4)
                pass

            elif la_ == 2:
                localctx = InterpreterParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.reference()
                self.state = 31
                self.match(InterpreterParser.T__5)
                self.state = 32
                self.expression(0)
                self.state = 33
                self.match(InterpreterParser.T__6)
                pass

            elif la_ == 3:
                localctx = InterpreterParser.ExecuteContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.expression(0)
                self.state = 36
                self.match(InterpreterParser.T__6)
                pass

            elif la_ == 4:
                localctx = InterpreterParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(InterpreterParser.T__7)
                self.state = 39
                self.expression(0)
                self.state = 40
                self.match(InterpreterParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GuardContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterpreterParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(InterpreterParser.ExpressionContext,i)


        def guard(self):
            return self.getTypedRuleContext(InterpreterParser.GuardContext,0)


        def getRuleIndex(self):
            return InterpreterParser.RULE_guard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuard" ):
                listener.enterGuard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuard" ):
                listener.exitGuard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGuard" ):
                return visitor.visitGuard(self)
            else:
                return visitor.visitChildren(self)




    def guard(self):

        localctx = InterpreterParser.GuardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_guard)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.expression(0)
            self.state = 45
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==InterpreterParser.T__5 or _la==InterpreterParser.T__8):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 46
            self.expression(0)
            self.state = 49
            _la = self._input.LA(1)
            if _la==InterpreterParser.T__9:
                self.state = 47
                self.match(InterpreterParser.T__9)
                self.state = 48
                self.guard()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return InterpreterParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterpreterParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(InterpreterParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(InterpreterParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class Function_blockContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(InterpreterParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_block" ):
                listener.enterFunction_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_block" ):
                listener.exitFunction_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_block" ):
                return visitor.visitFunction_block(self)
            else:
                return visitor.visitChildren(self)


    class ReferContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reference(self):
            return self.getTypedRuleContext(InterpreterParser.ReferenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRefer" ):
                listener.enterRefer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRefer" ):
                listener.exitRefer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRefer" ):
                return visitor.visitRefer(self)
            else:
                return visitor.visitChildren(self)


    class Refer_propContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(InterpreterParser.ExpressionContext,0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(InterpreterParser.IDENTIFIER)
            else:
                return self.getToken(InterpreterParser.IDENTIFIER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRefer_prop" ):
                listener.enterRefer_prop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRefer_prop" ):
                listener.exitRefer_prop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRefer_prop" ):
                return visitor.visitRefer_prop(self)
            else:
                return visitor.visitChildren(self)


    class Par_enclosingContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(InterpreterParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar_enclosing" ):
                listener.enterPar_enclosing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar_enclosing" ):
                listener.exitPar_enclosing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar_enclosing" ):
                return visitor.visitPar_enclosing(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = InterpreterParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            token = self._input.LA(1)
            if token in [InterpreterParser.STRING]:
                localctx = InterpreterParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 52
                self.match(InterpreterParser.STRING)

            elif token in [InterpreterParser.T__0]:
                localctx = InterpreterParser.Function_blockContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.block()

            elif token in [InterpreterParser.T__13, InterpreterParser.IDENTIFIER]:
                localctx = InterpreterParser.ReferContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.reference()

            elif token in [InterpreterParser.T__10]:
                localctx = InterpreterParser.Par_enclosingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(InterpreterParser.T__10)
                self.state = 56
                self.expression(0)
                self.state = 57
                self.match(InterpreterParser.T__11)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = InterpreterParser.AddContext(self, InterpreterParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 61
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 62
                        self.match(InterpreterParser.ADD)
                        self.state = 63
                        self.expression(2)
                        pass

                    elif la_ == 2:
                        localctx = InterpreterParser.Refer_propContext(self, InterpreterParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 64
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 67 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 65
                                self.match(InterpreterParser.T__12)
                                self.state = 66
                                self.match(InterpreterParser.IDENTIFIER)

                            else:
                                raise NoViableAltException(self)
                            self.state = 69 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ReferenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(InterpreterParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return InterpreterParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference" ):
                return visitor.visitReference(self)
            else:
                return visitor.visitChildren(self)




    def reference(self):

        localctx = InterpreterParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==InterpreterParser.T__13:
                self.state = 76
                self.match(InterpreterParser.T__13)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(InterpreterParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




