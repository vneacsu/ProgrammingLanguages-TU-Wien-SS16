package at.tuwien.progspr16.calculator.interpreter

import at.tuwien.progspr16.calculator.grammar.CalculatorBaseVisitor
import at.tuwien.progspr16.calculator.grammar.CalculatorParser.{BlockContext, CalculatorContext, IntegerContext, OperationContext}
import com.typesafe.scalalogging.Logger

class CalculatorInterpretVisitor extends CalculatorBaseVisitor[Unit] {
  val logger = Logger(classOf[CalculatorInterpretVisitor])

  var stack = List[StackContent]()

  def getCurrentState = stack
    .reverse
    .map {
      case IntStackContent(value) => value
      case BlockStackContent(value) => value.getText
    }
    .mkString(" ")

  override def visitCalculator(ctx: CalculatorContext): Unit = {
    visitChildren(ctx)

    val output = stack
      .reverse
      .mkString(", ")
    logger.info(s"$output")
  }

  override def visitInteger(ctx: IntegerContext): Unit = {
    stack = IntStackContent(ctx.getText.toInt) :: stack
  }

  override def visitBlock(ctx: BlockContext): Unit = {
    stack = BlockStackContent(ctx) :: stack
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
      case "~" => performNegation()
      case "a" => performApplyOperation()
      case "c" => performCopyOperation()
      case "d" => performDeleteOperation()
      case op => throw new UnsupportedOperationException(s"Unsupported operation '$op'")
    }
  }

  def performDeleteOperation(): Unit =
    stack = {
      stack.head match {
        case IntStackContent(value) =>
          stack.tail.take(value - 1) ++ stack.tail.drop(value)
        case _ => throw new IllegalArgumentException
      }
    }

  def performCopyOperation(): Unit =
    stack = {
      stack.head match {
        case IntStackContent(value) =>
          stack(value) :: stack.tail
        case _ => throw new IllegalArgumentException
      }
    }

  def performNegation(): Unit = {
    stack = stack.head match {
      case IntStackContent(value) => IntStackContent(value * -1) :: stack.tail
      case _ => throw new IllegalArgumentException
    }
  }

  private def performApplyOperation(): Unit = {
    stack.head match {
      case BlockStackContent(ctx) =>
        stack = stack.tail
        visit(ctx.calculator())
      case _ => throw new IllegalArgumentException
    }
  }

  private def performIntOperation(func: (IntStackContent, IntStackContent) => Int): Unit = {
    val (el1, el2) = CalculatorInterpretVisitor.takeTop2Elems(stack)

    stack = (el1, el2) match {
      case (el1: IntStackContent, el2: IntStackContent) => IntStackContent(func(el1, el2)) :: stack.drop(2)
      case _ => throw new IllegalArgumentException
    }
  }

  private def performBitsOperation(func: (IntStackContent, IntStackContent) => Int): Unit = {
    val (el1, el2) = CalculatorInterpretVisitor.takeTop2Elems(stack)

    val validValues = Set[StackContent](IntStackContent(0), IntStackContent(1))

    if (!validValues.contains(el1) || !validValues.contains(el2)) {
      throw new IllegalArgumentException
    } else {
      stack = (el1, el2) match {
        case (el1: IntStackContent, el2: IntStackContent) => IntStackContent(func(el1, el2)) :: stack.drop(2)
        case _ => throw new IllegalArgumentException
      }
    }
  }

  private def performBoolOperation(func: (IntStackContent, IntStackContent) => Boolean): Unit = {
    val (el1, el2) = CalculatorInterpretVisitor.takeTop2Elems(stack)

    stack = (el1, el2) match {
      case (el1: IntStackContent, el2: IntStackContent) =>
        if (func(el1, el2)) IntStackContent(1) :: stack.drop(2)
        else IntStackContent(0) :: stack.drop(2)
      case _ => throw new IllegalArgumentException
    }
  }

  sealed trait StackContent

  case class IntStackContent(value: Int) extends StackContent

  case class BlockStackContent(blockCtx: BlockContext) extends StackContent

}

object CalculatorInterpretVisitor {
  def takeTop2Elems[T](stack: List[T]): (T, T) = (stack.head, stack.tail.head)
}