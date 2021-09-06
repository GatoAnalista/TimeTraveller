import os
import csv
import time
from datetime import datetime
from datetime import date
import shutil

pastaOrigem = ''
dataAtual = date.today()
dataAtual = dataAtual.strftime('%Y%m%d')
pastaDestino = './backups/'+dataAtual

def inicializar(data):
    try:
        os.makedirs('backups')
    except:
        print('.')
    try:
        os.makedirs('./backups/'+data)
    except:
        print('..')
    try:
        open('caminhos.csv','r')
    except:
        with open('caminhos.csv','w') as c:
            indices = ['origem']
            caminhos = csv.DictWriter(c, fieldnames=indices, delimiter=';', lineterminator='\n')
            caminhos.writeheader()

def main():
    log = ''
    inicializar(dataAtual)
    with open('caminhos.csv','r') as c:
        indices = ['origem']
        caminhos = csv.DictReader(c,fieldnames=indices, delimiter=';', lineterminator='\n')
        for caminho in caminhos:
            pastaOrigem = caminho['origem']
            for diretorio, subpastas, arquivos in os.walk(pastaOrigem):
                for arquivo in arquivos:
                    data_arquivo = (datetime.fromtimestamp(os.path.getctime(diretorio+'/'+arquivo))).strftime('%Y%m%d')
                    if(dataAtual == data_arquivo):
                        shutil.copy2(os.path.join(diretorio, arquivo),pastaDestino)
                        #data_arquivo = (datetime.fromtimestamp(os.path.getctime(diretorio+'/'+arquivo))).strftime('%d/%m/%Y %H:%M:%S')

while True:
    main()
    time.sleep(5)