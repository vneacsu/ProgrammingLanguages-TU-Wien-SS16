# Generated from Interpreter.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\25")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\7\2\r\n\2\f")
        buf.write("\2\16\2\20\13\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\30\n\3\f\3")
        buf.write("\16\3\33\13\3\3\3\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\3\3")
        buf.write("\3\3\5\3\'\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\60\n\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4\67\n\4\3\5\3\5\3\5\3\5\7\5=\n")
        buf.write("\5\f\5\16\5@\13\5\3\5\3\5\3\5\3\5\3\5\5\5G\n\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\6\5O\n\5\r\5\16\5P\7\5S\n\5\f\5\16\5")
        buf.write("V\13\5\3\5\2\3\b\6\2\4\6\b\2\3\4\2\t\t\f\fa\2\n\3\2\2")
        buf.write("\2\4/\3\2\2\2\6\61\3\2\2\2\bF\3\2\2\2\n\16\7\3\2\2\13")
        buf.write("\r\5\4\3\2\f\13\3\2\2\2\r\20\3\2\2\2\16\f\3\2\2\2\16\17")
        buf.write("\3\2\2\2\17\21\3\2\2\2\20\16\3\2\2\2\21\22\7\4\2\2\22")
        buf.write("\3\3\2\2\2\23\24\7\5\2\2\24\25\5\6\4\2\25\31\7\6\2\2\26")
        buf.write("\30\5\4\3\2\27\26\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2")
        buf.write("\31\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2\2\2\34\35\7\7\2")
        buf.write("\2\35\60\3\2\2\2\36 \7\b\2\2\37\36\3\2\2\2 #\3\2\2\2!")
        buf.write("\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#!\3\2\2\2$%\7\21\2\2")
        buf.write("%\'\7\t\2\2&!\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2()\5\b\5\2")
        buf.write(")*\7\n\2\2*\60\3\2\2\2+,\7\13\2\2,-\5\b\5\2-.\7\n\2\2")
        buf.write(".\60\3\2\2\2/\23\3\2\2\2/&\3\2\2\2/+\3\2\2\2\60\5\3\2")
        buf.write("\2\2\61\62\5\b\5\2\62\63\t\2\2\2\63\66\5\b\5\2\64\65\7")
        buf.write("\r\2\2\65\67\5\6\4\2\66\64\3\2\2\2\66\67\3\2\2\2\67\7")
        buf.write("\3\2\2\289\b\5\1\29G\7\22\2\2:G\5\2\2\2;=\7\b\2\2<;\3")
        buf.write("\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3\2\2")
        buf.write("\2AG\7\21\2\2BC\7\16\2\2CD\5\b\5\2DE\7\17\2\2EG\3\2\2")
        buf.write("\2F8\3\2\2\2F:\3\2\2\2F>\3\2\2\2FB\3\2\2\2GT\3\2\2\2H")
        buf.write("I\f\3\2\2IJ\7\23\2\2JS\5\b\5\4KN\f\4\2\2LM\7\20\2\2MO")
        buf.write("\7\21\2\2NL\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QS\3")
        buf.write("\2\2\2RH\3\2\2\2RK\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2")
        buf.write("\2U\t\3\2\2\2VT\3\2\2\2\r\16\31!&/\66>FPRT")
        return buf.getvalue()


