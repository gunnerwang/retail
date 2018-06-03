import os
import subprocess

def wav2flac():
    for d,sd,files in os.walk('.'):
        for f in files:
            src = os.path.join(d, f)
            (prefix, sep, suffix) = src.rpartition('.')
            if suffix != 'wav':
                continue
            des = prefix + '.flac'
            #print '"', src, '"', 'to', '"', des, '"'
            cmd = ['flac', '--keep-foreign-metadata', '--verify', src]
            subprocess.call(cmd)