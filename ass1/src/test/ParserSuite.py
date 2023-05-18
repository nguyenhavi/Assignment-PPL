import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test201(self):
        input = """main: function void() {if (x=y) printInteger(x);}"""
        expect = """Error on line 1 col 28: ="""
        self.assertTrue(TestParser.test(input, expect, 201))

    def test202(self):
        """Simple program: int main() {} """
        input = """main: function void() {
            delta: integer = fact(3);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test203(self):
        input = """fl: float = 1234.4312;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 203))

    def test204(self):
        input = """main: function integer(){n = n + delta;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test205(self):
        input = """int: integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 205))
    
    def test206(self):
        input = """fl: float;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 206))
    
    def test207(self):
        input = """str: string;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 207))
    
    def test208(self):
        input = """t: boolean; f:boolean;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 208))
    
    def test209(self):
        input = """
            main: function void() {
                if (n == 0) {
                    return n-1;
                }
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 209))
    
    def test210(self):
        input = """x: integer = 10;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 210))
    
    def test211(self):
        input = """t: float = 123.433;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 211))
    
    def test212(self):
        input = """x, y, z: integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 212))
    
    def test213(self):
        input = """i, j: boolean;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 213))
    
    def test_214(self):
        input = """int: integer = 123456789;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 214))
    
    def test215(self):
        input = """t: boolean = true;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 215))
    
    def test216(self):
        input = """str: string = "helloworld";"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 216))
    
    def test217(self):
        input = """name: string = "Peter";"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 217))

    def test218(self):
        """Simple program: int main() {} """
        input = """main: function void(out n: integer, delta: integer) {
            n = n + delta;
            b = b + 1;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test219(self):
        input = """main: function void(out n: integer) {}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 219))

    def test220(self):
        input = """main: function void() { if (a > 2) b=a-2; else b=a+2; }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 220))
    
    def test221(self):
        input = """b: float = 12345.54312;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 221))
    
    def test222(self):
        input = """main: function void() { for(i = 1, i <10, i+1){if (i>5) break;}}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222))
    
    def test223(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 223))

    def test224(self):
        input = """
        x: integer = 65;
        y: float = 1e10;
        fact: function integer (n: integer) {
            if (n == 0) return 1; 
            else return n * fact(n - 1);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 224))
    
    def test225(self):
        input = """
        main: function integer (n: integer) {
            if (n == 0) return 1; 
            else return n * fact(n - 1);
        }
        x: integer = 65;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 225))
    def test226(self):
        input = """
        delta: integer = fact(3);
        a: integer = 5;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 226))
    def test227(self):
        input = """
        main: function integer (n: integer) {
            if (n == 0) return 1; 
            else return n * fact(n - 1);
        }
        x: integer = 65;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227))
    
    def test228(self):
        input = """
        main: function integer (n: integer) {
            for(i = 0, i < 10 , i + 1) {
                if (n == 0) return 1; 
                else return n * fact(n - 1);
            }
            foo(2+x, 4.0 / y);
            goo();
        }
        x: integer = main(5+6);
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 228))
    
    def test229(self):
        input = """
        main: function integer (n: integer) {
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
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 229))

    def test230(self):
        input = """
        fact: function integer (n: integer) {
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
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 230))

    def test231(self):
        input = """
        main: function array [2,3] of integer (n: integer) {
            x: integer = 65;
            y: array [2] of integer = {2, 4};
            printInt(1244123);
            writeFloat(1.23);
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 231))

    def test232(self):
        input ="""x: array [2] of string = {"hello", "world"};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 232))
    
    def test233(self):
        input = """
        x: array [2,2] of integer = {{2, 3}, {5, 6}};
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 233))
    
    def test234(self):
        input = """
        x: array [2,2] of float = {{2.1, 3e-10}, {5.1E+12, 6.00}};
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 234))
    
    def test235(self):
        input = """
        x: array [2,3] of boolean = {{true, false, true}, {false, true, false}};
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 235))
    
    def test236(self):
        input = """
        sum2number: function integer(a: integer, b: integer) {
            return a+b;
        }
        sum_array: function integer(out result: integer, a: array [10] of integer) {
            sum: integer = 0;
            for(i = 0, i < 10, i + 1) {
                sum = sum + a[i];
            }
            result = sum;
            return;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 236))
    
    def test237(self):
        input = """main: function void() {
            readInteger(a);
            a = ((a-2) * (8/2)) + a/a + a%2;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 237))
    
    def test238(self):
        input = """main: function void(){
            a,b,c: integer = 10, 20 ,30;
            d: integer = a*b+c;
            printInteger(d);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 238))
    
    def test239(self):
        input = """
        x: array [2,3] of float = {{1.2, -2, 3.5e2}, {-2_3.5e10, -100.1, 2.3434}};
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 239))
    
    def test240(self):
        input = """main: function void(){
            myself: boolean;
            printString("Why are you running?");
            keeprunning(myself);
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 240))
    
    def test241(self):
        input = """main: function void(){
            name: string;
            printString("What is your name?");
            readString(name);
            printStringn("My name is "::name);
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 241))
    
    def test242(self):
        input = """
        abc: array [2,3] of string = {{"hi", "aaa", "!"}, {"nope", "no", "nah"}};
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 242))
    
    def test243(self):
        input = """main: function void(){
            a,b,c: integer;
            a = 4;
            b = 6;
            c=  7;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 243))
    
    def test244(self):
        input = """a, b, c: integer = 3, 4, 5, 6;"""
        expect = """Error on line 1 col 26: ,"""
        self.assertTrue(TestParser.test(input, expect, 244))
    
    def test245(self):
        input = """
        x: array [3] of string = {"hello", "world", "!"};
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 245))
    def test246(self):
        input = """ aB12: string = "anb" ;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 246))
    def test247(self):
        input = """main: function integer(){
        foo1(2 + x + z, 4.0 / y * w); 
        goo1();
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 247))
    def test248(self):
        input = """main: function void() {            
            r, s: integer;
            r = 2.0;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 248))
    def test249(self):
        input = """main: function void() {
        n1, n2, max: integer;
        readInteger(n1,n2);
        if (n1>n2) max = n1;
        else max = n2;
        return 0;
        } """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 249))
    def test250(self):
        input = """main: function void() {
        do {
        if ( (max % n1 == 0) && (max % n2 == 0) )
            {
                print("LCM = ");
                printInteger(max);
                break;
            }
        else max = max +1;
        } while (true);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 250))
    def test251(self):
        input = """main: function void() {
            max: integer;
            for (i=0, i<10, i + 1) {
                max = max + i;
            }
            printInteger(max);
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 251))
    def test252(self):
        input = """main: function void(){
            while (a>b) {
                while (b<c) 
                    b = b + 1;         
                break;
            }
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 252))
    def test253(self):
        input = """main: function void(){
            while (a!=b){
                writeInteger(a);
                a = a + 1;
                }
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 253))
    def test254(self):
        input = """main: function void()[]"""
        expect = """Error on line 1 col 21: ["""
        self.assertTrue(TestParser.test(input, expect, 254))
    def test255(self):
        input = """main: function string(){
            for (i = 2, i!=100, i+1)  
                if ((a+b)>(c+d))  
                    return "Something\\"Just Like This\\n"; 
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 255))
    def test256(self):
        input = """main: function integer(){a = "abc"::"bcd";}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 256))
    def test257(self):
        input = """main: function integer(){printString("Hello World")}"""
        expect = """Error on line 1 col 51: }"""
        self.assertTrue(TestParser.test(input, expect, 257))
    def test258(self):
        input = """main: function void(){
            while (x != 10){
                x = x + 1;
                if (x > 10) break;
            }
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 258))
    def test259(self):
        input = """main: function void() {
            a: integer;
            readInteger(a);
            if (a%2 ==0) printString("Even");
            else printString("Odd");
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 259))
    def test260(self):
        input = """main: function void() {
            a,b: integer = 10,20 ;
            tam: integer = a;
            a = b; 
            b = tam;
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 260))
    def test261(self):
        input = """fact: function integer (n: integer){
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 261))
    def test262(self):
        input = """inc: function void(out n: integer, delta: integer){
            n = n + delta;
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 262))
    def test263(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 263))
    def test264(self):
        input = """main: function integer(n:integer){
            sum: integer = n*(n+1)/2 ;
            return sum;
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 264))

    def test265(self):
        input = """x : array[5] of integer = {1,2,3,4,5};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 265))

    def test266(self):
        input = """main: function integer(){
        arr: array[3,2] of integer;
        arr = {{2,3},{5,4},{6,7}};
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 266))

    def test267(self):
        input = """main: function void(){
                for (i = 0, i < n, i+1) {
                    count: integer = 1 ;
                    for (j = i + 1, j < n, j+1) 
                        if (arr[i] == arr[j]) count = count +1; 
                    if (count > max_count)
                        max_count = count;
                }
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 267))

    def test268(self):
        input = """main: function void(){
            for (i = 1; i< n; i +1){
                printInteger(i);
            }
            }"""
        expect = """Error on line 2 col 22: ;"""
        self.assertTrue(TestParser.test(input, expect, 268))

    def test269(self):
        input = """main: function float(){
            return 7e3 * 7.2 ;
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 269))

    def test270(self):
        input = """main: function string(a: string, b: string){
            return a::b;
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 270))

    def test271(self):
        input = """main: function integer(){
            if (a >= b) return 5%2;
            else if (a < b) return (2+3)*7;
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 271))

    def test272(self):
        input = """main: function integer(){
        a : array[2,3] of integer = {{3,4,5},{5,6,7}};
        a[0,1] = 2;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 272))

    def test273(self):
        input = """main: function void() {a = array[5] of integer;}"""
        expect = """Error on line 1 col 27: array"""
        self.assertTrue(TestParser.test(input, expect, 273))

    def test274(self):
        input = """a,b,c,d,e : integer = 5,6,7,8;"""
        expect = """Error on line 1 col 29: ;"""
        self.assertTrue(TestParser.test(input, expect, 274))

    def test275(self):
        input = """main: function void() {
            a,b,c :string = "hello", "123", "cd";
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 275))

    def test276(self):
        input = """main: function void() {
        num : integer;
        readInteger(num);
        if ((num > 10) && (num < 100))
            printString("\\nWhat a True Guess!");
        else printString("\\nOpps!");
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 276))

    def test277(self):
        input = """x,a: integer"""
        expect = """Error on line 1 col 12: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 277))

    def test278(self):
        input = """main: function void() {
        for (i= 1, i < 10, i+1){
            if (i>5) continue;
            else printInteger(i);
            }
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 278))

    def test279(self):
        input = """main: function void() {printInteger(2+5*6-10);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 279))

    def test280(self):
        input = """main: function void() {readBoolean(5>10);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 280))

    def test281(self):
        input = """main: function void() {
        a:integer;
        a = -5*10/2 + 10;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 281))

    def test282(self):
        input = """main: function void() {printString("abc");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 282))

    def test283(self):
        input = """main: function void() {sum = a[1] + a[2] +a[3] ;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 283))

    def test284(self):
        input = """main: function void() {sum =;}"""
        expect = """Error on line 1 col 28: ;"""
        self.assertTrue(TestParser.test(input, expect, 284))

    def test285(self):
        input = """test: function array[2] of string(){
            return {"hello", "hi"};
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 285))

    def test286(self):
        input = """float = 10.2;"""
        expect = """Error on line 1 col 0: float"""
        self.assertTrue(TestParser.test(input, expect, 286))

    def test287(self):
        input = """auto : integer = 1;"""
        expect = """Error on line 1 col 0: auto"""
        self.assertTrue(TestParser.test(input, expect, 287))

    def test288(self):
        input = """ a + b = c"""
        expect = """Error on line 1 col 3: +"""
        self.assertTrue(TestParser.test(input, expect, 288))

    def test289(self):
        input = """main: function void() {if (n == 0) printString("Hello");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 289))

    def test290(self):
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test291(self):
        input = """delta: integer = fact(3);"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 291))

    def test292(self):
        input = """test :function integer(inherit n:integer) inherit test1 {
            return 0;
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 292))

    def test293(self):
        input = """test :function integer(inherit n:integer, out m: integer) inherit test1 {
            m = 0;
            return 0;
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 293))

    def test294(self):
        input = """main: function void() inherit test {
            a = super(b,c);
            printInteger(a);
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 294))

    def test295(self):
        input = """main: function void() {
            printBoolean(aaa && bqqq);
            printBoolean(a12 || blp); 
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 295))

    def test296(self):
        input = """main: function void() {}
        //Test linecomment !@#$%^&*()"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 296))

    def test297(self):
        input = """main: function void() {
            //Test line comment !@#$%^&*()
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 297))

    def test298(self):
        input = """main: function void() {/*Test comment ~!@# */}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 298))

    def test299(self):
        input = """main: function void() {
            abc : array[2,3,2] of integer = {{{1,2},{2,3},{3,4}},{{4,5},{5,6},{7,8}}};
            i : integer;
            sum = a[0,3,0] + a[1,2,1];
            printInteger(sum);
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 299))

    def test300(self):
        input = """endtest: function void(){
            printString("ahihi");
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 300))