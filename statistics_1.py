import matplotlib.pyplot as plt
from beautifultable import BeautifulTable

# get datas
datas = input('get me datas: ')
datas = list(map(int, datas.split(" ")))
row = int(input('how many rows you need: '))

# get needed values and make null array to poush it in loops
changesRange = max(datas) - min(datas)
staticRow = changesRange / row
results = []
aroundCategory = []
miangin = []

# make n array into results to push it catgorys
for i in range(int(row)):
   results += [[]]

# get minimulest number
min_num = min(datas)

# loop to orgnaize datas
for i in range(row):
  # around category text like: 0 ≤ x < 5
  aroundCategory += [str(min_num)+" ≤ x < "+str(min_num+staticRow)]

  # average of numbers in around catgory to : "markaz dasteh"
  miangin += [(min_num+(min_num+staticRow))/2]
  # push standard numbers to result
  for j in datas:
      if j >= min_num and j < min_num+staticRow:
        results[i] += [j]
  # add static row to minmulest number to use in another loop
  min_num += staticRow

# somtimes bigest number is not result for that we do it in last row : 5≤ x ≤11
# so we check result if bigest number is not in that we add them bigest number
if(max(datas) not in results[-1]):
   for i in range(datas.count(max(datas))):
      results[-1] += [max(datas)]
################# make plot #################

# round number
def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)

# set x and y to plot
y = []
x = []

for i in results:
   y += [len(i)] # Batch frequency
   x += [round_to_multiple(min(i), 5)] # hight of plot

# plot

#bar
def bar():
   fig = plt.figure(figsize = (10, 5))
   plt.bar(x, y, width=0.4, edgecolor="white")
   plt.show()

#pie
def pie():
   # fig, ax = plt.subplots()
   fig = plt.subplot()
   ax = plt.subplot()
   ax.pie(y, labels=aroundCategory,autopct='%1.1f%%')
   plt.show()

#line
def line():
   fig, ax = plt.subplots(figsize=(6, 6))
   ax.plot(x, y, label="Line")
   ax.legend()
   plt.show()

#tabel
def make_table():
   table = BeautifulTable()
   table.columns.header = ["faravani", "markaz dasteh", "faravany * markaz dasteh"]

   lenght_miangin = 0
   majmoe_faravani = 0
   majmoe_faravaniDarMiangin = 0
   for i in results:
      faravni = len(i)
      faravnyDarMiangin = faravni * miangin[lenght_miangin]
      table.rows.append([faravni, miangin[lenght_miangin], faravnyDarMiangin])
      majmoe_faravani += faravni
      majmoe_faravaniDarMiangin += faravnyDarMiangin
      lenght_miangin += 1

   table.rows.append([majmoe_faravani, '-', majmoe_faravaniDarMiangin])
   table.rows.header = aroundCategory + ['majmoe']
   print(table)


################# user command #################
while True:
   command = input("what do you want do? (say help to help you): ")

   if command == "help":
      print("""say "plot chart bar" to make you chart bar of data s\n
               say "plot chart pie" to make you chart pie of data s\n
               say "plot chart line" to make you chart line of data s\n
               say "table" to make you orgnaized tabel of data s\n
               say "exit" to exit program\n

            """)
   elif command == "plot chart bar":
      bar()
   elif command == "plot chart pie":
      pie()
   elif command == "plot chart line":
      line()
   elif command == "table":
      make_table()
   elif command == "exit":
      break
   else:
      print("undifind command")
