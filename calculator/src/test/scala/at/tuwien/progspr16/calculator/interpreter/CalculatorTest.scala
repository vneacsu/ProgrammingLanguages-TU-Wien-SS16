package at.tuwien.progspr16.calculator.interpreter

import org.scalatest.{BeforeAndAfter, FunSuite, Matchers}

class CalculatorTest extends FunSuite with Matchers with BeforeAndAfter {

  test ("compute basic operations of two numbers") {
    interpretAndExpect("2 3 +", "5")
    interpretAndExpect("3 2 -", "-1")
    interpretAndExpect("2 3 *", "6")
    interpretAndExpect("3 6 /", "2")
    interpretAndExpect("5 6 %", "1")
    interpretAndExpect("1 0 &", "0")
    interpretAndExpect("1 0 |", "1")
    interpretAndExpect("8 2 =", "0")
    interpretAndExpect("5 5 =", "1")
    interpretAndExpect("5 6 >", "1")
    interpretAndExpect("6 5 >", "0")
    interpretAndExpect("6 5 <", "1")
    interpretAndExpect("5 6 <", "0")
  }

  test ("should throw exception on invalid arguments") {
    val calculator = new Calculator
    a [ArithmeticException] should be thrownBy {
      calculator.interpret("0 6 %")
    }
    a [ArithmeticException] should be thrownBy {
      calculator.interpret("0 6 /")
    }
    a [IllegalArgumentException] should be thrownBy {
      calculator.interpret("0 2 &")
    }
    a [IllegalArgumentException] should be thrownBy {
      calculator.interpret("1 6 |")
    }
  }

  def interpretAndExpect(expr: String, expected: String): Unit = {
    val calculator = new Calculator
    calculator.interpret(expr) should be (expected)
  }

}
