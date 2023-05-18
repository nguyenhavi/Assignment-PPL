# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#notebnf.
    def visitNotebnf(self, ctx:MT22Parser.NotebnfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declare.
    def visitDeclare(self, ctx:MT22Parser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#item.
    def visitItem(self, ctx:MT22Parser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#itemprime.
    def visitItemprime(self, ctx:MT22Parser.ItemprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable.
    def visitVariable(self, ctx:MT22Parser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier_list.
    def visitIdentifier_list(self, ctx:MT22Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_declare.
    def visitVar_declare(self, ctx:MT22Parser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable_type.
    def visitVariable_type(self, ctx:MT22Parser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomtype.
    def visitAtomtype(self, ctx:MT22Parser.AtomtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_size.
    def visitArray_size(self, ctx:MT22Parser.Array_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#first_decl.
    def visitFirst_decl(self, ctx:MT22Parser.First_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paratype.
    def visitParatype(self, ctx:MT22Parser.ParatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intlitlist.
    def visitIntlitlist(self, ctx:MT22Parser.IntlitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatlitlist.
    def visitFloatlitlist(self, ctx:MT22Parser.FloatlitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolitlist.
    def visitBoolitlist(self, ctx:MT22Parser.BoolitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringlitlist.
    def visitStringlitlist(self, ctx:MT22Parser.StringlitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylitlist.
    def visitArraylitlist(self, ctx:MT22Parser.ArraylitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_declare.
    def visitPara_declare(self, ctx:MT22Parser.Para_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_para_declare_prime.
    def visitList_para_declare_prime(self, ctx:MT22Parser.List_para_declare_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#one_para_declare.
    def visitOne_para_declare(self, ctx:MT22Parser.One_para_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_declare.
    def visitFunc_declare(self, ctx:MT22Parser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function.
    def visitFunction(self, ctx:MT22Parser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp8.
    def visitExp8(self, ctx:MT22Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#explist.
    def visitExplist(self, ctx:MT22Parser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#value_list.
    def visitValue_list(self, ctx:MT22Parser.Value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#valueprime.
    def visitValueprime(self, ctx:MT22Parser.ValueprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#value.
    def visitValue(self, ctx:MT22Parser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_statement.
    def visitAssign_statement(self, ctx:MT22Parser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_statement.
    def visitIf_statement(self, ctx:MT22Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_statement.
    def visitFor_statement(self, ctx:MT22Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#before_assign.
    def visitBefore_assign(self, ctx:MT22Parser.Before_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_statement.
    def visitWhile_statement(self, ctx:MT22Parser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhile_statement.
    def visitDowhile_statement(self, ctx:MT22Parser.Dowhile_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_statement.
    def visitBreak_statement(self, ctx:MT22Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_statement.
    def visitContinue_statement(self, ctx:MT22Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_statement.
    def visitReturn_statement(self, ctx:MT22Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_statement.
    def visitCall_statement(self, ctx:MT22Parser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_statement.
    def visitBlock_statement(self, ctx:MT22Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressionlist.
    def visitExpressionlist(self, ctx:MT22Parser.ExpressionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprime.
    def visitExprime(self, ctx:MT22Parser.ExprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt_prime.
    def visitStmt_prime(self, ctx:MT22Parser.Stmt_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt_list.
    def visitStmt_list(self, ctx:MT22Parser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)



del MT22Parser