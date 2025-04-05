import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

dados_mundiais = [
         ["País", "Colocação", "Ano", "Nota Série Única", "Nota Série Mista", "Nota Total"],
         ["Italy", 1, 2011, 27.350, 27.800, 55.150],
         ["Russia", 2, 2011,27.250, 27.600, 54.850],
         ["Bulgaria", 3, 2011, 26.800, 27.325, 54.125],
         ["Belarus", 4, 2011, 27.525, 25.325, 52.850],
         ["Japan", 5, 2011, 26.250, 26.475, 52.725],
         ["Germany", 6, 2011, 26.200,26.475, 52.675],
         ["Ukraine", 7, 2011, 26.000, 25.850, 51.850],
         ["Switzerland", 8, 2011, 25.525, 26.300, 51.825],
         ["France", 9, 2011, 26.125, 25.650, 51.775],
         ["Israel", 10, 2011, 25.025, 26.675, 51.700],
         ["Greece", 11, 2011, 25.825, 25.050, 50.875],
         ["Spain", 12, 2011, 26.500, 24.000, 50.500],
         ["Azerbaijan", 13, 2011, 25.350, 25.100, 50.450],
         ["Hungary", 14, 2011, 25.050, 25.100, 50.150],
         ["Poland", 15, 2011, 24.450, 25.500, 49.950], 
         ["China", 16, 2011, 23.900, 25.950, 49.850],
         ["Canada", 17, 2011, 24.775, 24.175, 48.950],
         ["Uzbekistan", 18, 2011, 24.225, 23.575, 47.800],
         ["Austria", 19, 2011, 23.825, 23.775, 47.600],
         ["United States", 20, 2011, 24.775, 21.650, 46.425],
         ["Korea", 21, 2011, 23.850, 22.550, 46.400],
         ["Brazil", 22, 2011, 23.650, 21.875, 45.525],
         ["Finland", 23, 2011, 22.650, 21.950, 44.600],
         ["Kazakhstan", 24, 2011, 20.450, 22.200, 42.650],
         ["Belarus", 1, 2013, 17.783, 17.925, 35.708],
         ["Italy", 2, 2013, 17.600, 17.133, 34.73],
         ["Russia", 3, 2013, 16.775, 17.450, 34.225] ,
         ["Spain", 4, 2013, 17.133, 16.816, 33.949],
         ["Bulgaria", 5, 2013, 15.783, 17.150, 32.933],
         ["China", 6, 2013, 16.683, 15.900, 32.583],
         ["Azerbaijan", 7, 2013, 15.666, 16.166, 31.832],
         ["Japan", 8, 2013, 16.116, 15.533, 31.649],
         ["Germany", 9, 2013, 16.400, 15.158, 31.558],
         ["Switzerland", 10, 2013, 15.866, 15.000, 30.866],
         ["Greece", 11, 2013, 15.183, 15.516, 30.699],
         ["Brazil", 12, 2013, 15.083, 15.300, 30.383],
         ["France", 13, 2013, 14.883, 15.133, 30.016],
         ["United States", 14, 2013, 15.600, 14.316, 29.916],
         ["Ukraine", 15, 2013, 16.766, 12.500, 29.266],
         ["Czech Republic", 16, 2013, 14.700, 14.000, 28.700],
         ["Israel", 17, 2013, 13.983, 14.441, 28.424],
         ["Republic of Korea", 18, 2013, 13.758, 14.250, 28.008],
         ["Uzbekistan", 19, 2013, 13.666, 13.733, 27.399],
         ["Finland", 20, 2013, 15.333, 11.958, 27.291],
         ["Poland", 21, 2013, 13.258, 13.850, 27.108],
         ["Kazakhstan", 22, 2013, 13.058, 12.733, 25.791],
         ["Portugal", 23, 2013, 13.483, 12.166, 25.649],
         ["Hungary", 24, 2013, 11.075, 11.650, 22.725],
         ["Mexico", 25, 2013, 12.233, 9.866, 22.099],
         ["Austria", 26, 2013, 11.491,9.633, 21.124],
         ["Cuba", 27, 2013, 12.100, 8.525, 20.625],
         ["Chile", 28, 2013, 8.283, 7.950, 16.233],
         ["Angola", 29, 2013, 5.516, 3.616, 09.132],
         ["Bulgaria", 1, 2014, 17.133, 17.316, 34.449],
         ["Italy", 2, 2014, 17.216, 17.066, 34.282],
         ["Belarus", 3, 2014, 16.750, 17.383, 34.133],
         ["Russia", 4, 2014, 16.133, 17.816, 33.949],
         ["Israel", 5, 2014, 16.800, 16.966, 33.766],
         ["Azerbaijan", 6, 2014, 16.466, 16.866, 33.332],
         ["Ukraine", 7, 2014, 16.400, 16.716, 33.116],
         ["Japan", 8, 2014, 16.100, 16.633, 32.733],
         ["Germany", 9, 2014, 16.433, 16.116, 32.549],
         ["China", 10, 2014, 16.266, 16.233, 32.499],
         ["Spain", 11, 2014, 17.183, 14.733, 31.916],
         ["Greece", 12, 2014, 16.233, 15.466, 31.699],
         ["Switzerland", 13, 2014, 15.450, 15.383, 30.833],
         ["United States", 14, 2014, 15.633, 15.050, 30.683],
         ["Brazil", 15, 2014, 15.283, 15.200, 30.483],
         ["Uzbekistan", 16, 2014, 15.850, 14.266, 30.116],
         ["Finland", 17, 2014, 15.466, 14.116, 29.582],
         ["France", 18, 2014, 13.800, 15.716, 29.516],
         ["Republic of Korea", 19, 2014, 14.050, 13.783, 27.833],
         ["Poland", 20, 2014, 12.750, 14.216, 26.966],
         ["Canada", 21, 2014, 13.916, 12.441, 26.357],
         ["Portugal", 22, 2014, 13.966, 12.208, 26.174],
         ["Mexico", 23, 2014, 12.800, 13.116, 25.916],
         ["Egypt", 24, 2014, 13.116, 12.650, 25.766],
         ["Hungary", 25, 2014, 14.200, 11.425, 25.625],
         ["Latvia", 26, 2014, 13.866, 11.616, 25.482],
         ["Czech Republic", 27, 2014, 13.816, 11.350, 25.166],
         ["Austria", 28, 2014, 13.008, 12.116, 25.124],
         ["Turkey", 29, 2014, 12.483, 12.433, 24.916],
         ["Thailand", 30, 2014, 7.950, 7.316, 15.266],
         ["Angola", 31, 2014, 8.058, 6.558, 14.616],
         ["Russia", 1, 2015, 18.016, 18.250, 36.266],
         ["Bulgaria", 2, 2015, 17.783, 17.800, 35.583],
         ["Spain", 3, 2015, 17.450, 17.450, 34.900],
         ["Italy", 4, 2015, 17.066, 17.716, 34.782],
         ["Japan", 5, 2015, 17.366, 17.316, 34.682],
         ["Israel", 6, 2015, 17.333,16.950, 34.283],
         ["Belarus", 7, 2015, 16.383, 17.633, 34.016],
         ["China", 8, 2015, 16.566, 16.633, 33.199],
         ["Ukraine", 9, 2015, 16.400, 16.766, 33.166],
         ["Uzbekistan", 10, 2015, 15.700, 16.866, 32.566],
         ["Germany", 10, 2015, 15.650, 16.916, 32.566],
         ["Azerbaijan", 12, 2015, 15.666, 16.866, 32.532],
         ["United States", 13, 2015, 16.066, 16.233, 32.299],
         ["Greece", 14, 2015, 15.833, 16.400, 32.233],
         ["Finland", 15, 2015, 15.750, 16.400, 32.150],
         ["Brazil", 16, 2015, 16.041, 15.900, 31.941],
         ["France", 17, 2015, 15.650, 15.000, 30.650],
         ["Republic of Korea", 18, 2015, 15.650, 15.000, 30.650],
         ["Canada", 19, 2015, 14.908, 15.375, 30.283],
         ["Poland", 20, 2015, 14.816, 15.033, 29.849],
         ["Switzerland", 21, 2015, 15.475, 14.350, 29.825],
         ["Egypt", 22, 2015, 13.933, 13.566, 27.499],
         ["Portugal", 23, 2015, 13.675, 13.516, 27.191],
         ["Mexico", 24, 2015, 13.416, 12.791, 26.207],
         ["Russia", 1, 2017, 18.950, 18.750, 37.700],
         ["Bulgaria", 2, 2017, 18.650, 18.300, 36.950],
         ["Japan", 3, 2017, 18.400, 18.250, 36.650],
         ["Italy", 4, 2017, 18.700, 17.925, 36.625],
         ["Belarus", 5, 2017, 18.050, 18.375, 36.425],
         ["Ukraine", 6, 2017, 17.450, 18.150, 35.600],
         ["Azerbaijan", 7, 2017, 18.000, 17.450, 35.450],
         ["China", 8, 2017, 17.300, 16.950, 34.250],
         ["France", 9, 2017, 16.450, 16.600, 33.050],
         ["Uzbekistan", 10, 2017, 16.725, 15.800, 32.525],
         ["Finland", 11, 2017, 16.800, 15.550, 32.350],
         ["United States", 12, 2017, 16.050, 16.200, 32.250],
         ["Brazil", 13, 2017, 16.050, 15.650, 31.700],
         ["Germany", 14, 2017, 16.550, 14.650, 31.200],
         ["Spain", 15, 2017, 14.500, 16.150, 30.650],
         ["Greece", 16, 2017, 15.150, 14.850, 30.000],
         ["Hungary", 17, 2017, 15.800, 13.200, 29.000],
         ["Poland", 18, 2017, 15.500, 13.350, 28.850],
         ["Latvia", 19, 2017, 15.500, 12.800, 28.300],
         ["Mexico", 20, 2017, 14.100, 14.050, 28.150],
         ["Canada", 21, 2017, 13.750, 14.250, 28.000],
         ["Kazakhstan", 22, 2017, 14.350, 13.150, 27.500],
         ["Republic of Korea", 23, 2017, 14.450, 12.550, 27.000],
         ["Slovenia", 24, 2017, 13.500, 13.100, 26.600],
         ["Switzerland", 25, 2017, 14.050, 11.950, 26.000],
         ["Estonia", 26, 2017, 12.100, 9.850, 21.950],
         ["Egypt", 27, 2017, 9.300, 12.000, 21.300],
         ["Norway", 28, 2017, 11.100, 10.050, 21.150],
         ["Singapore", 29, 2017, 11.450, 9.300, 20.750],
         ["Russia", 1, 2018, 23.250, 23.050, 46.300],
         ["Itali", 2, 2018, 22.775, 22.050, 44.825],
         ["Bulgaria", 3, 2018, 19.700 , 22.350, 42.050],
         ["Ukraine", 4, 2018, 19.900, 21.250, 41.150],
         ["Japan", 5, 2018, 19.750, 20.900, 40.650],
         ["Belarus", 6, 2018, 20.000, 19.200, 39.200],
         ["Azerbaijan", 7, 2018, 19.200, 19.900, 39.100],
         ["France", 8, 2018, 18.700, 18.350, 37.050],
         ["Mexico", 9, 2018, 18.300, 18.650, 36.950],
         ["Finland", 10, 2018, 18.650, 18.100, 36.750],
         ["China", 11, 2018, 17.550, 18.550, 36.100],
         ["Germany", 12, 2018, 18.550, 17.450, 36.000],
         ["Estonia", 13, 2018, 17.600, 18.275, 35.875],
         ["United States", 14, 2018, 17.300, 18.500, 35.800],
         ["Israel", 15, 2018, 17.550, 18.100, 35.650 ],
         ["Poland", 16, 2018, 18.100, 16.800, 34.900],
         ["Uzbekistan", 17, 2018, 17.500, 17.200, 34.700],
         ["Brazil", 18, 2018, 16.800, 16.975, 33.775],
         ["Hungary", 19, 2018, 18.000, 15.700, 33.700],
         ["Spain", 20, 2018, 14.450, 19.150, 33.600],
         ["Democratic People's Republic of Korea", 21, 2018, 17.550, 15.450, 33.000],
         ["Greece", 22, 2018, 17.550, 15.450, 32.300],
         ["Canada", 23, 2018, 16.700, 15.550 , 32.250],
         ["Kazakhstan", 24, 2018, 15.050, 16.800 , 31.850],
         ["Switzerland", 25, 2018, 15.350, 16.200, 31.550],
         ["Egypt", 26, 2018, 15.450, 15.050, 30.500],
         ["Slovenia", 27, 2018, 14.500, 14.650, 29.150],
         ["Czech Republic", 28, 2018, 14.000, 15.150, 29.150],
         ["Australia",29, 2018, 14.725, 14.200, 28.925],
         ["Turkey", 30, 2018, 15.250, 13.650, 28.900],
         ["Republic of Korea", 31, 2018, 15.250, 13.650, 28.625],
         ["Austria", 32, 2018, 13.400, 13.850 , 27.250],
         ["Georgia", 33, 2018, 10.700, 11.900, 22.600],
         ["New Zealand", 34, 2018, 11.700, 10.150, 21.850],
         ["Serbia", 35, 2018, 10.200, 11.550, 21.750],
         ["India", 36, 2018, 8.000, 8.450, 16.450],
         ["Russia", 1, 2019, 30.000, 28.700, 58.700],
         ["Japan", 2, 2019, 29.200 , 29.000 , 58.200],
         ["Bulgaria", 3, 2019, 29.200 , 28.800 , 58.000],
         ["Belarus", 4, 2019, 28.400, 28.000, 56.400],
         ["Italy", 5, 2019, 27.800, 27.400, 55.200],
         ["Israel", 6, 2019, 27.450, 27.500, 54.950],
         ["China", 7, 2019, 27.150, 26.100, 53.250],
         ["Azerbaijan", 8, 2019, 26.400, 26.700, 53.100],
         ["Ukraine", 9, 2019, 28.250, 22.900, 51.150],
         ["United States", 10, 2019, 25.050, 25.600, 50.650],
         ["Mexico", 11, 2019, 24.950, 25.600, 50.550],
         ["Finland", 12, 2019, 25.550, 24.975, 50.525],
         ["Brazil", 13, 2019, 25.450, 24.250, 49.700],
         ["Uzbekistan", 14, 2019, 24.000, 25.400, 49.400],
         ["Germany", 15, 2019, 24.750, 24.550, 49.300],
         ["France", 16, 2019, 23.400, 25.400, 48.800],
         ["Spain", 17, 2019, 23.200, 25.600, 48.800],
         ["Poland", 18, 2019, 24.300, 23.350, 47.650],
         ["Estonia", 19, 2019, 23.300, 23.250, 46.550],
         ["Canada", 20, 2019, 22.400, 23.050, 45.450],
         ["Hungary", 21, 2019, 23.850, 20.900, 44.750],
         ["Greece", 22, 2019, 22.000, 20.900, 42.90],
         ["Democratic People's Republic of Korea", 23, 2019, 19.800, 21.950, 41.750],
         ["Kazakhstan", 24, 2019, 19.675, 19.800, 39.475],
         ["Russia", 1, 2021, 46.250, 42.100, 88.350],
         ["Italy", 2, 2021, 44.350, 41.650, 86.000],
         ["Belarus", 3, 2021, 44.900, 40.500, 85.400],
         ["Japan", 4, 2021, 45.000, 39.900, 84.900],
         ["China", 5, 2021, 42.250, 39.950, 82.200],
         ["Azerbaijan", 6, 2021, 39.600, 38.000 , 77.600],
         ["Germany", 7, 2021, 38.050, 37.700, 75.750],
         ["Ukraine", 8, 2021, 37.350, 38.350, 75.700],
         ["Brazil", 9, 2021, 39.450, 36.000, 75.450],
         ["United States", 10, 2021, 37.500, 36.600, 74.100],
         ["France", 11, 2021, 38.600, 35.400, 74.000],
         ["Spain", 12, 2021, 34.800, 39.150, 73.950],
         ["Estnonia", 13, 2021, 34.450, 34.550, 69.000],
         ["Hungary", 14, 2021, 33.150, 33.250, 66.400],
         ["Finland", 15, 2021, 29.800, 34.150, 63.950],
         ["Kazakhstan", 16, 2021, 28.500, 29.950, 58.450],
         ["Great Britain", 17, 2021, 27.200, 27.100, 54.300],
         ["India", 18, 2021, 16.650, 13.450, 30.100],
         ["Bulgaria", 1, 2022,33.800, 32.800, 66.600],
         ["Israel", 2, 2022, 33.850, 30.800, 64.650],
         ["Spain", 3, 2022,33.450,	29.750,	63.200],
         ["Italy", 4, 2022, 34.150,	27.900,	62.050],
         ["Brazil", 5, 2022,33.550,	27.150,	60.700],
         ["Mexico", 6, 2022,32.150,	28.000,	60.150],
         ["China", 7, 2022,31.900,	28.100,	60.000],
         ["Japan", 8, 2022,33.750,	26.050,	59.800],
         ["Azerbaijan", 9, 2022,30.000,	29.250,	59.250],
         ["Greece", 10, 2022, 30.950, 27.850, 58.800],
         ["France", 11, 2022, 31.400, 26.550, 57.950],
         ["Ukraine", 12, 2022, 30.800, 27.100, 57.900],
         ["Poland", 13, 2022, 30.950, 25.850, 56.800],
         ["Germany", 14, 2022, 25.950, 28.050, 54.000],
         ["United States", 15, 2022, 28.650, 25.250, 53.900],
         ["Hungary", 16, 2022, 28.500, 25.350, 53.850],
         ["Finland", 17, 2022, 27.600, 25.100, 52.700],
         ["Uzbekistan", 18, 2022, 30.000, 22.250, 52.250],
         ["Georgia", 19, 2022, 28.150, 21.600, 49.750],
         ["Estonia", 20, 2022, 22.250, 24.500, 46.750],
         ["Turkey", 21, 2022, 28.200, 17.750, 45.950],
         ["Australia", 22, 2022, 24.750, 20.500, 45.250],
         ["Czech Republic", 23, 2022, 25.600, 19.600, 45.200],
         ["Kazakhstan", 24, 2022, 23.250, 21.850, 45.100],
         ["Portugal", 25, 2022, 20.750,	24.300,	45.050],
         ["Republic of Korea", 26, 2022, 25.600, 19.400, 45.000],
         ["Venezuela", 27, 2022, 23.450, 20.350, 43.800],
         ["Chinese Taipei", 28, 2022, 26.400, 17.400, 43.800],
         ["Armenia", 29, 2022, 16.200,	8.200,	24.400],
         ["Israel", 1, 2023,38.150,	32.650,	70.800],
         ["China", 2, 2023,36.900,	33.150,	70.050],
         ["Spain", 3, 2023,35.600,	33.000,	68.600],
         ["Italy", 4, 2023,37.650,	30.500,	68.150],
         ["Ukraine", 5, 2023,34.800, 32.600, 67.400],
         ["Brazil", 6, 2023,34.900,	30.100,	65.000],
         ["France", 7, 2023,35.350,	29.350,	64.700],
         ["Germany", 8, 2023,33.450, 30.950, 64.400],
         ["Azerbaijan", 9, 2023,31.700,	32.200,	63.900],
         ["Poland", 10, 2023,34.850, 28.850, 63.700],
         ["Greece", 11, 2023,34.150, 28.550, 62.700],
         ["Bulgaria", 12, 2023,28.600, 34.100, 62.700],
         ["Japan", 13, 2023,31.650,	31.050,	62.700],
         ["Mexico", 14, 2023,31.200, 31.050, 62.250],
         ["Uzbekistan", 15, 2023,30.650, 28.750, 59.400],
         ["Hungary", 16, 2023,32.000, 22.350, 54.350],
         ["Finland", 17, 2023,29.350, 23.300, 52.650],
         ["United States", 18, 2023,25.850,	26.700,	52.550],
         ["Czechia", 19, 2023,26.650, 25.850, 52.500],
         ["Kazakhstan", 20, 2023,30.300, 21.450, 51.750],
         ["Georgia", 21, 2023,26.050, 24.850, 50.900],
         ["Turkey", 22, 2023,26.250, 24.500, 50.750],
         ["Australia", 23, 2023,26.400,	21.800,	48.200],
         ["Estonia", 24, 2023,29.700, 17.600, 47.300]
          ]

