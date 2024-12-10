print('welcome to KBC')
print('lets play')
score = 0
def q1(c1):
 score = 0
 if c1 == 1:
  print('that is correct')
  score = score+1
  print("+1 point")
 elif c1 == 2:
  print('that is wrong')
  score = score-1
  print("-1 point")

def q2(c1):
 score = 0
 if c1 == 1:
  print('that is wrong')
  score = score-1
  print('-1 point')
 elif c1 == 2:
  print('that is correct')
  score = score+1
  print("+1 point")

print('Q1.what is smallest car ?')
print('1.Renault Twizy')
print('Or')
print('2.Citroen Amy')
c1=(int(input('enter your answer ')))
q1(c1)

print('Q2.who is the new president of America')
print('1.Donald Trump')
print('Or')
print('2.Narendra Modi')
c2=(int(input('enter your answer ')))
q1(c2)

print("Q3.What is the most common surname in the United States?")
print("1.Smith")
print("Or")
print("2.Ray")
c3=(int(input("enter your answer ")))
q1(c3)

print("Q4.Who wrote the play, Romeo and Juliet? ")
print("1.Jeff Kinney")
print("Or")
print("2.William Shakespeare")
c4=(int(input("enter your answer ")))
q2(c4)

print("Q5.Who was the Ancient Greek God of the Sun?")
print("1.Lord Shiva")
print("Or")
print("2.Helios")
c5=(int(input("enter your answer ")))
q2(c5)

print("Q6.As per 2024, which country has the highest life expectancy?")
print("1.Monaco")
print("Or")
print("2.Hong Kong")
c6=(int(input("enter your answer ")))
q2(c6)

print("Q7.The folk dance “Fugdi” is related to which state of India? ")
print("1.Goa")
print("Or")
print("2.Haryana")
c7=(int(input("enter your answer ")))
q1(c7)


print("Q8.Which organization publishes the World Economic Outlook (WEO) report?")
print("1.The International Monetary Fund (IMF)")
print("Or")
print("2.The Hindu Times")
c8=(int(input("enter your answer ")))
q1(c8)

print("Q9.Which artist painted the Mona Lisa?")
print("1.Leonardo da Vinci")
print("Or")
print("2.Pablo Picaso")
c9=(int(input("enter your answer ")))
q1(c9)

print("Q10.What is the study of birds called?")
print("1.Ornithology")
print("Or")
print("2.Zoology")
c10=(int(input("enter your answer ")))
q1(c10)

print("Q11.Which gas is most abundant in Earth's atmosphere?")
print("1.Nirogen")
print("Or")
print("2.Oxygen")
c10=(int(input("enter your answer ")))
q1(c10)

print ("That's the end of that.\n Bye.See you until next time.")
print ("Your score was:",score)