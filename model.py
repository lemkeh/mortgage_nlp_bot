import joblib
from nltk.stem import SnowballStemmer
from parser import parsing


model = joblib.load('models/model_svc.sav')
encoder = joblib.load('models/encoder.sav')
vectorizer = joblib.load('models/vectorizer.sav')

snowball = SnowballStemmer(language="russian")

dict_ = {
          '1': ['ставк', 'процент', 'дол'],

          '0': [ 'перв', 'взнос', 'начальн', 'первоначальн', 'платеж', 'выплат', 'плат', 'стартов']}




# dict_par = {'Вторичное жильё': ['9,9', '0'],
#             'Новостройки': ['9,9', '0'],
#             'Семейная ипотека': ['5,3', '15'],
#             'Ипотека с господдержкой': ['6,3', '15']}

dict_par = parsing()

def predict(text=str, model = model, vectorizer=vectorizer,  dict_ = dict_, snowball= snowball):
  text = text.lower()
  stem = ' '.join([snowball.stem(i) for i in text.split()])

  cat_2 = None

  for c in dict_.keys():
    for i in dict_[c]:
      if i in stem: cat_2 = c

  text = vectorizer.transform([text])
  y_pred = model.predict(text)
  cat_1 = encoder.inverse_transform(y_pred)[0]



  if cat_2 == None:
    result = f'Информация по кредиту категории {cat_1}: Ставка: {dict_par[cat_1][0]}%, Первый взнос: {dict_par[cat_1][1]}%'
  elif int(cat_2)==1: 
    result = f'Ставка в категории "{cat_1}": {dict_par[cat_1][int(cat_2)]}%'
  elif int(cat_2)==0 : 
    result = f'Первый взнос в категории "{cat_1}": {dict_par[cat_1][int(cat_2)]}%'


  return result

