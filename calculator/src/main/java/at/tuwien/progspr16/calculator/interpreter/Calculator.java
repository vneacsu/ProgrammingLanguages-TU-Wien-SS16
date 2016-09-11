package at.tuwien.progspr16.calculator.interpreter;

import org.antlr.v4.runtime.misc.Nullable;
import org.antlr.v4.runtime.tree.ParseTree;

import java.io.InputStream;
import java.io.PrintStream;
import java.util.Scanner;

public class Calculator implements Runnable {

    private final Scanner scanner;
    private final PrintStream out;
    private final CalculatorInterpretVisitor interpreter;

    public Calculator(InputStream in, PrintStream out) {
        this.scanner = new Scanner(in);
        this.out = out;
        this.interpreter = new CalculatorInterpretVisitor();
    }

    @Override
    public void run() {
        while (!Thread.currentThread().isInterrupted()) {
            String expr = nextCalculatorExpression();
            if (expr == null) break;

            interpret(expr);
        }
    }

    @Nullable
    private String nextCalculatorExpression() {
        out.print("Next calculator command: ");

        if (!scanner.hasNextLine()) return null;

        return scanner.nextLine();
    }

    private void interpret(String expr) {
        ParseTree tree = ParseUtils.parseCalculatorExpression(expr);

        interpreter.visit(tree);
    }
}
