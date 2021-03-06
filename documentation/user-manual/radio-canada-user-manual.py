# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# Note: Run this script from the project root directory with DrawBot installed in editable mode.
# Note: e.g. $ python3 documentation/slide-decks/final-project-presentation/final-project-presentation.py
# Typeface Used: https://input.fontbureau.com
# Unit Space: 72dpi (dots per inch)
from drawBot import *
from datetime import date
import math

# CONSTANTS
W = 792  # Width
H = 612  # Height
M = 36    # Margin
U = 18    # Unit
TODAY = str(date.today())
ROMAN_FONT = "fonts/variable/Radio-Canada[wdth,wght].ttf"
ITALIC_FONT = "fonts/variable/Radio-Canada-Italic[wdth,wght].ttf"
GF_PLUS = '''! " # $ % & ' ( ) * + , - . 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~ ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ ® ¯ ° ± ² ³ ´ µ ¶ · ¸ ¹ º » ¼ ½ ¾ ¿ À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ ı Œ œ – — ‘ ’ ‚ “ ” „ • … ‹ › ⁴ € − Ā ā Ă ă Ą ą Ć ć Ĉ ĉ Ċ ċ Č č Ď ď Đ đ Ē ē Ĕ ĕ Ė ė Ę ę Ě ě Ĝ ĝ Ğ ğ Ġ ġ Ģ ģ Ĥ ĥ Ħ ħ Ĩ ĩ Ī ī Ĭ ĭ Į į İ Ĵ ĵ Ķ ķ ĸ Ĺ ĺ Ļ ļ Ľ ľ Ŀ ŀ Ł ł Ń ń Ņ ņ Ň ň Ŋ ŋ Ō ō Ŏ ŏ Ő ő Ŕ ŕ Ŗ ŗ Ř ř Ś ś Ŝ ŝ Ş ş Š š Ţ ţ Ť ť Ŧ ŧ Ũ ũ Ū ū Ŭ ŭ Ů ů Ű ű Ų ų Ŵ ŵ Ŷ ŷ Ÿ Ź ź Ż ż Ž ž Ə ƒ Ơ ơ Ư ư Ǆ ǅ ǆ Ǉ ǈ ǉ Ǌ ǋ ǌ Ǧ ǧ Ǫ ǫ Ǻ ǻ Ǽ ǽ Ǿ ǿ Ȁ ȁ Ȃ ȃ Ȅ ȅ Ȇ ȇ Ȉ ȉ Ȋ ȋ 
Ȍ ȍ Ȏ ȏ Ȑ ȑ Ȓ ȓ Ȕ ȕ Ȗ ȗ Ș ș Ț ț Ȫ ȫ Ȭ ȭ Ȱ ȱ Ȳ ȳ ȷ ə ʹ ʺ ʼ Ẁ ẁ Ẃ ẃ Ẅ ẅ ẞ Ạ ạ Ả ả Ấ ấ Ầ ầ Ẩ ẩ Ẫ ẫ Ậ ậ Ắ ắ Ằ ằ Ẳ ẳ Ẵ ẵ Ặ ặ Ẹ ẹ Ẻ ẻ Ẽ ẽ Ế ế Ề ề Ể ể Ễ ễ Ệ ệ Ỉ ỉ Ị ị Ọ ọ Ỏ ỏ Ố ố Ồ ồ Ổ ổ Ỗ ỗ Ộ ộ Ớ ớ Ờ ờ Ở ở Ỡ ỡ Ợ ợ Ụ ụ Ủ ủ Ứ ứ Ừ ừ Ử ử Ữ ữ Ự ự Ỳ ỳ Ỵ ỵ Ỷ ỷ Ỹ ỹ ‐ † ‡ ‰ ′ ″ ⁒ ₡ ₣ ₤ ₦ ₧ ₩ ₫ ₭ ₱ ₲ ₵ ₹ ₺ ₼ ₽ № ™ ∙ ≈ ≠ ≤ ≥ ⟨ ⟩ ﬁ ﬂ
'''
RC_TEXT_ONE = '''
Ici Radio-Canada Télé (stylized as ICI Radio-Canada TēLē, and formerly known as Télévision de Radio-Canada) is a Canadian French-language free-to-air television network owned by the Canadian Broadcasting Corporation (known in French as Société Radio-Canada), the national public broadcaster. It is the French-language counterpart of CBC Television, the broadcaster's English-language television network.

Its headquarters are at Maison Radio-Canada in Montreal, which is also home to the network's flagship station, CBFT-DT. Until the 2012 closedown of the CBC / Radio-Canada rebroadcaster network, it was the only francophone network in Canada to broadcast terrestrially in all Canadian provinces.
'''
RC_TEXT_TWO = '''
Ici Radio-Canada Télé (stylized as ICI Radio-Canada TēLē, and formerly known as Télévision de Radio-Canada) is a Canadian French-language free-to-air television network owned by the Canadian Broadcasting Corporation (known in French as Société Radio-Canada), the national public broadcaster. It is the French-language counterpart of CBC Television, the broadcaster's English-language television network.
'''
LANGUAGE_SUPPORT = '''
Arbëreshë Albanian, Eastern Abnaki, Afar, Arvanitika Albanian, Western Abnaki, Achinese, Achuar-Shiwiar, Acheron, Eastern Arrernte, Afrikaans, Aguaruna, Gheg Albanian, Tosk Albanian, Amahuaca, Yanesha', Amis, Amarakaeri, Uab Meto, Aragonese, Mapudungun, Asu (Tanzania), Waorani, Anuta, Southern Aymara, Central Aymara, South Azerbaijani, North Azerbaijani, Bemba (Zambia), Bena (Tanzania), Bari, Bikol, Bini, Bislama, Bosnian, Breton, Garifuna, Kaqchikel, Catalan, Chachi, Chavacano, Cashibo-Cacataibo, Cashinahua, Candoshi-Shapra, Cebuano, Czech, Chiga, Chamorro, Ojitlán Chinantec, Chuukese, Cimbrian, Chokwe, Central Kurdish, Asháninka, Montenegrin, Cofán, Cornish, Corsican, Caquinte, Pichis Ashéninka, Crimean Tatar, Seselwa Creole French, Chiltepec Chinantec, Kashubian, Tedim Chin, Welsh, Danish, Taita, German, Andaandi, Dongolawi, Dehu, Dimli, Lower Sorbian, Jola-Fonyi, Embu, Standard Estonian, English, Ese Ejja, Basque, Faroese, Nobiin, Fijian, Filipino, Finnish, Kven Finnish, French, Western Frisian, Friulian, Gagauz, Borana-Arsi-Guji Oromo, West Central Oromo, Guadeloupean Creole French, Gilbertese, Scottish Gaelic, Irish, Galician, Manx, Gooniyandi, Ga’anda, Swiss German, Wayuu, Gusii, Gwichʼin, Eastern Oromo, Haitian, Hawaiian, Northern Qiandong Miao, Hiligaynon, Southern Qiandong Miao, Hani, Caribbean Hindustani, Hopi, Croatian, Upper Sorbian, Hungarian, Huastec, Iloko, Indonesian, Icelandic, Italian, Jamaican Creole English, Javanese, Shuar, Japanese (Rōmaji), Kalaallisut, Kamba (Kenya), Makonde, Kabuverdianu, Kekchí, Kaingang, Khasi, Koyra Chiini Songhay, Kikuyu, Kinyarwanda, Kirmanjki, Kalenjin, Kimbundu, Northern Kurdish, Kongo, Konzo, Kaonde, Karelian, Shambala, Kölsch, Kituba (DRC), Kuanyama, Ladino, Latin, Ligurian, Lithuanian, Ladin, Lombard, Otuho, Lozi, Latgalian, Luxembourgish, Luba-Lulua, Ganda, Luo (Kenya and Tanzania), Standard Latvian, Matsés, Meru, Mauritian Creole, Makhuwa-Meetto, Minangkabau, Mískito, Malagasy, Maltese, Montagnais, Mohawk, Maori, Totontepec Mixe, Creek, Murrinh-Patha, Mirandese, Kala Lagaw Ya, Ixcatlán Mazatec, Naga Pidgin, Neapolitan, Navajo, South Ndebele, North Ndebele, Ndonga, Low German, Central Nahuatl, Niuean, Ao Naga, Dutch, Norwegian, Nomatsiguenga, Pedi, Nyanja, Nyankole, Occitan, Northwestern Ojibwa, Orma, Oroqen, Mezquital Otomi, Pampanga, Papiamento, Palauan, Páez, Picard, Pijin, Pintupi-Luritja, Paluan, Piemontese, Polish, Pohnpeian, Portuguese, Potawatomi, Upper Guinea Crioulo, Pipil, Ashéninka Perené, K'iche', Quechua, Cook Islands Māori, Romansh, Romanian, Rotokas, Rundi, Istro Romanian, Macedo-Romanian, Rwa, Sango, Samburu, Sangu (Tanzania), Sicilian, Sena, Seri, Koyraboro Senni Songhai, Secoya, Shipibo-Conibo, Pite Sami, Ume Sami, Shawnee, Slovak, Slovenian, Southern Sami, Northern Sami, Lule Sami, Inari Sami, Samoan, Shona, Soninke, Somali, Southern Sotho, Spanish, Sardinian, Saramaccan, Sranan Tongo, Swati, Sundanese, Maore Comorian, Congo Swahili, Swedish, Swahili, Silesian, Tahitian, Atayal, Tetun Dili, Teso, Tetum, Tagalog, Tiv, Tokelau, Tsakhur, Talysh, Toba, Tonga (Zambia), Tonga (Tonga Islands), Papantla Totonac, Tok Pisin, Tswana, Tsonga, Purepecha, Muslim Tat, Turkmen, Tumbuka, Turkish, Tasawaq, Tzeltal, Tzotzil, Meriam Mir, Umbundu, Munsee, Northern Uzbek, Venetian, Veps, Vietnamese, Makhuwa, Võro, Walser, Waray (Philippines), Warlpiri, Wik-Mungkan, Ho-Chunk, Walloon, Mwani, Wolof, Wiradjuri, Wangaaybuwan-Ngiyambaa, Xavánte, Xhosa, Kenzi, Mattokki, Soga, Yao, Yapese, Yindjibarndi, Makwe, Yucateco, Zapotec, Ngazidja Comorian, Malaysian, Záparo, Standard Malay, Zulu, Zuni
'''
INTRO = '''
In early 2017, work started on a custom typeface for use by CBC/Radio-Canada. In 2021 this typeface was expanded to cover a wider range of weights, plus roman and italic variable fonts. The expanded character set developed in 2021 increased the number of supported languages using the Latin script from 106 to 317, and the original glyph count of 490 has been expanded to 679.

In 2021, extensive work was done organizing the upstream Git repository, improving the way marks are handled, adding currency and other symbols to cover the Google Fonts Latin Plus character set, and drawing missing condensed light source files for both the roman and italic.

If you have any issues with, or questions about this variable font project, please leave an issue in the upstream Git repository. Pull requests are welcome, just remember to check your work in the proofs if you are adjusting the drawing and spacing.

—Eli Heuer
'''

