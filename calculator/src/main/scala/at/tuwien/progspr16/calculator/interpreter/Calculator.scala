package at.tuwien.progspr16.calculator.interpreter

import java.io.{InputStream, PrintStream}
import java.util.Scanner

import org.antlr.v4.runtime.tree.ParseTree

import scala.util.control.Breaks._

class Calculator(val in: InputStream, val out: PrintStream) extends Runnable {

  val scanner: Scanner = new Scanner(in)
  val interpreter: CalculatorInterpretVisitor = new CalculatorInterpretVisitor

  def run() {
    while (!Thread.currentThread.isInterrupted) {
      val expr: String = nextCalculatorExpression

      breakable {
        if (expr == null) break
      }

      interpret(expr)
    }
  }

  private def nextCalculatorExpression: String = {
    out.print("Next calculator command: ")
    if (!scanner.hasNextLine) return null
    scanner.nextLine
  }

  private def interpret(expr: String) {
    val tree: ParseTree = ParseUtils.parseCalculatorExpression(expr)
    interpreter.visit(tree)
  }
}