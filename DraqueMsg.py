from pygame_functions import *

# 定数
SCREEN_X = 1200
SCREEN_Y = 800
FONT_SIZE = 30
FONT_COLOR = "white"
FONT_FILE = "fonts/DragonQuestFCIntact.ttf"
BG_COLOR = "black"
BGM = makeSound("sounds/battle.ogg")
SOUND = makeSound("sounds/pi.ogg")
KOIKE_IMAGE = "images/koike.png"
HIKAKIN_IMAGE = "images/hikakin.png"
MESSAGE_SIZE = 40
MESSAGE_COLOR = "green"

WAKU_KADO_1 = "＆"
WAKU_KADO_2 = "’"
WAKU_KADO_3 = "）"
WAKU_KADO_4 = "（"
WAKU_YOKO_1 = "＃"
WAKU_YOKO_2 = "％"
WAKU_TATE_1 = "”"
WAKU_TATE_2 = "＄"
WAKU_SPACE = "　"

screen = screenSize(SCREEN_X, SCREEN_Y)

def draw_status():
    str_status = "＆＃＃＝こいけゆ＃＃＃’＆＃＃＃＃＃＃＃＃＃＃’<br>"\
                "”　　　　　　　　　　＄”　　　　　　　　　　＄<br>"\
                "”　とうきょうとちじ　＄”　　　ちから：２５５＄<br>"\
                "”　　　＜　　　　　　＄”　　　＜　　　　　　＄<br>"\
                "”　せいへつ：おんな　＄”　　すはやさ：１３２＄<br>"\
                "”　　　＜　　　　　　＄”　　　　　　　　　　＄<br>"\
                "”　　レヘル：　９９　＄”　たいりょく：２５５＄<br>"\
                "”　　　　　　　　　　＄”　　　　　　　　　　＄<br>"\
                "”　　　ＨＰ：６５３　＄”　　かしこさ：　６２＄<br>"\
                "”　　　　　　　　　　＄”　　　　　　　　　　＄<br>"\
                "”　　　ＭＰ：　　０　＄”　うんのよさ：１４０＄<br>"\
                "）％％％％％％％％％％（”　　＜　　　　　　　＄<br>"\
                "＆＃＃＃＃＃＃＃＃＃＃’”さいたいＨＰ：６５３＄<br>"\
                "”　　＜　　　　　　　＄”　　＜　　　　　　　＄<br>"\
                "＾　はくれメタルのけん＄”さいたいＭＰ：　　０＄<br>"\
                "”　　＜　　　　　　　＄”　　　＜　　　　　　＄<br>"\
                "＾　はくれメタルよろい＄”　こうけきカ：３８５＄<br>"\
                "”　　　　　　　　　　＄”　　　　＜　　　　　＄<br>"\
                "＾　ちからのたて　　　＄”　　しゅひカ：１９３＄<br>"\
                "”　　　　　　　　　　＄”　　　　　　　　　　＄<br>"\
                "＾　てっかめん　　　　＄”￥：１０００００００＄<br>"\
                "）％％％％％％％％％％（）％％％％％％％％％％（"
    Label1 = makeLabel(str_status, FONT_SIZE, 150, 30, fontColour=FONT_COLOR, font=FONT_FILE, background=BG_COLOR)
    showLabel(Label1)

class Message():
    def __init__(self, person, str, x, y, hideflg=True, size=MESSAGE_SIZE, color=MESSAGE_COLOR, bgcolor=BG_COLOR):
        self.str_array = str.split(',')
        self.waku_width = max([len(x) for x in self.str_array])
        if len(person) > 0: 
            self.message = WAKU_KADO_1 + WAKU_YOKO_1 * 1 + person + WAKU_YOKO_1 * (self.waku_width - len(person) - 1) + WAKU_KADO_2 + "<br>"
        else:
            self.message = WAKU_KADO_1 + WAKU_YOKO_1 * self.waku_width + WAKU_KADO_2 + "<br>"
        #self.message += WAKU_TATE_1 + WAKU_SPACE * self.waku_width + WAKU_TATE_2 + "<br>"
        for i in range(len(self.str_array)):
            self.message += WAKU_TATE_1
            self.message += self.str_array[i] + "　" * ( self.waku_width - len(self.str_array[i]) )
            self.message += WAKU_TATE_2 + "<br>"
        self.message += WAKU_TATE_1 + WAKU_SPACE * (self.waku_width - 4) + "｛　　　" + WAKU_TATE_2 + "<br>"
        self.message += WAKU_KADO_3 + WAKU_YOKO_2 * self.waku_width + WAKU_KADO_4
        self.label = makeLabel(self.message, size, x, y, fontColour=color, font=FONT_FILE, background=bgcolor)
        showLabel(self.label)
        while True:
            if keyPressed("space"):
                break
        playSound(SOUND)
        while keyPressed("space"):
            pass
        if hideflg:
            self.hide()
    def hide(self):
        hideLabel(self.label)
    
