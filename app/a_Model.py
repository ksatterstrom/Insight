#def ModelIt(fromUser  = 'Default', CNV_data = 0):
def ModelIt(miRNA_data):

  import cPickle as pickle

  rf_model = pickle.load( open( "miRNA model, 5000 trees.p", "rb" ) )
  prediction = rf_model.predict(miRNA_data)
  predicted_prob = rf_model.predict_proba(miRNA_data)[0:,1]

  return predicted_prob

  #if fromUser != 'Default':
  #  return prediction
  #else:
  #  return 'check your input'
