# coding:utf-8
import codecs
from multiprocessing import Pool
import jieba
 
 
fin = "news.txt"
fout = "news.seg"
 
def read_data():
    fr = codecs.open(fin, "r", "utf-8")
    trunk = 100000  # 每次返回10条数据
    icount = 0
    texts = []
    for line in fr:
        line = line.strip()
        texts.append(line)
        icount += 1
        if icount % trunk == 0:
            yield texts
            texts = []
 
def seg(texts):
    result = []
    for text in texts:
        result.append(" ".join(jieba.cut(text)))
    return result
 
 
def parallel_seg():
    fw = codecs.open(fout, "w", "utf-8")
    texts = read_data()
    cpus = 10  # CPU个数
    ichunk = 0  # 第ichunk个生成器
    for t in texts:
        pool = Pool(cpus)
        step = int(len(t) / cpus)
        tmp = [t[i:i+step] for i in range(0, len(t) , step)]
        results = pool.map(seg, tmp)
        pool.close()
        pool.join()
        # 写入
        for r in results:
            for i in r:
                fw.write(i + "\n")
        ichunk += 1
        print "finished samples:",len(t) * ichunk
    fw.close()
 
 
if __name__ == "__main__":
    parallel_seg()