# Draws a Grid
def grid():
    strokeWidth(1)
    stroke(0.9)
    step_X = 0
    step_Y = 0
    increment_X = U
    increment_Y = U
    for x in range(40):
        polygon( (M+step_X, M), (M+step_X, H-M) )
        step_X += increment_X
    for y in range(30):
        polygon( (M, M+step_Y), (W-M, M+step_Y) )
        step_Y += increment_Y
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# Draw page info
def draw_page_info(page_number):
    fill(0)
    stroke(0)
    strokeWidth(1)
    line((M, H - M - U), (W - M, H - M - U))
    line((M, M), (W - M, M))
    font("InputMonoCompressed-Regular")
    stroke(None)
    fontSize(13)
    text(str(int(page_number)), (M, (U*31)+3))
    text("Radio-Canada Variable Font v1.400", (M+(U*10), (U*31)+3))
    text(TODAY, (M+(U*25), (U*31)+3))
    text("Font Engineer: Eli Heuer", (M+(U*30.8), (U*31)+3))

# New Page
def new_page():
    newPage(W, H)
    fill(1)
    rect(-2, -2, W+2, H+2)

# START DRAWBOT
newDrawing()

# TEST FONTS
font(ROMAN_FONT)
for axis, data in listFontVariations().items():
    print((axis, data))
