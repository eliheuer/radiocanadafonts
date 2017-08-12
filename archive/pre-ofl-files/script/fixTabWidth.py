tablist = [".notdef", "asciicircum", "asciitilde", "bulletoperator", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "plus", "minus", "plusminus", "equal", "notequal", "approxequal", "multiply", "less", "greater", "lessequal", "greaterequal", "divide", "logicalnot", "Euro", "currency", "dollar", "cent", "florin", "sterling", "yen", "space.tab", "period.tab", "comma.tab", "colon.tab", "semicolon.tab"]

tabwidth = 500

font = CurrentFont()

for glyphname in tablist:
    
    glyph = font[glyphname]
    width = int(round(glyph.width))
    
    if width !=tabwidth:
        print width, tabwidth, glyph
        d = tabwidth-width
        glyph.move((d/2, 0))
        glyph.width = tabwidth
        glyph.update()
    glyph.mark = (1.0, 0.4, 1.0, 1.0)
        