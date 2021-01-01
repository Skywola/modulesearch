from collections import deque

q = deque()

s = '\n\r  What is the module you wish to search?   Search Options:\n\r'
mods = [s, '\t\t1. numpy', '\t\t2. pandas', '\t\t3. plotly', '\t\t4. matplotlib', '\t\t5. matplotlib.pyplot', '\t\t6. seaborn','\t\t7. sklearn','\t\t8. sympy\n\r\n\r', ' Format: search(4,\'searchitem\')\n\r']
for i in mods:
    print(i)



def mod(module):
    if(module == 1):
        import numpy
        nmp = dir(numpy)
        nmp.insert(0, 'numpy')
        q.append(nmp)        
    elif(module == 2):
        import pandas
        pan = dir(pandas)
        pan.insert(0, 'pandas')
        q.append(pan)
    elif(module == 3):
        import plotly
        plty = dir(plotly)
        plty.insert(0, 'plotly')
        q.append(plty)
        pltcolors = dir(plotly.colors)
        pltcolors.insert(0, 'plotly.colors')
        q.append(pltcolors)
        pltdata = dir(plotly.data)
        pltdata.insert(0, 'plotly.data')
        q.append(pltdata)
        pltgraph_objects = dir(plotly.graph_objects)
        pltgraph_objects.insert(0, 'plotly.graph_objects')
        q.append(pltgraph_objects)
        pltio = dir(plotly.io)
        pltio.insert(0, 'plotly.io')
        q.append(pltio)
        pltoffline = dir(plotly.offline)
        pltoffline.insert(0, 'plotly.offline')
        q.append(pltoffline)
        plttools = dir(plotly.tools)
        plttools.insert(0, 'plotly.tools')
        q.append(plttools)
        pltutils = dir(plotly.utils)
        pltutils.insert(0, 'plotly.utils')
        q.append(pltutils)
    elif(module == 4):
        import matplotlib
        mpltl = dir(matplotlib)
        mpltl.insert(0, 'matplotlib')
        q.append(mpltl)
    elif(module == 5):
        import matplotlib.pyplot
        pyplt = dir(matplotlib.pyplot)
        pyplt.insert(0, 'matplotlib.pyplot')
        q.append(pyplt)        
    elif(module == 6):
        import seaborn
        sea = dir(seaborn)
        sea.insert(0, 'seaborn')
        q.append(sea)
    elif(module == 7):
        import sklearn
        skln = dir(sklearn)
        skln.insert(0, 'sklearn')
        q.append(skln)
        skbase = dir(sklearn.base)
        skbase.insert(0, 'sklearn.base')
        q.append(skbase)
        skclone = dir(sklearn.clone)
        skclone.insert(0, 'sklearn.clone')
        q.append(skclone)
        skconfig_context = dir(sklearn.config_context)
        skconfig_context.insert(0, 'sklearn.config_context')
        q.append(skconfig_context)
        skexceptions = dir(sklearn.exceptions)
        skexceptions.insert(0, 'sklearn.exceptions')
        q.append(skexceptions)
        skexternals = dir(sklearn.externals)
        skexternals.insert(0, 'sklearn.externals')
        q.append(skexternals)
        skget_config = dir(sklearn.get_config)
        skget_config.insert(0, 'sklearn.get_config')
        q.append(skget_config)
        sklogger = dir(sklearn.logger)
        sklogger.insert(0, 'sklearn.logger')
        q.append(sklogger)
        sklogging = dir(sklearn.logging)
        sklogging.insert(0, 'sklearn.logging')
        q.append(sklogging)
        skos = dir(sklearn.os)
        skos.insert(0, 'sklearn.os')
        q.append(skos)
        skre = dir(sklearn.re)
        skre.insert(0, 'sklearn.re')
        q.append(skre)
        skset_config = dir(sklearn.set_config)
        skset_config.insert(0, 'sklearn.set_config')
        q.append(skset_config)
        sksetup_module = dir(sklearn.setup_module)
        sksetup_module.insert(0, 'sklearn.setup_module')
        q.append(sksetup_module)
        skshow_versions = dir(sklearn.show_versions)
        skshow_versions.insert(0, 'sklearn.show_versions')
        q.append(skshow_versions)
        sksys = dir(sklearn.sys)
        sksys.insert(0, 'sklearn.sys')
        q.append(sksys)
        skutils = dir(sklearn.utils)
        skutils.insert(0, 'sklearn.utils')
        q.append(skutils)
        skwarnings = dir(sklearn.warnings)
        skwarnings.insert(0, 'sklearn.warnings')
        q.append(skwarnings)
    elif(module == 8):
        import sympy
        smp = dir(sympy)
        smp.insert(0, 'sympy')
        q.append(smp)
    elif(module == '?'):
        for i in mods:
            print(i)
            
        return
    else:
        print('Module entered does not exist!')
        search('?')
        return

def search(module, searchitem='axis'):
    mod(module)
    if(module=='?'):
        return
    searchitem = str(searchitem)
    notfound = True
    for list in q:
        for item in list:
            if searchitem.lower() in item.lower():
                print(list[0] + "." + item)
                notfound = False
    #
    q.clear()
    if(notfound):
        print('Item not found')

search('?')
