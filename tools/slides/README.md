# スライド生成（社内説明資料 #0001）

社内説明スライド（8枚）の生成元。できあがった文書は `docs/` にある。

- 公開URL（Claude Design。閲覧・文字の修正・PNG/PDF書き出し）: https://claude.ai/code/artifact/208fd26f-99c5-4bcc-bde8-0ab38506f27e
- PDF: [docs/20260915_DOC_0001_ALL_社内説明資料（語彙道場）.pdf](../../docs/20260915_DOC_0001_ALL_社内説明資料（語彙道場）.pdf)
- 説明文書: [docs/20260915_DOC_0001_ALL_社内説明資料（語彙道場）.md](../../docs/20260915_DOC_0001_ALL_社内説明資料（語彙道場）.md)
- 話す台本: [docs/20260915_DOC_0002_ALL_プレゼンの進め方（語彙道場）.md](../../docs/20260915_DOC_0002_ALL_プレゼンの進め方（語彙道場）.md)
- `gen.py` … スライド8枚（`Main.dc.html` = 表紙、`S02`〜）と `canvas.json`、PDF用の `deck.html` を生成し、PDF を `docs/` に書き出す
- 見た目はアプリ本体（index.html）と同じ配色（藍の地・金・ミント・朱）と書体（しっぽり明朝 / Zen Kaku Gothic New / Barlow Condensed）
- 構成：表紙 / ねらい / 遊び方（4択の例） / 5つのモード / 収録（7分野×3難易度） / 続ける仕掛け / 現状 / 次のステップと費用

## 作り直す

文言は `gen.py` を直す。アプリのフォルダで:

```bash
python3 tools/slides/gen.py
```

```bash
bash docs/manager/generate_docs_json.sh
```
