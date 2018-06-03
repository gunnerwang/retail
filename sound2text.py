import os
import re
import record_sound
import wav2flac

def sound2text():
    #REQUIRE: connection to the microphone
    record_sound.my_record()
    wav2flac.wav2flac()
    os.system("curl -X POST -u '4816a2bc-dbeb-4492-81ca-6733566a608a':'sBuyiDkXYCi0' --header 'Content-Type: audio/flac' --data-binary @output.flac  'https:/stream.watsonplatform.net/speech-to-text/api/v1/recognize'>sound.txt")
    file = open("sound.txt")
    transcript = []
    for line in file.readlines():
        if (re.match('\"transcript\":*', line.strip(" "))):
            transcript.append(eval(line.strip(" ").strip("\n").split(":")[1]))
    file.close()
    transcript = " ".join(transcript)
    os.system("rm output.wav")
    os.system("rm output.flac")
    return transcript
