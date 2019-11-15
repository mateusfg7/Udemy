saida = open("genomas.html", "w")

def genes(genes):
    entrada = open("{}.fasta".format(genes)).read()

    cont = {}

    for i in ['A', 'T', 'C', 'G']:
        for j in ['A', 'T', 'C', 'G']:
            cont[i+j] = 0

    entrada = entrada.replace("\n", "")

    for k in range(len(entrada)-1):
        cont[entrada[k]+entrada[k+1]] += 1

    # HTML

    i = 1
    saida.write("<h1>{}</h1>".format(genes))
    for k in cont:
        transparencia = str(cont[k]/max(cont.values()))
        saida.write("<div style='width:100px; height:100px; border:1px solid #111; float:left; background:rgba(0,0,0,{}); color:#fff'>{}</div>\n".format(transparencia, k))

        if i%4 == 0:
            saida.write("<div style='clear:both;'></div>\n")
        
        i += 1





genes('bacteria')
genes('human')
saida.close()