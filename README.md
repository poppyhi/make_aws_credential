# AWSでセッショントークンを作成し、環境変数に設定するシェルを生成するツール
動作環境：python3

arn:aws:iam::[hoge] の箇所を自分のIAMユーザに書き換える必要がある。
セッショントークン作成用のクレデンシャル情報は別途設定しておく必要がある。
※AWS CLIでMFAが有効な人向けのツール。

作成したセッショントークンの有効期限は10時間。
変更したい場合は、--duration-seconds 36000 の数値を書き換えること。

## make_aws_credential_sh.py
Linux環境用
ツールを実行すると、「set_aws_credential.sh」が生成される。
以下のコマンドを実行し、環境変数を設定する。
```
$ source set_aws_credential.sh 
```

## make_aws_credential_bat.py
Windows環境用
ツールを実行すると、「set_aws_credential.bat」が生成される。
バッチファイルを実行し、環境変数を設定する。
