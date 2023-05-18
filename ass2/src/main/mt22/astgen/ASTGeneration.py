from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
#MSSV 2013907

class ASTGeneration(MT22Visitor):
    #program: notebnf EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.notebnf()))

    #notebnf: declare notebnf | declare;
    def visitNotebnf(self, ctx: MT22Parser.NotebnfContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.declare())
        return self.visit(ctx.declare()) + self.visit(ctx.notebnf())

    def visitDeclare(self, ctx: MT22Parser.DeclareContext):
        if ctx.var_declare():
            return self.visit(ctx.var_declare())
        return [self.visit(ctx.func_declare())]

    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        return self.visit(ctx.item())

    def visitItem(self, ctx: MT22Parser.ItemContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.itemprime())

    def visitItemprime(self, ctx: MT22Parser.ItemprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.variable())]
        return [self.visit(ctx.variable())] + self.visit(ctx.itemprime())

    def visitVariable(self, ctx: MT22Parser.VariableContext):
        if ctx.expression():
            return self.visit(ctx.expression())
        return self.visit(ctx.arraylit())

    #identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;
    def visitIdentifier_list(self, ctx: MT22Parser.Identifier_listContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        return [ctx.IDENTIFIER().getText()] + self.visit(ctx.identifier_list())


    def visitVar_declare(self, ctx: MT22Parser.Var_declareContext):
        #var_declare: identifier_list COLON variable_type SEMICOLON | first_decl SEMICOLON;
        if ctx.getChildCount() == 4:
            variable_type = self.visit(ctx.variable_type())
            identifier_list = self.visit(ctx.identifier_list())
            return list(map(lambda x: VarDecl(x, variable_type, None), identifier_list))
        return self.visit(ctx.first_decl())
    
    def visitVariable_type(self, ctx: MT22Parser.Variable_typeContext):
        if ctx.atomtype():
            return self.visit(ctx.atomtype())
        return self.visit(ctx.array_type())

    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.array_size()), self.visit(ctx.atomtype()))

    def visitArray_size(self, ctx: MT22Parser.Array_sizeContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.array_size())

    def visitParatype(self, ctx: MT22Parser.ParatypeContext):
        if ctx.AUTO():
            return AutoType()
        return self.visit(ctx.variable_type())

    def visitFirst_decl(self, ctx: MT22Parser.First_declContext):
        if ctx.paratype():
            return [VarDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.paratype()), self.visit(ctx.value()))]
        lhs = [ctx.IDENTIFIER().getText()] + self.takeID(ctx.first_decl())
        paramtype = self.takeType(ctx.first_decl())
        rhs = [self.visit(ctx.value())] + self.takeValue(ctx.first_decl())
        return list(map(lambda x,y: VarDecl(x, paramtype, y), lhs, rhs[::-1]))        

    def takeID(self, ctx: MT22Parser.First_declContext):
        if ctx.ASSIGN():
            return [ctx.IDENTIFIER().getText()]
        return [ctx.IDENTIFIER().getText()] + self.takeID(ctx.first_decl())
    
    def takeValue(self, ctx: MT22Parser.First_declContext):
        if ctx.ASSIGN():
            return [self.visit(ctx.value())]
        return [self.visit(ctx.value())] + self.takeValue(ctx.first_decl())

    def takeType(self, ctx: MT22Parser.First_declContext):
        if ctx.ASSIGN():
            return self.visit(ctx.paratype())
        return self.takeType(ctx.first_decl())

    def visitAtomtype(self, ctx : MT22Parser.AtomtypeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else: return AutoType()

    def visitIntlitlist(self, ctx: MT22Parser.IntlitlistContext):
        return None

    def visitFloatlitlist(self, ctx: MT22Parser.FloatlitlistContext):
        return None

    def visitBoolitlist(self, ctx: MT22Parser.BoolitlistContext):
        return None

    def visitStringlitlist(self, ctx: MT22Parser.StringlitlistContext):
        return None

    def visitArraylitlist(self, ctx: MT22Parser.ArraylitlistContext):
        return None

    def visitPara_declare(self, ctx: MT22Parser.Para_declareContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.list_para_declare_prime())

    def visitList_para_declare_prime(self, ctx: MT22Parser.List_para_declare_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.one_para_declare())]
        return [self.visit(ctx.one_para_declare())] + self.visit(ctx.list_para_declare_prime())

    def visitOne_para_declare(self, ctx: MT22Parser.One_para_declareContext):
        if ctx.getChildCount() == 3:
            return ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.paratype()), False, False)
        if ctx.getChildCount() == 4:
            if ctx.INHERIT():
                return ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.paratype()), False, True)
            if ctx.OUT():
                return ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.paratype()), True, False)
        return ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.paratype()), True, True)

    def visitFunc_declare(self, ctx: MT22Parser.Func_declareContext):
        if ctx.INHERIT():
            return FuncDecl(ctx.IDENTIFIER(0).getText(), self.visit(ctx.return_type()), self.visit(ctx.para_declare()), ctx.IDENTIFIER(1).getText(), self.visit(ctx.function()))
        return FuncDecl(ctx.IDENTIFIER(0).getText(), self.visit(ctx.return_type()), self.visit(ctx.para_declare()), False, self.visit(ctx.function()))

    def visitFunction(self, ctx: MT22Parser.FunctionContext):
        return self.visit(ctx.block_statement())

    def visitReturn_type(self, ctx: MT22Parser.Return_typeContext):
        if ctx.VOID():
            return VoidType()
        if ctx.AUTO():
            return AutoType()
        return self.visit(ctx.variable_type())

    def visitExpression(self, ctx: MT22Parser.ExpressionContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            op = ctx.CONCAT().getText()
            return BinExpr(op, left, right)
        if ctx.exp1():
            return self.visit(ctx.exp1(0))
        return self.visit(ctx.function_call())

    def visitExp1(self, ctx: MT22Parser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        if ctx.EQUAL():
            return BinExpr(ctx.EQUAL().getText(),self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        if ctx.NOTEQUAL():
            return BinExpr(ctx.NOTEQUAL().getText(),self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))            
        if ctx.GREATERTHAN():
            return BinExpr(ctx.GREATERTHAN().getText(),self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        if ctx.LESSTHAN():
            return BinExpr(ctx.LESSTHAN().getText(),self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        if ctx.GTOE():
            return BinExpr(ctx.GTOE().getText(),self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        if ctx.LTOE():
            return BinExpr(ctx.LTOE().getText(),self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))

    def visitExp2(self, ctx: MT22Parser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        if ctx.CONJUNCTION():
            return BinExpr(ctx.CONJUNCTION().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        if ctx.DISJUNCTION():
            return BinExpr(ctx.DISJUNCTION().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))

    def visitExp3(self, ctx: MT22Parser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        if ctx.ADDOP():
            return BinExpr(ctx.ADDOP().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        if ctx.NEGOP():
            return BinExpr(ctx.NEGOP().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))

    def visitExp4(self, ctx: MT22Parser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        if ctx.MULOP():
            return BinExpr(ctx.MULOP().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        if ctx.DIVOP():
            return BinExpr(ctx.DIVOP().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        if ctx.REMAINOP():
            return BinExpr(ctx.REMAINOP().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))

    def visitExp5(self, ctx: MT22Parser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        return UnExpr(ctx.NEGATION().getText(), self.visit(ctx.exp5()))

    def visitExp6(self, ctx: MT22Parser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        return UnExpr(ctx.NEGOP().getText(), self.visit(ctx.exp6()))

    def visitExp7(self, ctx: MT22Parser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp8())
        return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.explist())) 

    def visitExp8(self, ctx: MT22Parser.Exp8Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expression())
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.FLOATLIT():
            return FloatLit(float('0' + ctx.FLOATLIT().getText()))
        if ctx.STRINGLIT():
            return StringLit(str(ctx.STRINGLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLit(ctx.BOOLIT().getText() == "true")
        return self.visit(ctx.function_call())

    def visitExplist(self, ctx: MT22Parser.ExplistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.explist())

    def visitValue_list(self, ctx: MT22Parser.Value_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.valueprime())
    
    def visitValueprime(self, ctx: MT22Parser.ValueprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.value())]
        return [self.visit(ctx.value())] + self.visit(ctx.valueprime())

    def visitValue(self, ctx: MT22Parser.ValueContext):
        if ctx.expression():
            return self.visit(ctx.expression())
        return self.visit(ctx.arraylit())

    def visitFunction_call(self, ctx: MT22Parser.Function_callContext):
        return FuncCall(ctx.IDENTIFIER().getText(), self.visit(ctx.value_list()))

    def visitBlock_statement(self, ctx: MT22Parser.Block_statementContext):
        if ctx.getChildCount() == 2:
            return BlockStmt([])
        return BlockStmt(self.visit(ctx.stmt_prime()))

    def visitBefore_assign(self, ctx: MT22Parser.Before_assignContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.IDENTIFIER().getText())
        return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.explist()))

    def visitAssign_statement(self, ctx: MT22Parser.Assign_statementContext):
        if ctx.expression():
            return AssignStmt(self.visit(ctx.before_assign()), self.visit(ctx.expression()))
        return AssignStmt(self.visit(ctx.before_assign()), self.visit(ctx.arraylit()))

    def visitIf_statement(self, ctx: MT22Parser.If_statementContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expression()), self.visit(ctx.stmt_list(0)), self.visit(ctx.stmt_list(1)))
        return IfStmt(self.visit(ctx.expression()), self.visit(ctx.stmt_list(0)))

    def visitFor_statement(self, ctx: MT22Parser.For_statementContext):
        return ForStmt(AssignStmt(self.visit(ctx.before_assign()), self.visit(ctx.expression(0))), 
        self.visit(ctx.expression(1)), self.visit(ctx.expression(2)), self.visit(ctx.stmt_list()))

    def visitWhile_statement(self, ctx: MT22Parser.While_statementContext):
        return WhileStmt(self.visit(ctx.expression()), self.visit(ctx.stmt_list()))

    def visitDowhile_statement(self, ctx: MT22Parser.Dowhile_statementContext):
        return DoWhileStmt(self.visit(ctx.expression()), self.visit(ctx.block_statement()))

    def visitBreak_statement(self, ctx: MT22Parser.Break_statementContext):
        return BreakStmt()

    def visitContinue_statement(self, ctx: MT22Parser.Continue_statementContext):
        return ContinueStmt()

    def visitReturn_statement(self, ctx: MT22Parser.Return_statementContext):
        if ctx.getChildCount() == 2:
            return ReturnStmt(None)
        if ctx.expression():
            return ReturnStmt(self.visit(ctx.expression()))
        if ctx.arraylit():
            return ReturnStmt(self.visit(ctx.arraylit()))

    def visitCall_statement(self, ctx: MT22Parser.Call_statementContext):
        return CallStmt(ctx.IDENTIFIER().getText(), self.visit(ctx.value_list()))

    def visitExpressionlist(self, ctx: MT22Parser.ExpressionlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.exprime())

    def visitExprime(self, ctx: MT22Parser.ExprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression())
        return self.visit(ctx.expression()) + self.visit(ctx.exprime())

    def visitStmt_list(self, ctx: MT22Parser.Stmt_listContext):
        if ctx.stmt():
            return self.visit(ctx.stmt())[0]
        return self.visit(ctx.block_statement())

    def visitStmt_prime(self, ctx: MT22Parser.Stmt_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stmt())
        return self.visit(ctx.stmt()) + self.visit(ctx.stmt_prime())

    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assign_statement():
            return [self.visit(ctx.assign_statement())]
        if ctx.if_statement():
            return [self.visit(ctx.if_statement())]
        if ctx.for_statement():
            return [self.visit(ctx.for_statement())]
        if ctx.while_statement():
            return [self.visit(ctx.while_statement())]
        if ctx.dowhile_statement():
            return [self.visit(ctx.dowhile_statement())]
        if ctx.break_statement():
            return [self.visit(ctx.break_statement())]
        if ctx.continue_statement():
            return [self.visit(ctx.continue_statement())]
        if ctx.return_statement():
            return [self.visit(ctx.return_statement())]
        if ctx.call_statement():
            return [self.visit(ctx.call_statement())]                                                    
        return self.visit(ctx.var_declare())