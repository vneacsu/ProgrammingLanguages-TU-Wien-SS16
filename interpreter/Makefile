default:
	java -jar $(ANTLR_PATH) Interpreter.g4
	javac *.java

tokens:
	java org.antlr.v4.runtime.misc.TestRig Interpreter block -tokens ${file}

tree:
	java org.antlr.v4.runtime.misc.TestRig Interpreter block -tree ${file}

gui:
	java org.antlr.v4.runtime.misc.TestRig Interpreter block -gui ${file}

clean:
	rm -rf *.java *.class
