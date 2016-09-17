package at.tuwien.progspr16.calculator.interpreter

import org.antlr.v4.runtime.tree.ParseTree

class Calculator {

  private val interpreter: CalculatorInterpretVisitor = new CalculatorInterpretVisitor

  def interpret(expr: String): String = {
    val tree: ParseTree = ParseUtils.parseCalculatorExpression(expr)
    interpreter.visit(tree)
    interpreter.getCurrentState
  }
}