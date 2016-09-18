package at.tuwien.progspr16.calculator.interpreter

import java.io.{InputStream, PrintStream}
import java.util.Scanner

import at.tuwien.progspr16.calculator.grammar.CalculatorParser.BlockContext
import org.antlr.v4.runtime.ParserRuleContext
import org.antlr.v4.runtime.tree.ParseTree

class Calculator(in: InputStream = System.in, out: PrintStream = System.out) {
  val scanner: Scanner = new Scanner(in)

  private var active: Boolean = true
  private val interpreter: CalculatorInterpretVisitor = new CalculatorInterpretVisitor(this)
  def run(): Unit = {
    while (active) {
      val optNextLine = nextCalculatorExpression

      if (optNextLine.nonEmpty) {
        interpret(optNextLine.get)
      } else {
        setInactive()
      }
    }
  }

  private def nextCalculatorExpression: Option[String] = {
    out.print("--> ")
    if (!scanner.hasNextLine) Option.empty
    else Option(scanner.nextLine)
  }

  def setInactive(): Unit = active = false

  def interpret(expr: String): String = {
    val tree: ParseTree = ParseUtils.parseCalculatorExpression(expr)
    interpreter.visit(tree)
    interpreter.getCurrentState
  }

  def write(text: String) = out.print(text+ " ")

  def readInt() = scanner.nextInt()

  def readBlockCtx(): BlockContext = {
    val parseTree = ParseUtils.parseCalculatorExpression(scanner.next)
    parseTree.asInstanceOf[ParserRuleContext].children.get(0).asInstanceOf[BlockContext]
  }
}