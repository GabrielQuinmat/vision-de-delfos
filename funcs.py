CATEGORY_PALETTE = ['#3C7A89','#B2FFD6','#2E4756','#AA78A6','#B75D69']
CATEGORY_PALETTE_OPACITY = ['rgba(60, 122, 137, x)','rgba(178, 255, 214, x)','rgba(46, 71, 86, x)','rgba(170, 120, 166, x)','rgba(183, 93, 105, x)']
GRADIENT_PALETTE = ['#BA92D8','#3D718A','#8AF8B9']

def aggregate_patient(df, agg_cols):
  cols = ['Patient ID', 'Ingress Month', 'Interest Supplies', *agg_cols]
  patientDF = df.groupby(cols)
  tpDF = patientDF['Treatment Cost'].sum()
  tpDF = tpDF.reset_index()
  tpDF = tpDF[tpDF['Treatment Cost'] > 0]
  return tpDF

def mean_treatment(df, agg_cols):
  gDF = df.groupby(['Ingress Month', 'Interest Supplies',  *agg_cols])['Treatment Cost'].mean()
  gDF = gDF.reset_index()
  gDF = gDF[gDF['Treatment Cost'].notna()]
  return gDF

def defineEdadCat(x):
  if x >= 0 and x <= 18:
    return '0-18'
  elif x >= 19 and x <= 35:
    return '19-35'
  elif x >= 36 and x <= 50:
    return '36-50'
  elif x >= 51 and x <= 65:
    return '51-65'
  else:
    return '65+'