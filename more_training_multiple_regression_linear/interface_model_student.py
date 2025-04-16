import pandas as pd 
import joblib
import gradio as gr

# passo 1 importar o modelo
modelo = joblib.load('./modelo_perfomance.pkl')



# Criar função para fazer a predição
def predict(Hours_Studied, Previous_Scores, Extracurricular_Activities, Sleep_Hours, Sample_Question_Papers_Practiced):
  predicao_individual = {
  'Hours_Studied' : Hours_Studied,
  'Previous_Scores': Previous_Scores,
  'Extracurricular_Activities': Extracurricular_Activities,
  'Sleep_Hours': Sleep_Hours,
  'Sample_Question_Papers_Practiced': Sample_Question_Papers_Practiced,
}
  predict_df = pd.DataFrame(predicao_individual, index=[1])
  perfomance = modelo.predict(predict_df)
  return float(perfomance[0])