class AnalisadorGR:
    def __init__(self, root):
        self.root = root
        self.root.title("Análise GR - Regressão Múltipla")
        self.root.geometry("1200x900")
        
        # Carrega e prepara os dados
        self.carregar_dados()
        
        # Normalização
        self.scaler = StandardScaler()
        self.normalizar_dados()
        
        # Interface
        self.criar_widgets()
    
    def carregar_dados(self):
        """Carrega e prepara os dados para análise"""
        self.dados = pd.DataFrame(dados_mundiais[1:], columns=dados_mundiais[0])
        
        # Converte para numérico e remove inválidos
        for col in ['Colocação', 'Ano', 'Nota Série Única', 'Nota Série Mista', 'Nota Total']:
            self.dados[col] = pd.to_numeric(self.dados[col], errors='coerce')
        self.dados = self.dados.dropna()
        
        # Renomeia colunas
        self.dados = self.dados.rename(columns={
            'Nota Série Única': 'Série Única',
            'Nota Série Mista': 'Série Mista',
            'Nota Total': 'Nota Geral'
        })
        
        # Remove Rússia e Bielorrússia (sanções esportivas)
        paises_excluidos = ['Rússia', 'Russia', 'Belarus', 'Bielorrússia']  # Nomes alternativos para garantir
        self.dados = self.dados[~self.dados['País'].isin(paises_excluidos)]
        
        self.paises = sorted(self.dados['País'].unique())
    
    def normalizar_dados(self):
        """Normaliza as notas para comparação entre ciclos"""
        cols_notas = ['Série Única', 'Série Mista', 'Nota Geral']
        self.dados[cols_notas] = self.scaler.fit_transform(self.dados[cols_notas])
    
    def criar_widgets(self):
        """Cria a interface gráfica"""
        # Frame de controle
        frame_controle = tk.Frame(self.root, padx=10, pady=10)
        frame_controle.pack(fill="x")
        
        # Seleção de país
        tk.Label(frame_controle, text="País:", font=('Arial', 10)).pack(side="left")
        self.combo_paises = ttk.Combobox(frame_controle, values=self.paises, 
                                       font=('Arial', 10), state="readonly")
        self.combo_paises.set("Brasil" if "Brasil" in self.paises else self.paises[0])
        self.combo_paises.pack(side="left", padx=10)
        
        # Botões
        tk.Button(frame_controle, text="Análise Detalhada", command=self.analisar_pais,
                bg="#3498db", fg="white", font=('Arial', 10)).pack(side="left", padx=5)
        tk.Button(frame_controle, text="Previsão 2025 (Todos)", command=self.analisar_todos,
                bg="#2ecc71", fg="white", font=('Arial', 10)).pack(side="left", padx=5)
        
        # Área de gráficos
        self.frame_graficos = tk.LabelFrame(self.root, text="Visualização", padx=10, pady=10)
        self.frame_graficos.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Área de relatório
        self.frame_relatorio = tk.LabelFrame(self.root, text="Relatório Técnico", padx=10, pady=10)
        self.frame_relatorio.pack(fill="x", padx=10, pady=5)
        
        # Componentes dinâmicos serão criados nas análises
    
    def analisar_pais(self):
        """Gera análise detalhada para um país específico"""
        pais = self.combo_paises.get()
        dados_pais = self.dados[self.dados['País'] == pais].copy()
        
        if len(dados_pais) < 3:
            messagebox.showerror("Erro", f"Dados insuficientes para {pais} (mínimo 3 anos requeridos)")
            return
            
        # Limpa frames anteriores
        self.limpar_frames()
        
        # Regressão Múltipla
        X = dados_pais[['Ano', 'Série Única', 'Série Mista']]
        y = dados_pais['Colocação']
        modelo = LinearRegression().fit(X, y)
        
        # Previsão 2025
        previsao_2025 = modelo.predict([[2025, 
                                      dados_pais['Série Única'].mean(), 
                                      dados_pais['Série Mista'].mean()]])[0]
        
        # Cria gráficos
        self.criar_graficos(dados_pais, modelo, previsao_2025)
        
        # Gera relatório
        self.gerar_relatorio(pais, modelo, previsao_2025, dados_pais)
    
    def limpar_frames(self):
        """Limpa os frames de gráficos e relatório"""
        for widget in self.frame_graficos.winfo_children():
            widget.destroy()
        for widget in self.frame_relatorio.winfo_children():
            widget.destroy()
    
    def criar_graficos(self, dados, modelo, previsao):
        """Cria os 4 gráficos de análise"""
        self.fig = plt.Figure(figsize=(12, 10))
        gs = self.fig.add_gridspec(3, 2)
        
        # Gráfico 1: Evolução com regressão
        ax1 = self.fig.add_subplot(gs[0, :])
        self.plotar_evolucao(ax1, dados, modelo, previsao)
        
        # Gráfico 2: Série Única
        ax2 = self.fig.add_subplot(gs[1, 0])
        self.plotar_serie(ax2, dados, 'Série Única', '#FF7F0E')
        
        # Gráfico 3: Série Mista
        ax3 = self.fig.add_subplot(gs[1, 1])
        self.plotar_serie(ax3, dados, 'Série Mista', '#2CA02C')
        
        # Gráfico 4: Nota Geral
        ax4 = self.fig.add_subplot(gs[2, :])
        self.plotar_serie(ax4, dados, 'Nota Geral', '#1F77B4')
        
        self.fig.tight_layout()
        
        # Adiciona canvas
        canvas = FigureCanvasTkAgg(self.fig, master=self.frame_graficos)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def plotar_evolucao(self, ax, dados, modelo, previsao):
        """Plota a evolução com linha de regressão"""
        anos = dados['Ano']
        colocacoes = dados['Colocação']
        
        # Linha de regressão
        anos_continuos = np.linspace(min(anos), 2025, 100)
        X_pred = np.column_stack([
            anos_continuos,
            np.full(100, dados['Série Única'].mean()),
            np.full(100, dados['Série Mista'].mean())
        ])
        
        ax.scatter(anos, colocacoes, color='#D62728', s=100, label='Dados Históricos')
        ax.plot(anos_continuos, modelo.predict(X_pred), '--', color='#9467BD', label='Modelo')
        ax.scatter(2025, previsao, color='#2CA02C', s=200, marker='*', 
                  label=f'Previsão 2025: {previsao:.1f}ª')
        
        ax.set_title(f"Evolução da Colocação - {dados['País'].iloc[0]}", pad=15)
        ax.set_xlabel("Ano")
        ax.set_ylabel("Colocação")
        ax.invert_yaxis()
        ax.legend()
        ax.grid(True)
    
    def plotar_serie(self, ax, dados, serie, cor):
        """Plota a evolução de uma série específica"""
        ax.plot(dados['Ano'], dados[serie], 'o-', color=cor)
        ax.set_title(serie)
        ax.set_xlabel("Ano")
        ax.set_ylabel("Nota Normalizada")
        ax.grid(True)
    
    def gerar_relatorio(self, pais, modelo, previsao, dados):
        """Gera relatório técnico detalhado com posições formatadas"""
        try:
            # Cálculo de métricas
            coef_ano = modelo.coef_[0]
            coef_unica = modelo.coef_[1]
            coef_mista = modelo.coef_[2]
            r2 = modelo.score(dados[['Ano', 'Série Única', 'Série Mista']], dados['Colocação'])
            melhoria = dados['Colocação'].iloc[0] - dados['Colocação'].iloc[-1]
            
            # Formatação robusta da posição
            try:
                posicao_arredondada = int(round(float(previsao)))
                posicao_formatada = f"{posicao_arredondada}ª"
                
                # Garante que não tenha posição 0 ou negativa
                if posicao_arredondada < 1:
                    posicao_formatada = "1ª"
            except (ValueError, TypeError) as e:
                print(f"Erro ao formatar posição: {e}")
                posicao_formatada = "N/A"

            # Criação do relatório
            texto_relatorio = tk.Text(self.frame_relatorio, wrap="word", height=12, font=('Arial', 10))
            scroll = ttk.Scrollbar(self.frame_relatorio, orient="vertical", command=texto_relatorio.yview)
            texto_relatorio.configure(yscrollcommand=scroll.set)
            
            scroll.pack(side="right", fill="y")
            texto_relatorio.pack(fill="both", expand=True)
            
            relatorio = f"""📊 RELATÓRIO AVANÇADO - {pais.upper()}

    🔮 Previsão 2025: {posicao_formatada} posição
    📈 Qualidade do Modelo (R²): {r2:.2f}

    📌 Fatores de Influência:
    • Tempo (Ano): {coef_ano:.3f} pts/ano
    • Série Única: {coef_unica:.3f} pts/nota
    • Série Mista: {coef_mista:.3f} pts/nota

    📅 Evolução Recente:
    • Melhoria: {melhoria} posições
    • Nota Geral Atual: {dados['Nota Geral'].iloc[-1]:.2f}
    • Tendência: {'⬆️ Melhorando' if melhoria > 0 else '⬇️ Regredindo'}
    """
            texto_relatorio.insert("end", relatorio)
            
        except Exception as e:
            messagebox.showerror("Erro no Relatório", f"Não foi possível gerar o relatório:\n{str(e)}")

    
    def analisar_todos(self):
        """Gera análise comparativa com gráfico de dispersão"""
        janela = tk.Toplevel(self.root)
        janela.title("Análise Comparativa - Previsões 2025")
        janela.geometry("1200x800")
        
        frame_principal = tk.Frame(janela)
        frame_principal.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Cria figura
        fig = plt.Figure(figsize=(12, 8))
        ax = fig.add_subplot(111)
        
        # Coleta resultados
        resultados = []
        for pais in self.paises:
            dados_pais = self.dados[self.dados['País'] == pais]
            if len(dados_pais) >= 3:
                X = dados_pais[['Ano', 'Série Única', 'Série Mista']]
                y = dados_pais['Colocação']
                modelo = LinearRegression().fit(X, y)
                previsao = modelo.predict([[2025, 
                                        dados_pais['Série Única'].mean(), 
                                        dados_pais['Série Mista'].mean()]])[0]
                resultados.append({
                    'País': pais,
                    'Previsão': previsao,
                    'Nota Média': dados_pais['Nota Geral'].mean(),
                    'Melhoria': dados_pais['Colocação'].iloc[0] - dados_pais['Colocação'].iloc[-1]
                })
        
        # Converte para DataFrame
        df_resultados = pd.DataFrame(resultados).sort_values('Previsão')
        
        # Chama a função para mostrar a classificação
        self.mostrar_classificacao(
            sorted([(row['País'], row['Previsão']) for _, row in df_resultados.iterrows()], 
                key=lambda x: x[1])
        )
        
        # Gráfico de dispersão
        scatter = ax.scatter(
            x=df_resultados['Nota Média'],
            y=df_resultados['Previsão'],
            c=df_resultados['Melhoria'],
            s=150,
            cmap='viridis',
            alpha=0.7
        )
        
        # Linha de referência
        ax.axhline(y=8, color='red', linestyle='--', alpha=0.5, label='Top 8')
        
        # Configurações do gráfico
        ax.set_title("Comparação entre Países - Previsão 2025", pad=20, fontsize=14)
        ax.set_xlabel("Nota Geral Média (normalizada)", fontsize=12)
        ax.set_ylabel("Posição Prevista em 2025", fontsize=12)
        ax.invert_yaxis()
        ax.grid(True, alpha=0.3)
        
        # Barra de cores para melhoria
        cbar = fig.colorbar(scatter)
        cbar.set_label('Melhoria na Colocação (posições)', rotation=270, labelpad=20)
        
        # Adiciona rótulos apenas para os top 15 e países relevantes
        for i, row in df_resultados.iterrows():
            if row['Previsão'] <= 15 or row['País'] in ['Brazil', 'Portugal', 'Spain']:
                ax.annotate(row['País'], 
                        (row['Nota Média'], row['Previsão']),
                        textcoords="offset points",
                        xytext=(0,5),
                        ha='center',
                        fontsize=9)
        
        ax.legend()
        fig.tight_layout()
        
        # Adiciona ao tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_principal)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, side="top")
        
        # Adiciona tabela com os resultados
        frame_tabela = tk.Frame(frame_principal)
        frame_tabela.pack(fill="x", pady=10)
        
        # Cria Treeview
        tree = ttk.Treeview(frame_tabela, columns=('País', 'Previsão'), show='headings', height=10)
        tree.heading('País', text='País')
        tree.heading('Previsão', text='Posição Prevista 2025')
        
        # Adiciona scrollbar
        scroll = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        
        scroll.pack(side="right", fill="y")
        tree.pack(fill="both", expand=True)
        
        # Preenche a tabela
        for _, row in df_resultados.iterrows():
            tree.insert("", "end", values=(row['País'], f"{int(round(row['Previsão']))}ª"))
        
        texto_observacao = tk.Label(
        frame_principal,
        text="Observação: Bielorrússia e Rússia excluídas devido a sanções esportivas (2022-atual)",
        font=('Arial', 9, 'italic'),
        fg='#666'
    )
        texto_observacao.pack(side="bottom", pady=5)

    def mostrar_classificacao(self, resultados):
        """Exibe a tabela de classificação em janela separada"""
        janela = tk.Toplevel(self.root)
        janela.title("Classificação Prevista para 2025")
        janela.geometry("600x800")
        
        # --- Cria o frame principal DENTRO desta janela ---
        frame_principal = tk.Frame(janela, padx=10, pady=10)
        frame_principal.pack(fill="both", expand=True)
        
        # Título
        tk.Label(
            frame_principal, 
            text="Previsão de Colocações - Mundial 2025",
            font=('Arial', 14, 'bold')
        ).pack(pady=10)
        
        # Treeview (tabela)
        tree = ttk.Treeview(
            frame_principal,
            columns=('posicao', 'pais', 'pontuacao'),
            show='headings',
            height=25
        )
        
        # Configuração das colunas
        tree.heading('posicao', text='Posição')
        tree.column('posicao', width=80, anchor='center')
        
        tree.heading('pais', text='País')
        tree.column('pais', width=180, anchor='w')
        
        tree.heading('pontuacao', text='Posição Prevista 2025')
        tree.column('pontuacao', width=120, anchor='center')
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Layout
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Preenche a tabela
        for idx, (pais, previsao) in enumerate(resultados, 1):
            tree.insert(
                "", 
                "end", 
                values=(
                    f"{idx}ª",
                    pais,
                    f"{int(round(previsao))}ª"  # Arredonda a posição prevista
                )
            )
        
        # Botão de fechar
        tk.Button(
            frame_principal,
            text="Fechar",
            command=janela.destroy,
            bg="#f44336",
            fg="white"
        ).pack(pady=10, side="bottom")
# Execução principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AnalisadorGR(root)
    root.mainloop()