str_waku_1_start = "＆＃＃＃＃＃＃＃＃＃＃’<br>"\
        "”　　　　　　　　＜<br>"\
        "”アリーナの　こうけき！<br>"\
        "”　　　　　　　　＜<br>"\
        "”かいしんの　いちけき！<br>"\
        "”＜　＞　　　　　　　　＜　　＜<br>"\
        "”テスヒサロに　２６２のタメーシ！<br>"

str3 = "！”＃＄％＆’（）＝～｜<br>"\
        "＠「；：」<br>"\
        "｛＋＊｝＜＞？＿<br>"

playSound(BGM, -1)
draw_status()

koi = makeSprite(KOIKE_IMAGE)
showSprite(koi)
transformSprite(koi, 0, 1.8)
moveSprite(koi, 880, 20)

hika = makeSprite(HIKAKIN_IMAGE)
showSprite(hika)
transformSprite(hika, 0, 1)
moveSprite(hika, 15, 15)

pause(5000)
mes = Message("だんな",\
               "　　　　　＜　＜,ゆーちゅーふ　て,"\
               "　,ヒカキンさんと　こいけ　とちじの,"\
               "　,たいだんの　ようすを　みました。"\
               ,100, 230, color="white")
mes = Message("だんな",\
               "　,ヒカキンさん　とてもわかいのに,"\
               "　　　　　　　　　　　＜　　　　　　＜　　　＜,にほんのことをよくかんかえていて　すはらしいてす。,"\
               "＜,ほくにも　なにかてつだえないか　とおもい,"\
               ",たいだんの　ようすを　ドラクエけいしきにして,"\
               "＞　　　＜　＞　＜,ハイソンて　フロクラムをつくってみました。"\
               ,60, 230, color="white")
mes = Message("ヒカキン",\
               ",こいけとちじ、,"\
               "　　　　　　　　　　　　　　　　　　＜,わかいみんなへ　せいかくなじょうほうか,"\
               ",とどくように　しつもんさせて　ください。"\
               ,120, 30, color="pink")
mes = Message("こいけゆ",\
               "　　　　　＜＜,ゆーちゅーふて　３つのみつのことを　はなして,"
               "　　　　　　＜　　＜＜,くれて　ありかとうこさいます。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　＜,すこい　みなさんに　みてもらって,"\
               "　　　＜,いるんてすよね。"\
               ,100, 350)
mes1 = Message("ヒカキン",\
               "　　　＜　　　　　＜,いま　ほくたちに　てきること,"\
               "　　＜　　　　　　　＜,やるへきことは　なんてしょうか？"\
               ,120, 30, hideflg=False, color="pink")
mes = Message("こいけゆ",\
               "　　　　　　　＜　　　　　　　　　　　＜,せんじつ　くにか　きんきゅうじたいせんけん,"\
               "　,って　いうのを　だしました。,"\
               "　　　　　　　　　　　　　＜,とうきょうと　は　そのせんけんを　うけて"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　,みなさんに　こうしてください　ああしてください,"\
               "　,という　きんきゅうじたい　そち　を,"\
               "　　＜　　　　　　　　＜,おねかいしている　わけてす。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　　　　＜　　　＜,そのなかて　いちはん　おおきいのは"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　,お　う　ち　に　　い　ま　し　ょ　う　　,"\
               "　,ステイ　ホーム,"\
               "　　　　　　　＜,って　ことなんてす。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　,とはいえ　ね,"\
               "　,おかいもの　とか　ひつような　ものありますよね。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　　＜　　　　　　　＞,コンヒニ　とか　スーハー　などは,"\
               "　,あいています　から　にちじょうひん　を　かいに,"\
               "　,いくことは　もんだい　ありません。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　,だけど　きほんは　おうちに　いてくださいね,"\
               "　　　　　＜,ということてす。"\
               ,100, 350)
mes1.hide()
mes = Message("ヒカキン",\
               "　＜　＜,じふんか　コロナ　ウイルスなんじゃ　ないか　と,"\
               "　　＜　　　　　　　　　　　＜　＜,うたかいのある　しょうじょうか　てたときに,"\
               "　　　　　　　　　　　　　　＜,どこに　れんらくしたら　よいてしょう？"\
               ,120, 30, color="pink")
mes2 = Message("ヒカキン",\
               "　　　　　　＜　　　　　　＜　＜,どういう　うこきを　するのか　ヘストなのか,"\
               "　　　　　　　　　＜,を　おききしたい　てす。"\
               ,120, 30, hideflg=False, color="pink")
