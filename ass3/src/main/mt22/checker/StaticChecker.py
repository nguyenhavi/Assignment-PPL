from AST import *
from Visitor import Visitor
from StaticError import *
from abc import ABC
#MSSV 2013907

class Symbol:
    pass

class Var(Symbol):
    def __init__(self, name: str, typ: Type):
        self.name = name
        self.typ = typ

class Func(Symbol):
    def __init__(self, name: str, param: List[Symbol], returntype: Type, inherit: str or None, flag: bool = False, flag_returnstmt: bool = False, flag_havereturn: bool = False, flag_havesuper: int = 0):
        self.name = name
        self.param = param
        self.returntype = returntype
        self.inherit = inherit
        self.flag = flag
        self.flag_returnstmt = flag_returnstmt #current function
        self.flag_havereturn = flag_havereturn #true if this function have return
        self.flag_havesuper = flag_havesuper

class Arr(Symbol):
    def __init__(self, name: str, typ: Type, dimen: List[int]):
        self.name = name
        self.typ = typ
        self.dimen = dimen

class Param(Symbol):
    def __init__(self, name: str, typ: Type, out: bool = False, inherit: bool = False, passToSon: bool = False):
        self.name = name
        self.typ = typ
        self.out = out
        self.inherit = inherit
        self.passToSon = passToSon

def infer(name, typ, o):
    for x in o:
        for y in x:
            if y.name == name and type(y) is Func:
                y.returntype = typ
            elif y.name == name and type(y) is Var:
                y.typ = typ
            elif y.name == name and type(y) is Param:
                y.typ = typ
    return o

def infer_param(name_func, name_param, typ, o):
    for x in o[len(o)-1]:
        if x.name == name_func and type(x) is Func:
            for y in x.param:
                if y.name == name_param:
                    y.typ = typ
    return

def checkPr(list_param):
    meet = 0
    for i in range(len(list_param)):
        meet = 0
        for j in range(len(list_param)):
            if list_param[j].name == list_param[i].name and list_param[j].inherit is True:
                meet = meet + 1
            if meet == 2:
                return list_param[j].name
    return True

class Get_Env(Visitor):
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast, [])

    def visitProgram(self, ctx, o):
        o = [[]]
        for x in ctx.decls:
            o = self.visit(x, o)
        return o

    def visitFuncDecl(self, ctx, o):
        list_param = []
        for x in ctx.params:
            list_param = self.visit(x, list_param)
        if ctx.name not in ["readInteger","printInteger","readFloat", "writeFloat", "readBoolean", "printBoolean", "readString", "printString", "super"]:
            o[0] += [Func(ctx.name, list_param, ctx.return_type, ctx.inherit, False)]
        return o

    def visitParamDecl(self, ctx, o):
        o += [Param(ctx.name, ctx.typ, ctx.out, ctx.inherit)]
        return o
    
    def visitVarDecl(self, ctx, o):
        return o

