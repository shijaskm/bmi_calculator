import pandas as pd
import numpy as np
bmidf = pd.read_json ('bmi.json')
#print(bmidf)

bmidf['BMI'] = ''
bmidf['BMI_category'] = ''
bmidf['Health_risk'] = ''

bmidf['BMI'] = round(bmidf['WeightKg']/((bmidf['HeightCm']/100)**2),2)
#print(bmidf)
def catFunc(s):
    if (s['BMI'] <= 18.4 ):
        return 'Underweight'
    elif(s['BMI'] >= 18.5 and s['BMI'] <= 24.9 ):
        return 'Normal weight'
    elif (s['BMI'] >= 25 and s['BMI'] <= 29.9):
        return 'Overweight'
    elif (s['BMI'] >= 30 and s['BMI'] <= 34.9):
        return 'Moderately obese'
    elif (s['BMI'] >= 35 and s['BMI'] <= 39.9):
        return 'Severely obese'
    elif (s['BMI'] > 40 ):
        return 'Very severely obese'

def heathRiskfunc(s):
    if (s['BMI'] <= 18.4 ):
        return 'Malnutrition risk'
    elif(s['BMI'] >= 18.5 and s['BMI'] <= 24.9 ):
        return 'Low risk'
    elif (s['BMI'] >= 25 and s['BMI'] <= 29.9):
        return 'Enhanced risk'
    elif (s['BMI'] >= 30 and s['BMI'] <= 34.9):
        return 'Medium risk'
    elif (s['BMI'] >= 35 and s['BMI'] <= 39.9):
        return 'High risk'
    elif (s['BMI'] > 40 ):
        return 'Very high risk'

#finding BMI category
bmidf['BMI_category'] = bmidf.apply(catFunc, axis=1)

#finding Health risk
bmidf['Health_risk'] = bmidf.apply(heathRiskfunc, axis=1)

#finding overweight people count
print(bmidf[bmidf['BMI_category'] == 'Overweight']['BMI'].count())
print(bmidf)