# for eachFontName in installedFonts():
#    print(eachFontName)

page_number = 0

new_page() #--------------------------------------------------#
# Cover Page
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(None)
stroke(0)
strokeWidth(1)
rect(M+U*10, M+U*8, M+(U*18), M+(U*10))
oval(M+U*9.5, M+U*19.5, U, U)
oval(M+U*19.5, M+U*19.5, U, U)
oval(M+U*29.5, M+U*19.5, U, U)
oval(M+U*9.5, M+U*7.5, U, U)
oval(M+U*19.5, M+U*7.5, U, U)
oval(M+U*29.5, M+U*7.5, U, U)
fill(0)
oval(M+U*9.75, M+U*19.75, U/2, U/2)
oval(M+U*19.75, M+U*19.75, U/2, U/2)
oval(M+U*29.75, M+U*19.75, U/2, U/2)
oval(M+U*9.75, M+U*7.75, U/2, U/2)
oval(M+U*19.75, M+U*7.75, U/2, U/2)
oval(M+U*29.75, M+U*7.75, U/2, U/2)
stroke(None)
fontSize(50)
font(ROMAN_FONT)
fontVariations(wght = 300 )
fontVariations(wdth = 100 )
text("Aa",  (M+U*11, M+U*17))
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
text("Aa",  (M+U*18.3, M+U*17))
fontVariations(wght = 700 )
fontVariations(wdth = 100 )
text("Aa",  (M+U*25.8, M+U*17))
fontVariations(wght = 300 )
fontVariations(wdth = 75 )
text("Aa",  (M+U*11, M+U*9))
fontVariations(wght = 400 )
fontVariations(wdth = 75 )
text("Aa",  (M+U*18.5, M+U*9))
fontVariations(wght = 700 )
fontVariations(wdth = 75 )
text("Aa",  (M+U*26.3, M+U*9))
stroke(None)
fill(0)
fontSize(50)
font(ROMAN_FONT)
fontVariations(wght = 700 )
fontVariations(wdth = 100 )
text("Radio-Canada",  (M, (U*28)))
fontSize(25)
font(ITALIC_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
text("Variable Font User Manual",  (M, M+3))


new_page() #--------------------------------------------------#
# Intro
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("Introduction", (M, U*29))
text("Font Engineering Notes", (M, U*28))
text("12/18pt Roman", (M, U*26))
text("Weight Axis: 400", (M, U*25))
text("Width Axis:  100", (M, U*24))
stroke(None)
fill(0)
fontSize(12)
font(ROMAN_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
lineHeight(12.0*1.5)
textBox(INTRO, (M+(U*10), M, U*19, U*28.7))


new_page() #--------------------------------------------------#
# Designspace
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(None)
font("InputMonoCompressed-Regular")
fontSize(13)
text("Radio-Canada Roman", (M, U*28))
text("File Name: Radio-Canada[wdth,wght].ttf", (M, U*27))
text("File Size: 164k", (M, U*26))
text("Width Axis [wdth]", (M, U*24))
text("Range: 100-75", (M, U*23))
text("Weight Axis [wght]", (M, U*21))
text("Range: 300-700", (M, U*20))

text("Radio-Canada Italic", (M, U*6))
text("File Name: Radio-Canada-Italic[wdth,wght].ttf", (M, U*5))
text("File Size: 147k", (M, U*4))
text("Width Axis [wdth]", (M, U*9))
text("Range: 100-75", (M, U*8))
text("Weight Axis [wght]", (M, U*12))
text("Range: 300-700", (M, U*11))

fill(None)
stroke(0)
strokeWidth(1)

rect(M+U*20, M+U*17, M+(U*16), M+(U*8))
rect(M+U*20, M+U*2, M+(U*16), M+(U*8))

polygon((M+U*7, M+U*22), (M+U*19, M+U*22), close=False)
polygon((M+U*19.5, M+U*17), (M+U*19, M+U*17), (M+U*19, M+U*27), (M+U*19.5, M+U*27), close=False)
polygon((M+U*7, M+U*7), (M+U*19, M+U*7), close=False)
polygon((M+U*19.5, M+U*2), (M+U*19, M+U*2), (M+U*19, M+U*12), (M+U*19.5, M+U*12), close=False)

polygon((M+U*7, M+U*10), (M+U*10, M+U*10), (M+U*10, M+U*14), (M+U*29, M+U*14), (M+U*29, M+U*13), close=False)
polygon((M+U*20, M+U*12.5), (M+U*20, M+U*13), (M+U*38, M+U*13), (M+U*38, M+U*12.5), close=False)

polygon((M+U*7, M+U*19), (M+U*10, M+U*19), (M+U*10, M+U*15), (M+U*29, M+U*15), (M+U*29, M+U*16),  close=False)
polygon((M+U*20, M+U*16.5), (M+U*20, M+U*16), (M+U*38, M+U*16), (M+U*38, M+U*16.5), close=False)

fill(0)
oval(M+U*19.75, M+U*16.75, U/2, U/2)
oval(M+U*28.75, M+U*16.75, U/2, U/2)
oval(M+U*37.75, M+U*16.75, U/2, U/2)
oval(M+U*19.75, M+U*26.75, U/2, U/2)
oval(M+U*28.75, M+U*26.75, U/2, U/2)
oval(M+U*37.75, M+U*26.75, U/2, U/2)

oval(M+U*19.75, M+U*1.75, U/2, U/2)
oval(M+U*28.75, M+U*1.75, U/2, U/2)
oval(M+U*37.75, M+U*1.75, U/2, U/2)
oval(M+U*19.75, M+U*11.75, U/2, U/2)
oval(M+U*28.75, M+U*11.75, U/2, U/2)
oval(M+U*37.75, M+U*11.75, U/2, U/2)
fill(None)

stroke(None)
fontSize(50)
font(ROMAN_FONT)
fill(0)
space = 21
e_wght = 300
fontVariations(wdth = 100 )
for i in range(8):
    fontVariations(wght = e_wght )
    text("e",  (M+U*space, M+U*24))
    space += 2.05
    e_wght += 100
space = 21
e_wght = 300
fontVariations(wdth = 100-(6.25*1) )
for i in range(8):
    fontVariations(wght = e_wght )
    text("e",  (M+U*space, M+U*22))
    space += 2.061
    e_wght += 100
space = 21
e_wght = 300
fontVariations(wdth = 100-(6.25*2) )
for i in range(8):
    fontVariations(wght = e_wght )
    text("e",  (M+U*space, M+U*20))
    space += 2.073
    e_wght += 100
space = 21
e_wght = 300
fontVariations(wdth = 75 )
for i in range(8):
    fontVariations(wght = e_wght )
    text("e",  (M+U*space, M+U*18))
    space += 2.085
    e_wght += 100

stroke(None)
fontSize(50)
font(ITALIC_FONT)
fill(0)
space = 21
e_wght = 300
fontVariations(wdth = 100 )
for i in range(8):
    fontVariations(wght = e_wght )
    text("e",  (M+U*space, M+U*9))
    space += 2.05
    e_wght += 100
space = 21
e_wght = 300
fontVariations(wdth = 100-(6.25*1) )
for i in range(8):
    fontVariations(wght = e_wght )
    text("e",  (M+U*space, M+U*7))
    space += 2.061
    e_wght += 100
space = 21
e_wght = 300
fontVariations(wdth = 100-(6.25*2) )
for i in range(8):
    fontVariations(wght = e_wght )
    text("e",  (M+U*space, M+U*5))
    space += 2.073
    e_wght += 100
space = 21
e_wght = 300
fontVariations(wdth = 75 )
for i in range(8):
    fontVariations(wght = e_wght )
    text("e",  (M+U*space, M+U*3))
    space += 2.085
    e_wght += 100

new_page() #--------------------------------------------------#
# Weight Axis
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(None)
font("InputMonoCompressed-Regular")
fontSize(13)
text("32pt", (M, U*29))
text("Weight Range", (M, U*28))
text("700-300", (M, U*27))
step = 29
wght_value = 700
for i in range(14):
    text(str(int(wght_value)), (M+(U*8.5), U*step))
    text(str(int(wght_value)), (M+(U*23.5), U*step))
    wght_value -= 31
    if wght_value <= 300: wght_value = 300
    step -= 2
font(ROMAN_FONT)
fontSize(32)
fontVariations(wdth = 100 )
wght_value = 700
x_pos = 10
y_pos = 29
for i in range(14):
    fontVariations(wght = wght_value)
    text("Radio-Canada", (M+(U*x_pos), U*y_pos))
    wght_value -= 31
    y_pos -= 2
font(ITALIC_FONT)
fontSize(32)
fontVariations(wdth = 100 )
wght_value = 700
x_pos = 25
y_pos = 29
for x in range(14):
    fontVariations(wght = wght_value)
    text("Radio-Canada", (M+(U*x_pos), U*y_pos))
    wght_value -= 31
    y_pos -= 2

new_page() #--------------------------------------------------#
# Width Axis
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(None)
font("InputMonoCompressed-Regular")
fontSize(13)
text("32pt", (M, U*29))
text("Width Range", (M, U*28))
text("100-75", (M, U*27))
step = 29
wdth_value = 100
for i in range(14):
    text(str(int(wdth_value)), (M+(U*8.5), U*step))
    text(str(int(wdth_value)), (M+(U*23.5), U*step))
    wdth_value -= 2
    if wdth_value <= 75: wdth_value = 75
    step -= 2
font(ROMAN_FONT)
fontSize(32)
fontVariations(wght = 500 )
wdth_value = 100
x_pos = 10
y_pos = 29
for i in range(14):
    fontVariations(wdth = wdth_value)
    text("Radio-Canada", (M+(U*x_pos), U*y_pos))
    wdth_value -= 2
    y_pos -= 2
font(ITALIC_FONT)
fontSize(32)
fontVariations(wght = 500 )
wdth_value = 100
x_pos = 25
y_pos = 29
for x in range(14):
    fontVariations(wdth = wdth_value)
    text("Radio-Canada", (M+(U*x_pos), U*y_pos))
    wdth_value -= 2
    y_pos -= 2

new_page() #--------------------------------------------------#
# Glyph Count
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("Partial Character Set", (M, U*29))
text("Google Fonts Latin Plus", (M, U*28))
text("Glyph Count: 697", (M, U*26))
stroke(None)
fill(0)
fontSize(18)
font(ROMAN_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
lineHeight(30)
textBox(GF_PLUS, (M+(U*10), M, U*30, (U*28)+4))


new_page() #--------------------------------------------------#
# Language Support
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(None)
font("InputMonoCompressed-Regular")
fontSize(13)
text("Language Support", (M, U*29))
text("317 Languages", (M, U*28))
text("*Approximate", (M, U*27))
text("*Source: Hyperglot CLI", (M, U*3))
font(ROMAN_FONT)
fontSize(10)
lineHeight(14.6)
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
textBox(LANGUAGE_SUPPORT, (M+(U*10), M, U*30, (U*28)+7))


new_page() #--------------------------------------------------#
#Text-Example-One
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12/18pt Roman", (M, (U*29)))
text("Weight Axis: 400", (M, (U*28)))
text("Width Axis:  100", (M, (U*27)))
text("12/18pt Italic", (M, (U*15)))
text("Weight Axis: 400", (M, (U*14)))
text("Width Axis:  100", (M, (U*13)))
stroke(None)
fill(0)
fontSize(12)
lineHeight(18)
font(ROMAN_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+13, U*20, U*13))
font(ITALIC_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+13, U*20, U*13))


new_page() #--------------------------------------------------#
#Text-Example-Two
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12/18pt Roman", (M, (U*29)))
text("Weight Axis: 700", (M, (U*28)))
text("Width Axis:  100", (M, (U*27)))
text("12/18pt Italic", (M, (U*15)))
text("Weight Axis: 700", (M, (U*14)))
text("Width Axis:  100", (M, (U*13)))
stroke(None)
fill(0)
fontSize(12)
lineHeight(18)
font(ROMAN_FONT)
fontVariations(wght = 700 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+13, U*20, U*13))
font(ITALIC_FONT)
fontVariations(wght = 700 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+13, U*20, U*13))


