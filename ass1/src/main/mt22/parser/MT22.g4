grammar MT22;
//MSSV 2013907
@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
program: declare+ EOF;

declare: var_declare | func_declare;

BOOLIT: TRUE | FALSE;
//KEYWORD
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

//SEPERATOR
LB: '(';
RB: ')';
DOT: '.';
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
LPAREN: '{';
RPAREN: '}';
ASSIGN: '=';

//OPERATOR
ADDOP: '+';
NEGOP: '-';
MULOP: '*';
DIVOP: '/';
REMAINOP: '%';
NEGATION: '!';
CONJUNCTION: '&&';
DISJUNCTION: '||';
EQUAL: '==';
NOTEQUAL: '!=';
LESSTHAN: '<';
GREATERTHAN: '>';
LTOE: '<=';
GTOE: '>=';
CONCAT: '::';

IDENTIFIER: (UNDERLETTER | UPERLETTER | UNDERSCORE) (UNDERLETTER | UPERLETTER | DIGIT | UNDERSCORE)*;

//Literals
FLOATLIT: INTLIT ((DOT (DIGIT+ | DIGIT+ [eE] [+-]? DIGIT+)) | ([eE] [+-]? DIGIT+)) {self.text = self.text.replace('_','')};
INTLIT: DIGIT | ([1-9] UNDERSCORE? (DIGIT UNDERSCORE? DIGIT?)+) {self.text = self.text.replace('_','')};
//1__2345
STRINGLIT: DOUBLEQUOTE STRINGCHAR* DOUBLEQUOTE{
	result = str(self.text)
	self.text = result[1:-1]
};
//{123},{134}
//                x: array [2,3] of boolean = {{true, false, true}, {false, true, false}};
arraylit: LPAREN (explist | arraylitlist) RPAREN;
//x: array [2,3] of integer = {},{};
//Identifier

//TYPE SYSTEM AND VALUES
//ATOMIC TYPE
//ARRAY TYPE
//VOID TYPE
//AUTO TYPE
//Special Function

//The fragment of Lexer
fragment DIGIT: [0-9];
fragment UNDERLETTER: [a-z];
fragment UPERLETTER: [A-Z];
fragment STRINGCHAR: ~[\b\t\f\r\n"\\] | ESCAPESEQUENCE;
fragment ESCAPESEQUENCE: '\\' [bfrnt"\\];
fragment ILLEGALSTRING: '\\' ~[bfrnt"\\] | '\\' ;
UNDERSCORE: '_';
DOUBLEQUOTE: '"';
SINGLEQUOTE: '\'';

//DECLARATIONS
//Variable declare
declare_var: IDENTIFIER COMMA declare_var COMMA expression
			| IDENTIFIER COMMA declare_var COMMA arraylit
			| IDENTIFIER COLON typ ASSIGN expression
			| IDENTIFIER COLON typ ASSIGN arraylit;
//arr: array[2,3,4] of integer = {123,1231,23};
declare_var_no_assign: identifier_list COLON typ ('[' intlitlist ']' OF typ)?;
identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;
//a : array[2,2] of integer;
arr_declare: '['intlitlist']' OF typ;

var_declare: (declare_var | declare_var_no_assign) SEMICOLON;
typ: INTEGER | FLOAT | STRING | BOOLEAN | AUTO | (ARRAY '[' intlitlist ']' OF typ);
intlitlist: INTLIT COMMA intlitlist | INTLIT;
floatlitlist: FLOATLIT COMMA floatlitlist | FLOATLIT;
boolitlist: BOOLIT COMMA boolitlist | BOOLIT;
stringlitlist: STRINGLIT COMMA stringlitlist | STRINGLIT;
arraylitlist: arraylit COMMA arraylitlist | arraylit;

//Parameter declare
para_declare: list_para_declare;
list_para_declare: list_para_declare_prime | ;
list_para_declare_prime: (one_para_declare COMMA) list_para_declare_prime | one_para_declare;
one_para_declare: INHERIT? OUT? IDENTIFIER COLON typ;

//Function declare
func_declare: IDENTIFIER COLON FUNCTION return_type LB para_declare RB (INHERIT IDENTIFIER)? block_statement;
return_type: INTEGER | BOOLEAN | STRING | FLOAT | VOID | AUTO | (ARRAY '[' intlitlist ']' OF typ);

//EXPRESSIONS
//Arithmetic operators
expression: exp1 CONCAT exp1 | exp1; 																	//String operator
exp1: exp2 (EQUAL | NOTEQUAL | GREATERTHAN | LESSTHAN | GTOE | LTOE) exp2 | exp2;						//Relational
exp2: exp2 (CONJUNCTION | DISJUNCTION) exp3 | exp3;														//Logical
exp3: exp3 (ADDOP | NEGOP) exp4 | exp4;																	//Adding
exp4: exp4 (MULOP | DIVOP | REMAINOP) exp5 | exp5;														//Multiplying
exp5: NEGATION exp5 | exp6;																				//Logical
exp6: NEGOP exp6 | exp7;																				//Sign
exp7: IDENTIFIER '[' explist ']' | exp8;																//Index operator
exp8: LB expression RB | IDENTIFIER | INTLIT | FLOATLIT | STRINGLIT | BOOLIT | function_call;			//value
explist: expressionprime | ;
expressionprime: expression COMMA expressionprime | expression;

//Function Call
function_call: IDENTIFIER LB (explist | arraylitlist) RB;
//Statement
assign_statement: (IDENTIFIER | IDENTIFIER '[' explist ']') ASSIGN (expression | arraylit) SEMICOLON;

if_statement: IF LB expression RB stmt (ELSE stmt)?;

for_statement: FOR LB assign_for COMMA expression COMMA expression RB stmt;
assign_for: expression ASSIGN expression;

while_statement: WHILE LB expression RB stmt;

dowhile_statement: DO block_statement WHILE LB expression RB SEMICOLON;

break_statement: BREAK SEMICOLON;

continue_statement: CONTINUE SEMICOLON;

return_statement: (RETURN | (RETURN (expression | arraylitlist))) SEMICOLON;

call_statement: IDENTIFIER LB (expressionlist | arraylitlist) RB SEMICOLON;

block_statement: LPAREN (stmt | var_declare)* RPAREN;

expressionlist: exprime | ;
exprime: expression COMMA exprime | expression;

stmt: assign_statement | 
		  if_statement | 
		 for_statement | 
	   while_statement | 
	  dowhile_statement|
	    break_statement|
	 continue_statement|
	   return_statement|
	     call_statement|
		block_statement|
		 var_declare;
//Comment
COMMENTINLINE: DIVOP DIVOP ~[\r\n]* -> skip;
COMMENTBLOCK: DIVOP MULOP .*? MULOP DIVOP -> skip;

WS : [ \b\f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines



UNCLOSE_STRING: DOUBLEQUOTE STRINGCHAR* ([\b\t\f\n\r"\\] | EOF){
	unclose_str = str(self.text);
	possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
	if unclose_str[-1] in possible:
		raise UncloseString(unclose_str[1:-1])
	else:
		raise UncloseString(unclose_str[1:])
};

ILLEGAL_ESCAPE: DOUBLEQUOTE STRINGCHAR* ILLEGALSTRING{
	illegal_str = str(self.text)
	raise IllegalEscape(illegal_str[1:])
};

ERROR_CHAR: .{raise ErrorToken(self.text)};