class StaticChecker(Visitor):

    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visit(self.ast, None)

    def visitProgram(self, ctx, o):
        special_function = [
        Func("readInteger", [], IntegerType(), None, True),
        Func("printInteger", [Param("function", IntegerType())], VoidType(), None, True),
        Func("readFloat", [], FloatType(), None, True),
        Func("writeFloat", [Param("function", FloatType())], VoidType(), None, True),
        Func("readBoolean", [], BooleanType(), None, True),
        Func("printBoolean", [Param("function", BooleanType())], VoidType(), None, True),
        Func("readString", [], StringType(), None, True),
        Func("printString", [Param("function", StringType())], VoidType(), None, True),
        Func("preventDefault", [], VoidType(), None, True)
    ]        
        o = Get_Env(self.ast).visit(ctx, o)
        is_entry_point = False
        o[0] += special_function
        for x in ctx.decls:
            if type(x) is VarDecl:
                o = self.visit(x, o)
            if type(x) is FuncDecl:
                if x.name == "main" and type(x.return_type) is VoidType and len(x.params) == 0:
                    is_entry_point = True
                o = self.visit(x, o)
        
        if not is_entry_point:
            raise NoEntryPoint()

    def visitVarDecl(self, ctx, o):
        if ctx.name == "super":
            raise Redeclared(Variable(), ctx.name)
        for x in o[0]:
            if ctx.name == x.name:
                if type(x) is Func:
                    if x.flag is False:
                        continue
                    else:
                        raise Redeclared(Variable(), ctx.name)
                else:
                    raise Redeclared(Variable(), ctx.name)
        typ = ctx.typ
        if ctx.init is None and type(typ) is AutoType:
            raise Invalid(Variable(), ctx.name)
        
        if type(typ) is ArrayType:
            if ctx.init is not None:
                val = self.visit(ctx.init, o)
                if val is False:
                    raise IllegalArrayLiteral(ctx.init)
            if type(ctx.init) is ArrayLit:
                if len(typ.dimensions) == 1:
                    #array[3] of integer = {{1},{2},{3}}
                    if type(ctx.init.explist[0]) is ArrayLit:
                        raise TypeMismatchInVarDecl(ctx)
                    #array[3] of integer = {1,2,3,4}
                    if typ.dimensions[0] != len(ctx.init.explist):
                        raise TypeMismatchInVarDecl(ctx)
                if len(typ.dimensions) == 2:
                    if type(ctx.init.explist[0]) is not ArrayLit:
                        raise TypeMismatchInVarDecl(ctx)
                    if typ.dimensions[0] != len(ctx.init.explist):
                        raise TypeMismatchInVarDecl(ctx)
                    if typ.dimensions[1] != len(ctx.init.explist[0].explist):
                        raise TypeMismatchInVarDecl(ctx)
            ###################
            o[0] += [Arr(ctx.name, typ, ctx.typ.dimensions)]
            return o
        
        typemismtach = False
        if ctx.init is not None:
            val = self.visit(ctx.init, o)
            if type(typ) is AutoType:
                typ = val
            if type(val) is AutoType:
                val = typ
                infer(ctx.init.name, typ, o)
            if type(typ) is FloatType and type(val) is IntegerType:
                o[0] += [Var(ctx.name, typ)]
                return o
            if type(val) is not type(typ):
                    typemismtach = True
                
        if typemismtach:
            raise TypeMismatchInVarDecl(ctx)
                
        o[0] += [Var(ctx.name, typ)]
        return o

    def visitFuncDecl(self, ctx, o):
        func_cur = None
        father = 0
        for x in o[0]:
            if x.name == ctx.name:
                if type(x) is Func:
                    if x.flag is False:
                        x.flag = True
                        func_cur = x
                    else:
                        raise Redeclared(Function(), ctx.name)
                else:
                    raise Redeclared(Function(), ctx.name)
        env = [[]] + o
        if func_cur.inherit is not False:
            for x in o[0]:
                if x.name == func_cur.inherit:
                    if type(x) is Func:
                        father = x
        if father != 0:
            for x in father.param:
                if x.inherit is True:
                    x.passToSon = True
                    env[0] += [x]
        for x in ctx.params:
            env = self.visit(x, env)
        for i in range(len(env[0])):
            if type(env[0][i].typ) is AutoType:
                for x in func_cur.param:
                    if x.name == env[0][i].name:
                        env[0][i].typ = x.typ
        func_cur.flag_returnstmt = True
        env = self.visit(ctx.body, env)
        func_cur.flag_returnstmt = False
        return o

    def visitParamDecl(self, ctx, o):
        for i in o[0]:
            if ctx.name is i.name:
                if i.passToSon is True:
                    raise Invalid(Parameter(), ctx.name)
                raise Redeclared(Parameter(), ctx.name)
        typ = ctx.typ
        o[0] += [Param(ctx.name, typ, ctx.out, ctx.inherit)]
        return o 

    def visitUnExpr(self, ctx, o):
        e = self.visit(ctx.val, o)
        if ctx.op in ['!']:
            if type(e) is AutoType:
                infer(ctx.val.name, BooleanType(), o)
                return BooleanType()
            if type(e) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['-']:
            if type(e) is AutoType:
                infer(ctx.val.name, IntegerType(), o)
                return IntegerType()
            if type(e) is IntegerType or type(e) is FloatType:
                return e
            raise TypeMismatchInExpression(ctx)

    def visitBinExpr(self, ctx, o):
        e1t = self.visit(ctx.left, o)
        if type(ctx.left) not in [IntegerLit,StringLit,BooleanLit,FloatLit,ArrayLit, BinExpr, UnExpr]:
            e1_name = ctx.left.name
        e2t = self.visit(ctx.right, o)
        if type(ctx.right) not in [IntegerLit,StringLit,BooleanLit,FloatLit,ArrayLit, BinExpr,UnExpr]:
            e2_name = ctx.right.name
        if ctx.op in ['+', '-', '*', '/']:
            if type(e1t) is AutoType and type(e2t) is AutoType:
                infer(e1_name, IntegerType(), o)
                infer(e2_name, IntegerType(), o)
                return IntegerType()
            if type(e1t) is AutoType and (type(e2t) is IntegerType or type(e2t) is FloatType):
                infer(e1_name, e2t, o)
                return e2t
            elif (type(e1t) is IntegerType or type(e1t) is FloatType) and type(e2t) is AutoType:
                infer(e2_name, e1t, o)
                return e1t
            if (type(e1t) is type(e2t)) and ((type(e1t) is IntegerType) or (type(e1t) is FloatType)):
                return e1t
            elif type(e1t) is IntegerType and type(e2t) is FloatType:
                return FloatType()
            elif type(e1t) is FloatType and type(e2t) is IntegerType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['%']:
            if type(e1t) is AutoType:
                infer(e1_name, IntegerType(), o)
                return IntegerType()
            if type(e2t) is AutoType:
                infer(e2_name, IntegerType(), o)
                return IntegerType()
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return IntegerType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['&&', '||']:
            if type(e1t) is AutoType and type(e2t) is BooleanType:
                infer(e1_name, BooleanType(), o)
                return e2t
            if type(e2t) is AutoType and type(e1t) is BooleanType: 
                infer(e2_name, BooleanType(), o)
                return e1t
            if type(e1t) is AutoType and type(e2t) is AutoType:
                infer(e1_name, BooleanType(), o)
                infer(e2_name, BooleanType(), o)
                return BooleanType()            
            if type(e1t) is BooleanType and type(e2t) is BooleanType:
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['==', '!=']:
            if type(e1t) is AutoType and type(e2t) is AutoType:
                infer(e1_name, IntegerType(), o)
                infer(e2_name, IntegerType(), o)
                return BooleanType()
            if type(e1t) is AutoType and (type(e2t) is IntegerType or type(e2t) is BooleanType):
                infer(e1_name, e2t, o)
                return BooleanType()
            if type(e2t) is AutoType and (type(e1t) is IntegerType or type(e1t) is BooleanType):
                infer(e2_name, e1t, o)                
                return BooleanType()
            if (type(e1t) is IntegerType or type(e1t) is BooleanType) and (type(e2t) is IntegerType or type(e2t) is BooleanType):
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['>', '<', '<=', '>=']:
            if type(e1t) is AutoType and type(e2t) is AutoType:
                infer(e1_name, IntegerType(), o)
                infer(e2_name, IntegerType(), o)
                return BooleanType()
            if type(e1t) is AutoType and (type(e2t) is IntegerType or type(e2t) is FloatType):
                infer(e1_name, e2t, o)
                return BooleanType()
            if type(e2t) is AutoType and (type(e1t) is IntegerType or type(e1t) is FloatType):
                infer(e2_name, e1t, o)                
                return BooleanType()
            if (type(e1t) is not IntegerType and type(e1t) is not FloatType) and (type(e2t) is not IntegerType and type(e2t) is not FloatType):
                raise TypeMismatchInExpression(ctx)
            return BooleanType()
        elif ctx.op in ['::']:
            if type(e1t) is AutoType and type(e2t) is AutoType:
                infer(e1_name, StringType(), o)
                infer(e2_name, StringType(), o)
                return StringType() 
            if type(e2t) is AutoType:
                infer(e2_name, StringType(), o)
                return StringType()
            if type(e1t) is AutoType:
                infer(e1_name, StringType(), o)
                return StringType()
            if type(e1t) is not StringType or type(e2t) is not StringType:
                raise TypeMismatchInExpression(ctx)
            return StringType()


    def visitId(self, ctx, o):
        for x in o:
            for y in x:
                if y.name == ctx.name:
                    if type(y) is Func:
                        return y.returntype
                    elif type(y) is Var or type(y) is Arr or type(y) is Param:
                        return y.typ
        raise Undeclared(Identifier(), ctx.name)

    def visitArrayCell(self, ctx, o):
        ans = None
        for x in o:
            for y in x:
                if y.name == ctx.name:
                    if type(y) is Arr:
                        ans = y.typ
                        break
                    else:
                        raise TypeMismatchInExpression(ctx)
        for i in ctx.cell:
            rt = self.visit(i, o)
            if type(rt) is not IntegerType:
                raise TypeMismatchInExpression(ctx)
        if ans is not None:
            return ans
        raise Undeclared(Identifier(), ctx.name)

    def visitAssignStmt(self, ctx, o):
        right = self.visit(ctx.rhs, o)
        if right is False:
            raise IllegalArrayLiteral(ctx.rhs)
        left = self.visit(ctx.lhs, o)
        if type(left) is FloatType and type(right) is IntegerType:
            return FloatType()
        if type(left) is VoidType:
            raise TypeMismatchInStatement(ctx)
        if type(left) is ArrayType:
            if type(left.typ) is type(right):
                return right
            raise TypeMismatchInStatement(ctx)
        if type(left) is IntegerType and type(right) is FloatType:
            raise TypeMismatchInStatement(ctx)
        if type(left) is AutoType or type(right) is AutoType:
            if type(left) is AutoType and type(right) is AutoType:
                return AutoType()
            if type(left) is AutoType and type(right) is not AutoType: 
                infer(ctx.lhs.name, right, o)
                return right
            if type(left) is not AutoType and type(right) is AutoType:
                infer(ctx.rhs.name, left, o)
                return left
        if type(left) is not type(right):
            raise TypeMismatchInStatement(ctx)
        return left
    def visitBlockStmt(self, ctx, o):
        #check super and preventdefault
        checkFirstStmt = False
        func_cur = None
        found = False
        for i in o[len(o)-1]:
            if type(i) is Func and i.flag_returnstmt:
                if i.inherit is False:
                    break
                else:
                    checkFirstStmt = True
                    func_cur = i
                    for i in o[len(o) - 1]:
                        if type(i) is Func and i.name == func_cur.inherit:
                            found = True
                            func_inherit = i
                            break
                    if not found:
                        raise Undeclared(Function(), func_cur.inherit)                    
                    if func_cur.flag_havesuper == 0:
                        if len(func_inherit.param) == 0 and len(o) == 2:
                            found = False
                        elif len(o) == 2 and len(ctx.body) == 0:
                            raise InvalidStatementInFunction(func_cur.name)
                    break
        if checkFirstStmt and func_cur.flag_havesuper == 0:
            for i in o[len(o) - 1]:
                if type(i) is Func and i.name == func_cur.inherit:
                    found = True
                    func_inherit = i
                    break
            if not found:
                raise Undeclared(Function(), func_cur.inherit)
            if len(func_inherit.param) != 0:
                if len(ctx.body) != 0:
                    if type(ctx.body[0]) is VarDecl:
                        raise InvalidStatementInFunction(func_cur.name)

                    elif type(ctx.body[0]) is CallStmt:
                        if ctx.body[0].name != "super" and ctx.body[0].name != "preventDefault":
                            raise InvalidStatementInFunction(func_cur.name)
                    else:
                        raise InvalidStatementInFunction(func_cur.name)
                    if ctx.body[0].name == "preventDefault" and len(ctx.body[0].args) != 0:
                        raise TypeMismatchInExpression(ctx.body[0].args[0])
                    if ctx.body[0].name == "super":
                        if checkPr(func_inherit.param) is not True:
                            raise Redeclared(Parameter(), checkPr(func_inherit.param))
                        if len(ctx.body[0].args) > len(func_inherit.param):
                            idx = len(func_inherit.param)
                            raise TypeMismatchInExpression(ctx.body[0].args[idx])
                        elif len(ctx.body[0].args) < len(func_inherit.param):
                            raise TypeMismatchInExpression(None)
                        elif len(ctx.body[0].args) == len (func_inherit.param):
                            list_arg = []
                            list_para = []
                            for x in func_inherit.param:
                                list_para += [x.typ]
                            for x in ctx.body[0].args:
                                list_arg += [self.visit(x,o)]
                            for i in range(len(list_arg)):
                                if type(list_arg[i]) is not type(list_para[i]):
                                    if type(list_arg[i]) is AutoType and type(list_para[i]) is not AutoType:
                                        infer(ctx.body[0].args[i].name, list_para[i], o)
                                        continue
                                    elif type(list_arg[i]) is not AutoType and type(list_para[i]) is AutoType:
                                        infer_param(func_inherit.name, func_inherit.param[i].name, list_arg[i], o)
                                        continue
                                    if type(list_arg[i]) is IntegerType and type(list_para[i]) is FloatType:
                                        continue
                                    raise TypeMismatchInExpression(ctx.body[0].args[i])
            else:
                if len(ctx.body) != 0:
                    if type(ctx.body[0]) is CallStmt:
                        if ctx.body[0].name == "super":
                            if len(ctx.body[0].args) != 0:
                                raise TypeMismatchInExpression(ctx.body[0].args[0])
                        if ctx.body[0].name == "preventDefault" and len(ctx.body[0].args) != 0:
                            raise TypeMismatchInExpression(ctx.body[0].args[0])
        for i in ctx.body:
            if type(i) is VarDecl:
                self.visit(i, o)
            elif type(i) is BlockStmt:
                env = [[]] + o
                self.visit(i, env)
            elif type(i) is ReturnStmt:
                self.visit(i, o)
            else:
                self.visit(i, o)

    def visitIfStmt(self, ctx, o):
        cond = self.visit(ctx.cond, o)
        if type(cond) is AutoType:
            if type(ctx.cond) is Id:
                infer(ctx.cond.name, BooleanType(), o)
                cond = BooleanType()
            if type(ctx.cond) is FuncCall:
                infer(ctx.cond.name, BooleanType(), o)
                cond = BooleanType()
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        for i in o[len(o) - 1]:
            if type(i) is Func:
                if i.flag_returnstmt is True:
                    func_cur = i
        if type(ctx.tstmt) is BlockStmt:
            env = [[]] + o
            self.visit(ctx.tstmt, env)
        else:
            self.visit(ctx.tstmt, o)
        if func_cur.flag_havereturn is True and ctx.fstmt is not None:
            func_cur.flag_havereturn = False
        if ctx.fstmt is not None:            
            if type(ctx.fstmt) is BlockStmt:
                env = [[]] + o
                self.visit(ctx.fstmt, env)
            else:
                self.visit(ctx.fstmt, o)
        

    def visitForStmt(self, ctx, o):
        init = self.visit(ctx.init, o)
        if type(init) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        cond = self.visit(ctx.cond, o)
        if type(cond) is AutoType:
            if type(ctx.cond) is Id:
                infer(ctx.cond.name, BooleanType(), o)
                cond = BooleanType()
            if type(ctx.cond) is FuncCall:
                infer(ctx.cond.name, BooleanType(), o)
                cond = BooleanType()
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        upd = self.visit(ctx.upd, o)
        if type(cond) is AutoType:
            if type(ctx.cond) is Id:
                infer(ctx.cond.name, IntegerType(), o)
                cond = IntegerType()
            if type(ctx.cond) is FuncCall:
                infer(ctx.cond.name, IntegerType(), o)
                cond = IntegerType() 
        if type(upd) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        env = [[Var("for", VoidType())]] + o
        self.visit(ctx.stmt, env)

    def visitWhileStmt(self, ctx, o):
        cond = self.visit(ctx.cond, o)
        if type(cond) is AutoType:
            if type(ctx.cond) is Id:
                infer(ctx.cond.name, BooleanType(), o)
                cond = BooleanType()
            if type(ctx.cond) is FuncCall:
                infer(ctx.cond.name, BooleanType(), o)
                cond = BooleanType()        
        if type(cond) is not BooleanType:
                raise TypeMismatchInStatement(ctx)

        env = [[Var("for", VoidType())]] + o
        self.visit(ctx.stmt, env)

    def visitDoWhileStmt(self, ctx, o):
        cond = self.visit(ctx.cond, o)
        if type(cond) is AutoType:
            if type(ctx.cond) is Id:
                infer(ctx.cond.name, BooleanType(), o)
                cond = BooleanType()
            if type(ctx.cond) is FuncCall:
                infer(ctx.cond.name, BooleanType(), o)
                cond = BooleanType()        
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        env = [[Var("for", VoidType())]] + o
        self.visit(ctx.stmt, env)

    def visitBreakStmt(self, ctx, o):
        for i in o[0]:
            if i.name == "for":
                return None
        raise MustInLoop(ctx)

    def visitContinueStmt(self, ctx, o):
        for x in range(len(o) - 2):
            for y in o[x]:
                if y.name == "for":
                    return None
        raise MustInLoop(ctx)

    def visitReturnStmt(self, ctx, o):
        for i in o[len(o) - 1]:
            if i.flag_returnstmt is True:
                x = i
                break
        if x.flag_havereturn is True:
            return None        
        if ctx.expr is None:
            if type(x.returntype) is VoidType:
                x.flag_havereturn = True
                return None
            else:
                raise TypeMismatchInStatement(ctx)
        else:
            rt_type = self.visit(ctx.expr, o)
            if type(x.returntype) is AutoType:
                x.returntype = rt_type
                infer(x.name, rt_type, o)
            elif type(x.returntype) is VoidType:
                raise TypeMismatchInStatement(ctx)
            elif type(x.returntype) is not type(rt_type):
                raise TypeMismatchInStatement(ctx)
            x.flag_havereturn = True
        return None

    def visitCallStmt(self, ctx, o):
        for i in o[len(o) - 1]:
            if type(i) is Func and i.flag_returnstmt:
                func_cur = i
                break
        if ctx.name == "super" or ctx.name == "preventDefault":
            if len(o) > 2:
                raise InvalidStatementInFunction(func_cur.name)
            func_cur.flag_havesuper += 1
            if func_cur.inherit is False:
                raise InvalidStatementInFunction(func_cur.name)
            if func_cur.flag_havesuper > 1:
                raise InvalidStatementInFunction(func_cur.name)
            else:
                return None
        found = False
        for i in o[len(o) - 1]:

            if ctx.name == i.name and type(i) is Func:
                found = True
                func = i
                break
        if not found:
            raise Undeclared(Function(), ctx.name)
        if len(func.param) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)
        para_type = []
        for i in func.param:
            para_type += [i.typ]
        for i in range(len(para_type)):
            if type(para_type[i]) is ArrayType:
                para_type[i] = para_type[i].typ
        arg_type = []
        for i in ctx.args:
            arg_type += [self.visit(i, o)]
        
        if len(para_type) != len(arg_type):
            raise TypeMismatchInStatement(ctx)
        else:
            for i in range(len(para_type)):
                if type(para_type[i]) is AutoType or type(arg_type[i]) is AutoType:
                    continue
                elif type(para_type[i]) is not type(arg_type[i]):
                    if type(para_type[i]) is FloatType and type(arg_type[i]) is IntegerType:
                        continue
                    raise TypeMismatchInStatement(ctx)
                
        #if everything is done, let's start infer
        for i in range(len(arg_type)):
            if type(self.visit(ctx.args[i],o)) is AutoType and type(func.param[i].typ) is not AutoType:
                infer(ctx.args[i].name, func.param[i].typ, o)
            elif type(self.visit(ctx.args[i],o)) is not AutoType and type(func.param[i].typ) is AutoType:
                func.param[i].typ = self.visit(ctx.args[i],o)
            else:
                continue
        return None

    def visitFuncCall(self, ctx, o):
        if ctx.name == "preventDefault" or ctx.name == "super":
            raise TypeMismatchInExpression(ctx)
        found = False
        for i in o[len(o)-1]:
            if ctx.name == i.name and type(i) is Func:
                found = True
                func = i
                break
        if not found:
            raise Undeclared(Function(), ctx.name)

        if len(func.param) != len(ctx.args):
            raise TypeMismatchInExpression(ctx)
        para_type = []
        #para_type = [arrtype, inttype, floatype]
        #foo(1,a,)
        for i in func.param:
            para_type += [i.typ]
        arg_type = []
        for i in ctx.args:
            arg_type += [self.visit(i, o)]
        
        if len(para_type) != len(arg_type):
            raise TypeMismatchInExpression(ctx)
        else:
            for i in range(len(para_type)):
                if type(para_type[i]) is AutoType or type(arg_type[i]) is AutoType:
                    continue                
                if type(para_type[i]) is not type(arg_type[i]):
                    if type(para_type[i]) is FloatType and type(arg_type[i]) is IntegerType:
                        continue                    
                    raise TypeMismatchInExpression(ctx)
        for i in range(len(arg_type)):
            if type(self.visit(ctx.args[i],o)) is AutoType and type(func.param[i].typ) is not AutoType:
                infer(ctx.args[i].name, func.param[i].typ, o)
            elif type(self.visit(ctx.args[i],o)) is not AutoType and type(func.param[i].typ) is AutoType:
                func.param[i].typ = self.visit(ctx.args[i],o)
            else:
                continue

        if type(func.returntype) is VoidType:
            raise TypeMismatchInExpression(ctx)
        return func.returntype

    def visitIntegerLit(self, ctx, o):
        return IntegerType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitStringLit(self, ctx, o):
        return StringType()

    def visitBooleanLit(self, ctx, o):
        return BooleanType()

    def visitArrayType(self, ctx, o):
        return ctx.typ

    #{1,2,3,4}
    def visitArrayLit(self, ctx, o):
        if len(ctx.explist) == 0:
            return False
        typ = self.visit(ctx.explist[0], o)
        for x in ctx.explist:
            if type(typ) is not type(self.visit(x, o)):
                return False
        return typ