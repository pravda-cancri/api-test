from datetime import datetime
def log(ip,type,*notes):
    now = datetime.now()
    time = now.strftime("%d%m%Y%H%M%S")
    g = open("log.txt", "a")
    g.write("{}#{}#{}#{}\n".format(ip,type,time,[x for x in notes]))
    g.close()