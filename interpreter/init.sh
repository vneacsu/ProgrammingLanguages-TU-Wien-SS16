#! /bin/sh

CURR_FOLDER=`pwd`
ANTLR_FOLDER=antlr
ANTLR_JAR=antlr.jar
export ANTLR_PATH=$CURR_FOLDER/$ANTLR_FOLDER/$ANTLR_JAR

mkdir -p $ANTLR_FOLDER/
if [ ! -f ${ANTLR_PATH} ]; then
    curl 'http://www.antlr.org/download/antlr-4.5.3-complete.jar' -o $ANTLR_FOLDER/$ANTLR_JAR
fi

export CLASSPATH=".:$ANTLR_PATH:$CLASSPATH"

alias antlr4='java -jar $ANTLR_PATH'
alias grun='java org.antlr.v4.runtime.misc.TestRig'
