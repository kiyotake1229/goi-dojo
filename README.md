# 語彙道場

語彙力を鍛えるクイズゲーム。スマホ縦持ち前提の単一HTMLアプリ。

| 項目 | 内容 |
|------|------|
| 状態 | **Web版 公開中 / PWA対応済み / iOSプロジェクト構築済み（pod install 待ち）** |
| 公開URL（開発確認用） | https://claude.ai/code/artifact/b6bb42a1-e191-4d1e-b665-2f7a28ca4db2 |
| サポートURL / Web公開 | https://kiyotake1229.github.io/goi-dojo/ （GitHub Pages） |
| Bundle ID | `work.ltv.goidojo` |
| 収録 | 681語・1,362問（7分野・難易度3段階）。すべて自作 |
| 通信 | なし。データは localStorage（iOS版は Preferences にも二重保存） |

---

## 内容

- 出題は「語→意味」「意味→語」の双方向、4択。誤答肢は同じ分野からランダム
- モード：今日の修行（日替わり10問・連勝日数）／時間攻め（60秒）／真剣勝負（3ミス終了）／弱点復習／分野別
- 連続正解でスコア倍率（最大3倍）、結果で段位判定、経験値で称号が育つ
- 出会った語は語彙帳に蓄積（正誤・苦手・習得済みで絞り込み）
- 効果音・BGMは Web Audio で合成（音源ファイルなし）。触覚フィードバックあり
- 結果画面から「取りこぼした語を今すぐ復習」で間違えた語だけを再出題

## ファイル

```
語彙力/
  index.html              アプリ本体（CSS/JS/語彙データすべて内包）
  README.md               このファイル
  manifest.json / sw.js   PWA用
  icon.svg                アイコン元データ
  icon-192.png / icon-512.png / apple-touch-icon.png
  tools/icon-gen.html     アイコンPNGの生成元（Canvas描画。Chromeヘッドレスで撮影）
  ios-app/                iOSアプリ（Capacitor）。手順は ios-app/岩崎さんへの引き渡し手順.md
```

## 公開の更新

`index.html` を変更したら、このフォルダで commit → push すると GitHub Pages に反映される（数分）。

```bash
git add -A && git commit -m "変更内容" && git push
```

## 語彙の追加

`index.html` 内の `DATA` 配列に1行追加する。

```js
["語","読み","意味","分野",難易度],
```

- 分野：`goi`（語彙）`yoji`（四字熟語）`kan`（慣用句）`koji`（故事成語）`biz`（敬語・仕事語）`kata`（カタカナ語）`iikae`（大人の言い換え）
- 難易度：1=初級 / 2=中級 / 3=上級（得点ベース 100 / 120 / 150）
- 読みが無い語（カタカナ語など）は `""` にする
- 同じ分野内で意味文が重複すると4択が成立しないので避ける

## 残作業

- [ ] Xcode をインストールした環境で `ios-app/` にて `npx cap sync ios`（pod install）
- [ ] 実機で触覚・通知・データ永続化を確認
- [x] GitHub Pages（`goi-dojo` リポジトリ）を作成しサポートURLを公開
- [ ] App Store 用スクリーンショット（6.7 / 6.5 / 5.5 インチ）
- [ ] Apple Developer Program 登録 → 岩崎さんへ引き渡し

## 今後の候補

- 間隔反復（間違えた語を1日後・3日後・7日後に自動再出題）
- 結果のシェア画像生成
- 語彙の追加（目標 1,000語）

## 補足

教育カテゴリは審査で「コンテンツの質」を見られやすい。語彙データはすべて自作（辞書的な定義を参照して独自に執筆）で、引用・転載はない。引き渡し手順にも明記済み。