class InterpreterParser ( Parser ):

    grammarFileName = "Interpreter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'['", "':'", "']'", "'*'", 
                     "'='", "';'", "'^'", "'#'", "','", "'('", "')'", "'.'", 
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

    ruleNames =  [ "block", "command", "guard", "expression" ]

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
            self.state = 8
            self.match(InterpreterParser.T__0)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << InterpreterParser.T__0) | (1 << InterpreterParser.T__2) | (1 << InterpreterParser.T__5) | (1 << InterpreterParser.T__8) | (1 << InterpreterParser.T__11) | (1 << InterpreterParser.IDENTIFIER) | (1 << InterpreterParser.STRING))) != 0):
                self.state = 9
                self.command()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
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

        def guard(self):
            return self.getTypedRuleContext(InterpreterParser.GuardContext,0)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterpreterParser.CommandContext)
            else:
                return self.getTypedRuleContext(InterpreterParser.CommandContext,i)


        def expression(self):
            return self.getTypedRuleContext(InterpreterParser.ExpressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(InterpreterParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return InterpreterParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = InterpreterParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 45
            token = self._input.LA(1)
            if token in [InterpreterParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(InterpreterParser.T__2)
                self.state = 18
                self.guard()
                self.state = 19
                self.match(InterpreterParser.T__3)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << InterpreterParser.T__0) | (1 << InterpreterParser.T__2) | (1 << InterpreterParser.T__5) | (1 << InterpreterParser.T__8) | (1 << InterpreterParser.T__11) | (1 << InterpreterParser.IDENTIFIER) | (1 << InterpreterParser.STRING))) != 0):
                    self.state = 20
                    self.command()
                    self.state = 25
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 26
                self.match(InterpreterParser.T__4)

            elif token in [InterpreterParser.T__0, InterpreterParser.T__5, InterpreterParser.T__11, InterpreterParser.IDENTIFIER, InterpreterParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self._errHandler.sync(self);
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==InterpreterParser.T__5:
                        self.state = 28
                        self.match(InterpreterParser.T__5)
                        self.state = 33
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 34
                    self.match(InterpreterParser.IDENTIFIER)
                    self.state = 35
                    self.match(InterpreterParser.T__6)


                self.state = 38
                self.expression(0)
                self.state = 39
                self.match(InterpreterParser.T__7)

            elif token in [InterpreterParser.T__8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.match(InterpreterParser.T__8)
                self.state = 42
                self.expression(0)
                self.state = 43
                self.match(InterpreterParser.T__7)

            else:
                raise NoViableAltException(self)

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
            self.state = 47
            self.expression(0)
            self.state = 48
            _la = self._input.LA(1)
            if not(_la==InterpreterParser.T__6 or _la==InterpreterParser.T__9):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 49
            self.expression(0)
            self.state = 52
            _la = self._input.LA(1)
            if _la==InterpreterParser.T__10:
                self.state = 50
                self.match(InterpreterParser.T__10)
                self.state = 51
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


    class BlkContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(InterpreterParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlk" ):
                listener.enterBlk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlk" ):
                listener.exitBlk(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlk" ):
                return visitor.visitBlk(self)
            else:
                return visitor.visitChildren(self)


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


    class IdentifierContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(InterpreterParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
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


    class SubobjContext(ExpressionContext):

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
            if hasattr( listener, "enterSubobj" ):
                listener.enterSubobj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubobj" ):
                listener.exitSubobj(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubobj" ):
                return visitor.visitSubobj(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a InterpreterParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(InterpreterParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = InterpreterParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            token = self._input.LA(1)
            if token in [InterpreterParser.STRING]:
                localctx = InterpreterParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 55
                self.match(InterpreterParser.STRING)

            elif token in [InterpreterParser.T__0]:
                localctx = InterpreterParser.BlkContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.block()

            elif token in [InterpreterParser.T__5, InterpreterParser.IDENTIFIER]:
                localctx = InterpreterParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==InterpreterParser.T__5:
                    self.state = 57
                    self.match(InterpreterParser.T__5)
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 63
                self.match(InterpreterParser.IDENTIFIER)

            elif token in [InterpreterParser.T__11]:
                localctx = InterpreterParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(InterpreterParser.T__11)
                self.state = 65
                self.expression(0)
                self.state = 66
                self.match(InterpreterParser.T__12)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = InterpreterParser.AddContext(self, InterpreterParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 70
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 71
                        self.match(InterpreterParser.ADD)
                        self.state = 72
                        self.expression(2)
                        pass

                    elif la_ == 2:
                        localctx = InterpreterParser.SubobjContext(self, InterpreterParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 73
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 76 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 74
                                self.match(InterpreterParser.T__13)
                                self.state = 75
                                self.match(InterpreterParser.IDENTIFIER)

                            else:
                                raise NoViableAltException(self)
                            self.state = 78 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                        pass

             
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
         