mes = Message("こいけゆ",\
               "　　　　　　　　　＜　　　　＜　　　＜,いくつかの　ルートか　あるんてすけれとも,"\
               "　　,いつも　いっていらっしゃる　かかりつけの,"\
               "　　　　　　　　　＜　＜,おいしゃさんに　ます　てんわしてください。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　　　　　　　　　　　　　　　　　　　　　＜,もう　かんせんしている　かもしれない　なかて,"\
               "　,そこにいくと　おいしゃさんや　まっているひとに,"\
               "　　　　　　　　　　　　＜,うつっちゃうことも　かんかえられます。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　　＜　　＜　　＜　　＜,なのて　ますは　てんわて　そうだん,"\
               "　,していただきたい。"\
               ,100, 350)
mes2.hide()
mes3 = Message("ヒカキン",\
               "　　　　　　　　　　　　　　　　　＜,１０だい　２０だいの　かんせんしゃか,"\
               "　　　　　＜　　　　　　　　＜,ふえているか　わかいひとは　とんなことに,"\
               "　　　　　＜　　　　＜,きをつけれは　いいてすか？"\
               ,120, 30, hideflg=False, color="pink")
mes = Message("こいけゆ",\
               "　　　　　　　　　　　　　　　＜,３つの　みつを　さけてもらうのか,"\
               ",わかい　ひとにも　じゅうように　なります。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　　　　　　　　　　　　　　　　　　　　　　＜,おっしゃるとおり　１０だいのかた　のかんせんか,"\
               "　　　　　　　＜,ふえて　いるんてすよ。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　　　　　　　　　　　　＜,ろうにゃくなんにょ　とわす,"\
               "　　　　　　　　　　　　　　　　　　　＜,きほん　いえに　いましょう　ということてすね。"\
               ,100, 350)
mes3.hide()
mes = Message("こいけゆ",\
               "　,ひとと　ひとの　きょりを　２メートルあける,"\
               "　,ことも　せかいの　じょうしきに　なっています。"\
               ,100, 350)
mes = Message("ヒカキン",\
               "　　　＜　　＜,たとえは　レシをまつときに　しっかりと,"\
               "　　　　　　　　　　　　　　　＜　　＜,きょりを　はなすことを　こころかけれは,"\
               "　　＜　＜　　　　　　　　＜,１かけつこの　かんせんしゃか　てんと　ち,"\
               "　　　　　　＜,ということ　てすね？"
               ,120, 30, color="pink")
mes = Message("こいけゆ",\
               "　　　　　　　　　　＜,はい　そういうこと　てす。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　　＜,さいこに　わかい　みなさんには　おうちに,"\
               "　　　　　　　　　　＜　＜,いていただいて　そこて　へんきょうや,"\
               "　,ネットを　つかって　ともだちと　はなしをしたり,"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　　　　　　　＞,ときには　かんはい　したり　して,"\
               "　,おうちに　いていただきたいと　おもいます。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　　　　　　　　　　　　　　　　　＜,コロナの　ときは　こんなふうに　すこしたよなぁ,"\
               "　　　　　＜＜,と　おもいてか　かたれるように　いちにちも,"\
               "　　　　　　　　　　　　　　　　　　＜,はやく　このコロナウイルスに　みんなて,"\
               "　,うちかって　いきたいと　おもいます。"\
               ,100, 350)
mes = Message("こいけゆ",\
               "　＜　　　＜,すへて　しふんのこと　だとおもって,"\
               "　　　　　　　　　　　　　＜,コロナウイルスたいさくの　こきょうりょくを,"\
               "　　＜,おねかいします。,"\
               "　　　　　　　　　　　　　　　　＜,おうちにいましょう　よろしくおねかいします。"\
               ,100, 350)
mes = Message("ヒカキン",\
               "　　　　　　　　＜　　　　　　　　　　　＜,いま　ゆーちゅーはーや　インフルエンサーか,"\
               "＜　　　　　　　　＞　　　　　＜　　＜,てきることは　やっはり　おうちて　すこそう,"\
               "　　＜　　　　　　　　　　　　　　＜　＜,なんてすよね。　これを　みている　とうきょうしゃ,"\
               "＜　　　　　　＜　　＜,かいましたら　ほくらて　ひろめて　いきましょう。"
               ,120, 30, color="pink")
mes = Message("だんな",\
               "　　　＞　＜,この　ふろくらむは,"\
               "　　　　　　＜　＜＜　　　　　　＜,あゆすた　のフロクて　ソースコートを,"\
               "　　　　　　　　　　　　＜　　＜,こうかい　しています。　せひ　こらん　ください。"\
               ,100, 220, color="white")
endWait()
