from worktime import worktime as wt

始業時間 = wt(830)    # 8:30         wt("8:30") でも可
終業時間1 = wt(2155)  # 21:55        wt("21:55") でも可
終業時間2 = wt(1700)  # 17:00        wt("17:00") でも可
休憩1 = wt(45)  # 45分間の休憩  wt("0:45") でも可
休憩2 = wt(15)  # 15分間の休憩  wt("0:15") でも可
休憩3 = wt(10)  # 10分間の休憩  wt("0:10") でも可

定時間 = 終業時間2 - 始業時間 - 休憩1  

月 = 火 = 木 = 終業時間1 - 始業時間 - 休憩1 - 休憩2 - 休憩3  # フル残業
水 = 金 = 終業時間2 - 始業時間 - 休憩1  # 強制定時退社日

残業_月 = 月 - 定時間  # 月曜日の残業時間(実労働時間 - 定時間)
残業_火 = 火 - 定時間  # 火曜日  々
残業_水 = 水 - 定時間  # 水曜日　々
残業_木 = 木 - 定時間  # 木曜日　々
残業_金 = 金 - 定時間  # 金曜日　々

週間実労働時間 = 月 + 火 + 水 + 木 + 金
週間残業時間 = 残業_月 + 残業_火 + 残業_水 + 残業_木 + 残業_金

月間残業時間 = 週間残業時間 * 4

print(f"(月) 実労働時間: {月}, 残業: {残業_月}")
print(f"(火) 実労働時間: {火}, 残業: {残業_火}")
print(f"(水) 実労働時間: {水}, 残業: {残業_水}")
print(f"(木) 実労働時間: {木}, 残業: {残業_木}")
print(f"(金) 実労働時間: {金}, 残業: {残業_金}")

print(f"週間実労働時間: {週間実労働時間}, 数値表示:{float(週間実労働時間)}")
print(f"週間残業時間  : {週間残業時間}, 数値表示:{float(週間残業時間)}")
print(f"月間残業時間  : {月間残業時間}, 数値表示:{float(月間残業時間)}")

if 月間残業時間 >= wt("45:00"):  # 月間残業時間が45時間を超える場合
    print("三六協定違反")
else:
    print("まだ残業できる")