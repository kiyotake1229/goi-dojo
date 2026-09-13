# 語彙道場 iOSアプリ（Capacitor）

Webアプリ本体（`../index.html`）をネイティブiOSアプリとして同梱したプロジェクトです。

- **申請・アップロードは岩崎さんが実施** → 手順は [`岩崎さんへの引き渡し手順.md`](岩崎さんへの引き渡し手順.md)
- このREADMEは開発側（アプリを作る人）向けのメモです

---

## 現在の状態

| 項目 | 状態 |
|------|------|
| Capacitorプロジェクト | 構築済み（`work.ltv.goidojo` / 語彙道場） |
| Xcodeプロジェクト生成 | 済み（`ios/App/App.xcworkspace`） |
| Webアプリ同梱 | 済み（`ios/App/App/public/`） |
| アプリアイコン・スプラッシュ | 生成済み（1024px・透過なし） |
| ネイティブ触覚・通知・保存 | 組み込み済み（`../index.html` 内で `NATIVE` 分岐） |
| 縦画面固定・ダーク表示 | 設定済み（`Info.plist`） |
| `pod install` | **未実行**。Xcodeが無い環境で構築したため。Xcodeのある環境で下記を1回実行 |

```bash
npm install
npx cap sync ios      # ← pod install が走る（要 Xcode）
open ios/App/App.xcworkspace
```

> 日本語パスで CocoaPods がエラーになる場合は `export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8` を先に実行。

---

## 構成

```
ios-app/
├── package.json              npm設定（Capacitor + プラグイン）
├── capacitor.config.json     アプリID・名前・プラグイン設定
├── sync-web.sh               ../のWebアプリを www/ にコピー
├── assets/icon.png           アイコン元画像（1024px）
├── www/                      同梱するWeb資産（sync-web.sh の出力）
└── ios/                      Xcodeプロジェクト
    └── App/App.xcworkspace   ← これを開く
```

## よく使うコマンド

```bash
npm install        # 依存取得（初回のみ。node_modules は Dropbox 同期負荷のため削除してある）
npm run sync       # ../index.html の変更をiOSプロジェクトへ反映
npm run icons      # アイコン・スプラッシュ再生成（assets/icon.png から）
npm run open       # Xcodeで開く（要Xcode）
```

## アプリ本体を修正したら

1. `../index.html` を編集
2. `npm run sync` を実行
3. Xcodeで再ビルド

## ネイティブ専用の動作

`../index.html` 内で `NATIVE`（Capacitor検出）により分岐しています。

| 機能 | Web版 | ネイティブ版 |
|------|-------|-------------|
| 触覚 | `navigator.vibrate`（iPhoneのSafariでは無反応） | Capacitor Haptics（正解＝軽い衝撃、誤答＝エラー触覚） |
| 今日の修行リマインド | 非表示 | 毎日指定時刻にローカル通知（アプリを閉じていても届く） |
| データ保存 | localStorage | localStorage ＋ Preferences の二重保存（WebView側の消失対策） |

## メモ

- BGM・効果音はすべて Web Audio で合成しており、音源ファイルはありません。
- `Pods/` `node_modules/` `www/` はgit管理外（`.gitignore`）です。
