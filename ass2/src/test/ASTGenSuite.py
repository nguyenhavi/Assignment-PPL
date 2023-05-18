import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def testAST1(self):
        input = """ x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printFloat(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printFloat, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def testAST2(self):
        input = '''
             main: function void () {
                nope: string = "AVENGER";
                printString(nope);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nope, StringType, StringLit(AVENGER)), CallStmt(printString, Id(nope))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def testAST3(self):
        input = '''
            main: function void () {
                i: integer = 0;
                while (i<8){
                    i=i+1;
                }
                return i;
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), IntegerLit(8)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def testAST4(self):
        input = '''
            func1: function integer(n: integer){
                return n+1;
            }
            main: function void () {
                abc: integer = 3;
                func1(abc);
                return abc;
            }
        '''
        expect = """Program([
	FuncDecl(func1, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(n), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(abc, IntegerType, IntegerLit(3)), CallStmt(func1, Id(abc)), ReturnStmt(Id(abc))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def testAST5(self):
        input = '''
            main: function void () {
                n: float = 123.4e5;
                printFloat(n);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, FloatType, FloatLit(12340000.0)), CallStmt(printFloat, Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def testAST6(self):
        input = '''
            main: function void () {
                n: integer = 1+3*4-2*3;
                printInteger(n);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(3), IntegerLit(4))), BinExpr(*, IntegerLit(2), IntegerLit(3)))), CallStmt(printInteger, Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def testAST7(self):
        input = '''
            funcA: function integer(n: integer){
                for (i = 1, i < 5, i + 1) {
                    if (3 > i){
                        writeInt(i);
                        break;
                    }
                }
            }
            main: function void () {
                funcA(10);
            }
        '''
        expect = """Program([
	FuncDecl(funcA, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, IntegerLit(3), Id(i)), BlockStmt([CallStmt(writeInt, Id(i)), BreakStmt()]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(funcA, IntegerLit(10))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def testAST8(self):
        input = '''
             main: function void () {
                s: string = "123";
                printString(s + "45");
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, StringType, StringLit(123)), CallStmt(printString, BinExpr(+, Id(s), StringLit(45)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def testAST9(self):
        input = '''
            main: function void () {
                n: integer = 369;
                return (n);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, IntegerLit(369)), ReturnStmt(Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def testAST10(self):
        input = '''
            main: function void () {
                b: array [5,4] of integer;
                b[1,2] = 5;
                printInt(b[1,2]);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(b, ArrayType([5, 4], IntegerType)), AssignStmt(ArrayCell(b, [IntegerLit(1), IntegerLit(2)]), IntegerLit(5)), CallStmt(printInt, ArrayCell(b, [IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def testAST11(self):
        input = """main: function void(){
        if (me == 5){
            print("a > 2");
        }
        else{
            print("a <= 2");
        }}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(me), IntegerLit(5)), BlockStmt([CallStmt(print, StringLit(a > 2))]), BlockStmt([CallStmt(print, StringLit(a <= 2))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def testAST12(self):
        input = '''
            main: function void () {
                delta: float = 3.45;
                printFloat(delta);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, FloatType, FloatLit(3.45)), CallStmt(printFloat, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def testAST13(self):
        input = '''
            main : function void() {
                x : boolean = false;
                while (x == true) {
                }
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, BooleanType, BooleanLit(False)), WhileStmt(BinExpr(==, Id(x), BooleanLit(True)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def testAST14(self):
        input = """main: function void(){
            name: string;
            printString("What is your name?");
            readString(name);
            printStringn("My name is "::name);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(name, StringType), CallStmt(printString, StringLit(What is your name?)), CallStmt(readString, Id(name)), CallStmt(printStringn, BinExpr(::, StringLit(My name is ), Id(name)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def testAST15(self):
        input = """main: function void(){
            a,b,c: integer;
            a = 4;
            b = 6;
            c=  7;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType), AssignStmt(Id(a), IntegerLit(4)), AssignStmt(Id(b), IntegerLit(6)), AssignStmt(Id(c), IntegerLit(7))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def testAST16(self):
        input = """main: function void() {            
            r, s: integer;
            r = 2.0;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def testAST17(self):
        input = """main: function void() {
            max: integer;
            for (i=0, i<10, i + 1) {
                max = max + i;
            }
            printInteger(max);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(max, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(max), BinExpr(+, Id(max), Id(i)))])), CallStmt(printInteger, Id(max))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def testAST18(self):
        input = """x: function auto(){while(false) return _1 + x();}"""
        expect = """Program([
	FuncDecl(x, AutoType, [], None, BlockStmt([WhileStmt(BooleanLit(False), ReturnStmt(BinExpr(+, Id(_1), FuncCall(x, []))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def testAST19(self):
        input = """main: function void(){for(a[1]=1,a[1]<4,a[1]&&a){}}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)), BinExpr(<, ArrayCell(a, [IntegerLit(1)]), IntegerLit(4)), BinExpr(&&, ArrayCell(a, [IntegerLit(1)]), Id(a)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def testAST20(self):
        input = """x: array[1,2_9] of string;"""
        expect = """Program([
	VarDecl(x, ArrayType([1, 29], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def testAST21(self):
        input = """main: function void(){
            do {
                abc =  ! 12344 * 2345 / 2345 % 4567 - abc;
                for (abc = 0, abc < 100000, abc*12){
                    do {
                        abc = abc1234;
                    } while(abc < 100000);
                }
            } while(1);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(IntegerLit(1), BlockStmt([AssignStmt(Id(abc), BinExpr(-, BinExpr(%, BinExpr(/, BinExpr(*, UnExpr(!, IntegerLit(12344)), IntegerLit(2345)), IntegerLit(2345)), IntegerLit(4567)), Id(abc))), ForStmt(AssignStmt(Id(abc), IntegerLit(0)), BinExpr(<, Id(abc), IntegerLit(100000)), BinExpr(*, Id(abc), IntegerLit(12)), BlockStmt([DoWhileStmt(BinExpr(<, Id(abc), IntegerLit(100000)), BlockStmt([AssignStmt(Id(abc), Id(abc1234))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def testAST22(self):
        input = """main:function void() {for(a=5,a<10,a+1) {a:integer = 5;}}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(5)), BinExpr(<, Id(a), IntegerLit(10)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([VarDecl(a, IntegerType, IntegerLit(5))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def testAST23(self):
        input = """recPlus : function void (n : integer, a: float ) {
            if ((n == 1) || (a == 5.0)) return;
            else return recurPlus(n + 1, a + 2);
        }
        main: function void(){
            recPlus(2,4.2);
        }
        """
        expect = """Program([
	FuncDecl(recPlus, VoidType, [Param(n, IntegerType), Param(a, FloatType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(1)), BinExpr(==, Id(a), FloatLit(5.0))), ReturnStmt(), ReturnStmt(FuncCall(recurPlus, [BinExpr(+, Id(n), IntegerLit(1)), BinExpr(+, Id(a), IntegerLit(2))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(recPlus, IntegerLit(2), FloatLit(4.2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def testAST24(self):
        input = '''
            main : function void() {
                x : auto = 8;
                printInt(x);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, AutoType, IntegerLit(8)), CallStmt(printInt, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def testAST25(self):
        input = '''
          test: function integer (out x:integer, data:string){
            c : integer;
        }
        '''
        expect = """Program([
	FuncDecl(test, IntegerType, [OutParam(x, IntegerType), Param(data, StringType)], None, BlockStmt([VarDecl(c, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def testAST26(self):
        input = '''
            main: function void () {
                delta: float = 123.45e6;
                printFloat(delta);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, FloatType, FloatLit(123450000.0)), CallStmt(printFloat, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def testAST27(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==96) {y :integer= 69;}
            }
        '''
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(96)), BlockStmt([VarDecl(y, IntegerType, IntegerLit(69))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def testAST28(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==69) {y :integer = 96;}
                else {y : integer = 35;}
            }
        '''
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(69)), BlockStmt([VarDecl(y, IntegerType, IntegerLit(96))]), BlockStmt([VarDecl(y, IntegerType, IntegerLit(35))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def testAST29(self):
        input = '''
            main : function void() {
                x : integer ;
                if(x==69){}
            }  
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(69)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def testAST30(self):
        input = '''
            main : function void() {
                x : integer ;
                if(x==69){} else {y : integer = 96;}
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(69)), BlockStmt([]), BlockStmt([VarDecl(y, IntegerType, IntegerLit(96))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def testAST31(self):
        input = '''
            main : function void() {
                for (i = 1, i < 10, i + 1) {
                    printInteger(i);
                }
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def testAST32(self):
        input = """main: function void() {
            delta: integer = fact(3);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def testAST33(self):
        input = """str: string = "helloworld";"""
        expect = """Program([
	VarDecl(str, StringType, StringLit(helloworld))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def testAST34(self):
        input = """main: function void() { for(i = 1, i <10, i+1){if (i>5) break;}}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(5)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def testAST35(self):
        input = """int: integer = 100;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            return 5;
            inc(x);
        }"""
        expect = """Program([
	VarDecl(int, IntegerType, IntegerLit(100))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(IntegerLit(5)), CallStmt(inc, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def testAST36(self):
        input = """x: integer = 65;
        y: float = 1e10;
        fact: function integer (n: integer) {
            if (n == 0) return 1; 
            else return n * fact(n - 1);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	VarDecl(y, FloatType, FloatLit(10000000000.0))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def testAST37(self):
        input = """main: function integer (n: integer) {
            if (n == 0) return 1; 
            else return n * fact(n - 1);
        }
        x: integer = 65;"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	VarDecl(x, IntegerType, IntegerLit(65))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def testAST38(self):
        input = """delta: integer = fact(3);
        a: integer = 5;"""
        expect = """Program([
	VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)]))
	VarDecl(a, IntegerType, IntegerLit(5))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def testAST39(self):
        input = """main: function integer (n: integer) {
            for(i = 0, i < 10 , i + 1) {
                if (n == 0) return 1; 
                else return n * fact(n - 1);
            }
            foo(2+x, 4.0 / y);
            goo();
        }
        x: integer = main(5+6);"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))])), CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, )]))
	VarDecl(x, IntegerType, FuncCall(main, [BinExpr(+, IntegerLit(5), IntegerLit(6))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def testAST40(self):
        input = """main: function integer (n: integer) {
            do {
                b: integer = 3;
                a: string = "hello";
                for(i = 0, i < 10 , i + 1) {
                    if (n == 0) return 1; 
                    else return n * fact(n - 1);
                }
                if (n == 0) return 1; 
                else return n * fact(n - 1);
            } while (i < 10);
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(n, IntegerType)], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([VarDecl(b, IntegerType, IntegerLit(3)), VarDecl(a, StringType, StringLit(hello)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def testAST41(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) return 1; 
            else return n * fact(n - 1);
        }
        x: integer = 65;
        add: function void(out result: integer, a: integer, b: integer) {
            result = a + b;
            return;
        }
        main: function integer (n: integer) {
            while (i < 5) 
            if (n == 0) return 1; 
            else return n * fact(n - 1);
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(add, VoidType, [OutParam(result, IntegerType), Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(a), Id(b))), ReturnStmt()]))
	FuncDecl(main, IntegerType, [Param(n, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(5)), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))])))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def testAST42(self):
        input = """
        main : function void(args: string) {}
            foo: function boolean(a:string, b: string){
                return a == b;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(args, StringType)], None, BlockStmt([]))
	FuncDecl(foo, BooleanType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([ReturnStmt(BinExpr(==, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def testAST43(self):
        input = """
          main : function void() {    
                return 0;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def testAST44(self):
        input = """
         main : function void() {    
                if(true){
                    break;
                }
                else{
                    continue;
                }
                return;    
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([BreakStmt()]), BlockStmt([ContinueStmt()])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def testAST45(self):
        input = """
        x,y: integer = 2 , 3;
        main: function void () {
            while (x + y == 5) {
                x = 2+y;
            }
            printInt(x);
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2))
	VarDecl(y, IntegerType, IntegerLit(3))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, BinExpr(+, Id(x), Id(y)), IntegerLit(5)), BlockStmt([AssignStmt(Id(x), BinExpr(+, IntegerLit(2), Id(y)))])), CallStmt(printInt, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def testAST46(self):
        input = """
        main: function void () {
                b: array [5] of integer;
                b[4] = 3;
                printInt(b[4]);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(ArrayCell(b, [IntegerLit(4)]), IntegerLit(3)), CallStmt(printInt, ArrayCell(b, [IntegerLit(4)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def testAST47(self):
        input = """
        x,y: float;
        main: function void () {
            x: boolean;
            x = true;
            printBoolean(x);
        }
        """
        expect = """Program([
	VarDecl(x, FloatType)
	VarDecl(y, FloatType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, BooleanType), AssignStmt(Id(x), BooleanLit(True)), CallStmt(printBoolean, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def testAST48(self):
        input = """
       main: function void () {
                delta: boolean = !true&&!false||true||false||!false;
                printBoolean(delta);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, BooleanType, BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(&&, UnExpr(!, BooleanLit(True)), UnExpr(!, BooleanLit(False))), BooleanLit(True)), BooleanLit(False)), UnExpr(!, BooleanLit(False)))), CallStmt(printBoolean, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
    
    def testAST49(self):
        input = """
        main: function void () {
                a,c: string = "true","!true";
                v: string = a::c;
                printString(a);
                printString(v);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(true)), VarDecl(c, StringType, StringLit(!true)), VarDecl(v, StringType, BinExpr(::, Id(a), Id(c))), CallStmt(printString, Id(a)), CallStmt(printString, Id(v))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
    
    def testAST50(self):
        input = """
        voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34));
                printInt(delta);
            }
        """
        expect = """Program([
	FuncDecl(voidA, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(n), IntegerLit(4)), IntegerLit(2)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(voidA, [FuncCall(voidA, [IntegerLit(34)])])), CallStmt(printInt, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
    
    def testAST51(self):
        input = """
        main : function void(a: float) {
                a = 1.2;
                a = a - 1.7;
                printFloat(x + 2.5);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, FloatType)], None, BlockStmt([AssignStmt(Id(a), FloatLit(1.2)), AssignStmt(Id(a), BinExpr(-, Id(a), FloatLit(1.7))), CallStmt(printFloat, BinExpr(+, Id(x), FloatLit(2.5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def testAST52(self):
        input = """main: function void() {
            a,b,c :string = "hello", "123", "cd";
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(hello)), VarDecl(b, StringType, StringLit(123)), VarDecl(c, StringType, StringLit(cd))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def testAST53(self):
        input = """main: function void() {
        num : integer;
        readInteger(num);
        if ((num > 10) && (num < 100))
            printString("\\nWhat a True Guess!");
        else printString("\\nOpps!");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(num, IntegerType), CallStmt(readInteger, Id(num)), IfStmt(BinExpr(&&, BinExpr(>, Id(num), IntegerLit(10)), BinExpr(<, Id(num), IntegerLit(100))), CallStmt(printString, StringLit(\\nWhat a True Guess!)), CallStmt(printString, StringLit(\\nOpps!)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def testAST54(self):
        input = """main: function void() {
        for (i= 1, i < 10, i+1){
            if (i>5) continue;
            else printInteger(i);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(5)), ContinueStmt(), CallStmt(printInteger, Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def testAST55(self):
        input = """main: function void() {printInteger(2+5*6-10);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, BinExpr(-, BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(5), IntegerLit(6))), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def testAST56(self):
        input = """main: function void() {readBoolean(5>10);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(readBoolean, BinExpr(>, IntegerLit(5), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def testAST57(self):
        input = """main: function void() {
        a:integer;
        a = -5*10/2 + 10;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(+, BinExpr(/, BinExpr(*, UnExpr(-, IntegerLit(5)), IntegerLit(10)), IntegerLit(2)), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def testAST58(self):
        input = """main: function void() {sum = a[1] + a[2] +a[3] ;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(sum), BinExpr(+, BinExpr(+, ArrayCell(a, [IntegerLit(1)]), ArrayCell(a, [IntegerLit(2)])), ArrayCell(a, [IntegerLit(3)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def testAST59(self):
        input = """main: function void() inherit test {
            a = super(b,c);
            printInteger(a);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], test, BlockStmt([AssignStmt(Id(a), FuncCall(super, [Id(b), Id(c)])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def testAST60(self):
        input = """main: function void() {if (n == 0) printString("Hello");}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), CallStmt(printString, StringLit(Hello)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def testAST61(self):
        input = """test :function integer(inherit n:integer) inherit test1 {
            return 0;
            }"""
        expect = """Program([
	FuncDecl(test, IntegerType, [InheritParam(n, IntegerType)], test1, BlockStmt([ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def testAST62(self):
        input = """test :function integer(inherit n:integer, out m: integer) inherit test1 {
            m = 0;
            return 0;
            }"""
        expect = """Program([
	FuncDecl(test, IntegerType, [InheritParam(n, IntegerType), OutParam(m, IntegerType)], test1, BlockStmt([AssignStmt(Id(m), IntegerLit(0)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def testAST63(self):
        input = """main: function void() {
            printBoolean(a && b);
            printBoolean(a || b); 
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, BinExpr(&&, Id(a), Id(b))), CallStmt(printBoolean, BinExpr(||, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def testAST64(self):
        input = """main: function void(){
            name: string;
            printString("What is your name?");
            readString(name);
            printStringn("My name is "::name);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(name, StringType), CallStmt(printString, StringLit(What is your name?)), CallStmt(readString, Id(name)), CallStmt(printStringn, BinExpr(::, StringLit(My name is ), Id(name)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def testAST65(self):
        input = """main: function void(){
            a,b,c: integer;
            a = 4;
            b = 6;
            c=  7;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType), AssignStmt(Id(a), IntegerLit(4)), AssignStmt(Id(b), IntegerLit(6)), AssignStmt(Id(c), IntegerLit(7))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def testAST66(self):
        input = """main: function void() {            
            r, s: integer;
            r = 2.0;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def testAST67(self):
        input = """main: function void() {
            max: integer;
            for (i=0, i<10, i + 1) {
                max = max + i;
            }
            printInteger(max);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(max, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(max), BinExpr(+, Id(max), Id(i)))])), CallStmt(printInteger, Id(max))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def testAST68(self):
        input = """main: function void(){
            while (a>b) {
                while (b<c) 
                    b = b + 1;         
                break;
            }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([WhileStmt(BinExpr(<, Id(b), Id(c)), AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1)))), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def testAST69(self):
        input = """main: function void(){
            while (x != 10){
                x = x + 1;
                if (x > 10) break;
            }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, Id(x), IntegerLit(10)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(x), IntegerLit(10)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def testAST70(self):
        input = """main: function void() {
            a: integer;
            readInteger(a);
            if (a%2 ==0) printString("Even");
            else printString("Odd");
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), CallStmt(readInteger, Id(a)), IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(0)), CallStmt(printString, StringLit(Even)), CallStmt(printString, StringLit(Odd)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def testAST71(self):
        input = """main: function void() {
            a,b: integer = 10,20 ;
            tam: integer = a;
            a = b; 
            b = tam;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(10)), VarDecl(b, IntegerType, IntegerLit(20)), VarDecl(tam, IntegerType, Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(tam))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def testAST72(self):
        input = """fact: function integer (n: integer){
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def testAST73(self):
        input = """inc: function void(out n: integer, delta: integer){
            n = n + delta;
            }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def testAST74(self):
        input = """main: function void() {
            if((a >= b) && (a >= c)) {
                printString("Largest number: ");
                printInteger(a); 
            }
            if((b >= a) && (b >= c)){
                printString("Largest number: ");
                printInteger(b);
            }
            if((c >= a) && (c >= b)){
                printString("Largest number: ");
                printInteger(c);
            }
            return 0;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, Id(a), Id(b)), BinExpr(>=, Id(a), Id(c))), BlockStmt([CallStmt(printString, StringLit(Largest number: )), CallStmt(printInteger, Id(a))])), IfStmt(BinExpr(&&, BinExpr(>=, Id(b), Id(a)), BinExpr(>=, Id(b), Id(c))), BlockStmt([CallStmt(printString, StringLit(Largest number: )), CallStmt(printInteger, Id(b))])), IfStmt(BinExpr(&&, BinExpr(>=, Id(c), Id(a)), BinExpr(>=, Id(c), Id(b))), BlockStmt([CallStmt(printString, StringLit(Largest number: )), CallStmt(printInteger, Id(c))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def testAST75(self):
        input = """main: function integer(n:integer){
            sum: integer = n*(n+1)/2 ;
            return sum;
            }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, BinExpr(/, BinExpr(*, Id(n), BinExpr(+, Id(n), IntegerLit(1))), IntegerLit(2))), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def testAST76(self):
        input = '''
          test: function integer (out x:integer, data:string){
            c : integer;
        }
        '''
        expect = """Program([
	FuncDecl(test, IntegerType, [OutParam(x, IntegerType), Param(data, StringType)], None, BlockStmt([VarDecl(c, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def testAST77(self):
        input = '''
            main: function void () {
                delta: float = 123.45e6;
                printFloat(delta);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, FloatType, FloatLit(123450000.0)), CallStmt(printFloat, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def testAST78(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==96) {y :integer= 69;}
            }
        '''
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(96)), BlockStmt([VarDecl(y, IntegerType, IntegerLit(69))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def testAST79(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==69) {y :integer = 96;}
                else {y : integer = 35;}
            }
        '''
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(69)), BlockStmt([VarDecl(y, IntegerType, IntegerLit(96))]), BlockStmt([VarDecl(y, IntegerType, IntegerLit(35))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def testAST80(self):
        input = '''
            main : function void() {
                x : integer ;
                if(x==69){}
            }  
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(69)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def testAST81(self):
        input = '''
            main : function void() {
                x : integer ;
                if(x==69){} else {y : integer = 96;}
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(69)), BlockStmt([]), BlockStmt([VarDecl(y, IntegerType, IntegerLit(96))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def testAST82(self):
        input = '''
            main : function void() {
                for (i = 1, i < 10, i + 1) {
                    printInteger(i);
                }
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def testAST83(self):
        input = '''
            voidA: function integer(out n: integer){
                return n+4+2;
            }
            main: function void () {
                x: integer = 0;
                delta: integer = voidA(5+voidA(2));
                delta = delta/2 + delta/3;
                printInt(delta);
            }
        '''
        expect = """Program([
	FuncDecl(voidA, IntegerType, [OutParam(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(n), IntegerLit(4)), IntegerLit(2)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), VarDecl(delta, IntegerType, FuncCall(voidA, [BinExpr(+, IntegerLit(5), FuncCall(voidA, [IntegerLit(2)]))])), AssignStmt(Id(delta), BinExpr(+, BinExpr(/, Id(delta), IntegerLit(2)), BinExpr(/, Id(delta), IntegerLit(3)))), CallStmt(printInt, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def testAST84(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==69) {y : integer = 96; x = y; printInt(x);}
            }
        '''
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(69)), BlockStmt([VarDecl(y, IntegerType, IntegerLit(96)), AssignStmt(Id(x), Id(y)), CallStmt(printInt, Id(x))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def testAST85(self):
        input = '''
            x : integer = 2;
            main : function void() {
                if(x==3) x = 5;
            }
        '''
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), AssignStmt(Id(x), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
    
    def testAST86(self):
        input = '''
            x : integer =5 ;
            main : function void() {
                if(x==3+2) x = 4;
            }
        '''
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(5))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), BinExpr(+, IntegerLit(3), IntegerLit(2))), AssignStmt(Id(x), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def testAST87(self):
        input = '''
           main : function void(x: float) {    
                    a = x[y[2,2],5*6] + 6969 ;
                } 
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, ArrayCell(x, [ArrayCell(y, [IntegerLit(2), IntegerLit(2)]), BinExpr(*, IntegerLit(5), IntegerLit(6))]), IntegerLit(6969)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def testAST88(self):
        input = '''
            main : function string() {    
                return "CEM CLUB";
            }
        '''
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([ReturnStmt(StringLit(CEM CLUB))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def testAST89(self):
        input = '''
           main : function void() {
                return;
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def testAST90(self):
        input = '''
           main : function void(){
                if(true){
                    a: integer;
                }
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([VarDecl(a, IntegerType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def testAST91(self):
        input = """
         main : function void() {
                    a = b::c;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, Id(b), Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def testAST92(self):
        input = """n: integer = add(4,5);
        s: string = concat("hello", "world");
        a: boolean = find(s, "word");"""
        expect = """Program([
	VarDecl(n, IntegerType, FuncCall(add, [IntegerLit(4), IntegerLit(5)]))
	VarDecl(s, StringType, FuncCall(concat, [StringLit(hello), StringLit(world)]))
	VarDecl(a, BooleanType, FuncCall(find, [Id(s), StringLit(word)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def testAST93(self):
        input = """s: string = "hello";
        main: function void(){}
        add: function void(){}"""
        expect = """Program([
	VarDecl(s, StringType, StringLit(hello))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(add, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def testAST94(self):
        input = """main: function void(){
        if (me == 5){
            print("a > 2");
        }
        else{
            print("a <= 2");
        }}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(me), IntegerLit(5)), BlockStmt([CallStmt(print, StringLit(a > 2))]), BlockStmt([CallStmt(print, StringLit(a <= 2))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def testAST95(self):
        input = """a: boolean = (b + v) == (c + d == abd);"""
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(==, BinExpr(+, Id(b), Id(v)), BinExpr(==, BinExpr(+, Id(c), Id(d)), Id(abd))))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def testAST96(self):
        input = """main: function void(){print(a || b + 2);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, BinExpr(||, Id(a), BinExpr(+, Id(b), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def testAST97(self):
        input = """main: function void(){
            ___ = 1; 
            __ = 2;
            ____ = 4;
            _ = 3;
            print("What is the number?");
            print(___);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(___), IntegerLit(1)), AssignStmt(Id(__), IntegerLit(2)), AssignStmt(Id(____), IntegerLit(4)), AssignStmt(Id(_), IntegerLit(3)), CallStmt(print, StringLit(What is the number?)), CallStmt(print, Id(___))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def testAST98(self):
        input = """a: integer = 10;
        b, c: boolean = true, false;
        x, y: float = 3.4, 2.6e2;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(10))
	VarDecl(b, BooleanType, BooleanLit(True))
	VarDecl(c, BooleanType, BooleanLit(False))
	VarDecl(x, FloatType, FloatLit(3.4))
	VarDecl(y, FloatType, FloatLit(260.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def testAST99(self):
        input = """main: function void() {
            x[3] = 2.1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(3)]), FloatLit(2.1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def testAST100(self):
        input = """endtest: function void(){
            printString("Let's end test ASTGensuite. I'm tired");
        }"""
        expect = """Program([
	FuncDecl(endtest, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(Let's end test ASTGensuite. I'm tired))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))