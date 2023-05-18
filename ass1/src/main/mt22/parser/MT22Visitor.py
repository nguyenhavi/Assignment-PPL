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


    # Visit a parse tree produced by MT22Parser#declare.
    def visitDeclare(self, ctx:MT22Parser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declare_var.
    def visitDeclare_var(self, ctx:MT22Parser.Declare_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declare_var_no_assign.
    def visitDeclare_var_no_assign(self, ctx:MT22Parser.Declare_var_no_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier_list.
    def visitIdentifier_list(self, ctx:MT22Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arr_declare.
    def visitArr_declare(self, ctx:MT22Parser.Arr_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_declare.
    def visitVar_declare(self, ctx:MT22Parser.Var_declareContext):
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


    # Visit a parse tree produced by MT22Parser#list_para_declare.
    def visitList_para_declare(self, ctx:MT22Parser.List_para_declareContext):
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


    # Visit a parse tree produced by MT22Parser#expressionprime.
    def visitExpressionprime(self, ctx:MT22Parser.ExpressionprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
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


    # Visit a parse tree produced by MT22Parser#assign_for.
    def visitAssign_for(self, ctx:MT22Parser.Assign_forContext):
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


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)



del MT22Parser