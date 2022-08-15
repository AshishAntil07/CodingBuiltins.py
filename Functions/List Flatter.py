multiDimensional = [
  'al;edg',
  [289, [420, '29803age4', [2893]], 'glj'],
  [2893, ['gj;la', ['28934'], 6903], 90],
  2384,
  [28347, [58023, [32409783, 532489, [50923, [258709], 198], 59], 7], 20, 59]
]

def flat(arr):
  flatArr = []
  def flatter(elem):
    if type(elem) == type(flatArr):
      for j in elem:
        flatter(j)
    else:
      flatArr.append(elem)
  flatter(arr)

  return flatArr
  # NOTE: Our function doesn't change the original List.

print(multiDimensional)
print(flat(multiDimensional))
