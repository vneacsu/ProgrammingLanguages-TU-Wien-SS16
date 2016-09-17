package at.tuwien.progspr16.calculator.interpreter

import at.tuwien.progspr16.calculator.grammar.{CalculatorLexer, CalculatorParser}
import org.antlr.v4.runtime._
import org.antlr.v4.runtime.tree.ParseTree

object ParseUtils {

  def parseCalculatorExpression(expr: String): ParseTree = {
    val lexer: CalculatorLexer = new CalculatorLexer(new ANTLRInputStream(expr))
    val parser: CalculatorParser = new CalculatorParser(new CommonTokenStream(lexer))
    parser.removeErrorListeners()
    parser.addErrorListener(new ParseUtils.BailoutErrorListener)
    parser.calculator
  }

  private class BailoutErrorListener extends BaseErrorListener {
    override def syntaxError(recognizer: Recognizer[_, _], offendingSymbol: Any, line: Int, charPositionInLine: Int, msg: String, e: RecognitionException) {
      System.err.println("@(offset: " + charPositionInLine + "): " + msg)
      System.exit(1)
    }
  }

}
