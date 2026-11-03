# セットアップガイド

日本語 | [English](./setup-guide.en.md)

このガイドでは、Dataverse Bulk Operations の接続、環境固有の値、テスト手順を説明します。インポート後、フローを実行する前に設定してください。

## ソリューションの構成

ソリューションには、Dataverse の一括作成・更新サンプル、削除サンプル、FetchXMLによる取得サンプル、Microsoft Entra IDのグループ確認サンプル、および動作確認用のキャンバスアプリとテーブルが含まれます。

| フロー | 主な接続 | 確認する値 |
|---|---|---|
| `create_and_update_multiple_sampleAction` | HTTP with Microsoft Entra ID（事前承認） | Dataverse環境URL、作成するデータ、更新対象の行ID |
| `deleteMultiple_sampleAction` | Microsoft Dataverse、HTTP with Microsoft Entra ID（事前承認） | `dd_employees` テーブルと削除対象データ |
| `tmp_FetchXML` | Microsoft Dataverse | FetchXML内のテーブル名・列名 |
| `tmp_search_in_group` | Microsoft Entra ID | メンバーを調べるユーザーとグループID |

フローは手動トリガーです。各フローの接続参照と実行権限を確認し、利用者が実行する場合は実行専用ユーザーの接続設定も行ってください。

## Dataverse Web API の接続先

`create_and_update_multiple_sampleAction` の `baseURL` Compose アクションには、サンプル値 `https://example.crm.dynamics.com` が設定されています。実行前に、接続先環境のURLに置き換えてください。末尾に `/` は付けません。

```text
https://<環境の組織URL>
```

URLはPower Platform管理センターまたは環境の詳細で確認します。呼び出しに使うHTTP with Microsoft Entra ID接続が、その環境に対する認証・アクセス権を持つことも確認してください。

## 作成・更新フローのサンプル値

このフローは、環境URLのほかにもテスト用の値をフロー定義内に持っています。実行前に各アクションを開いて確認してください。

- `createMultiple` は固定の3行を `dd_employees` に作成します。メールアドレスなどをテスト環境用の値に変更してください。
- `Create_Records_in_Bulk` スコープには、範囲の設定値 `100` から生成したデータをまとめて作成する処理があります。現在は1から99までのサンプル行を生成します。必要な件数だけに変更して実行してください。
- `updateMultiple` は3つの固定行IDを更新します。これらのIDがインポート先環境に存在することを確認し、必要に応じてテストレコードのIDに置き換えてください。
- 作成と更新のアクションは、同じ手動実行でそれぞれ処理されます。最初は少数のテストデータで実行し、実行履歴とDataverse上の結果を照合してください。

テーブルの論理名は `dd_employee`、コレクション名は `dd_employees` です。列名やデータ型を変更する場合は、送信するJSONとテーブル定義の両方を合わせてください。

## 削除フローの重要な注意

`deleteMultiple_sampleAction` は、`dd_employees` の行を最大1000件ずつ条件なしで取得し、Web API の `$batch` によるDELETEを繰り返します。テーブルが空になるまで続くため、実行するとこのテーブルのデータがすべて削除されます。

このフローは名前に `deleteMultiple` を含みますが、Dataverse の `DeleteMultiple` メッセージは使用していません。フローのフィルターや対象テーブルを確認しただけで安全と判断しないでください。

- 本番環境では実行しないでください。
- 専用の使い捨てテスト環境でのみ検証してください。
- テーブル内に必要なデータがないことを、実行直前に確認してください。
- 削除が許可されていない場合は、フローを無効のままにしてください。

## その他のフロー

### `tmp_FetchXML`

`dd_employee` と `dd_onboardingtraining` をメールアドレスで関連付け、オンボーディング研修レコードが存在しない従業員を取得するFetchXMLサンプルです。テーブルや列の論理名を変更した場合は、FetchXMLの `entity`、`attribute`、`link-entity` の設定も更新します。

### `tmp_search_in_group`

Microsoft Entra ID コネクタを使って、フロー定義にあるユーザーとグループIDのメンバーシップを確認します。実行前にユーザーUPNとテナント内のグループIDをテスト用の値に置き換えてください。

## 動作確認

1. 開発・テスト環境にテスト用の従業員レコードを用意します。
2. 接続参照と各フローの接続先を確認します。
3. 作成・更新フローの環境URL、作成データ、更新対象IDをテスト用に設定します。
4. `create_and_update_multiple_sampleAction` を手動実行し、実行履歴とDataverseのレコードを確認します。
5. `tmp_FetchXML` と `tmp_search_in_group` は、対象テーブル・ユーザー・グループをテスト環境用に設定して個別に実行します。
6. 削除処理を検証する必要がある場合は、専用の使い捨て環境でのみ実施し、実行前に対象テーブルが空にしてよい状態であることを確認します。

## トラブルシューティング

- **接続参照エラー**: ソリューション内の接続参照が、対象環境で認証済みの接続に割り当てられているか確認します。
- **HTTP 401/403**: HTTP with Microsoft Entra ID接続の認証状態、対象環境へのアクセス権、テナントのコネクタ利用ポリシーを確認します。
- **HTTP 404**: 環境URL、APIパス、テーブルのコレクション名（例: `dd_employees`）を確認します。
- **作成・更新エラー**: 列の論理名、データ型、必須項目、更新対象ID、要求データを確認します。
- **FetchXMLエラー**: テーブルや列の論理名、およびリンク条件がインポート先のスキーマと一致するか確認します。

Dataverse Web APIのバージョン、要求形式、テーブルごとの一括操作のサポート状況は、利用する環境の仕様に合わせて確認してください。
