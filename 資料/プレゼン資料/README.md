# プレゼン資料（社内説明・8枚）

- 公開URL（Claude Design。閲覧・文字の修正・PNG/PDF書き出し）: https://claude.ai/code/artifact/208fd26f-99c5-4bcc-bde8-0ab38506f27e
- PDF: `語彙道場_社内説明.pdf`（このフォルダ。そのまま配れる）
- 話す台本: [../プレゼンの進め方.md](../プレゼンの進め方.md)
- `gen.py` … スライド8枚（`Main.dc.html` = 表紙、`S02`〜）と `canvas.json`、PDF用の `deck.html`、PDF を生成するスクリプト。文言を直すときはここを編集する
- 見た目はアプリ本体（index.html）と同じ配色（藍の地・金・ミント・朱）と書体（しっぽり明朝 / Zen Kaku Gothic New / Barlow Condensed）
- 構成：表紙 / ねらい / 遊び方（4択の例） / 5つのモード / 収録（7分野×3難易度） / 続ける仕掛け / 現状 / 次のステップと費用

## 作り直す

アプリのフォルダで次を実行する（Chrome があれば PDF も更新される）。

```bash
python3 資料/プレゼン資料/gen.py
```
