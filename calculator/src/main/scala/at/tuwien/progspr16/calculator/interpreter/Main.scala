package at.tuwien.progspr16.calculator.interpreter

import java.io.{InputStream, PrintStream}
import java.util.Scanner

import scala.util.control.Breaks._

object Main {

  def main(args: Array[String]) {
    val calculator = new Calculator()

    new CalculatorRunnable(calculator, System.in, System.out).run()
  }

  class CalculatorRunnable(calculator: Calculator, in: InputStream, out: PrintStream) extends Runnable {
    val scanner: Scanner = new Scanner(in)

    override def run(): Unit = {
      while (!Thread.currentThread.isInterrupted) {
        val expr: String = nextCalculatorExpression

        breakable {
          if (expr == null) break
        }

        calculator.interpret(expr)
      }

    }

    private def nextCalculatorExpression: String = {
      out.print("--> ")
      if (!scanner.hasNextLine) return null
      scanner.nextLine
    }

  }

}
