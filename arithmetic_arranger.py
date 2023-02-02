

def arithmetic_arranger(problems, result = False):
  if len(problems) > 5:
    return 'Error: Too many problems.'

  firstline = ''
  secondline = ''
  thirdline = ''
  fourthline = ''

  for i in problems:
    newi = i.split()

    max = 0
    
    if len(newi[0]) >= len(newi[2]):
      max = len(newi[0])
    elif len(newi[0]) < len(newi[2]):
      max = len(newi[2])
        
    if len(newi[0]) > 4 or len(newi[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    elif newi[1] == '/' or newi[1] == 'x':
      return "Error: Operator must be '+' or '-'."
    elif not newi[0].isdigit() or not newi[2].isdigit():
      return "Error: Numbers must only contain digits."

    if max - len(newi[0]) == 3:
      firstline += "     " + newi[0] + "    "
    elif max - len(newi[0]) == 2:
      firstline += "    " + newi[0] + "    "
    elif max - len(newi[0]) == 1:
      firstline += "   " + newi[0] + "    "
    elif max - len(newi[0]) == 0:
      firstline += "  " + newi[0] + "    "

    if max - len(newi[2]) == 3:
      secondline += newi[1] + "    " + newi[2] + "    "
    elif max - len(newi[2]) == 2:
      secondline += newi[1] + "   " + newi[2] + "    "
    elif max - len(newi[2]) == 1:
      secondline += newi[1] + "  " + newi[2] + "    "
    elif max - len(newi[2]) == 0:
      secondline += newi[1] + " " + newi[2] + "    "

    if max == 4:
      thirdline += '------    '
    elif max == 3:
      thirdline += '-----    '
    elif max == 2:
      thirdline += '----    '
    elif max == 1:
      thirdline += '---    '

    answer = 0

    if newi[1] == '+':
      answer = int(newi[0]) + int(newi[2])
    elif newi[1] == '-':
      answer = int(newi[0]) - int(newi[2])

    print(type(answer))
    print(answer)

    if len(str(answer)) == 5:
      fourthline += " " + str(answer) + "    "
    elif len(str(answer)) == 4:
      fourthline += " " + str(answer) + "    "
    elif len(str(answer)) == 3:
      fourthline += "  " + str(answer) + "    "
    elif len(str(answer)) == 2:
      fourthline += "  " + str(answer) + "    "
    elif len(str(answer)) == 1:
      fourthline += "    " + str(answer) + "    "
  
  firstline = firstline.rstrip()
  secondline = secondline.rstrip()
  thirdline = thirdline.rstrip()
  fourthline = fourthline.rstrip()

  if result is False:
    return "{}\n{}\n{}".format(firstline, secondline, thirdline)
  elif result is True:
    return "{}\n{}\n{}\n{}".format(firstline, secondline, thirdline, fourthline)
    

    
      

      


  
