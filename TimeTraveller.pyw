import os
import csv
import time
from datetime import datetime
from datetime import date
import shutil

pastaOrigem = ''

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

def backup(pastaOrigem,pastaDestino,dataAtual):
    for diretorio, subpastas, arquivos in os.walk(pastaOrigem):
        for arquivo in arquivos:
            arq = os.path.join(diretorio, arquivo)
            try:
                data_arquivo = (datetime.fromtimestamp(os.path.getmtime(arq))).strftime('%Y%m%d')
                if(dataAtual == data_arquivo):
                    shutil.copy(arq,pastaDestino)
            except:
                print('Erro: '+arquivo)
        for subpasta in subpastas:
            pastaOrigem = os.path.join(diretorio, subpasta)
            backup(pastaOrigem,pastaDestino,dataAtual)

def main():
    log = ''
    dataAtual = date.today()
    dataAtual = dataAtual.strftime('%Y%m%d')
    pastaDestino = './backups/'+dataAtual
    inicializar(dataAtual)
    with open('caminhos.csv','r') as c:
        indices = ['origem']
        caminhos = csv.DictReader(c,fieldnames=indices, delimiter=';', lineterminator='\n')
        for caminho in caminhos:
            pastaOrigem = caminho['origem']
            backup(pastaOrigem,pastaDestino,dataAtual)                

while True:
    main()
    time.sleep(5)