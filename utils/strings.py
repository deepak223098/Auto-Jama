"""
+------------------------------------------------------------------------------+
|                       Copyright 2017 Rockwell Collins                        |
|                             All Rights Reserved                              |
|                           Proprietary Information                            |
+------------------------------------------------------------------------------+

Utilities for interacting with strings
"""
from unicodedata import lookup


__version__ = '$Rev: 235184 $'

UNICODE_REPLACEMENTS = {
    lookup('NO-BREAK SPACE'): ' ',
    lookup('INVERTED EXCLAMATION MARK'): '!',
    lookup('COPYRIGHT SIGN'): '(c)',
    lookup('LEFT-POINTING DOUBLE ANGLE QUOTATION MARK'): '<<',
    lookup('RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK'): '>>',
    lookup('VULGAR FRACTION ONE QUARTER'): '1/4',
    lookup('VULGAR FRACTION ONE HALF'): '1/2',
    lookup('VULGAR FRACTION THREE QUARTERS'): '3/4',
    lookup('INVERTED QUESTION MARK'): '?',
    lookup('REGISTERED SIGN'): '(R)',
    lookup('PLUS-MINUS SIGN'): '+/-',
    lookup('MICRO SIGN'): 'u',
    lookup('MIDDLE DOT'): '.',
    lookup('DIVISION SIGN'): '/',
    lookup('MULTIPLICATION SIGN'): 'x',
    lookup('HYPHEN'): '-',
    lookup('NON-BREAKING HYPHEN'): '-',
    lookup('FIGURE DASH'): '-',
    lookup('EN DASH'): '-',
    lookup('EM DASH'): '-',
    lookup('HORIZONTAL BAR'): '-',
    lookup('DOUBLE VERTICAL LINE'): '||',
    lookup('LEFT SINGLE QUOTATION MARK'): '\'',
    lookup('RIGHT SINGLE QUOTATION MARK'): '\'',
    lookup('LEFT DOUBLE QUOTATION MARK'): '"',
    lookup('RIGHT DOUBLE QUOTATION MARK'): '"',
    lookup('RIGHT DOUBLE QUOTATION MARK'): '"',
    lookup('BULLET'): '.',
    lookup('ONE DOT LEADER'): '.',
    lookup('TWO DOT LEADER'): '..',
    lookup('HORIZONTAL ELLIPSIS'): '...',
    lookup('PRIME'): '\'',
    lookup('DOUBLE PRIME'): '\'\'',
    lookup('TRIPLE PRIME'): '\'\'\'',
    lookup('REVERSED PRIME'): '\'',
    lookup('REVERSED DOUBLE PRIME'): '\'\'',
    lookup('REVERSED TRIPLE PRIME'): '\'\'\'',
    lookup('CARET'): '^',
    lookup('SINGLE LEFT-POINTING ANGLE QUOTATION MARK'): '<',
    lookup('SINGLE RIGHT-POINTING ANGLE QUOTATION MARK'): '>',
    lookup('DOUBLE EXCLAMATION MARK'): '!!',
    lookup('INTERROBANG'): '!?',
    lookup('HYPHEN BULLET'): '-',
    lookup('FRACTION SLASH'): '/',
    lookup('DOUBLE QUESTION MARK'): '??',
    lookup('QUESTION EXCLAMATION MARK'): '?!',
    lookup('EXCLAMATION QUESTION MARK'): '!?',
    lookup('TRADE MARK SIGN'): 'tm',
    lookup('VULGAR FRACTION ONE SEVENTH'): '1/7',
    lookup('VULGAR FRACTION ONE NINTH'): '1/9',
    lookup('VULGAR FRACTION ONE TENTH'): '1/10',
    lookup('VULGAR FRACTION ONE THIRD'): '1/3',
    lookup('VULGAR FRACTION TWO THIRDS'): '2/3',
    lookup('VULGAR FRACTION ONE FIFTH'): '1/5',
    lookup('VULGAR FRACTION TWO FIFTHS'): '2/5',
    lookup('VULGAR FRACTION THREE FIFTHS'): '3/5',
    lookup('VULGAR FRACTION FOUR FIFTHS'): '4/5',
    lookup('VULGAR FRACTION ONE SIXTH'): '1/6',
    lookup('VULGAR FRACTION FIVE SIXTHS'): '5/6',
    lookup('VULGAR FRACTION ONE EIGHTH'): '1/8',
    lookup('VULGAR FRACTION THREE EIGHTHS'): '3/8',
    lookup('VULGAR FRACTION FIVE EIGHTHS'): '5/8',
    lookup('VULGAR FRACTION SEVEN EIGHTHS'): '7/8',
    lookup('FRACTION NUMERATOR ONE'): '1/',
    lookup('ROMAN NUMERAL ONE'): 'I',
    lookup('ROMAN NUMERAL TWO'): 'II',
    lookup('ROMAN NUMERAL THREE'): 'III',
    lookup('ROMAN NUMERAL FOUR'): 'IV',
    lookup('ROMAN NUMERAL FIVE'): 'V',
    lookup('ROMAN NUMERAL SIX'): 'VI',
    lookup('ROMAN NUMERAL SEVEN'): 'VII',
    lookup('ROMAN NUMERAL EIGHT'): 'VIII',
    lookup('ROMAN NUMERAL NINE'): 'IX',
    lookup('ROMAN NUMERAL TEN'): 'X',
    lookup('ROMAN NUMERAL ELEVEN'): 'XI',
    lookup('ROMAN NUMERAL TWELVE'): 'XII',
    lookup('ROMAN NUMERAL FIFTY'): 'L',
    lookup('ROMAN NUMERAL ONE HUNDRED'): 'C',
    lookup('ROMAN NUMERAL FIVE HUNDRED'): 'D',
    lookup('ROMAN NUMERAL ONE THOUSAND'): 'M',
    lookup('SMALL ROMAN NUMERAL ONE'): 'i',
    lookup('SMALL ROMAN NUMERAL TWO'): 'ii',
    lookup('SMALL ROMAN NUMERAL THREE'): 'iii',
    lookup('SMALL ROMAN NUMERAL FOUR'): 'iv',
    lookup('SMALL ROMAN NUMERAL FIVE'): 'v',
    lookup('SMALL ROMAN NUMERAL SIX'): 'vi',
    lookup('SMALL ROMAN NUMERAL SEVEN'): 'vii',
    lookup('SMALL ROMAN NUMERAL EIGHT'): 'viii',
    lookup('SMALL ROMAN NUMERAL NINE'): 'ix',
    lookup('SMALL ROMAN NUMERAL TEN'): 'x',
    lookup('SMALL ROMAN NUMERAL ELEVEN'): 'xi',
    lookup('SMALL ROMAN NUMERAL TWELVE'): 'xii',
    lookup('SMALL ROMAN NUMERAL FIFTY'): 'l',
    lookup('SMALL ROMAN NUMERAL ONE HUNDRED'): 'c',
    lookup('SMALL ROMAN NUMERAL FIVE HUNDRED'): 'd',
    lookup('SMALL ROMAN NUMERAL ONE THOUSAND'): 'm',
    lookup('LEFTWARDS ARROW'): '<-',
    lookup('RIGHTWARDS ARROW'): '->',
    lookup('LEFT RIGHT ARROW'): '<->',
    lookup('LEFTWARDS DOUBLE ARROW WITH STROKE'): '</=',
    lookup('LEFT RIGHT DOUBLE ARROW WITH STROKE'): '<=/=>',
    lookup('RIGHTWARDS DOUBLE ARROW WITH STROKE'): '=/>',
    lookup('LEFTWARDS DOUBLE ARROW'): '<=',
    lookup('RIGHTWARDS DOUBLE ARROW'): '=>',
    lookup('LEFTWARDS ARROW TO BAR'): '|<-',
    lookup('RIGHTWARDS ARROW TO BAR'): '->|',
    lookup('LEFTWARDS WHITE ARROW'): '<=',
    lookup('RIGHTWARDS WHITE ARROW'): '=>',
    lookup('LEFTWARDS OPEN-HEADED ARROW'): '<-',
    lookup('RIGHTWARDS OPEN-HEADED ARROW'): '->',
    lookup('LEFT RIGHT OPEN-HEADED ARROW'): '<->',
    lookup('MINUS SIGN'): '-',
    lookup('DIVISION SLASH'): '/',
    lookup('SET MINUS'): '\\',
    lookup('ASTERISK OPERATOR'): '*',
    lookup('BULLET OPERATOR'): '.',
    lookup('DIVIDES'): '|',
    lookup('PARALLEL TO'): '||',
    lookup('RATIO'): ':',
    lookup('PROPORTION'): '::',
    lookup('TILDE OPERATOR'): '~',
    lookup('REVERSED TILDE'): '~',
    lookup('SINE WAVE'): '~',
    lookup('NOT TILDE'): '/~',
    lookup('APPROXIMATELY EQUAL TO'): '~=',
    lookup('ALMOST EQUAL TO'): '~=',
    lookup('NOT EQUAL TO'): '/=',
    lookup('LESS-THAN OR EQUAL TO'): '<=',
    lookup('GREATER-THAN OR EQUAL TO'): '>=',
    lookup('NOT LESS-THAN'): '</',
    lookup('NOT GREATER-THAN'): '>/',
    lookup('NEITHER LESS-THAN NOR EQUAL TO'): '<=/',
    lookup('NEITHER GREATER-THAN NOR EQUAL TO'): '>=/',
    lookup('LESS-THAN OR EQUIVALENT TO'): '~<',
    lookup('GREATER-THAN OR EQUIVALENT TO'): '~>',
    lookup('DOT OPERATOR'): '.',
    lookup('STAR OPERATOR'): '*',
    lookup('MUCH LESS-THAN'): '<<',
    lookup('MUCH GREATER-THAN'): '>>',
    lookup('VERY MUCH LESS-THAN'): '<<<',
    lookup('VERY MUCH GREATER-THAN'): '>>>',
    lookup('WHITE BULLET'): '.',
    lookup('WHITE SMILING FACE'): ':)',
    lookup('WHITE FROWNING FACE'): ':(',
    lookup('WHITE HEART SUIT'): '<3',
    lookup('BLACK HEART SUIT'): '<3',
    lookup('HEAVY BLACK HEART'): '<3',
    lookup('LONG LEFTWARDS ARROW'): '<--',
    lookup('LONG RIGHTWARDS ARROW'): '-->',
    lookup('LONG LEFT RIGHT ARROW'): '<-->',
    lookup('LONG LEFTWARDS DOUBLE ARROW'): '<==',
    lookup('LONG RIGHTWARDS DOUBLE ARROW'): '==>',
    lookup('LONG LEFT RIGHT DOUBLE ARROW'): '<==>',
    lookup('LONG LEFTWARDS ARROW FROM BAR'): '<--|',
    lookup('LONG RIGHTWARDS ARROW FROM BAR'): '|-->',
    lookup('LONG LEFTWARDS DOUBLE ARROW FROM BAR'): '<==|',
    lookup('LONG RIGHTWARDS DOUBLE ARROW FROM BAR'): '|==>',
    lookup('LEFTWARDS DOUBLE DASH ARROW'): '<--',
    lookup('RIGHTWARDS DOUBLE DASH ARROW'): '-->',
    lookup('LEFTWARDS TRIPLE DASH ARROW'): '<---',
    lookup('RIGHTWARDS TRIPLE DASH ARROW'): '--->',
    lookup('SMALL EM DASH'): '-',
    lookup('FULLWIDTH EXCLAMATION MARK'): '!',
    lookup('FULLWIDTH QUOTATION MARK'): '"',
    lookup('FULLWIDTH NUMBER SIGN'): '#',
    lookup('FULLWIDTH DOLLAR SIGN'): '$',
    lookup('FULLWIDTH PERCENT SIGN'): '%',
    lookup('FULLWIDTH AMPERSAND'): '&',
    lookup('FULLWIDTH APOSTROPHE'): '\'',
    lookup('FULLWIDTH LEFT PARENTHESIS'): '(',
    lookup('FULLWIDTH RIGHT PARENTHESIS'): ')',
    lookup('FULLWIDTH ASTERISK'): '*',
    lookup('FULLWIDTH PLUS SIGN'): '+',
    lookup('FULLWIDTH COMMA'): ',',
    lookup('FULLWIDTH HYPHEN-MINUS'): '-',
    lookup('FULLWIDTH FULL STOP'): '.',
    lookup('FULLWIDTH SOLIDUS'): '/',
    lookup('FULLWIDTH DIGIT ZERO'): '0',
    lookup('FULLWIDTH DIGIT ONE'): '1',
    lookup('FULLWIDTH DIGIT TWO'): '2',
    lookup('FULLWIDTH DIGIT THREE'): '3',
    lookup('FULLWIDTH DIGIT FOUR'): '4',
    lookup('FULLWIDTH DIGIT FIVE'): '5',
    lookup('FULLWIDTH DIGIT SIX'): '6',
    lookup('FULLWIDTH DIGIT SEVEN'): '7',
    lookup('FULLWIDTH DIGIT EIGHT'): '8',
    lookup('FULLWIDTH DIGIT NINE'): '9',
    lookup('FULLWIDTH COLON'): ':',
    lookup('FULLWIDTH SEMICOLON'): ';',
    lookup('FULLWIDTH LESS-THAN SIGN'): '<',
    lookup('FULLWIDTH EQUALS SIGN'): '=',
    lookup('FULLWIDTH GREATER-THAN SIGN'): '>',
    lookup('FULLWIDTH QUESTION MARK'): '?',
    lookup('FULLWIDTH COMMERCIAL AT'): '@',
    lookup('FULLWIDTH LATIN CAPITAL LETTER A'): 'A',
    lookup('FULLWIDTH LATIN CAPITAL LETTER B'): 'B',
    lookup('FULLWIDTH LATIN CAPITAL LETTER C'): 'C',
    lookup('FULLWIDTH LATIN CAPITAL LETTER D'): 'D',
    lookup('FULLWIDTH LATIN CAPITAL LETTER E'): 'E',
    lookup('FULLWIDTH LATIN CAPITAL LETTER F'): 'F',
    lookup('FULLWIDTH LATIN CAPITAL LETTER G'): 'G',
    lookup('FULLWIDTH LATIN CAPITAL LETTER H'): 'H',
    lookup('FULLWIDTH LATIN CAPITAL LETTER I'): 'I',
    lookup('FULLWIDTH LATIN CAPITAL LETTER J'): 'J',
    lookup('FULLWIDTH LATIN CAPITAL LETTER K'): 'K',
    lookup('FULLWIDTH LATIN CAPITAL LETTER L'): 'L',
    lookup('FULLWIDTH LATIN CAPITAL LETTER M'): 'M',
    lookup('FULLWIDTH LATIN CAPITAL LETTER N'): 'N',
    lookup('FULLWIDTH LATIN CAPITAL LETTER O'): 'O',
    lookup('FULLWIDTH LATIN CAPITAL LETTER P'): 'P',
    lookup('FULLWIDTH LATIN CAPITAL LETTER Q'): 'Q',
    lookup('FULLWIDTH LATIN CAPITAL LETTER R'): 'R',
    lookup('FULLWIDTH LATIN CAPITAL LETTER S'): 'S',
    lookup('FULLWIDTH LATIN CAPITAL LETTER T'): 'T',
    lookup('FULLWIDTH LATIN CAPITAL LETTER U'): 'U',
    lookup('FULLWIDTH LATIN CAPITAL LETTER V'): 'V',
    lookup('FULLWIDTH LATIN CAPITAL LETTER W'): 'W',
    lookup('FULLWIDTH LATIN CAPITAL LETTER X'): 'X',
    lookup('FULLWIDTH LATIN CAPITAL LETTER Y'): 'Y',
    lookup('FULLWIDTH LATIN CAPITAL LETTER Z'): 'Z',
    lookup('FULLWIDTH LEFT SQUARE BRACKET'): '[',
    lookup('FULLWIDTH REVERSE SOLIDUS'): '\\',
    lookup('FULLWIDTH RIGHT SQUARE BRACKET'): ']',
    lookup('FULLWIDTH CIRCUMFLEX ACCENT'): '^',
    lookup('FULLWIDTH LOW LINE'): '_',
    lookup('FULLWIDTH GRAVE ACCENT'): '`',
    lookup('FULLWIDTH LATIN SMALL LETTER A'): 'a',
    lookup('FULLWIDTH LATIN SMALL LETTER B'): 'b',
    lookup('FULLWIDTH LATIN SMALL LETTER C'): 'c',
    lookup('FULLWIDTH LATIN SMALL LETTER D'): 'd',
    lookup('FULLWIDTH LATIN SMALL LETTER E'): 'e',
    lookup('FULLWIDTH LATIN SMALL LETTER F'): 'f',
    lookup('FULLWIDTH LATIN SMALL LETTER G'): 'g',
    lookup('FULLWIDTH LATIN SMALL LETTER H'): 'h',
    lookup('FULLWIDTH LATIN SMALL LETTER I'): 'i',
    lookup('FULLWIDTH LATIN SMALL LETTER J'): 'j',
    lookup('FULLWIDTH LATIN SMALL LETTER K'): 'k',
    lookup('FULLWIDTH LATIN SMALL LETTER L'): 'l',
    lookup('FULLWIDTH LATIN SMALL LETTER M'): 'm',
    lookup('FULLWIDTH LATIN SMALL LETTER N'): 'n',
    lookup('FULLWIDTH LATIN SMALL LETTER O'): 'o',
    lookup('FULLWIDTH LATIN SMALL LETTER P'): 'p',
    lookup('FULLWIDTH LATIN SMALL LETTER Q'): 'q',
    lookup('FULLWIDTH LATIN SMALL LETTER R'): 'r',
    lookup('FULLWIDTH LATIN SMALL LETTER S'): 's',
    lookup('FULLWIDTH LATIN SMALL LETTER T'): 't',
    lookup('FULLWIDTH LATIN SMALL LETTER U'): 'u',
    lookup('FULLWIDTH LATIN SMALL LETTER V'): 'v',
    lookup('FULLWIDTH LATIN SMALL LETTER W'): 'w',
    lookup('FULLWIDTH LATIN SMALL LETTER X'): 'x',
    lookup('FULLWIDTH LATIN SMALL LETTER Y'): 'y',
    lookup('FULLWIDTH LATIN SMALL LETTER Z'): 'z',
    lookup('FULLWIDTH LEFT CURLY BRACKET'): '{',
    lookup('FULLWIDTH VERTICAL LINE'): '|',
    lookup('FULLWIDTH RIGHT CURLY BRACKET'): '}',
    lookup('FULLWIDTH TILDE'): '~'
}


def plainstr(s):
    """
    Converts a string to a plain ASCII bytestring.

    :param s: string to convert
    :type  s: basestring
    :return: plain ASCII string
    :rtype: str
    """
    if isinstance(s, unicode):
        # convert unicode to ASCII
        new_str = ''
        for i, ch in enumerate(s):
            ch = UNICODE_REPLACEMENTS.get(ch, ch)
            new_str += ch

        s = new_str

    try:
        return str(s)

    except UnicodeEncodeError:
        return unicode(s).encode('unicode_escape')