new_page() #--------------------------------------------------#
#Text-Example-Three
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12/18pt Roman", (M, (U*29)))
text("Weight Axis: 300", (M, (U*28)))
text("Width Axis:  100", (M, (U*27)))
text("12/18pt Italic", (M, (U*15)))
text("Weight Axis: 300", (M, (U*14)))
text("Width Axis:  100", (M, (U*13)))
stroke(None)
fill(0)
fontSize(12)
lineHeight(18)
font(ROMAN_FONT)
fontVariations(wght = 300 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+13, U*20, U*13))
font(ITALIC_FONT)
fontVariations(wght = 300 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+13, U*20, U*13))


new_page() #--------------------------------------------------#
#Text-Example-Four
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12/18pt Roman", (M, (U*29)))
text("Weight Axis: 400", (M, (U*28)))
text("Width Axis:  75", (M, (U*27)))
text("12/18pt Italic", (M, (U*15)))
text("Weight Axis: 400", (M, (U*14)))
text("Width Axis:  75", (M, (U*13)))
stroke(None)
fill(0)
fontSize(12)
lineHeight(18)
font(ROMAN_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+13, U*20, U*13))
font(ITALIC_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+13, U*20, U*13))


new_page() #--------------------------------------------------#
#Text-Example-Five
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12/18pt Roman", (M, (U*29)))
text("Weight Axis: 700", (M, (U*28)))
text("Width Axis:  75", (M, (U*27)))
text("12/18pt Italic", (M, (U*15)))
text("Weight Axis: 700", (M, (U*14)))
text("Width Axis:  75", (M, (U*13)))
stroke(None)
fill(0)
fontSize(12)
lineHeight(18)
font(ROMAN_FONT)
fontVariations(wght = 700 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+13, U*20, U*13))
font(ITALIC_FONT)
fontVariations(wght = 700 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+13, U*20, U*13))


