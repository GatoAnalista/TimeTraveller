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
    try:
        open('log.csv','r')
    except:
        with open('log.csv','w') as c:
            indices = ['Data do arquivo','Caminho do arquivo','arquivo']
            caminhos = csv.DictWriter(c, fieldnames=indices, delimiter=';', lineterminator='\n')
            caminhos.writeheader()

def backup(pastaOrigem,pastaDestino,dataAtual):
    log = [[]]
    for diretorio, subpastas, arquivos in os.walk(pastaOrigem):
        for arquivo in arquivos:
            arq = os.path.join(diretorio, arquivo)
            try:
                data_arquivo = (datetime.fromtimestamp(os.path.getmtime(arq))).strftime('%Y%m%d')
                if(dataAtual == data_arquivo):
                    shutil.copy(arq,pastaDestino)
                    log += [[str(data_arquivo)] + [str(arq)] + [str(arquivo)]]
            except:
                print('Erro: '+arquivo)
        for subpasta in subpastas:
            pastaOrigem = os.path.join(diretorio, subpasta)
            log += backup(pastaOrigem,pastaDestino,dataAtual)
    return log

def logger(log):
    with open('log.csv','a') as datalog:
        logs = csv.writer(datalog, delimiter = ';', lineterminator = '\n')
        for l in log:
            if l != []:
                logs.writerow(l)
    limpaLog()

def limpaLog():
    linhas = []
    with open('log.csv','r') as datalog:
        for log in datalog:
            linhas += [datalog.readline()]
    linhas = list(dict.fromkeys(linhas))
    with open('log.csv','w') as datalog:
        datalog.write('Data do arquivo;Caminho do arquivo;arquivo\n')
        for linha in linhas:
            datalog.writelines(linha)

def main():
    dataAtual = date.today()
    dataAtual = dataAtual.strftime('%Y%m%d')
    pastaDestino = './backups/'+dataAtual
    log = ''
    inicializar(dataAtual)
    with open('caminhos.csv','r') as c:
        indices = ['origem']
        caminhos = csv.DictReader(c,fieldnames=indices, delimiter=';', lineterminator='\n')
        for caminho in caminhos:
            pastaOrigem = caminho['origem']
            log = backup(pastaOrigem,pastaDestino,dataAtual)
    logger(log)
                        
while True:
    main()
    time.sleep(5)