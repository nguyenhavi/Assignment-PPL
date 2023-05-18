import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test101(self):
        """test identifiers"""
        input = '7E-10'
        expect = '7E-10,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 101))

    def test102(self):
        input = 'abc'
        expect = 'abc,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 102))
    
    def test103(self):
        input = 'true'
        expect = 'true,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 103))

    def test104(self):
        input = '"This is a string containing tab \\t"'
        expect = 'This is a string containing tab \\t,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 104))

    def test105(self):
        input = '"This is a string containing tab \\c"'
        expect = 'Illegal Escape In String: This is a string containing tab \\c'
        self.assertTrue(TestLexer.test(input,expect, 105))

    def test106(self):
        input = '"This is a string containing tab \\t'
        expect = 'Unclosed String: This is a string containing tab \\t'
        self.assertTrue(TestLexer.test(input,expect, 106))

    def test107(self):
        input = '1_234.456e-10'
        expect = '1234.456e-10,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 107))
    
    def test108(self):
        input = 'return n-1'
        expect = 'return,n,-,1,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 108))

    def test109(self):
        input = '1aaaa'
        expect = '1,aaaa,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 109))

    def test110(self):
        input = 'true'
        expect = 'true,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 110))

    def test111(self):
        input = 'false'
        expect = 'false,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 111))
    
    def test112(self):
        input = 'x: integer = 12'
        expect = 'x,:,integer,=,12,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 112))

    def test113(self):
        input = 'readInteger()'
        expect = 'readInteger,(,),<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 113))

    def test114(self):
        input = 'x: integer = 12'
        expect = 'x,:,integer,=,12,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 114))

    def test115(self):
        input = '"He asked me: \\"Where is John?\\""'
        expect = 'He asked me: \\"Where is John?\\",<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 115))
    
    def test116(self):
        input = 'if (n == 0) return 1;'
        expect = 'if,(,n,==,0,),return,1,;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 116))

    def test117(self):
        input = 'x = a + b'
        expect = 'x,=,a,+,b,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 117))
    
    def test118(self):
        input = 'inc: function void (out n: integer, delta: integer)'
        expect = 'inc,:,function,void,(,out,n,:,integer,,,delta,:,integer,),<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 118))
    
    def test119(self):
        input = '1234.567e?10'
        expect = '1234.567,e,Error Token ?'
        self.assertTrue(TestLexer.test(input,expect, 119))

    def test120(self):
        input = '"This is a string containing tab \\b"'
        expect = 'This is a string containing tab \\b,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 120))\
    
    def test121(self):
        input = '"This is a string containing tab \\f"'
        expect = 'This is a string containing tab \\f,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 121))
    
    def test122(self):
        input = '"This is a string containing tab \\n"'
        expect = 'This is a string containing tab \\n,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 122))

    def test123(self):
        input = '"This is a string containing tab \\r"'
        expect = 'This is a string containing tab \\r,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 123))

    def test124(self):
        input = '"This is a string containing tab \\\\"'
        expect = 'This is a string containing tab \\\\,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 124))

    def test125(self):
        input = 'array [2, 3] of integer'
        expect = 'array,[,2,,,3,],of,integer,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 125))

    def test126(self):
        input = 'a[1,1]'
        expect = 'a,[,1,,,1,],<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 126))

    def test127(self):
        input = 'delta: integer = fact(3);'
        expect = 'delta,:,integer,=,fact,(,3,),;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 127))

    def test128(self):
        input = 'for (i = 1,i < 10,i + 1)'
        expect = 'for,(,i,=,1,,,i,<,10,,,i,+,1,),<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 128))

    def test129(self):
        input = 'abc?d'
        expect = 'abc,Error Token ?'
        self.assertTrue(TestLexer.test(input,expect, 129))

    def test130(self):
        input = '1__234.567'
        expect = '1,__234,.,567,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 130))

    def test131(self):
        input = '1__234'
        expect = '1,__234,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 131))

    def test131(self):
        input = '.01'
        expect = '.,0,1,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 131))

    def test132(self):
        input = '0e123'
        expect = '0e123,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 132))

    def test133(self):
        input = 'writeInt(i);'
        expect = 'writeInt,(,i,),;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 133))

    def test134(self):
        input = '""'
        expect = ',<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 134))

    def test135(self):
        input = '"'
        expect = 'Unclosed String: '
        self.assertTrue(TestLexer.test(input,expect, 135))

    def test136(self):
        input = '"\'"'
        expect = "\',<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 136))

    def test137(self):
        input = """main: function void () {
            for (x[1] = 2, x == 1, x + 1) {
                x = 1;
                }
            }"""
        expect = 'main,:,function,void,(,),{,for,(,x,[,1,],=,2,,,x,==,1,,,x,+,1,),{,x,=,1,;,},},<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 137))

    def test138(self):
        input = '\\abc'
        expect = 'Error Token \\'
        self.assertTrue(TestLexer.test(input,expect, 138))

    def test139(self):
        input = 'break;'
        expect = 'break,;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 139))

    def test140(self):
        input = '!@#$!@$%$#^%^&^*&'
        expect = '!,Error Token @'
        self.assertTrue(TestLexer.test(input,expect, 140))

    def test141(self):
        input = '"CR7 is the greatest of all time! SIUUUUUUU"'
        expect = 'CR7 is the greatest of all time! SIUUUUUUU,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 141))

    def test142(self):
        input = '_____abc____1'
        expect = '_____abc____1,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 142))

    def test143(self):
        input = '1.e00000'
        expect = '1,.,e00000,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 143))

    def test144(self):
        input = '1_e00000'
        expect = '1,_e00000,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 144))

    def test145(self):
        input = '1.03454e10+918203-1230981+3_892734234e'
        expect = '1.03454e10,+,918203,-,1230981,+,3892734234,e,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 145))

    def test146(self):
        input = '1,e'
        expect = '1,,,e,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 146))

    def test147(self):
        input = '0e10'
        expect = '0e10,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 147))

    def test148(self):
        input = 'true + 123 + "abc" - 3 * 4'
        expect = 'true,+,123,+,abc,-,3,*,4,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 148))

    def test149(self):
        input = 'a[1,3,5,4,5,]'
        expect = 'a,[,1,,,3,,,5,,,4,,,5,,,],<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 149))

    def test150(self):
        input = '{1,2,3,4,5,6}'
        expect = '{,1,,,2,,,3,,,4,,,5,,,6,},<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 150))

    def test151(self):
        input = '0-1e-10'
        expect = '0,-,1e-10,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 151))

    def test152(self):
        input = 'nguyenha@gmail.com'
        expect = 'nguyenha,Error Token @'
        self.assertTrue(TestLexer.test(input,expect, 152))

    def test153(self):
        input = '"nguyenha@gmail.com"'
        expect = 'nguyenha@gmail.com,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 153))

    def test154(self):
        input = 'sdt: 09727586218'
        expect = 'sdt,:,0,9727586218,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 154))

    def test155(self):
        input = '+1234569'
        expect = '+,1234569,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 155))

    def test156(self):
        input = '"abc" :: "xyz"'
        expect = 'abc,::,xyz,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 156))

    def test157(self):
        input = '1234 + "abc"'
        expect = '1234,+,abc,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 157))

    def test158(self):
        input = '//////'
        expect = '<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 158))

    def test159(self):
        input = '/* abc */ abc'
        expect = 'abc,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 159))

    def test160(self):
        input = '// abcbcbccbcbcbab'
        expect = '<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 160))

    def test161(self):
        """test identifiers"""
        input = '"This is a string containing tab \\t'
        expect = 'Unclosed String: This is a string containing tab \\t'
        self.assertTrue(TestLexer.test(input,expect, 161))

    def test162(self):
        """test identifiers"""
        input = '7E-10'
        expect = '7E-10,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 162))

    def test163(self):
        input = 'abc'
        expect = 'abc,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 163))
    
    def test164(self):
        input = 'false'
        expect = 'false,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 164))

    def test165(self):
        input = '"This is not a string containing tab \\t"'
        expect = 'This is not a string containing tab \\t,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 165))

    def test166(self):
        input = '"This is a string containing tab \\c abc"'
        expect = 'Illegal Escape In String: This is a string containing tab \\c'
        self.assertTrue(TestLexer.test(input,expect, 166))

    def test167(self):
        input = '"This is a string containing tab \\\\ \\t'
        expect = 'Unclosed String: This is a string containing tab \\\\ \\t'
        self.assertTrue(TestLexer.test(input,expect, 167))

    def test168(self):
        input = '1_234.456e-100'
        expect = '1234.456e-100,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 168))
    
    def test169(self):
        input = 'return n-1+1'
        expect = 'return,n,-,1,+,1,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 169))

    def test170(self):
        input = '21aaaabbb'
        expect = '21,aaaabbb,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 170))

    def test171(self):
        input = '!'
        expect = '!,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 171))

    def test172(self):
        input = '||'
        expect = '||,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 172))
    
    def test173(self):
        input = 'x: integer = 123'
        expect = 'x,:,integer,=,123,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 173))

    def test174(self):
        input = 'readInteger(2)'
        expect = 'readInteger,(,2,),<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 174))

    def test175(self):
        input = 'x: string = 12'
        expect = 'x,:,string,=,12,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 175))

    def test176(self):
        input = '"He asked me: \\"Where is nguyen now?\\""'
        expect = 'He asked me: \\"Where is nguyen now?\\",<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 176))
    
    def test177(self):
        input = 'if (n == 0) return 11;'
        expect = 'if,(,n,==,0,),return,11,;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 177))

    def test178(self):
        input = 'x = a + b * c'
        expect = 'x,=,a,+,b,*,c,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 178))
    
    def test179(self):
        input = 'inc: function void (inherit out n: integer, delta: integer)'
        expect = 'inc,:,function,void,(,inherit,out,n,:,integer,,,delta,:,integer,),<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 179))
    
    def test180(self):
        input = '1234.567e?100'
        expect = '1234.567,e,Error Token ?'
        self.assertTrue(TestLexer.test(input,expect, 180))

    def test181(self):
        input = '"This is a abc containing tab \\b"'
        expect = 'This is a abc containing tab \\b,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 181))\
    
    def test182(self):
        input = '"This is a abc containing tab \\f"'
        expect = 'This is a abc containing tab \\f,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 182))
    
    def test183(self):
        input = '"This is a abc containing tab \\n"'
        expect = 'This is a abc containing tab \\n,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 183))

    def test184(self):
        input = '"This is a abc containing tab \\r"'
        expect = 'This is a abc containing tab \\r,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 184))

    def test185(self):
        input = '"This is a && containing tab \\\\"'
        expect = 'This is a && containing tab \\\\,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 185))

    def test186(self):
        input = 'array [2, 3] of string'
        expect = 'array,[,2,,,3,],of,string,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 186))

    def test187(self):
        input = 'a[1,1,1]'
        expect = 'a,[,1,,,1,,,1,],<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 187))

    def test188(self):
        input = 'This is a string containing tab \\ \\t'
        expect = 'This,is,a,string,containing,tab,Error Token \\'
        self.assertTrue(TestLexer.test(input,expect, 188))

    def test189(self):
        input = '"This is a string containing tab \\ \\t"'
        expect = 'Illegal Escape In String: This is a string containing tab \\ '
        self.assertTrue(TestLexer.test(input,expect, 189))

    def test190(self):
        input = 'abc?defgh'
        expect = 'abc,Error Token ?'
        self.assertTrue(TestLexer.test(input,expect, 190))

    def test191(self):
        input = '1__2345.5678'
        expect = '1,__2345,.,5678,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 191))

    def test192(self):
        input = '1__02345'
        expect = '1,__02345,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 192))

    def test193(self):
        input = '.0111'
        expect = '.,0,111,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 193))

    def test194(self):
        input = '0e1234'
        expect = '0e1234,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 194))

    def test195(self):
        input = '"\'"'
        expect = "\',<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 195))

    def test196(self):
        input = '""'
        expect = ',<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 196))

    def test197(self):
        input = '"'
        expect = 'Unclosed String: '
        self.assertTrue(TestLexer.test(input,expect, 197))

    def test198(self):
        input = r"""
                Illegal"\a"
            """
        expect =  r"""Illegal,Illegal Escape In String: \a"""
        self.assertTrue(TestLexer.test(input,expect, 198))

    def test199(self):
        input = 'writeInt(i,1);'
        expect = 'writeInt,(,i,,,1,),;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect, 199))

    def test200(self):
        """test identifiers"""
        input = '"This is a string ab \\t'
        expect = 'Unclosed String: This is a string ab \\t'
        self.assertTrue(TestLexer.test(input,expect, 100))