new_page() #--------------------------------------------------#
#Text-Example-Six
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("12/18pt Roman", (M, (U*29)))
text("Weight Axis: 300", (M, (U*28)))
text("Width Axis:  75", (M, (U*27)))
text("12/18pt Italic", (M, (U*15)))
text("Weight Axis: 300", (M, (U*14)))
text("Width Axis:  75", (M, (U*13)))
stroke(None)
fill(0)
fontSize(12)
lineHeight(18)
font(ROMAN_FONT)
fontVariations(wght = 300 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+13, U*20, U*13))
font(ITALIC_FONT)
fontVariations(wght = 300 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+13, U*20, U*13))


new_page() #--------------------------------------------------#
#18pt-Text-Example-One
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("18/24pt Roman", (M, (U*29)))
text("Weight Axis: 400", (M, (U*28)))
text("Width Axis:  100", (M, (U*27)))
text("18/24pt Italic", (M, (U*15)))
text("Weight Axis: 400", (M, (U*14)))
text("Width Axis:  100", (M, (U*13)))
stroke(None)
fill(0)
fontSize(18)
lineHeight(24)
font(ROMAN_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+25, U*29, U*13))
font(ITALIC_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+25, U*29, U*13))


new_page() #--------------------------------------------------#
#18pt-Text-Example-Two
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("18/24pt Roman", (M, (U*29)))
text("Weight Axis: 700", (M, (U*28)))
text("Width Axis:  100", (M, (U*27)))
text("18/24pt Italic", (M, (U*15)))
text("Weight Axis: 700", (M, (U*14)))
text("Width Axis:  100", (M, (U*13)))
stroke(None)
fill(0)
fontSize(18)
lineHeight(24)
font(ROMAN_FONT)
fontVariations(wght = 700 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+25, U*29, U*13))
font(ITALIC_FONT)
fontVariations(wght = 700 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+25, U*29, U*13))


