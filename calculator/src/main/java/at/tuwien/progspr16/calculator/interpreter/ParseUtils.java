package at.tuwien.progspr16.calculator.interpreter;

import at.tuwien.progspr16.calculator.grammar.CalculatorLexer;
import at.tuwien.progspr16.calculator.grammar.CalculatorParser;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;

public class ParseUtils {

    public static ParseTree parseCalculatorExpression(String expr) {
        CalculatorLexer lexer = new CalculatorLexer(new ANTLRInputStream(expr));

        CalculatorParser parser = new CalculatorParser(new CommonTokenStream(lexer));
        parser.removeErrorListeners();
        parser.addErrorListener(new BailoutErrorListener());

        return parser.calculator();
    }

    private static class BailoutErrorListener extends BaseErrorListener {
        @Override
        public void syntaxError(Recognizer<?, ?> recognizer, Object offendingSymbol, int line, int charPositionInLine, String msg, RecognitionException e) {
            System.err.println("@(offset: " + charPositionInLine + "): " + msg);
            System.exit(1);
        }
    }
}
