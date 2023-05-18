grammar MT22;
//MSSV 2013907
@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
program: notebnf EOF;

notebnf: declare notebnf | declare;

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
arraylit: LPAREN item RPAREN;
item: itemprime | ;
itemprime: variable COMMA itemprime | variable;
variable: expression | arraylit;
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
//arr: array[2,3,4] of integer = {123,1231,23};
identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;
//a : array[2,2] of integer;

//var_declare: (declare_var | declare_var_no_assign) SEMICOLON;
var_declare: identifier_list COLON variable_type SEMICOLON | first_decl SEMICOLON;
variable_type: atomtype | array_type;
atomtype: BOOLEAN | INTEGER | FLOAT | STRING | AUTO;
array_type: ARRAY '[' array_size ']' OF atomtype;
array_size: INTLIT COMMA array_size | INTLIT;
first_decl: IDENTIFIER COMMA first_decl COMMA value | IDENTIFIER COLON paratype ASSIGN value;
paratype: variable_type | AUTO;


typ: INTEGER | FLOAT | STRING | BOOLEAN | AUTO | (ARRAY '[' intlitlist ']' OF typ);
intlitlist: INTLIT COMMA intlitlist | INTLIT;
floatlitlist: FLOATLIT COMMA floatlitlist | FLOATLIT;
boolitlist: BOOLIT COMMA boolitlist | BOOLIT;
stringlitlist: STRINGLIT COMMA stringlitlist | STRINGLIT;
arraylitlist: arraylit COMMA arraylitlist | arraylit;

//Parameter declare
para_declare: list_para_declare_prime | ;
list_para_declare_prime: (one_para_declare COMMA) list_para_declare_prime | one_para_declare;
one_para_declare: IDENTIFIER COLON paratype | INHERIT IDENTIFIER COLON paratype | OUT IDENTIFIER COLON paratype | INHERIT OUT IDENTIFIER COLON paratype;

//Function declare
func_declare: IDENTIFIER COLON FUNCTION return_type LB para_declare RB function | IDENTIFIER COLON FUNCTION return_type LB para_declare RB INHERIT IDENTIFIER function;
function: block_statement;
return_type: variable_type | VOID | AUTO;

//EXPRESSIONS
//Arithmetic operators
expression: exp1 CONCAT exp1 | exp1 | function_call; 																	//String operator
exp1: exp2 (EQUAL | NOTEQUAL | GREATERTHAN | LESSTHAN | GTOE | LTOE) exp2 | exp2;						//Relational
exp2: exp2 (CONJUNCTION | DISJUNCTION) exp3 | exp3;														//Logical
exp3: exp3 (ADDOP | NEGOP) exp4 | exp4;																	//Adding
exp4: exp4 (MULOP | DIVOP | REMAINOP) exp5 | exp5;														//Multiplying
exp5: NEGATION exp5 | exp6;																				//Logical
exp6: NEGOP exp6 | exp7;																				//Sign
exp7: IDENTIFIER '[' explist ']' | exp8;																//Index operator
exp8: LB expression RB | IDENTIFIER | INTLIT | FLOATLIT | STRINGLIT | BOOLIT | function_call;			//value
explist: expression COMMA explist | expression;

//Function Call
function_call: IDENTIFIER LB value_list RB;
value_list: valueprime | ;
valueprime: value COMMA valueprime | value;
value: expression | arraylit;
//Statement
assign_statement: before_assign ASSIGN expression SEMICOLON | before_assign ASSIGN arraylit SEMICOLON;

if_statement: IF LB expression RB stmt_list | 
IF LB expression RB stmt_list ELSE stmt_list;

for_statement: FOR LB before_assign ASSIGN expression COMMA expression COMMA expression RB stmt_list;
before_assign: IDENTIFIER | IDENTIFIER '[' explist ']';

while_statement: WHILE LB expression RB stmt_list;

dowhile_statement: DO block_statement WHILE LB expression RB SEMICOLON;

break_statement: BREAK SEMICOLON;

continue_statement: CONTINUE SEMICOLON;

return_statement: RETURN expression SEMICOLON | RETURN SEMICOLON | RETURN arraylit SEMICOLON;

call_statement: IDENTIFIER LB value_list RB SEMICOLON;

block_statement: LPAREN stmt_prime RPAREN | LPAREN RPAREN;

expressionlist: exprime | ;
exprime: expression COMMA exprime | expression;
stmt_prime: stmt stmt_prime | stmt;
stmt_list: stmt | block_statement;
stmt: assign_statement | 
		  if_statement | 
		 for_statement | 
	   while_statement | 
	  dowhile_statement|
	    break_statement|
	 continue_statement|
	   return_statement|
	     call_statement|
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