new_page() #--------------------------------------------------#
#18pt-Text-Example-Three
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("18/24pt Roman", (M, (U*29)))
text("Weight Axis: 300", (M, (U*28)))
text("Width Axis:  100", (M, (U*27)))
text("18/24pt Italic", (M, (U*15)))
text("Weight Axis: 300", (M, (U*14)))
text("Width Axis:  100", (M, (U*13)))
stroke(None)
fill(0)
fontSize(18)
lineHeight(24)
font(ROMAN_FONT)
fontVariations(wght = 300 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+25, U*29, U*13))
font(ITALIC_FONT)
fontVariations(wght = 300 )
fontVariations(wdth = 100 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+25, U*29, U*13))


new_page() #--------------------------------------------------#
#18pt-Text-Example-Four
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("18/24pt Roman", (M, (U*29)))
text("Weight Axis: 400", (M, (U*28)))
text("Width Axis:  75", (M, (U*27)))
text("18/24pt Italic", (M, (U*15)))
text("Weight Axis: 400", (M, (U*14)))
text("Width Axis:  75", (M, (U*13)))
stroke(None)
fill(0)
fontSize(18)
lineHeight(24)
font(ROMAN_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+25, U*29, U*13))
font(ITALIC_FONT)
fontVariations(wght = 400 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+25, U*29, U*13))


