default:
	java -jar $(ANTLR_PATH) Interpreter.g4
	javac *.java

tokens:
	java org.antlr.v4.runtime.misc.TestRig Interpreter block -tokens 

tree:
	java org.antlr.v4.runtime.misc.TestRig Interpreter block -tree

clean:
	rm -rf *.java *.class
