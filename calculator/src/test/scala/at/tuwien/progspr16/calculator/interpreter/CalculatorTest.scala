package at.tuwien.progspr16.calculator.interpreter

import org.scalatest.{BeforeAndAfter, FunSuite, Matchers}

class CalculatorTest extends FunSuite with Matchers with BeforeAndAfter {

  test("compute basic operations with two numbers") {
    interpretAndExpect("2 3+", "5")
    interpretAndExpect("3 2-", "-1")
    interpretAndExpect("2 3*", "6")
    interpretAndExpect("3 6/", "2")
    interpretAndExpect("5 6%", "1")
    interpretAndExpect("1 0&", "0")
    interpretAndExpect("1 0|", "1")
    interpretAndExpect("8 2=", "0")
    interpretAndExpect("5 5=", "1")
    interpretAndExpect("5 6>", "1")
    interpretAndExpect("6 5>", "0")
    interpretAndExpect("6 5<", "1")
    interpretAndExpect("5 6<", "0")
  }


  test("compute sequences of basic operations") {
    interpretAndExpect("3 2 8 1 + * /", "6")
  }

  test("compute advanced operations") {
    interpretAndExpect("3 2 8 2d", "3 8")
    interpretAndExpect("0[9][8]0 4d", "[9] [8] 0")
    interpretAndExpect("0[9~][8]3c", "0 [9~] [8] 0")
    interpretAndExpect("4 3[2*]a+", "10")
  }

  test("execute conditional block") {
    interpretAndExpect("0[9~][8][3c4d1+da]a", "-9")
  }

  test("compute 3 factorial") {
    interpretAndExpect("3[2c1 3c-1c1=3c[][3c4d1+da]a2d*]2c3d2ca2d", "6")
  }

  test ("check if x is factor of y") {
    interpretAndExpect("63 3 [2c 2c 0 2c 3d 3c 4d % =]a", "63 3 1")
    interpretAndExpect("63 5 [2c 2c 0 2c 3d 3c 4d % =]a", "63 5 0")
  }

   test ("divide x by y on condition and put result on stack, otherwise increment divisor") {
     interpretAndExpect("63 3 1 [[1+] [2c 3d / 2] 3c 4d 1+ d a]a", "21 2")
     interpretAndExpect("63 2 0 [[1+] [2c 3d / 2] 3c 4d 1+ d a]a", "63 3")
   }

  test ("check if x is divisible by y, then divide, otherise increment divisor") {
    interpretAndExpect("63 3 [2c 2c 0 2c 3d 3c 4d % =]a [[1+] [2c 3d / 2] 3c 4d 1+ d a]a", "21 2")
    interpretAndExpect("63 2 [2c 2c 0 2c 3d 3c 4d % =]a [[1+] [2c 3d / 2] 3c 4d 1+ d a]a", "63 3")
  }

  // x y [1 3c 4d - 2c 3d] a                      -- decrement x by 1
  // x y [2c 1 = [] [x] 3c 4d 1+ d a] a           -- stop if x is 1

  // [[2c 2c 0 2c 3d 3c 4d % =]a [[1+] [1c w 2c 3d / 2] 3c 4d 1+ d a]a]     -- divide if x divisible by y, otherwise increment y
  // [2c 1 = [4ca3ca] [x] 3c 4d 1+ d a]                                     -- if x is not 1: call above method and then call myself

  // [[2c 2c 0 2c 3d 3c 4d % =]a [[1+] [1c w 2c 3d / 2] 3c 4d 1+ d a]a] [2c 1 = [4ca3ca] [x] 3c 4d 1+ d a] i 2 3ca

  test("throw exception on invalid arguments") {
    val calculator = new Calculator
    a[ArithmeticException] should be thrownBy {
      calculator.interpret("0 6 %")
    }
    a[ArithmeticException] should be thrownBy {
      calculator.interpret("0 6 /")
    }
    a[IllegalArgumentException] should be thrownBy {
      calculator.interpret("0 2 &")
    }
    a[IllegalArgumentException] should be thrownBy {
      calculator.interpret("1 6 |")
    }
  }

  def interpretAndExpect(expr: String, expected: String): Unit = {
    val calculator = new Calculator
    calculator.interpret(expr) should be(expected)
  }

}