new_page() #--------------------------------------------------#
#18pt-Text-Example-Five
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("18/24pt Roman", (M, (U*29)))
text("Weight Axis: 700", (M, (U*28)))
text("Width Axis:  75", (M, (U*27)))
text("18/24pt Italic", (M, (U*15)))
text("Weight Axis: 700", (M, (U*14)))
text("Width Axis:  75", (M, (U*13)))
stroke(None)
fill(0)
fontSize(18)
lineHeight(24)
font(ROMAN_FONT)
fontVariations(wght = 700 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+25, U*29, U*13))
font(ITALIC_FONT)
fontVariations(wght = 700 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+25, U*29, U*13))


new_page() #--------------------------------------------------#
#18pt-Text-Example-Three
#grid() # toggle for grid view
page_number += 1
draw_page_info(page_number)
fill(0)
stroke(0)
strokeWidth(1)
line((M, H - M - U*15), (W - M, H - M - U*15))
fill(0)
font("InputMonoCompressed-Regular")
stroke(None)
fontSize(13)
text("18/24pt Roman", (M, (U*29)))
text("Weight Axis: 300", (M, (U*28)))
text("Width Axis:  75", (M, (U*27)))
text("18/24pt Italic", (M, (U*15)))
text("Weight Axis: 300", (M, (U*14)))
text("Width Axis:  75", (M, (U*13)))
stroke(None)
fill(0)
fontSize(18)
lineHeight(24)
font(ROMAN_FONT)
fontVariations(wght = 300 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*15)+25, U*29, U*13))
font(ITALIC_FONT)
fontVariations(wght = 300 )
fontVariations(wdth = 75 )
textBox(RC_TEXT_ONE, (M+(U*10), M+(U*1)+25, U*29, U*13))

# Saving and post-processing
saveImage("documentation/user-manual/radio-canada-user-manual.pdf")
print("Updated user manual")
