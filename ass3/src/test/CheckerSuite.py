import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def Test1(self):
        self.assertTrue(TestChecker.test("""
		any: function void () {
 			printInteger(4);
 		}
		""", "No entry point", 401))

    def Test2(self):
        self.assertTrue(TestChecker.test("""
		mains: function string () {}
 		""", "No entry point", 402))

    def Test3(self):
        self.assertTrue(TestChecker.test("""
 		main: function void (a: boolean) {}
 		""", "No entry point", 403))

    def Test4(self):
        self.assertTrue(TestChecker.test("""
 		main: integer;
 		main: function void () {}
 		""", "Redeclared Function: main", 404))

    def Test5(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {}
 		main: float;
 		""", "Redeclared Variable: main", 405))

    def Test6(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {}
 		a: function void() {}
 		a: function void() {}
 		""", "Redeclared Function: a", 406))

    def Test7(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {}
 		foo: function void() {}
 		goo: function void(a: integer, a: string) inherit a {}
 		""", "Redeclared Parameter: a", 407))

    def Test8(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: integer;
 			a: string;
 		}
 		""", "Redeclared Variable: a", 406))

    def Test9(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {}
 		a: function void() {}
 		b: function void(a: integer) inherit a {
 			a: integer;
 		}
 		""", "Redeclared Variable: a", 408))

    def Test10(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {}
 		a: function void() {}
 		b: function void(a: integer) inherit a {
 			{
 				a: integer;
 			}
 		}
 		""", "", 409))

    def Test11(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a = b;
 		}
 		""", "Undeclared Identifier: b", 410))

    def Test12(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: integer = d;
 		}
 		""", "Undeclared Identifier: c", 411))

    def Test13(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: integer = foo();
 		}
 		""", "Undeclared Function: c", 412))

    def Test14(self):
        self.assertTrue(TestChecker.test("""
		main: function void () {
 			c();
 		}
 		""", "Undeclared Function: c", 413))

    def Test15(self):
        self.assertTrue(TestChecker.test("""
		main: function void () {
 			c();
 		}
 		c: function void() {}
 		""", "", 414))

    def Test16(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a[1] = 5;
 		}
 		""", "Undeclared Identifier: a", 415))


    def Test17(self):
        self.assertTrue(TestChecker.test("""
		main: function void () {
			a: auto;
		}
 		""", "Invalid Variable: a", 416))

    def Test18(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {}
 		x: function void (a: integer) {}
 		""", "", 417))

    def Test19(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: array[2] of integer;
 			a[1] = 5;
 		}
 		""", "", 418))

    def Test20(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: integer;
 			a[1] = 5;
 		}
 		""", "Type mismatch in expression: ArrayCell(a, [IntegerLit(1)])", 419))

    def Test21(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: array[2] of integer;
 			a["index string"] = 5;
 		}
 		""", "Type mismatch in expression: ArrayCell(a, [StringLit(index string)])", 420))

    def Test22(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: integer = 5 + 6;
 		}
 		""", "", 421))

    def Test23(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: integer = 4 + 6.5;
 		}
 		""", "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, IntegerLit(4), FloatLit(6.5)))", 422))

    def Test24(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: float = 5 + 6.5;
 		}
 		""", "", 423))

    def Test25(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: float = 5;
 		}
 		""", "", 424))

    def Test26(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: auto = 5 + 5 == 5;
 		}
 		""", "", 425))

    def Test27(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: float = --6;
 		}
 		""", "", 426))

    def Test28(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: boolean = !!true;
 		}
 		""", "", 427))

    def Test29(self):
        self.assertTrue(TestChecker.test("""
 		not: function integer() {
 			return 13;
 		}
		main: function void () {
 			a: integer = not();
 		}
 		""", "", 428))

    def Test30(self):
        self.assertTrue(TestChecker.test("""
 		aaa: function void() {
 			return 2131;
 		}
 		main: function void () {
 			a: integer = aaa();
 		}
 		""", "Type mismatch in statement: ReturnStmt(IntegerLit(5))", 429))

    def Test31(self):
        self.assertTrue(TestChecker.test("""
 		abcxyz: function integer() {
 			return 5;
 		}
 		main: function void () {
 			abcxyz();
 		}
 		""", "", 430))

    def Test32(self):
        self.assertTrue(TestChecker.test("""
 		nothing: function void() {}
 		ok: function void(a: integer) inherit nothing {
 			return;
 		}
 		main: function void () {
 			ok(5);
 		}
		""", "", 431))

    def Test33(self):
        self.assertTrue(TestChecker.test("""
 		nothing: function void() {}
 		ok: function void(a: integer) inherit nothing {
 			return;
 		}
 		main: function void () {
 			a: array[1] of integer;
 			ok(a);
 		}
 		""", "Type mismatch in statement: CallStmt(ok, Id(a))", 432))

    def Test34(self):
        self.assertTrue(TestChecker.test("""
	 	nothing: function void() {}
 		foo: function void(a: integer, b: array[3] of integer) inherit nothing {
 			return;
 		}
 		main: function void () {
 			foo(3, {1,2,3});
 		}
 		""", "", 433))

    def Test35(self):
        self.assertTrue(TestChecker.test("""
 		nothing: function void() {}
 		ok: function void(a: integer, b: array[2,2] of integer) inherit nothing {
 			{
 				a: integer;
 			}
 		}
 		main: function void () {
 			ok(3, {{1,2},{1,2}});
 		}
 		""", "", 435))

    def Test36(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: auto = false;
 			if (a) {
 				a: auto = 3;
 			} else
 				main();
 		}
 		""", "", 436))

    def Test37(self):
        self.assertTrue(TestChecker.test("""
 		a: function auto() {
 			return true;
 		}
 		main: function void () {
 			if (a()) {
 				a: auto = 3;
 			} else
 				main();
 		}
 		""", "", 437))

    def Test38(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			if (a()) {
 				a: auto = 3;
 			}
 		}
 		a: function auto() {
 			return true;
 		} 
 		""", "", 438))

    def Test39(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			x: auto = 5;
 			while (a())
 				x = a();
 		}
 		a: function auto() {
 			return true;
 		} 
 		""", "Type mismatch in statement: AssignStmt(Id(x), FuncCall(a, []))", 439))

    def Test40(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			do {
 				while (false) {
 					a: auto = 5;
	 			}
 			} while(x());
 		}
 		x: function boolean() {}
 		""", "", 440))

    def Test41(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: auto;
 			i: integer;
 			for (i = 3, i <= a, a) {
 				i: integer = i;
 			}
 		}
 		""", "Invalid Variable: a", 441))

    def Test41(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {}
 		foo: function void() {
 			return 123;
 		} 
 		""", "Type mismatch in statement: ReturnStmt(IntegerLit(5))", 443))

    def Test42(self):
        self.assertTrue(TestChecker.test("""
 		x: function string (a: integer) {}
 		y: function void () {}
 		main: function void () inherit x {
 			super(5);
 			a: integer;
 		}
 		""", "", 446))

    def Test43(self):
        self.assertTrue(TestChecker.test("""
 		x: function string (a: integer) {}
 		y: function void () {}
 		main: function void () inherit x {
			super(1);
 			a: integer;
		}
 		""", "", 447))

    def Test44(self):
        self.assertTrue(TestChecker.test("""
 		x: function string (a: integer) {}
 		y: function void () {}
 		main: function void () inherit x {
 			super("Hello World");
 			a: integer;
 		}
 		""", "Type mismatch in expression: StringLit(Hello World)", 448))

    def Test45(self):
        self.assertTrue(TestChecker.test("""
 		x: function string (a: integer) {}
 		y: function void () {}
 		main: function void () inherit x {
 			preventDefault();
 			a: integer;
 		}
 		""", "", 449))

    def Test46(self):
        self.assertTrue(TestChecker.test("""
 		x: function string (a: integer) {}
 		y: function void () {}
 		main: function void () inherit x {
 			a: integer;
 		}
 		""", "Invalid statement in function: main", 450))

    def Test47(self):
        self.assertTrue(TestChecker.test("""
 		x: function string (a: integer) {}
 		y: function void () {}
 		main: function void () inherit y {
 			a: integer;
		}
		 """, "", 451))

    def Test48(self):
        self.assertTrue(TestChecker.test("""
		x: function string (a: integer) {}
 		y: function void () {}
 		main: function void () inherit y {
 			preventDefault();
 			a: integer;
 		}
 		""", "", 452))

    def Test49(self):
        self.assertTrue(TestChecker.test("""
 		x: function string (a: integer) {}
 		y: function void () {}
 		main: function void () inherit y {
 			super();
 			a: integer;
 		}
 		""", "", 453))

    def Test50(self):
        self.assertTrue(TestChecker.test("""
 		y: function void () {}
 		main: function void () inherit y {
 			super(1,2);
 			a: integer;
 		}
 		""", "Type mismatch in expression: IntegerLit(1)", 454))

    def Test51(self):
        self.assertTrue(TestChecker.test("""
 		x: function string (a: integer) {}
 		y: function void () {}
 		main: function void () inherit y {
 			a: integer;
 			preventDefault();
		}
 		""", "", 455))

    def Test52(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			a: integer;
 			preventDefault();
 		}
 		""", "Invalid statement in function: main", 456))

    def Test53(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () inherit x {
 			a: integer;
 		}
 		""", "Undeclared Function: x", 457))

    def Test54(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () inherit x {
 			a: integer;
 		}
 		""", "Undeclared Function: x", 458))

    def Test55(self):
        self.assertTrue(TestChecker.test("""
 		x: function void(inherit a: integer) {}
 		y: function void(inherit b: string) inherit x {
 			preventDefault();
 		}
 		z: function void (a: boolean) inherit y {
 			super("a string");
 		}
 		main: function void () {}
 		""", "", 459))

    def Test56(self):
        self.assertTrue(TestChecker.test("""
 		x: function void(inherit a: integer) {}
 		y: function void(inherit b: string) inherit x {
 			preventDefault();
 		}
 		z: function void (b: boolean) inherit y {
 			super("a string");
 		}
 		main: function void () {}
 		""", "Invalid Parameter: b", 460))

    def Test57(self):
        self.assertTrue(TestChecker.test("""
 		y: function void(inherit b: string) {
 			preventDefault();
 		}
 		z: function void (c: boolean) inherit y {
 			super("a string");
 			d: boolean = c;
 			e: auto = b;
 			y(e);
 		}
 		main: function void () {}
 		""", "Invalid statement in function: y", 461))

    def Test58(self):
        self.assertTrue(TestChecker.test("""
 		y: function void(inherit b: string, c: string) {}
 		z: function void (c: boolean) inherit y {
 			super("a string", "another string");
 			d: boolean = c;
 			e: auto = b;
 			y(e, e);
 		}
 		main: function void () {}
 		""", "", 462))

    def Test59(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			return;
 			return 3;
 		}
 		""", "", 463))

    def Test60(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			return 3;
 			return;
 		}
 		""", "Type mismatch in statement: ReturnStmt(IntegerLit(3))", 464))

    def Test61(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			if (true) {
 				return;
 			} else {
 				return;
 				return {1,2,3};
 			}
 			return 3; 
 		}
 		""", "", 465))

    def Test62(self):
        self.assertTrue(TestChecker.test("""
		main: function void () {
 			if (true) {
 				break;
 			}
 		}
 		""", "Must in loop: BreakStmt()", 466))

    def Test63(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			while (true) {
 				if (true) {
 					continue;
 				}
 			}
 		}
 		""", "", 467))

    def Test64(self):
        self.assertTrue(TestChecker.test("""
 		x: function void (a: auto, b: auto) {
 			c: integer = a;
 			printBoolean(5 == a);
 			e: string = b;
 			f: string = e :: "Hello";
 		}
 		main: function void () {} 
 		""", "", 468))

    def Test65(self):
        self.assertTrue(TestChecker.test("""
 		x: function void (a: auto) {
 			i: integer;
 			a = i;
 			printBoolean(5 == a);
 		}
 		main: function void () {} 
 		""", "", 470))

    def Test66(self):
        self.assertTrue(TestChecker.test("""
 		y: function void (a: string) {}
 		x: function void (a: auto) {
 			y(a);
 			b: string = a :: "Hello"; 
 		}
 		main: function void () {
 			x("a string");
 		} 
 		""", "", 471))

    def Test67(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			x(5, {1,2,3});
 		} 
 		x: function void (a: integer, a: auto) {} 
 		""", "Redeclared Parameter: a", 473))

    def Test68(self):
        self.assertTrue(TestChecker.test("""
 		x: function void (a: auto, b: integer) {
 			a = a + b;
 		}
 		main: function void () {
 			x(5, 6); 
 		} 
 		""", "", 474))

    def Test69(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto() {}
 		main: function void () {
 			x();
 			a: integer = x(); 
 		} 
 		""", "", 475))

    def Test70(self):
        self.assertTrue(TestChecker.test("""
 		y: function auto() {}
 		x: function void (a: auto) {
 			a = a + y() + 1;
 			printInteger(a + y());
 		}
 		main: function void () {} 
 		""", "", 476))

    def Test71(self):
        self.assertTrue(TestChecker.test("""
 		y: function auto() {}
 		main: function void () {
 			a: auto = 5 + y() + 2.5;
 			writeFloat(a);
 		} 
 		""", "", 477))

    def Test72(self):
        self.assertTrue(TestChecker.test("""
 		y: function auto() {}
 		main: function void () {
 			a: auto = true && y() == false || (5 < 5.5);
 			printBoolean(a);
 		} 
 		""", "", 478))

    def Test73(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto() {}
 		y: function auto() {}
 		z: function auto() {}
 		t: function auto() {}
 		m: function auto() {}
 		main: function void () {
 			a: auto = z() && y() == false || (5 < x());
 			printBoolean(a);
 			b: auto = m() :: (t() :: "HCMUT");
 			printString(b);
 		} 
 		""", "", 479))

    def Test74(self):
        self.assertTrue(TestChecker.test("""
 		super: string;
 		main: function void () {} 
 		""", "Redeclared Variable: super", 480))

    def Test75(self):
        self.assertTrue(TestChecker.test("""
 		a: function void(a: integer) {
 			a();
 		}
 		main: function void () {} 
 		""", "Type mismatch in statement: CallStmt(a, )", 481))

    def Test75(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {} 
 		""", "", 482))

    def test76(self):
        self.assertTrue(TestChecker.test("""
		foo: function void(){}
		main: function integer(){}
 		""", "No entry point", 483))

    def test77(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto() {}
 		y: function auto() {}
 		z: function auto() {}
 		t: function auto() {}
 		m: function auto() {}
 		main: function void () {
 			a: auto = z() && y() == false || (t() + m() + 1 < x());
 			printInteger(t());
 			printInteger(x());
 		} 
 		""", "", 484))

    def test78(self):
        self.assertTrue(TestChecker.test("""
		x: integer;
 		mainx: function void (x: string) {
 			{
 				x: boolean;
 			}
 		} 
 		main: function void () {}
 		""", "", 485))

    def test79(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto() {}
 		main: function void () {
 			a: auto = -5 + 2 + x();
 			printInteger(a);
 			writeFloat(a);
 			b: auto = -5 * 2e5 / x();
 			writeFloat(b); 
 			printInteger(b); 
 		} 
 		""", "Type mismatch in statement: CallStmt(printInteger, Id(b))", 486))

    def test80(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto(y: auto) {
 			y = 4;
 			printInteger(y);
 		}
 		main: function void () {
 			printString(x(3)); 
 		} 
 		""", "", 487))

    def test81(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto(x: auto) {
 			x = 4;
 			printInteger(x);
 		}
 		main: function void () {
 			x();
 		} 
 		""", "Type mismatch in statement: CallStmt(x, )", 488))

    def test82(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto(x: auto) {
 			x = 4;
 			printInteger(x);
 		}
 		main: function void () {
 			x(4,6); 
 		} 
 		""", "Type mismatch in statement: CallStmt(x, IntegerLit(4), IntegerLit(6))", 489))

    def test83(self):
        self.assertTrue(TestChecker.test("""
 		a: float = foo(1, 2) + 1.5;
 		foo: function integer(a: integer, b: integer) {
 			return a + b; 
 		}
 		x: function auto() {
 			writeFloat(foo(1,2));
 		}
 		main: function void () inherit x {
			super();
 			printInteger(x());
 		} 
 		""", "", 490))

    def test84(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto() {
 			return false;
 		}
 		main: function void () {
 			a: integer = readInteger();
 			if (true) {
 				a: integer = 5;
 			} else if (false) {
 				a: auto = readFloat();
 			} else {
 				x();
 				i: auto = 123 + 34445;
 			for (i = i, i == i, i)
 				i = i;	
 			}
 		}
 		""", "", 491))

    def test85(self):
        self.assertTrue(TestChecker.test("""
 		main: function void () {
 			x();
 		}
 		x: function auto() {}
 		x: function auto(a: auto, b: auto) {}
 		""", "Redeclared Function: x", 492))

    def test86(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto(a: auto, b: auto) {}
 		main: function void () {
 			x(); 
 		}
 		x: function auto() {}
 		""", "Type mismatch in statement: CallStmt(x, )", 493))

    def test87(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto() inherit y {
 			super(abc);
 			a = x;
 		}
 		main: function void () {}
 		y: function auto(inherit a: auto, inherit b: auto, inherit a: auto, inherit b: integer) {} 
 		""", "Redeclared Parameter: a", 494))

    def test88(self):
        self.assertTrue(TestChecker.test("""
 		y: function void(c: auto) {}
 		x: function void(a: integer) inherit y {
 			super(a);
 		}
 		main: function void () {
 			x(1);
 			y("a string");
 		}
 		""", "Type mismatch in statement: CallStmt(y, StringLit(a string))", 495))

    def test89(self):
        self.assertTrue(TestChecker.test("""
 		y: function void(inherit c: auto) {}
 		x: function void(a: integer) inherit y {
 			super(6);
 			a = c;
 		} 
 		z: function void(a: integer) inherit y {
 			preventDefault();
 			a = c;
 		}
 		main: function void () {}
 		""", "", 496))

    def test90(self):
        self.assertTrue(TestChecker.test("""
 		y: function void(inherit c: auto, d: auto, e: auto) {}
 		x: function void(a: integer) inherit y {
 			super(5,6);
 		} 
 		main: function void () {}
 		""", "Type mismatch in expression: ", 497))

    def test91(self):
        self.assertTrue(TestChecker.test("""
 		y: float = -foo(1,1); 
 		foo: function auto(a: auto, b:auto){
 			x: auto = a;
 		} 
 		bar: function void() {}
 		main: function void() {
 			bar: integer = 1;
 			x: float = bar();
 			x = bar;
 		} 
 		""", "Type mismatch in expression: FuncCall(bar, [])", 498))

    def test92(self):
        self.assertTrue(TestChecker.test("""
 		foo: function void(a: integer){}
 		main: function void() {
 			foo(1, a); 
 		} 
 		""", "Type mismatch in statement: CallStmt(foo, IntegerLit(1), Id(a))", 499))

    def test93(self):
        self.assertTrue(TestChecker.test("""
 		foo: function auto(a: integer){}
 		main: function void() {
 			x: boolean = 1 == true;
 			y: array [1,2,3] of integer;
 			z: auto = y[1,1+1-0];
 			t: integer = foo(1, a);
 		} 
 		""", "Type mismatch in expression: FuncCall(foo, [IntegerLit(1), Id(a)])", 500))

    def test94(self):
        self.assertTrue(TestChecker.test("""
 		M: function void (a: integer) inherit N {} 
 		N: function void (inherit a: integer) {} 
 		""", "Invalid Parameter: a", 501))

    def test95(self):
        self.assertTrue(TestChecker.test("""
 		M: function array[3] of integer (a: integer) {
 			return {a + 1, a - 1, a, a + 1};
 		} 
 		""", "Type mismatch in statement: ReturnStmt(ArrayLit([BinExpr(+, Id(a), IntegerLit(1)), BinExpr(-, Id(a), IntegerLit(1)), Id(a), BinExpr(+, Id(a), IntegerLit(1))]))", 502))

    def test96(self):
        self.assertTrue(TestChecker.test("""
 		foo: function auto() {}
 		bar: function void (a: auto) {
 			a = foo() + foo();
 		} 
 		main: function void() {}
 		""", "", 504))

    def test97(self):
        self.assertTrue(TestChecker.test("""
 		bar: function void () {}
 		foo: function auto() inherit bar {
 			preventDefault(4);
 		}
 		main: function void () {} 
 		""", "Type mismatch in expression: IntegerLit(4)", 505))

    def test98(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto () {
 			if (true) 
 				return true;
 			else
 				return 1;
 		}
 		main: function void () {} 
 		""", "Type mismatch in statement: ReturnStmt(IntegerLit(1))", 507))

    def test99(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto (a: auto, b: auto) {
 			while(true)
 				return true;
 			return 1;
 		}
 		main: function void () {} 
 		""", "", 508))

    def test100(self):
        self.assertTrue(TestChecker.test("""
 		x: function auto () {
 			y("string", 4);
 		}
 		main: function void () {} 
 		y: function auto (a: auto, b: integer) {
 			x: integer = a + b;
 		}
 		""", "Type mismatch in expression: BinExpr(+, Id(a), Id(b))", 509))