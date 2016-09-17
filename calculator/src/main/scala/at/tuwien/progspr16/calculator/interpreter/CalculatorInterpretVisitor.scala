package at.tuwien.progspr16.calculator.interpreter

import at.tuwien.progspr16.calculator.grammar.CalculatorBaseVisitor
import at.tuwien.progspr16.calculator.grammar.CalculatorParser.{CalculatorContext, IntegerContext, OperationContext}
import com.typesafe.scalalogging.Logger

import scala.collection.immutable.Stack

class CalculatorInterpretVisitor extends CalculatorBaseVisitor[Unit] {
  val logger = Logger(classOf[CalculatorInterpretVisitor])

  var stack = Stack[StackContent]()

  def getCurrentState = stack
    .map(e => e.asInstanceOf[IntStackContent].value)
    .mkString(" ")

  override def visitCalculator(ctx: CalculatorContext): Unit = {
    visitChildren(ctx)

    val output = stack
      .mkString(", ")
    logger.info(s"$output")
  }

  override def visitInteger(ctx: IntegerContext): Unit = {
    stack = stack.push(IntStackContent(ctx.getText.toInt))
  }

  override def visitOperation(ctx: OperationContext): Unit = {
    ctx.getText match {
      case "+" => performIntOperation((el1, el2) => el1.value + el2.value)
      case "-" => performIntOperation((el1, el2) => el1.value - el2.value)
      case "*" => performIntOperation((el1, el2) => el1.value * el2.value)
      case "/" => performIntOperation((el1, el2) => el1.value / el2.value)
      case "%" => performIntOperation((el1, el2) => el1.value % el2.value)
      case "&" => performBitsOperation((el1, el2) => el1.value & el2.value)
      case "|" => performBitsOperation((el1, el2) => el1.value | el2.value)
      case "=" => performBoolOperation((el1, el2) => el1.value == el2.value)
      case "<" => performBoolOperation((el1, el2) => el1.value < el2.value)
      case ">" => performBoolOperation((el1, el2) => el1.value > el2.value)
      case op => throw new UnsupportedOperationException(s"Unsupported operation '$op'")
    }
  }

  def performIntOperation(func: (IntStackContent, IntStackContent) => Int): Unit = {
    val (el1, el2, poppedStack) = CalculatorInterpretVisitor.popTop2Elems(stack)

    val newElem = func(el1.asInstanceOf[IntStackContent], el2.asInstanceOf[IntStackContent])
    stack = poppedStack.push(IntStackContent(newElem))
  }

  def performBitsOperation(func: (IntStackContent, IntStackContent) => Int): Unit = {
    val (el1, el2, poppedStack) = CalculatorInterpretVisitor.popTop2Elems(stack)

    val validValues = Set[StackContent](IntStackContent(0), IntStackContent(1))

    if (!validValues.contains(el1) || !validValues.contains(el2)) {
      throw new IllegalArgumentException
    } else {
      val newElem = func(el1.asInstanceOf[IntStackContent], el2.asInstanceOf[IntStackContent])
      stack = poppedStack.push(IntStackContent(newElem))
    }
  }

  def performBoolOperation(func: (IntStackContent, IntStackContent) => Boolean): Unit = {
    val (el1, el2, poppedStack) = CalculatorInterpretVisitor.popTop2Elems(stack)

    val funcResult = func(el1.asInstanceOf[IntStackContent], el2.asInstanceOf[IntStackContent])
    val newElem: IntStackContent = if (funcResult) IntStackContent(1) else IntStackContent(0)
    stack = poppedStack.push(newElem)
  }

  sealed trait StackContent

  case class IntStackContent(value: Int) extends StackContent

}

object CalculatorInterpretVisitor {
  def popTop2Elems[T](stack: Stack[T]) = {
    val (el1, stack1) = stack.pop2
    val (el2, stack2) = stack1.pop2

    (el1, el2, stack2)
  }
}