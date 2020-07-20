from openpyxl import load_workbook
def test(a):
  print(a)

def excel(file_path,file_path_out):
  wb = load_workbook(filename=file_path)

  sheet = wb['Sheet11']
  print(sheet)
  ok=[]
  for row in sheet:
    values = [cell.value for cell in row]
    ok.append(values)
  #func check
  for i , v1 in enumerate(ok):
    for j , v2 in enumerate(v1):
      if str(ok[i][j]).find('=') == 0 : ok[i][j]='func'
  #check rows
  lap=[]
  check=[0]*len(ok)
  log=[]
  for i , v1 in enumerate(ok):
    if check[i] != 1 :
        log.append('MM')
        log.append(i+1)
        my_string1 = ''.join(str(x) for x in v1)
        for j ,v2 in enumerate(ok[i+1:len(ok)]):
          my_string2 = ''.join(str(x) for x in v2)
          if my_string1 == my_string2 : 
            lap.append(i+j+2)
            check[i+j+1]=1
            log.append(i+j+2)
  #remove row
  res=[]
  lap = sorted(lap)
  for j ,v2 in enumerate(lap):
    res.append(v2)
  for i , v1 in enumerate(lap):
    sheet.delete_rows(lap[i])
    for j ,v2 in enumerate(lap[i+1:len(lap)]): lap[i+j+1] = lap[i+j+1] -1 
  wb.save(file_path_out)
  return res