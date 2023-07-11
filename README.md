# Coffee_Voting
珈琲の味を評価して投票、投票結果を表示するアプリケーションです

# 機能
・一覧表示：作成した珈琲の一覧を表示します
・詳細表示：作成した珈琲の詳細情報(抽出条件、投票結果)を表示します
・新規作成、更新：新しい珈琲の登録、既に登録されている珈琲情報の更新を行います
・投票：作成した珈琲に対して、レビュー(5つの指標の5段階評価、自由コメント)を投票します

# DB構成概要

## Coffee(珈琲の情報を格納するテーブル)
-カラム
　-id
　-roasting(焙煎度：Roastingテーブルと関連付ける外部キー)
　-brand(豆の銘柄)
　-beans_grams(豆の量)
　-time(抽出時間)
　-temperature(湯の温度)
　-final_grams(最終的な量)
　-コメント
　-created_at(作成日)
　-updated_at(更新日)

## Voting(投票情報を格納するテーブル)
- カラム
　- id
　- bitterness(苦味)
　- sourness(酸味)
　- sweetness(甘み)
　- richness(コク)
　- flavor(香り)
　- review(レビュー)
　- coffee_id(Coffeeテーブルと関連付ける外部キー)
　- created_at(作成日)
　- updated_at(更新日)

## Roasting(焙煎度を格納するテーブル)
- カラム
　- id
　- name
　-created_at(作成日)
　・updated_at(更新日)
