# 語彙道場 社内説明資料（8枚）の生成。アプリ index.html の配色・書体をそのまま使う
# Python 3.9 のため f-string を入れ子にしない（部品を先に変数へ）
# 使い方: python3 tools/slides/gen.py  → このフォルダに Main.dc.html / S02〜.dc.html / canvas.json / deck.html、docs/ に PDF
#         そのあと docs/manager/generate_docs_json.sh を実行する
import json, os
OUT = os.path.dirname(os.path.abspath(__file__))
PDF_NAME = '20260915_DOC_0001_ALL_社内説明資料（語彙道場）.pdf'  # docs/ の命名規則（YYYYMMDD_種別_連番_場所_内容）
APP, DATE, N = '語彙道場', '2026-09-15', 8

BG0, BG1, BG2 = '#0A0D1A', '#141033', '#1E1240'
CARD, EDGE, EDGE2 = 'rgba(255,255,255,.055)', 'rgba(255,255,255,.13)', 'rgba(255,255,255,.22)'
TX, TX2, TX3 = '#F3F4FA', '#A9AEC8', '#6E7496'
GOLD, GOLDD, MINT, MINTD, RED = '#F2C14E', '#C89528', '#38DFA6', '#0F8F68', '#FF5B6E'
PAPER = '#F6F1E6'

