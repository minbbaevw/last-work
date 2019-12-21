def poun(ном):
        расти = str(ном).replace("-", "")
        if len(расти) == 1:
          if ном < 0:
            ном = abs(ном)
          else:
            ном *= -1
        else:
          laun = расти[::-1]
          ном = laun

        return int(ном)

print(poun(321))
print(poun(-7))
print(poun(7))