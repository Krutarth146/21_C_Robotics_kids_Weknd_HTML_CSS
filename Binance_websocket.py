# import websocket, json

# cc = 'btcusd'
# interval = '1s'
# socket = f'wss://stream.binance.com:9443/ws/{cc}t@kline_{interval}'

# print(socket)
# closes, highs, lows = [], [], []

# def on_message(ws, message):
#   json_message = json.loads(message)
#   candle = json_message['k']
#   is_candle_closed = candle['x']
#   close = candle['c']
#   high = candle['h']
#   low = candle['l']
#   vol = candle['v']
#   if is_candle_closed:
#     closes.append(float(close))
#     highs.append(float(high))
#     lows.append(float(low))

#     print(closes)
#     print(highs)
#     print(lows)
    
# def on_close(ws, close_status_code, close_msg):
#     print("Connection Closed")

# ws = websocket.WebSocketApp(socket,on_message = on_message,on_close=on_close)
# ws.run_forever()

students = {
    "Aakash" : 80,
    "Jeet" : 78,
    "Raksha" : 94,
    "Jigna" : 92,
    "Sweety" : 90,
    "Mahesh" : 95
}
sorted_list = dict(sorted(students.items()))
print(sorted_list)

temp1 = students.items()
print(temp1)
temp2 = []
for item in temp1:
    temp2.append(item[ : :-1])
temp2.sort()
print(temp2)
temp3 = []
for item in temp2:
    temp3.append(item[ : : -1])
final_dictionary = dict(temp3)
print(final_dictionary)

from sys import getsizeof
l1 = [x for x in range(1, 10)]
# print(l1)
print(getsizeof(l1))
marks = [
    ["Sr.", "Name", "Sub-1", "Sub-2"],
    [1, "Darshan", 30, 31],
    [2, "Rishi", 29, 33],
    [3, "Jay", 32, 32]
]
# print(marks[0])
title = next(marks)
print(marks)