HEAD = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho+B1:wght@600;800&family=Zen+Kaku+Gothic+New:wght@500;700;900&family=Barlow+Condensed:wght@600;700&display=swap">
  <style>
    body { margin: 0; background: #0A0D1A; color: #F3F4FA; font-family: "Zen Kaku Gothic New", "Hiragino Kaku Gothic ProN", "Hiragino Sans", sans-serif; -webkit-font-smoothing: antialiased; }
    a { color: #F2C14E; } a:hover { color: #38DFA6; }
    .fd { font-family: "Shippori Mincho B1", "Hiragino Mincho ProN", serif; }
    .fm { font-family: "Barlow Condensed", "Zen Kaku Gothic New", sans-serif; font-variant-numeric: tabular-nums; letter-spacing: .06em; }
    .ico { width: 24px; height: 24px; stroke: currentColor; fill: none; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; flex: none; }
  </style>
</helmet>
'''
TAIL = '''</x-dc>
</body>
</html>
'''

ICON = {
 'q': '<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 1-1 1.7M12 17h.01"/></svg>',
 'book': '<svg class="ico" viewBox="0 0 24 24"><path d="M5 4h14v16l-3-2-4 2-4-2-3 2z"/><path d="M9 9h6M9 13h4"/></svg>',
 'shield': '<svg class="ico" viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
 'swap': '<svg class="ico" viewBox="0 0 24 24"><path d="M4 8h13l-3-3M20 16H7l3 3"/></svg>',
 'combo': '<svg class="ico" viewBox="0 0 24 24"><path d="M4 18l5-6 4 4 7-9"/><path d="M16 7h4v4"/></svg>',
 'rank': '<svg class="ico" viewBox="0 0 24 24"><path d="M8 21h8M12 17v4M6 4h12v4a6 6 0 0 1-12 0z"/><path d="M6 6H3v2a3 3 0 0 0 3 3M18 6h3v2a3 3 0 0 1-3 3"/></svg>',
 'note': '<svg class="ico" viewBox="0 0 24 24"><path d="M6 3h12v18H6z"/><path d="M9 8h6M9 12h6M9 16h4"/></svg>',
 'sun': '<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M5.6 18.4L7 17M17 7l1.4-1.4"/></svg>',
 'clock': '<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l3 2M9 3h6"/></svg>',
 'heart': '<svg class="ico" viewBox="0 0 24 24"><path d="M12 20s-7-4.6-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.4-7 10-7 10z"/></svg>',
 'target': '<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>',
 'grid': '<svg class="ico" viewBox="0 0 24 24"><rect x="4" y="4" width="7" height="7" rx="1"/><rect x="13" y="4" width="7" height="7" rx="1"/><rect x="4" y="13" width="7" height="7" rx="1"/><rect x="13" y="13" width="7" height="7" rx="1"/></svg>',
 'check': '<svg class="ico" viewBox="0 0 24 24"><path d="M5 12l4 4L19 7"/></svg>',
 'bell': '<svg class="ico" viewBox="0 0 24 24"><path d="M6 16v-5a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 20a2 2 0 0 0 4 0"/></svg>',
 'fire': '<svg class="ico" viewBox="0 0 24 24"><path d="M12 3c1 4 5 5 5 10a5 5 0 0 1-10 0c0-2 1-3 2-4 0 2 1 3 2 3 0-4 1-6 1-9z"/></svg>',
 'redo': '<svg class="ico" viewBox="0 0 24 24"><path d="M20 11a8 8 0 1 0-2.3 5.7"/><path d="M20 4v7h-7"/></svg>',
}

MOTIF = '<div class="fd" style="width:30px;height:30px;border-radius:50%%;border:2px solid %s;color:%s;display:grid;place-items:center;font-size:15px;font-weight:800">道</div>' % (RED, RED)

def slide(n, body, eyebrow, title, title_size=44):
    foot = ('<div style="position:absolute;left:64px;bottom:30px;display:flex;align-items:center;gap:14px">'
            '<span class="fm" style="font-size:15px;color:%s">No. %02d / %02d</span>'
            '<span style="width:1px;height:14px;background:%s"></span>'
            '<span style="font-size:13px;color:%s">%s · 社内説明 · %s</span></div>'
            '<div style="position:absolute;right:64px;bottom:26px">%s</div>') % (TX3, n, N, EDGE2, TX3, APP, DATE, MOTIF)
    head = ''
    if title:
        head = ('<div style="display:flex;flex-direction:column;gap:8px">'
                '<div class="fm" style="font-size:15px;color:%s">%s</div>'
                '<h1 class="fd" style="margin:0;font-size:%dpx;font-weight:800;line-height:1.25;letter-spacing:.01em;color:%s;text-wrap:balance">%s</h1></div>') % (GOLD, eyebrow, title_size, TX, title)
    return HEAD + ('<div style="width:1280px;height:720px;position:relative;overflow:hidden;background:linear-gradient(160deg,%s 0%%,%s 60%%,%s 100%%);padding:56px 64px 72px;box-sizing:border-box;display:flex;flex-direction:column;gap:28px">'
                   '%s%s%s</div>\n') % (BG0, BG1, BG2, head, body, foot) + TAIL

def paper(inner, extra=''):
    return '<div style="background:%s;color:#1a1730;border-radius:14px;padding:24px 26px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 34px rgba(0,0,0,.45);%s">%s</div>' % (PAPER, extra, inner)

def card(inner, extra=''):
    return '<div style="background:%s;border:1px solid %s;border-radius:14px;padding:22px 24px;display:flex;flex-direction:column;gap:10px;%s">%s</div>' % (CARD, EDGE, extra, inner)

def tag(text, color=GOLD, bg='rgba(242,193,78,.14)'):
    return '<span class="fm" style="display:inline-flex;font-size:14px;padding:5px 9px;border-radius:6px;background:%s;color:%s">%s</span>' % (bg, color, text)

def head_row(icon, text, size=22, color=TX, icolor=GOLD):
    return '<div style="display:flex;align-items:center;gap:10px;color:%s">%s<span class="fd" style="font-size:%dpx;font-weight:800;color:%s">%s</span></div>' % (icolor, icon, size, color, text)

def p(text, size=16, color=TX2, lh=1.8):
    return '<p style="margin:0;font-size:%spx;line-height:%s;color:%s">%s</p>' % (size, lh, color, text)

def grid(cols, items, gap=18):
    return '<div style="display:grid;grid-template-columns:repeat(%d,minmax(0,1fr));gap:%dpx;flex:1;align-content:start">%s</div>' % (cols, gap, ''.join(items))

def check_line(text, size=16):
    return '<div style="display:flex;gap:10px;align-items:flex-start;font-size:%dpx;line-height:1.7;color:%s"><span style="color:%s;margin-top:2px">%s</span><span>%s</span></div>' % (size, TX, MINT, ICON['check'], text)

files = {}

# ---------- 01 表紙 ----------
seal = ('<div style="width:220px;flex:none;display:flex;align-items:center;justify-content:center;border-right:1px solid %s">'
        '<div class="fd" style="width:132px;height:132px;border-radius:50%%;border:4px solid %s;color:%s;display:grid;place-items:center;font-size:68px;font-weight:800;box-shadow:0 0 0 6px rgba(255,91,110,.12)">道</div></div>') % (EDGE, RED, RED)
cover_body = ('<div style="flex:1;padding:44px 52px 40px;display:flex;flex-direction:column;gap:14px;min-width:0">'
              '<div class="fm" style="font-size:16px;color:%s">社内説明 · アプリ開発 · %s</div>'
              '<div class="fd" style="font-size:100px;font-weight:800;line-height:1;letter-spacing:.04em;color:%s">語彙道場</div>'
              '<div style="font-size:26px;font-weight:700;line-height:1.5;color:%s">681語・1,362問で鍛える、大人の語彙力クイズ</div>'
              '<div class="fm" style="display:flex;gap:28px;font-size:16px;color:%s;border-top:1px solid %s;padding-top:16px;margin-top:6px">'
              '<span>SINGLE HTML · OFFLINE</span><span>PWA · iOS 構築済み</span><span>kiyotake1229.github.io/goi-dojo</span></div></div>') % (GOLD, DATE, TX, TX2, TX3, EDGE)
cover = ('<div style="display:flex;align-items:center;justify-content:center;flex:1">'
         '<div style="display:flex;width:1060px;background:%s;border:1px solid %s;border-radius:18px;box-shadow:0 30px 70px rgba(0,0,0,.6);overflow:hidden">%s%s</div></div>') % (CARD, EDGE2, seal, cover_body)
files['Main.dc.html'] = slide(1, cover, '', '')

# ---------- 02 ねらい ----------
aims = [
 ('q', '「知っているつもり」が多い', '四字熟語・慣用句・敬語。読めるが使えない、意味を取り違えている語が、大人ほど放置されている。'),
 ('book', '既存アプリは英語・受験向け', '日本語の語彙を大人向けに鍛えるアプリは少ない。あっても広告が多く、続ける仕組みが弱い。'),
 ('shield', '審査は「内容の質」を見る', '教育カテゴリは審査でコンテンツの質を問われる。681語すべてを自作し、引用・転載を一切なくした。'),
]
items = [paper(head_row(ICON[i], t, 25, '#1a1730', GOLDD) + p(d, 17, '#3f3b55', 1.85), 'min-height:250px') for i, t, d in aims]
body = grid(3, items, 22) + '<div style="font-size:18px;color:%s;line-height:1.7">1日10問、道場に通う感覚で語彙を増やす。学習アプリではなく「ゲーム」として設計した。</div>' % TX2
files['S02.dc.html'] = slide(2, body, '01 · ねらい', '大人の語彙力は、測る機会がない')

# ---------- 03 遊び方 ----------
quiz = paper('<div class="fm" style="font-size:14px;color:#7a7590;display:flex;justify-content:space-between"><span>Q 4 / 10</span><span>四字熟語 · 中級</span></div>'
             '<div class="fd" style="font-size:30px;font-weight:800;line-height:1.3;margin:6px 0 2px">「切磋琢磨」の意味は？</div>'
             '<div style="display:flex;flex-direction:column;gap:8px;margin-top:8px">'
             '<div style="padding:11px 14px;border-radius:10px;border:1px solid #d8d2c4;font-size:15px">相手を出し抜くために策を練ること</div>'
             '<div style="padding:11px 14px;border-radius:10px;border:2px solid %s;background:rgba(56,223,166,.12);font-size:15px;font-weight:700">仲間どうしで励まし合い、高め合うこと</div>'
             '<div style="padding:11px 14px;border-radius:10px;border:1px solid #d8d2c4;font-size:15px">苦労の末にようやく成し遂げること</div>'
             '<div style="padding:11px 14px;border-radius:10px;border:1px solid #d8d2c4;font-size:15px">言葉を飾らず率直に述べること</div></div>'
             '<div class="fm" style="display:flex;gap:18px;font-size:15px;color:#7a7590;border-top:1px dashed #d8d2c4;padding-top:12px;margin-top:6px"><span>連続正解 <b style="color:%s">5</b></span><span>倍率 <b style="color:%s">×2.0</b></span><span>SCORE <b style="color:#1a1730">1,240</b></span></div>' % (MINTD, MINTD, GOLDD), 'width:440px;flex:none')
steps = [
 ('swap', '双方向の4択', '「語 → 意味」と「意味 → 語」の両方で出題。誤答肢は同じ分野からランダムに選ぶので、消去法が効きにくい'),
 ('combo', '連続正解で倍率', '連続で当てるとスコア倍率が上がる（最大3倍）。1問の重みが変わるので、後半ほど緊張する'),
 ('rank', '段位と称号', '結果で段位を判定（見習い〜名人）。経験値で称号が育つ（入門〜）。伸びが見える'),
 ('note', '語彙帳に残る', '出会った語は語彙帳に蓄積。正誤・苦手・習得済みで絞り込み。間違えた語だけをその場で復習できる'),
]
right = '<div style="display:flex;flex-direction:column;gap:12px;flex:1">' + ''.join(card(head_row(ICON[i], t, 20) + p(d, 14.5, TX2, 1.65), 'padding:16px 20px;gap:6px') for i, t, d in steps) + '</div>'
body = '<div style="display:flex;gap:32px;flex:1;align-items:flex-start">%s%s</div>' % (quiz, right)
files['S03.dc.html'] = slide(3, body, '02 · 遊び方', '4択に答える。それだけで語彙が育つ')

# ---------- 04 モード ----------
modes = [
 ('sun', '今日の修行', '日替わり10問。毎日やると連勝日数が伸びる。通知でリマインド（iOS版）', '毎日の入口'),
 ('clock', '時間攻め', '60秒で何問解けるか。短時間で集中する', 'スコア勝負'),
 ('heart', '真剣勝負', '3回間違えたら終了。どこまで続けられるか', '緊張感'),
 ('target', '弱点復習', '間違えた語・苦手な語だけを出題。語彙帳と連動', '定着'),
 ('grid', '分野別', '7分野から選んで鍛える。難易度も選べる', '狙い撃ち'),
]
items = [card(head_row(ICON[i], t, 22) + p(d, 15, TX2, 1.7) + '<div style="margin-top:auto">%s</div>' % tag(k), 'min-height:220px') for i, t, d, k in modes]
body = grid(5, items, 16) + ('<div style="display:flex;align-items:center;gap:16px;background:%s;color:#1a1730;border-radius:14px;padding:18px 26px">'
                             '<span class="fd" style="font-size:24px;font-weight:800">毎日開く理由と、たまに燃える理由。</span>'
                             '<span style="font-size:17px;color:#5c5872">「今日の修行」で習慣にし、「時間攻め」「真剣勝負」でスコアを競う。</span></div>') % PAPER
files['S04.dc.html'] = slide(4, body, '03 · 5つのモード', '習慣にする入口と、燃える入口')

# ---------- 05 収録 ----------
fields = [('語彙', '雰囲気・矜持・忖度'), ('四字熟語', '切磋琢磨・臥薪嘗胆'), ('慣用句', '匙を投げる・気が置けない'), ('故事成語', '杞憂・蛇足・推敲'), ('敬語・仕事語', 'ご査収・拝承・所感'), ('カタカナ語', 'コンセンサス・アジェンダ'), ('大人の言い換え', '「すごい」→「圧巻」')]
rows = ''
for k, (f, ex) in enumerate(fields):
    rows += '<div style="display:grid;grid-template-columns:150px minmax(0,1fr);gap:14px;align-items:center;padding:9px 0;border-bottom:1px solid %s"><span class="fd" style="font-size:18px;font-weight:800;color:%s">%s</span><span style="font-size:14.5px;color:%s">%s</span></div>' % (EDGE, TX, f, TX2, ex)
left = card('<div class="fm" style="font-size:14px;color:%s">7分野</div><div style="display:flex;flex-direction:column">%s</div>' % (GOLD, rows), 'padding:16px 24px 8px;flex:1')
stats = ''.join('<div style="background:%s;border:1px solid %s;border-radius:12px;padding:16px 12px;text-align:center"><b class="fm" style="display:block;font-size:40px;font-weight:700;line-height:1;color:%s">%s</b><span style="font-size:13px;color:%s">%s</span></div>' % (CARD, EDGE, GOLD, v, TX2, l) for v, l in [('681', '収録語'), ('1,362', '問題数'), ('3', '難易度')])
lv = ''.join('<div style="display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid %s;font-size:15px"><span style="color:%s">%s</span><span class="fm" style="color:%s;font-size:16px">%s</span></div>' % (EDGE, TX, a, TX2, b) for a, b in [('初級', '100 点'), ('中級', '120 点'), ('上級', '150 点')])
right = ('<div style="display:flex;flex-direction:column;gap:14px;width:400px;flex:none">'
         '<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px">%s</div>'
         '%s%s</div>') % (stats, card('<div class="fm" style="font-size:14px;color:%s">難易度と得点</div>%s' % (GOLD, lv), 'padding:16px 20px 6px;gap:4px'),
                         paper('<div style="font-size:15px;line-height:1.75;color:#3f3b55"><b>すべて自作。</b>辞書的な定義を参照して独自に執筆。引用・転載はなく、審査で問われても説明できる。語の追加は1行書き足すだけ。</div>', 'padding:16px 20px'))
body = '<div style="display:flex;gap:28px;flex:1">%s%s</div>' % (left, right)
files['S05.dc.html'] = slide(5, body, '04 · 収録', '7分野 × 3難易度、全語自作')

# ---------- 06 続ける仕掛け ----------
hooks = [
 ('fire', '連勝日数', '今日の修行を続けた日数。途切れると0に戻るので、毎日開く理由になる'),
 ('rank', '段位と称号', '結果ごとに段位（見習い→門下生→初伝→目録→皆伝→師範→名人）。経験値で称号が育つ'),
 ('note', '語彙帳', '出会った語が全部残る。苦手・習得済みで絞り込み。自分の語彙の「地図」になる'),
 ('redo', '取りこぼし復習', '結果画面から「間違えた語だけ」を即再出題。悔しいうちに覚え直す'),
 ('bell', 'ローカル通知', 'iOS版は毎日同じ時刻に「今日の修行」を知らせる。通信なし・端末内'),
 ('heart', '音と触覚', '効果音・BGMは Web Audio で合成（音源ファイルなし）。正解・不正解に触覚フィードバック'),
]
items = [card(head_row(ICON[i], t, 21) + p(d, 15, TX2, 1.7), 'min-height:170px') for i, t, d in hooks]
files['S06.dc.html'] = slide(6, grid(3, items), '05 · 続ける仕掛け', '「明日も開く」を作る6つの要素')

# ---------- 07 現状 ----------
done = ['Web版 完成・公開中（GitHub Pages）。PWA対応', 'iOSプロジェクト構築済み（Capacitor）。Bundle ID: work.ltv.goidojo', 'GitHub Actions（macOS）で署名なしビルドが通ることを確認済み', '通信なし。データは localStorage（iOS版はネイティブ保存にも二重化）', '触覚フィードバック・ローカル通知を実装（審査4.2の根拠）', '申請文面（説明文・キーワード・カテゴリ・プライバシー）は下書き済み', '引き渡し手順書あり：語彙力/ios-app/岩崎さんへの引き渡し手順.md']
left = '<div style="display:flex;flex-direction:column;gap:9px">' + ''.join(check_line(d) for d in done) + '</div>'
right = paper('<div class="fm" style="font-size:14px;color:#7a7590">いま触れる</div>'
              '<div class="fd" style="font-size:22px;font-weight:800;line-height:1.3">kiyotake1229.github.io/goi-dojo/</div>'
              '<div style="font-size:15px;line-height:1.8;color:#3f3b55">iPhone の Safari で開き、共有メニューから「ホーム画面に追加」。まず「今日の修行」を10問。</div>'
              '<div class="fm" style="display:flex;flex-wrap:wrap;gap:8px;border-top:1px dashed #d8d2c4;padding-top:14px;font-size:14px;color:#7a7590"><span>単一 HTML</span><span>·</span><span>通信なし</span><span>·</span><span>端末内保存</span><span>·</span><span>約 165KB</span></div>', 'min-height:300px;justify-content:center')
body = '<div style="display:grid;grid-template-columns:minmax(0,1fr) 440px;gap:40px;flex:1;align-content:start">%s%s</div>' % (left, right)
files['S07.dc.html'] = slide(7, body, '06 · 現状', 'iOS は申請一歩手前。引き渡せる状態')

# ---------- 08 次のステップ ----------
road = [
 ('1', '実機確認', 'Xcode のある環境で pod install → 実機で触覚・通知・データ永続化を確認', '半日'),
 ('2', '素材と登録', 'App Store 用スクリーンショット3サイズ。Apple Developer Program の登録', '1週間'),
 ('3', '申請', '年齢制限 4+、カテゴリ「教育」または「ゲーム／単語」、「データを収集しません」。文面は下書き済み', '—'),
]
items = [card('<div class="fm" style="font-size:48px;font-weight:700;line-height:1;color:%s">%s</div><div class="fd" style="font-size:22px;font-weight:800">%s</div>%s<div class="fm" style="font-size:14px;color:%s;border-top:1px solid %s;padding-top:10px">目安 %s</div>' % (GOLD, n, t, p(d, 15, TX2, 1.75).replace('<p style="', '<p style="flex:1;'), TX3, EDGE, w), 'min-height:270px') for n, t, d, w in road]
cost = paper('<div class="fm" style="font-size:13px;color:#7a7590">費用</div><div style="display:flex;align-items:baseline;gap:10px"><span class="fd" style="font-size:36px;font-weight:800">¥12,800</span><span style="font-size:15px;color:#7a7590">/ 年 · Apple Developer Program のみ</span></div><div style="font-size:14px;color:#3f3b55">今後の候補：間隔反復（1日後・3日後・7日後に再出題）、1,000語への増量</div>', 'flex:1;padding:18px 24px;gap:6px')
decide = card('<div class="fm" style="font-size:13px;color:%s">今日決めたいこと</div><div style="font-size:18px;font-weight:700;line-height:1.6">コツコツの次に語彙道場を申請するか。iOSプロジェクトは構築済みなので、残りは実機確認と登録だけ。</div>' % GOLD, 'flex:1;padding:18px 24px;gap:6px;justify-content:center')
body = grid(3, items) + '<div style="display:flex;gap:20px">%s%s</div>' % (cost, decide)
files['S08.dc.html'] = slide(8, body, '07 · 次のステップ', '残りは実機確認と登録だけ')

# ---------- 書き出し ----------
for name, src in files.items():
    open(os.path.join(OUT, name), 'w', encoding='utf-8').write(src)

names = ['Main.dc.html'] + ['S%02d.dc.html' % i for i in range(2, N + 1)]
W, H, GX, GY = 1280, 720, 80, 140
boards = []
for i, f in enumerate(names):
    r, c = divmod(i, 5)
    boards.append({'file': f, 'x': c * (W + GX), 'y': r * (H + GY), 'w': W, 'h': H, 'title': '%02d' % (i + 1)})
json.dump({'artboards': boards, 'launch': {'view': 'focused', 'file': 'Main.dc.html'}}, open(os.path.join(OUT, 'canvas.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# PDF 用（全スライドを1ページずつ並べたHTML。Chrome で印刷して PDF にする）
helmet = HEAD.split('<helmet>')[1].split('</helmet>')[0]
pages = ''.join('<div style="width:1280px;height:720px;page-break-after:always;overflow:hidden">%s</div>' % files[f].split('</helmet>\n')[1].split('</x-dc>')[0] for f in names)
deck = '<!doctype html><html><head><meta charset="utf-8"><title>%s 社内説明</title>%s<style>@page{size:1280px 720px;margin:0}html,body{margin:0}</style></head><body>%s</body></html>' % (APP, helmet, pages)
open(os.path.join(OUT, 'deck.html'), 'w', encoding='utf-8').write(deck)
print('written', len(files))

# PDF（docs/ に書き出す。Chrome が無い環境ではスキップ）
import subprocess
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
PDF = os.path.normpath(os.path.join(OUT, '..', '..', 'docs', PDF_NAME))
if os.path.exists(CHROME):
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=8000',
                    '--print-to-pdf=' + PDF, 'file://' + os.path.join(OUT, 'deck.html')],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    print('pdf', PDF)
else:
    print('Chrome が見つからないため PDF は作っていません')
