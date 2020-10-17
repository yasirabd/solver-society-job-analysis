import re

DELIMITERS = '/""\',()?!:;&<>='
INDEL = '/""\',():;&<>='
sentenceMatcher = re.compile(r"(?<!\..)([\?\!\.]+)\s(?!.\.)")
refMatcher = re.compile(r"(\[)\d+(\])")


class Tokenization():

    def isabbrev(self, s):
        abbrev = ['H', 'Hj', 'Ir', 'Jend', 'Purn', 'Prof', 'rer', 'nat', 'Brig', 'Ny', 'Nn', 'Drs', 'Dra', 'dr', 'Ltd', 'Corp', 'Inc']
        last = s[:s.find('.')]
        return (last in abbrev) or ((len(last)<3) and (last == last.upper()))

    def removesubsetstr(self, strsub,strset):
        ls = list(strset)
        for c in strsub:
            if c in ls: ls.remove(c)
        return ''.join(ls)

    def cek_inner_delimiter(self, buf):
        if len(buf)>1:
            out = []
            for cdel in INDEL:
                if cdel in buf:
                    buf = buf.replace(cdel, " "+cdel+" ")
            if " " in buf:
                return buf.split(" ")
            else:
                return [buf]
        else:
            return [buf]

    def tokenisasi_kalimat(self, line):
        out = []
        tok = line.split(" ")
        for t in tok:
            buf = t
            i = 0
            while i<len(buf) and buf[i] in DELIMITERS:
                out += [buf[i]]
                i += 1
            if i < len(t):
                buf = buf[i:]
            i = -1
            akhir = []
            while i>=-len(buf) and buf[i] in DELIMITERS:
                akhir += [buf[i]]
                i -= 1
            if -i <= len(buf):
                buf = buf[:len(buf)+i+1]
            akhir.reverse()
            out = out + self.cek_inner_delimiter(buf) + akhir
        if len(out[-1])>1:
            buf = out[-1]
            i = -1
            akhir = []
            while i>=-len(buf) and buf[i] in DELIMITERS+'.':
                akhir += [buf[i]]
                i -= 1
            if -i <= len(buf):
                buf = buf[:len(buf)+i+1]
            if i < -1:
                out[-1] = buf
                akhir.reverse()
                out += akhir
        return out

    def sentence_extraction(self, line):
        out = []
        sent = sentenceMatcher.split(line)
        tmp = ''
        pre = []
        for l in sent:
            s = l.strip()
            # print s
            if len(s)==0: continue
            tmp += s.strip()
            if (s[-1] in "?!.") or (len(s)==1 and s[0] in "?!."):
                pre += [tmp]
                tmp = ''
        if len(tmp)>0:
            pre += [tmp]
            tmp = ''
        for s in pre:
            tmp += s.strip()
            if not self.isabbrev(s[s.rfind(' ')+1:]):
                out += [tmp]
                tmp = ''
            else:
                tmp += ' '
        if len(tmp)>0:
            out += [tmp]
            tmp = ''
        return out

    def cleaning(self, line):
        return refMatcher.sub("", line.strip())

if __name__=='__main__':
    l = 'response.content_type . acdef . '
    out = self.sentence_extraction(self.cleaning(l))
    for o in out:
        print(" ".join(self.tokenisasi_kalimat(o)))
